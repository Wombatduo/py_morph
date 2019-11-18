#!venv/bin/python
from flask import Flask, jsonify

from EnglishVerb import EnglishVerb

app = Flask(__name__)

@app.route('/morph/<infinitive>', methods=['GET'])
def index(infinitive):
    verb = EnglishVerb(infinitive)
    return jsonify({'infinitive':verb.get_infinitive()})

if __name__ == '__main__':
    app.run(debug=True)