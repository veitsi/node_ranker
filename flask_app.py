#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_file, \
    abort, request, jsonify, redirect, url_for, send_from_directory
import base64
import random, string, os, datetime
import transer
import fragments

app = Flask(__name__)
local_mode = os.getenv('USER') == 'pydev'
app.config['UPLOAD_FOLDER'] = \
    '/home/shopeiro/fmedia/static/uploads'  # default for pythonanywhere
if local_mode:
    print('start in local mode')
    app.config['UPLOAD_FOLDER'] = 'static/uploads/'


def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def log(msg):
    f = open("log.txt", "a")
    f.write(str(datetime.datetime.now().isoformat()) + ":" + msg + "\n")
    f.close()


@app.route('/')
def hello_world():
    log('we start /')
    # return "hello"
    return render_template('index.html')


@app.route('/pics')
def pics():
    return render_template('pics.html')


@app.route('/static/pics/<string:jpgfile>', methods=['GET'])
def pic(jpgfile):
    print('you ask for picure')
    jpgfile = jpgfile[:-3] + 'jpg'
    pathtopng = 'static/pics/'
    pngfile = pathtopng + jpgfile[:-3] + 'png'
    log('we look for jpg' + jpgfile)
    # abort(404)
    if os.path.exists(pngfile):
        try:
            return send_file(pngfile)
        except:
            abort(404)
    transer.save_transp(jpgfile, pngfile)
    return send_file(pngfile)


@app.route('/resize')
def hello_resize():
    return render_template('resize-test.html')


@app.route('/looks')
def looks():
    log('we are in  ' + os.getcwd())
    log('search for files in ' + app.config['UPLOAD_FOLDER'])
    return render_template("looks.html", files=os.listdir(app.config['UPLOAD_FOLDER']))


@app.route('/upload', methods=['GET'])
def upload_start():
    print("upload page")
    return render_template("upload.html")


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    img = request.form['img'][22:]
    fname = app.config['UPLOAD_FOLDER'] + "/" + randomword(20) + '.png'
    log('we try to save in ' + fname)
    f = open(fname, 'wb')
    f.write(base64.b64decode(img))
    f.close()
    log(fname + " Uploaded")


# make comment for pythonanywhere
if __name__ == "__main__":
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host, debug=True)
