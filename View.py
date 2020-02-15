#!venv/bin/python
from flask import Flask, jsonify, abort, request

from EnglishVerb import EnglishVerb

app = Flask(__name__, static_url_path="/static")

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/morph')
def root():
    return app.send_static_file('index.html')

@app.route('/morph/<infinitive>', methods=['GET'])
def index(infinitive):
    verb = EnglishVerb(infinitive)
    return jsonify({'infinitive':verb.get_infinitive()})

# curl -i -H "Content-Type: application/json" -X POST -d '{"person":"3","number":"1"}' http://127.0.0.1:5000/morph/be
@app.route('/morph/do', methods=['POST'])
def morph_verb():
    if not 'infinitive' or not 'person' or not 'number' in request.form:
        abort(400)
    infinitive = request.form['infinitive']
    person = int(request.form['person'])
    number = int(request.form['number'])
    verb = EnglishVerb(infinitive)

    return jsonify({'form':verb.morph(person,number,"Present",'M')})

if __name__ == '__main__':
    app.run(host= '192.168.1.69',debug=True) # 192.168.1.69 - paps # 192.168.1.77 - wombat