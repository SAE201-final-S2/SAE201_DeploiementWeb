from flask import Blueprint, render_template, jsonify
import random

bp_carte = Blueprint("carte", __name__)

@bp_carte.route("/carte")
def afficher_carte():
    return render_template("carte.html")


@bp_carte.route("/api/carte")
def api_carte():
    data = []

    # 95 départements
    for i in range(1, 96):
        code = str(i).zfill(2)
        data.append({
            "code": code,
            "densite": random.randint(10, 180)
        })

    return jsonify(data)
