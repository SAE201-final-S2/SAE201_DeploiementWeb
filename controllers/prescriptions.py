from flask import Blueprint, render_template, request
from models.db import Session
from models.dimensions import ProfessionSante, Departement, Region, TypePrescription
from services.ameli_api import AmeliAPI

bp_prescriptions = Blueprint("prescriptions", __name__)
api = AmeliAPI()


@bp_prescriptions.route("/prescriptions")
def afficher():
    """Affiche les prescriptions pour la sélection de l'utilisateur."""
    profession_id        = request.args.get("profession_id", type=int)
    departement_code     = request.args.get("departement_code", type=str)
    annee                = request.args.get("annee", type=int)
    type_prescription_id = request.args.get("type_prescription_id", type=int)

    session = Session()
    try:
        professions        = session.query(ProfessionSante).order_by(ProfessionSante.libelle).all()
        regions            = session.query(Region).order_by(Region.libelle).all()
        types_prescription = session.query(TypePrescription).order_by(TypePrescription.libelle).all()

        if not all([profession_id, departement_code, annee, type_prescription_id]):
            return render_template(
                "prescriptions.html",
                professions=professions, regions=regions,
                types_prescription=types_prescription,
                resultats=None, evolution=None,
                prof=None, dept=None, annee=None, type_presc=None,
                BASE_URL="",
            )

        prof       = session.get(ProfessionSante, profession_id)
        dept       = session.get(Departement, departement_code)
        type_presc = session.get(TypePrescription, type_prescription_id)

        if not prof or not dept or not type_presc:
            return render_template("erreur.html", message="Paramètre introuvable."), 400

        resultats = api.get_prescriptions(prof.libelle, dept.code, annee, str(type_presc.id))
        evolution = api.get_evolution_prescriptions(prof.libelle, dept.code, str(type_presc.id))

        return render_template(
            "prescriptions.html",
            professions=professions, regions=regions,
            types_prescription=types_prescription,
            resultats=resultats, evolution=evolution,
            prof=prof, dept=dept, annee=annee, type_presc=type_presc,
            BASE_URL="",
        )
    finally:
        session.close()
