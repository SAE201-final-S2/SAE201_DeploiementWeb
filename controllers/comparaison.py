from flask import Blueprint, render_template, request
from models.db import Session
from models.dimensions import ProfessionSante, Departement
from services.ameli_api import AmeliAPI

bp_comparaison = Blueprint("comparaison", __name__)
api = AmeliAPI()

@bp_comparaison.route("/comparaison")
def afficher():
    session = Session()
    try:
        professions = session.query(ProfessionSante).order_by(ProfessionSante.libelle).all()
        departements = session.query(Departement).order_by(Departement.code).all()

        # Paramètres du formulaire 1
        prof1_id = request.args.get("profession1_id", type=int)
        dept1_code = request.args.get("departement1_code", type=str)
        annee1 = request.args.get("annee1", type=int)

        # Paramètres du formulaire 2
        prof2_id = request.args.get("profession2_id", type=int)
        dept2_code = request.args.get("departement2_code", type=str)
        annee2 = request.args.get("annee2", type=int)

        evolution1 = []
        evolution2 = []
        label1 = ""
        label2 = ""

        if prof1_id and dept1_code and annee1:
            prof1 = session.get(ProfessionSante, prof1_id)
            dept1 = session.get(Departement, dept1_code)
            if prof1 and dept1:
                evolution1 = api.get_evolution_effectifs(prof1.libelle, dept1_code)
                label1 = f"{prof1.libelle} – {dept1.code} {dept1.libelle}"

        if prof2_id and dept2_code and annee2:
            prof2 = session.get(ProfessionSante, prof2_id)
            dept2 = session.get(Departement, dept2_code)
            if prof2 and dept2:
                evolution2 = api.get_evolution_effectifs(prof2.libelle, dept2_code)
                label2 = f"{prof2.libelle} – {dept2.code} {dept2.libelle}"

        return render_template("comparaison.html",
                               professions=professions,
                               departements=departements,
                               evolution1=evolution1,
                               evolution2=evolution2,
                               label1=label1,
                               label2=label2)
    finally:
        session.close()