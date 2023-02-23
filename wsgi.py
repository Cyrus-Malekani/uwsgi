from app import create_app

# Create the Flask application instance
app = create_app()

# Define the entry point for uWSGI to run the application
def application(env, start_response):
    # Call the Flask application with the WSGI environment and start response objects
    return app(env, start_response)
