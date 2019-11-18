#!venv/bin/python
from flask import Flask, jsonify, abort, request

from EnglishVerb import EnglishVerb

app = Flask(__name__)

@app.route('/morph/<infinitive>', methods=['GET'])
def index(infinitive):
    verb = EnglishVerb(infinitive)
    return jsonify({'infinitive':verb.get_infinitive()})

# curl -i -H "Content-Type: application/json" -X POST -d '{"person":"3","number":"1"}' http://127.0.0.1:5000/morph/be
@app.route('/morph/<infinitive>', methods=['POST'])
def morph_verb(infinitive):
    if not request.json or not 'person'  or not 'number' in request.json:
        abort(400)
    person = int(request.json['person'])
    number = int(request.json['number'])
    verb = EnglishVerb(infinitive)

    return jsonify({'infinitive':verb.morph(person,number,"Present",'M')})

if __name__ == '__main__':
    app.run(debug=True)