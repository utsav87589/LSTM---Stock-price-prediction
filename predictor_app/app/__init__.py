from flask import Flask

def create_app() : 

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'scret'

    from app.routes.home import home_bp
    from app.routes.predictions import predictions_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(predictions_bp)

    return app