from flask import render_template
from app.HomePage import bp

@bp.route('/')
def index():
    return render_template('index.html')