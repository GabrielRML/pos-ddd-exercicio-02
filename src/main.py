from flask import Flask
from infrastructure.database.init_db import init_db

from presentation.controllers.event_controller import event_bp
from presentation.controllers.participant_controller import participant_bp

def create_app():
    """
    Factory function para criar a aplicação Flask
    """
    app = Flask(__name__)
    
    app.config['DEBUG'] = True
    app.config['TESTING'] = False
    
    app.register_blueprint(event_bp, url_prefix='/api')
    app.register_blueprint(participant_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    init_db()
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
