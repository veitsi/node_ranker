#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import os
import shoes
import shoesdb
import neurons

app = Flask(__name__)#,static_folder="", template_folder=""
app.debug = True

@app.route('/')
def index():
    print('here are imgs data')
    print(shoes.imgs_ext)
    return render_template('index.html', imgs=shoes.imgs_ext)


@app.route('/<int:itemid>', methods=['GET'])
def get_alts(itemid):
    a=neurons.Alts(itemid)
    print(a.ranked_items[0])
    rez=[{'src':shoes.imgs_ext[itemid]['src'],
                    'descr':shoesdb.coll[itemid]['description']}]
    ids=a.ranked_items[:3]
    for i in range(len(ids)):
        id=a.ranked_items[i]['id']
        print('id in get_alts ',id)
        rez.append({'src':shoes.imgs_ext[id]['src'],
                    'descr':shoesdb.coll[id]['description']})
    return jsonify({'alts':rez})
     # return jsonify({'alts': list(range(itemid))})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)
