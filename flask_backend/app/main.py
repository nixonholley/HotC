from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import __init_app__

# run
def main():
    # # better to init oustide of function to avoid cyclic imports
    db = SQLAlchemy()
    app = __init_app__(db)
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == '__main__':
    main()