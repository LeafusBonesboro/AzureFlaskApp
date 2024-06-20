from flask import Flask, render_template
from flask_restful import Api

from .profiles import profiles_blueprint
from .api.profile import ProfileResource

# Application and Api initialization
app = Flask(__name__)
api = Api(app, prefix="/api")

# register blueprint
app.register_blueprint(profiles_blueprint)

# add resources to API
api.add_resource(ProfileResource, "/profiles")

# define a view function. 1. @app.route("/")
# Decorator (@app.route("/")):
# This line of code uses a decorator provided by Flask (@app.route("/")) to associate the / endpoint (root URL) with the index() function.
# In Flask, decorators are used to register a view function to handle HTTP requests to a specific URL pattern (endpoint)
@app.route("/")
def index():
    return render_template("index.html")



# Detailed Explanation
# Imports:

# Flask and render_template are imported from the Flask library to create the application and render HTML templates.
# Api is imported from Flask-RESTful to create RESTful API endpoints.

# Blueprints and Resources:
# profiles_blueprint and ProfileResource are imported from the application's modules. Blueprints are a way to organize your Flask application into smaller, reusable components. Resources are used in Flask-RESTful to handle API endpoints.

# Application Initialization:
# app = Flask(__name__)
# This initializes the Flask application.

# API Initialization:
# api = Api(app, prefix="/api")
# This initializes the Flask-RESTful API with a prefix of /api, meaning all API routes will start with /api.

# Register Blueprint:
# app.register_blueprint(profiles_blueprint)
# This registers the profiles_blueprint with the Flask application, allowing the routes defined in the blueprint to be included in the application.

# Add Resource:
# api.add_resource(ProfileResource, "/profiles")
# This adds a resource to the API. The ProfileResource will handle requests to the /api/profiles endpoint.

# Define View Function:
# @app.route("/")
# def index():
#     return render_template("index.html")
# This defines a view function for the root URL (/). When a GET request is made to the root URL, this function will be called, and it will render the index.html template.

# View Function
# Definition: A view function is a Python function that responds to a particular URL pattern.
# Purpose: It generates the HTTP response to be sent back to the client (browser) when a specific URL is requested.
# Responsibilities:
# Renders HTML templates using render_template.
# Returns JSON responses for API endpoints.
# Handles user input through request parameters, form data, or JSON payloads.

# Endpoint
# Definition: An endpoint is the URL pattern (route) at which a web application can be accessed.
# Purpose: It defines where clients (browsers or other applications) can interact with the web server to perform specific actions or retrieve information.
# Responsibilities:
# Identifies the location and functionality of a resource within the application.
# Can be associated with multiple HTTP methods (GET, POST, PUT, DELETE, etc.) to handle different types of requests.
# Example:
# /profile/<username> is an endpoint that serves the profile page for a specific user.
# Relationship
# Correlation: Each view function is associated with one or more endpoints/routes. When a client makes an HTTP request to an endpoint, Flask routes the request to the corresponding view function, which generates a response.
# Usage: Developers define view functions to handle specific endpoints/routes within their application. These endpoints serve as the interface through which clients interact with the application's functionality (e.g., displaying web pages, processing form submissions, serving API data).