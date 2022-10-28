from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def profile():
    data = {
        "slackUsername": "bernardchidi5", 
        "backend": True, 
        "age": 22, 
        "bio": "My name is Chidi-Bernard Emmanuel and I am a zealous learner."
    }
    json_format = json.dumps(data)

    return json_format

if __name__ == "__main__":
    app.run(port=7776)
