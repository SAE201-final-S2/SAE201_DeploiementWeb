from flask import Flask, render_template
from config import Config
from controllers.accueil import bp_accueil
from controllers.api import bp_api
from controllers.effectifs import bp_effectifs
from controllers.informations import bp_informations
from controllers.data import bp_data
from controllers.apropos import bp_apropos
from controllers.carte import bp_carte
from controllers.comparaison import bp_comparaison
from controllers.auth import bp_auth  # <-- Ajout pour la connexion
from controllers.admin import bp_admin  # <-- Ajout pour le tableau de bord admin

app = Flask(__name__)
app.config.from_object(Config)
# Assure-toi que Config contient bien :
# ADMIN_USER = "ton_user"
# ADMIN_PASSWORD = "ton_mot_de_passe"
# SECRET_KEY = "ta_clé_secrète" (nécessaire pour les sessions)

# Enregistrement des blueprints
app.register_blueprint(bp_accueil)
app.register_blueprint(bp_api)
app.register_blueprint(bp_effectifs)
app.register_blueprint(bp_informations)
app.register_blueprint(bp_data)
app.register_blueprint(bp_apropos)
app.register_blueprint(bp_carte)
app.register_blueprint(bp_comparaison)
app.register_blueprint(bp_auth)  # Routes : /auth/login, /auth/logout
app.register_blueprint(bp_admin)  # Route : /admin/dashboard

# Gestionnaires d'erreurs
@app.errorhandler(404)
def page_non_trouvee(e):
    return render_template("erreur.html", message="Page non trouvée."), 404

@app.errorhandler(500)
def erreur_serveur(e):
    return render_template("erreur.html", message="Erreur interne. Réessayez plus tard."), 500

@app.route("/erreur")
def erreur():
    return render_template("erreur.html", message="Ceci est un message d'erreur de test.")


if __name__ == "__main__":
    app.run(debug=True)
