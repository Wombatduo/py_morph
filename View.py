#!venv/bin/python
from flask import Flask, jsonify, abort, request, make_response
from werkzeug.serving import WSGIRequestHandler

from EnglishVerb import EnglishVerb

WSGIRequestHandler.protocol_version = "HTTP/1.1"
app = Flask(__name__, static_url_path="/static")

@app.route('/')
def main():
    return app.send_static_file('main.html')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/jquery-3.4.1.js')
def jquery():
    return app.send_static_file('jquery-3.4.1.js')

@app.route('/morph')
def root():
    return app.send_static_file('index.html')

@app.route('/morph/<infinitive>', methods=['GET'])
def index(infinitive):
    verb = EnglishVerb(infinitive)
    resp = make_response(jsonify({'infinitive':verb.get_infinitive()}))
    return resp

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
    app.run(host= '0.0.0.0',debug=True) # 192.168.1.69 - paps # 192.168.1.77 - wombat

# GET /morph/be HTTP/1.1
# Host: localhost:5000
# Connection: Keep-Alive
# Keep-Alive: timeout=5, max=100

# POST /morph/do HTTP/1.1
# Accept: */*
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Referer: http://localhost:5000/morph
# Content-Length: 31
# Host: localhost:5000
# Accept-Encoding: gzip, deflate
# Connection: keep-alive
# Keep-Alive: timeout=5, max=100
#
# infinitive=be&person=1&number=1