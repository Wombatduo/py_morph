#!venv/bin/python
import os

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, abort, request, make_response, render_template
from werkzeug.serving import WSGIRequestHandler

import VerbFabric
from AbstarctVerb import Person, Tense, Number

WSGIRequestHandler.protocol_version = "HTTP/1.1"
app = Flask(__name__, static_url_path="/static")

langs = {'russian': 'Русский', 'english': 'English', 'spanish': 'Español', 'german': 'Deutsche'}
default_verbs = {'english': 'be', 'spanish': 'ser', 'german': 'sein', 'russian': 'быть'}


@app.route('/')
def main():
    return app.send_static_file('index.html')


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.route('/morph')
def morph():
    return render_template('morph.html', langs=langs, verbs=default_verbs)


@app.route('/table')
def table():
    return render_template('table.html', langs=langs, verbs=default_verbs, tenses=Tense, persons=Person, numbers=Number)


@app.route('/morph/<lang>/<infinitive>', methods=['GET'])
def index(lang, infinitive):
    verb = VerbFabric.get_verb(lang, infinitive)
    resp = make_response(jsonify({'infinitive': verb.get_infinitive()}))
    return resp


@app.route('/lang/<lang>/top100', methods=['GET'])
def top100(lang):
    clazz = VerbFabric.get_verb_class(lang)
    if clazz is not None:
        return jsonify(clazz.get_top_100())
    return jsonify([])


@app.route('/morph/correct', methods=['POST'])
def correct_verb():
    lang = request.form['lang']
    infinitive = request.form['infinitive']
    infinitive__tsv = 'langs/' + lang + '/test_verbs/' + infinitive + '.tsv'
    if not os.path.exists(infinitive__tsv):
        with open(infinitive__tsv, 'w+') as tsv:
            for t in Tense:
                for n in Number:
                    for p in Person:
                        value_ = request.form["v" + str(t.value) + str(p.value) + str(n.value) + "1"]
                        # print(value_)
                        tsv.write(value_)
                        if p.value < 3:
                            tsv.write('\t')
                    tsv.write('\n')
                if n.value < 2:
                    tsv.write('\n')
    else:
        return jsonify(False)
    return jsonify([True])


# curl -i -H "Content-Type: application/json" -X POST -d '{"person":"3","number":"1"}' http://127.0.0.1:5000/morph/be
@app.route('/morph/do', methods=['POST'])
def morph_verb():
    if not 'lang' or not 'infinitive' or not 'person' or not 'number' in request.form:
        abort(400)
    lang = request.form['lang']
    infinitive = request.form['infinitive']
    person = int(request.form['person'])
    number = int(request.form['number'])
    tense = int(request.form['tense'])
    verb = VerbFabric.get_verb(lang, infinitive)
    if verb is None:
        abort(400, "Language not exists")

    return jsonify({'form': verb.morph(person, number, tense, 'M'), 'pronoun': verb.get_pronoun(person, number, 1)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # 192.168.1.69 - paps # 192.168.1.77 - wombat

# GET /morph/be HTTP/1.1
# Host: localhost:
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

# POST /morph/do HTTP/1.1
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Content-Length: 31
#
# infinitive=be&person=1&number=1
