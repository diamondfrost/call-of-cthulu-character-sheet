from flask import Blueprint

bp = Blueprint('character_sheet', __name__)

from app.CharacterSheetPage import routes