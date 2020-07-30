from flask import Flask

app = Flask(__name__)

# Below is a list of dependencies
from app import config
from app import helpers
from app import landing
from app import user
from app import search
from app import recipe
from app import footerviews
from app import errors
