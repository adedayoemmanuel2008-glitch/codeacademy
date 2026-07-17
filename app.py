from flask import Flask, render_template
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register all route blueprints
    from routes.public_routes import public_bp
    from routes.auth_routes import auth_bp
    from routes.dashboard_routes import dashboard_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    # Custom 404 error page
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('public/404.html'), 404

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)