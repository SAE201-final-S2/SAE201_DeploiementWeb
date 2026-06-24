from flask import Blueprint, jsonify, request
from models.db import Session
from models.dimensions import Departement
from services.ameli_api import AmeliAPI

bp_api = Blueprint("api", __name__, url_prefix="/api")

@bp_api.route("/departements/<string:region_code>")
def departements(region_code):
    session = Session()
    try:
        depts = (session.query(Departement)
                 .filter_by(region_code=region_code)
                 .order_by(Departement.code).all())
        return jsonify([{"code": d.code, "libelle": d.libelle} for d in depts])
    finally:
        session.close()

@bp_api.route("/evolution")
def evolution():
    profession = request.args.get("profession", "")
    dept = request.args.get("dept", "")

    if not profession or not dept:
        return jsonify([])

    api = AmeliAPI()
    data = []

    for annee in range(2015, 2024):
        resultats = api.get_effectifs(profession, dept, annee)
        if resultats:
            r = resultats[0]
            effectif = r.get("effectif") or 0
            if effectif:
                data.append({
                    "annee": annee,
                    "effectif": effectif
                })

    return jsonify(data)

@bp_api.route("/test-codes")
def test_codes():
    api = AmeliAPI()
    for code in ["00", "99", "France", "FR", "france", "75"]:
        r = api.get_effectifs("Médecins généralistes (hors médecins à expertise particulière - MEP)", code, 2023)
        if r:
            return jsonify({"code": code, "result": r})
    return jsonify({"message": "aucun code ne fonctionne"})
