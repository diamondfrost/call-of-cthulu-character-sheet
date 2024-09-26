from flask import render_template

from app.CharacterSheetPage import bp

@bp.route('/')
def index():
    return render_template('CoCCharaSheetTemplate/index.html')
