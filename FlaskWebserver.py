from flask import Flask, render_template, request
import logging
from pyFiles import config


def startWebserver():
    app = Flask(__name__)
    log = logging.getLogger('werkzeug')
    log.disabled = True

    @app.route("/")
    @app.route("/login")
    def login():
        return render_template("index.html")

    @app.route("/profile/<user>")
    def nycz(user):
        return render_template("profile.html", name=user)

    @app.route("/trap")
    def trap():
       return render_template("trap/trap.html")

    @app.route("/shutdown", methods= ["POST"])
    def shutdown_server():
        print("Shutdown Request via Post!")
        shutdown = request.environ.get("werkzeug.server.shutdown")
        if shutdown is None:
            raise RuntimeError("The function is unavailable!")
        else:
            shutdown()
            return "The Server is shutting down!"

    @app.route("/test")
    def test():
        return "<h1> test </h1>"

    app.run(host='0.0.0.0', port=config.port)

    if __name__ == "__main__":
        app.run(debug=True)
