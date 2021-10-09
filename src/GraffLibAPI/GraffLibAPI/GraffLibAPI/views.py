"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from GraffLibAPI import app

@app.route('/password')
def password_reset_unauthenticated():
    """Renders the contact page."""
    return render_template(
        'password-recovery/password-reset-unauthenticated.html',
        title='GraffLib - Password Reset',
        year=datetime.now().year,
    )