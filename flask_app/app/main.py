import os
from flask import Flask
from dotenv import load_dotenv

# Load environment from .env file
load_dotenv()

# Config classes
from config import DevelopmentConfig, ProductionConfig

# init app
app = Flask(__name__)

# configure app based on environment
env = os.getenv('ENV', 'development') # default to development
if env == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)


# define routes
@app.route('/')
def health_check():
    return {
        "status": "healthy",
        "environment": app.config['ENV'],
        "debug": app.config['DEBUG']
    }

# run
def main():
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == '__main__':
    main()