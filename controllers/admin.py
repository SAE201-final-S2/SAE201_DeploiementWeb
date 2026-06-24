from flask import Blueprint, render_template
from controllers.auth import login_required
from controllers.data import get_dashboard_context

bp_admin = Blueprint("admin", __name__)

@bp_admin.route("/admin")
@login_required
def dashboard():
    context = get_dashboard_context()
    return render_template("page_admin.html", **context)