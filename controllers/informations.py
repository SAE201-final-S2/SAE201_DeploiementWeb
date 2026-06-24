from flask import Blueprint, render_template

bp_informations = Blueprint("informations", __name__)

@bp_informations.route("/informations")
def index():
    return render_template("informations.html")