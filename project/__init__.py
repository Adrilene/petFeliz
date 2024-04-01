from flask import Flask

app = Flask(__name__)


from project.controller import pets
from project.controller import turmas