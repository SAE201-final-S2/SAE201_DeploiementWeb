from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps
from config import Config

bp_auth = Blueprint("auth", __name__)

# Décorateur réutilisable pour protéger les routes
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_connecte"):
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated

@bp_auth.route("/login", methods=["GET", "POST"])
def login():
    erreur = None
    print(">>> ADMIN_USER lu :", Config.ADMIN_USER)      # ← ajoute ces deux lignes
    print(">>> ADMIN_PASSWORD lu :", Config.ADMIN_PASSWORD)
    if request.method == "POST":
        user = request.form.get("username")
        mdp  = request.form.get("password")
        print(f">>> Saisi : '{user}' / '{mdp}'")
        print(f">>> Attendu : '{Config.ADMIN_USER}' / '{Config.ADMIN_PASSWORD}'")
        if user == Config.ADMIN_USER and mdp == Config.ADMIN_PASSWORD:
            session["admin_connecte"] = True
            return redirect(url_for("admin.dashboard"))
        erreur = "Identifiants incorrects."
    return render_template("login.html", erreur=erreur)

@bp_auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("accueil.index"))