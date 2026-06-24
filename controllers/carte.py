from flask import Blueprint, render_template, jsonify, request
from models.db import Session
from models.dimensions import ProfessionSante
from services.ameli_api import AmeliAPI

bp_carte = Blueprint("carte", __name__)

@bp_carte.route("/carte")
def afficher_carte():
    session = Session()
    try:
        professions = session.query(ProfessionSante).order_by(ProfessionSante.libelle).all()
        return render_template("carte.html", professions=professions)
    finally:
        session.close()

@bp_carte.route("/api/carte")
def api_carte():
    profession_id = request.args.get("profession_id", type=int)
    annee = request.args.get("annee", type=int, default=2023)

    session = Session()
    try:
        prof = session.get(ProfessionSante, profession_id)
        if not prof:
            return jsonify([])
    finally:
        session.close()

    api = AmeliAPI()
    # Liste de tous les codes départements de la base
    codes = [
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

    data = []
    for code in codes:
        resultats = api.get_effectifs(prof.libelle, code, annee)
        if resultats:
            r = resultats[0]
            data.append({
                "code": code,
                "densite": r.get("densite") or 0
            })

    return jsonify(data)