from flask import Flask, render_template, redirect, url_for
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    from routes.public_routes import public_bp
    from routes.auth_routes import auth_bp
    from routes.dashboard_routes import dashboard_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    # Custom 404
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('public/404.html'), 404

    # ── EMERGENCY LOGOUT ALL ROUTE ──
    # Visit /admin/logout-all to log out everyone
    # Change the secret key below to something only you know
    @app.route('/admin/logout-all/<secret_key>')
    def logout_all(secret_key):
        if secret_key != "seatech2026admin":
            return "Unauthorized", 403

        from services.access_code_service import logout_all_students
        logout_all_students()

        return """
        <html>
        <body style="background:#0A1F44;color:white;
                     font-family:Arial;text-align:center;
                     padding:80px;">
            <h1 style="color:#4D8CFF;">✅ All Students Logged Out</h1>
            <p>All access codes have been reset.</p>
            <p>Students will need to enter their
               access code again to log in.</p>
            <a href="/" style="color:#4D8CFF;">Go to Homepage</a>
        </body>
        </html>
        """

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)