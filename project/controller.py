from crypt import methods
from project import app

@app.route('/', methods=['GET'])
def hello():
    return "Hello, it's working!"

@app.route('/verPets', methods=['GET'])
    

@app.route('/cadastrarPet', methods=["POST"])
    return ''