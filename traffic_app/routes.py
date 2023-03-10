
"""
#from flask import Flask
from flask import render_template, current_app as app
@app.route("/")
def index():
    #Generates the home page.
    # Remove, left in to show what was here before render_template was used
    # return "Hello, World!"
    #return an HTML page by finding the page in our /templates folder:
    return render_template("index.html")

"""

"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)


@main_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        "dashboard.html",
        title="Flask-Login Tutorial",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))
