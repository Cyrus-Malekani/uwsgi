from flask import Flask

def create_app():
    app = Flask(__name__)

    # Set configuration options here, if needed
    app.config['DEBUG'] = True

    # Define routes and views here
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
