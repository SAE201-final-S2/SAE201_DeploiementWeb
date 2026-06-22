from flask import Blueprint, jsonify, request
from models.db import Session
from models.dimensions import Departement
from services.ameli_api import AmeliAPI

bp_api = Blueprint("api", __name__, url_prefix="/api")
api_ameli = AmeliAPI()

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

@bp_api.route("/evolution")
def evolution():
    """Retourne l'évolution des effectifs pour le graphique Plotly."""
    profession_libelle = request.args.get("profession")
    departement_code = request.args.get("dept")
    
    if not profession_libelle or not departement_code:
        return jsonify({"error": "Paramètres manquants"}), 400
        
    donnees = api_ameli.get_evolution_effectifs(profession_libelle, departement_code)
    return jsonify(donnees)