from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import __init_app__

# run
def main():
    app = __init_app__()
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == '__main__':
    main()