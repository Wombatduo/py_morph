#!venv/bin/python
from flask import Flask, jsonify, request, abort
import enum

from EnglishVerb import EnglishVerb

app = Flask(__name__)


@app.route('/morph/<infinitive>', methods=['GET'])
def index(infinitive):
    verb = EnglishVerb(infinitive)
    return jsonify({'infinitive': verb.get_infinitive()})


@app.route('/morph/<infinitive>', methods=['POST'])
def morph_verb(infinitive):
    if not request.json or not 'person' or not 'number' in request.json:
        abort(400)
    person = int(request.json['person'])
    number = int(request.json['number'])

    verb = EnglishVerb(infinitive)
    return jsonify({'form': verb.morph(person,number,"Present",'M')})


if __name__ == '__main__':
    app.run(debug=True)
