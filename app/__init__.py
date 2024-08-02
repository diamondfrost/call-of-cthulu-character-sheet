from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Initialize Flask extensions here
    
    # Register blueprints here
    from app.HomePage import bp as home_bp
    app.register_blueprint(home_bp)
    
    from app.CharacterSheetPage import bp as chara_sheet_bp
    app.register_blueprint(chara_sheet_bp, url_prefix='/coc-character')
    
    @app.route('/test/')
    def test_page():
        return '<h1>This is a test page.</h1>'
    
    return app
    