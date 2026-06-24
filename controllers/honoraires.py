from flask import Blueprint, render_template, request
from models.db import Session
from models.dimensions import ProfessionSante, Departement, Region, TypeHonoraire
from services.ameli_api import AmeliAPI

bp_honoraires = Blueprint("honoraires", __name__)
api = AmeliAPI()


@bp_honoraires.route("/honoraires")
def afficher():
    """Affiche les honoraires pour la sélection de l'utilisateur."""
    profession_id     = request.args.get("profession_id", type=int)
    departement_code  = request.args.get("departement_code", type=str)
    annee             = request.args.get("annee", type=int)
    type_honoraire_id = request.args.get("type_honoraire_id", type=int)

    session = Session()
    try:
        professions     = session.query(ProfessionSante).order_by(ProfessionSante.libelle).all()
        regions         = session.query(Region).order_by(Region.libelle).all()
        types_honoraire = session.query(TypeHonoraire).order_by(TypeHonoraire.id).all()

        # Formulaire vide si paramètres incomplets
        if not all([profession_id, departement_code, annee]):
            return render_template(
                "honoraires.html",
                professions=professions, regions=regions,
                types_honoraire=types_honoraire,
                resultats=None, evolution=None,
                prof=None, dept=None, annee=None, type_hon=None,
                BASE_URL="",
            )

        prof     = session.get(ProfessionSante, profession_id)
        dept     = session.get(Departement, departement_code)
        type_hon = session.get(TypeHonoraire, type_honoraire_id) if type_honoraire_id else None

        if not prof or not dept:
            return render_template("erreur.html", message="Profession ou département introuvable."), 400

        resultats = api.get_honoraires(prof.libelle, dept.code, annee, type_hon)
        evolution = api.get_evolution_honoraires(prof.libelle, dept.code, type_hon)
        # Essayer d'afficher les montants pour l'année sélectionnée.
        total_honoraires = None
        moyen_honoraires = None
        try:
            if resultats:
                first = resultats[0]
                total_honoraires = first.get('montant_honoraires')
                moyen_honoraires = first.get('montant_honoraires_moyens')
        except Exception:
            total_honoraires = None
            moyen_honoraires = None

        # Fallback : si resultats ne contient rien, chercher dans evolution l'année choisie
        if (total_honoraires is None or total_honoraires == '') and evolution:
            try:
                match = next((ev for ev in evolution if str(ev.get('annee')).startswith(str(annee))), None)
                if match:
                    total_honoraires = match.get('montant_honoraires')
                    moyen_honoraires = match.get('montant_honoraires_moyens')
            except Exception:
                pass

        # Normaliser en float/None
        try:
            total_honoraires = float(total_honoraires) if total_honoraires not in (None, '') else 0.0
        except Exception:
            total_honoraires = 0.0
        try:
            moyen_honoraires = float(moyen_honoraires) if moyen_honoraires not in (None, '') else None
        except Exception:
            moyen_honoraires = None

        return render_template(
            "honoraires.html",
            professions=professions, regions=regions,
            types_honoraire=types_honoraire,
            resultats=resultats, evolution=evolution,
            prof=prof, dept=dept, annee=annee, type_hon=type_hon,
            total_honoraires=total_honoraires, moyen_honoraires=moyen_honoraires,
            BASE_URL="",
        )
    finally:
        session.close()
