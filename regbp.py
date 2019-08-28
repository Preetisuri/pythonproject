from flask import Flask
from home import app

regbp = Flask(__name__)
regbp.register_blueprint(app)