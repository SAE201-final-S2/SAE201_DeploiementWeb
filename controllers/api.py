from flask import Blueprint, jsonify
from models.db import Session
from models.dimensions import Departement

bp_api = Blueprint("api", __name__, url_prefix="/api")

@bp_api.route("/departements/<string:region_code>") 
# Correction de region_id par region_code (c'est un string et non un int)
def departements(region_code):
    """Retourne les départements d'une région au format JSON."""
    session = Session()
    try:
        depts = (session.query(Departement)
                 .filter_by(region_code=region_code)
                 .order_by(Departement.code).all())
        return jsonify([{ "code": d.code, "libelle": d.libelle} for d in depts])
    finally:
        session.close()