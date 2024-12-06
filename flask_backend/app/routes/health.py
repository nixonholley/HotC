from flask import Blueprint, current_app
import psycopg2
from psycopg2 import OperationalError
from routes.utils import parse_database_uri

health_bp = Blueprint('health', __name__)

@health_bp.route('/')
def health_check():
    response = {
        "status": "healthy",
        "environment": current_app.config['ENV'],
        "debug": current_app.config['DEBUG']
    }

    if current_app.config['ENV'] != 'production':
        response['database_uri'] = current_app.config['SQLALCHEMY_DATABASE_URI']

    try:
        # Use the database connection URL stored in the environment variable
        db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
        
        # helper function to parse uri
        connection_params = parse_database_uri(db_uri)

        # Establish connection
        conn = psycopg2.connect(**connection_params) # **unpacks dict as keyword arguments

        # Close the connection after testing it
        conn.close()

        response['database'] = "Database connection successful"

    except OperationalError as e:
        response['database'] = f"Database connection failed: {str(e)}"
        
    return response