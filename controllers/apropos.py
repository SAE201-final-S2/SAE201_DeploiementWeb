from flask import Blueprint, render_template

bp_apropos = Blueprint("apropos", __name__)

@bp_apropos.route("/apropos")
def index():
    return render_template("apropos.html")