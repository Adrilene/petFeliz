from flask import Flask

app = Flask(__name__)


from project.controller import pet
from project.controller import turma