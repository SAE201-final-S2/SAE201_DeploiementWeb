from flask import Blueprint, render_template
from models.db import Session
from models.dimensions import ProfessionSante, Region, Departement

bp_graphique = Blueprint("graphique", __name__)

@bp_graphique.route("/graphique")
def index():
    session = Session()
    try:
        professions = session.query(ProfessionSante).order_by(ProfessionSante.libelle).all()
        regions = session.query(Region).order_by(Region.libelle).all()
        return render_template("graphique.html", professions=professions, regions=regions)
    finally:
        session.close()