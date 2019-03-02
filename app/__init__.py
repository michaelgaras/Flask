import code
from flask import Flask

#code.interact(local=dict(globals(), **locals()))

app = Flask(__name__)
#app = Flask(__name__.split('.')[0])

from app import routes

