from flask import Blueprint, render_template
from controllers.auth import login_required
from models.db import Session
from models.dimensions import ProfessionSante, Departement

bp_admin = Blueprint("admin", __name__)

@bp_admin.route("/admin")
@login_required
def dashboard():
    session_db = Session()
    try:
        nb_professions = session_db.query(ProfessionSante).count()
        nb_departements = session_db.query(Departement).count()
        return render_template("page_admin.html",
            nb_professions=nb_professions,
            nb_departements=nb_departements
        )
    finally:
        session_db.close()