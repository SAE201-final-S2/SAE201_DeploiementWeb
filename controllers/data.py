from flask import Blueprint, render_template
from controllers.auth import login_required
from models.db import Session
from models.dimensions import ProfessionSante, Departement, Region
from services.ameli_api import AmeliAPI
from concurrent.futures import ThreadPoolExecutor, as_completed

bp_data = Blueprint("data", __name__)

CODES_DEPTS = [
    "01","02","03","04","05","06","07","08","09","10",
    "11","12","13","14","15","16","17","18","19","21",
    "22","23","24","25","26","27","28","29","2A","2B",
    "30","31","32","33","34","35","36","37","38","39",
    "40","41","42","43","44","45","46","47","48","49",
    "50","51","52","53","54","55","56","57","58","59",
    "60","61","62","63","64","65","66","67","68","69",
    "70","71","72","73","74","75","76","77","78","79",
    "80","81","82","83","84","85","86","87","88","89",
    "90","91","92","93","94","95"
]

def get_total_effectif(profession_libelle, annee):
    api = AmeliAPI()
    total = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {
            executor.submit(api.get_effectifs, profession_libelle, code, annee): code
            for code in CODES_DEPTS
        }
        for future in as_completed(futures):
            try:
                resultats = future.result()
                if resultats:
                    effectif = resultats[0].get("effectif", 0) or 0
                    total += effectif
            except Exception:
                pass
    return total


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

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {
                executor.submit(get_total_effectif, p.libelle, 2023): p.libelle
                for p in professions
            }
            for future in as_completed(futures):
                libelle = futures[future]
                try:
                    total = future.result()
                    if total > 0:
                        top_professions.append({
                            "libelle": libelle,
                            "effectif": total
                        })
                except Exception:
                    pass

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