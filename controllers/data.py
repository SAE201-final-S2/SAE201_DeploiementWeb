from flask import Blueprint, render_template
from controllers.auth import login_required
from models.db import Session
from models.dimensions import ProfessionSante, Departement, Region
from services.ameli_api import AmeliAPI

bp_data = Blueprint("data", __name__)


def get_total_effectif(profession_libelle, annee):
    """Calcule l'effectif total national d'une profession pour une année."""
    api = AmeliAPI()
    resultats = api.get_effectifs(profession_libelle, "99", annee)
    if resultats:
        return resultats[0].get("effectif", 0) or 0
    return 0


def get_dashboard_context():
    session = Session()
    try:
        nb_professions = session.query(ProfessionSante).count()
        nb_departements = session.query(Departement).count()
        nb_regions = session.query(Region).count()

        stats = {
            "nb_professions": nb_professions,
            "nb_departements": nb_departements,
            "nb_regions": nb_regions,
            "annee_ref": 2023
        }

        professions = session.query(ProfessionSante).all()
        top_professions = []

        for p in professions:
            total = get_total_effectif(p.libelle, 2023)
            if total > 0:
                top_professions.append({
                    "libelle": p.libelle,
                    "effectif": total
                })

        top_professions = sorted(top_professions, key=lambda x: x["effectif"], reverse=True)[:5]

        return {
            "stats": stats,
            "top_professions": top_professions,
            "error": None,
        }

    except Exception as e:
        return {
            "stats": {
                "nb_professions": 0,
                "nb_departements": 0,
                "nb_regions": 0,
                "annee_ref": 2023,
            },
            "top_professions": [],
            "error": str(e),
        }

    finally:
        session.close()


@bp_data.route("/data")
@login_required
def index():
    context = get_dashboard_context()
    return render_template("data.html", **context)
