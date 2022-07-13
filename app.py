import flask
from flask import Flask, render_template
from flask import request
from flask.json import jsonify
import json
import chunking as chunking

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    print ("iniciando")
    return render_template('index.html')

@app.route("/chunks")
def chunks():
    frase = [request.args.get('word')]
    result = chunking.get_np(frase)
    return jsonify(result)

import os
port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port, debug=False)#map port to 5000
