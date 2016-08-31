#!/usr/bin/env python
#!-*- coding: utf-8 -*-
from lxml import etree
from checker import img_exists

def key2value_str(key, value):
    return "'" + key + "':'" + str(value) + "'"


assert key2value_str('_id', 123456) == "'_id':'123456'"


def lamoda_pathandfile(url):
    return url[19:]


def node2json(node):
    rez = "{"
    # print(node.tag, node.keys(), node.values())
    rez += key2value_str('_id', node.get('id')[:14])
    pictures_mode = False
    for subnode in node:
        # print(subnode.tag, subnode.keys(), subnode.values(), subnode.text)
        if pictures_mode and subnode.tag != 'picture':
            pictures_mode = False
            rez = rez + "]"
        if subnode.tag == 'typePrefix' or subnode.tag == 'description':
            rez = rez + ',' + key2value_str(subnode.tag, subnode.text.translate(str.maketrans( '\'\"',"  ")))
        elif subnode.tag == 'picture' and img_exists(subnode.text):
            # fp.write(lamoda_pathandfile(subnode.text) + "\n")
            if pictures_mode:
                rez = rez + ",'" + subnode.text[31:] + "'"
            else:
                pictures_mode = True
                rez = rez + ",'pictures':['" + subnode.text[31:] + "'"
        elif subnode.tag == "param" and len(subnode.keys()) != 2:
            rez = rez + "," + key2value_str(subnode.values()[0].lower(), subnode.text)

    return rez


def issue_size(node):
    for subnode in node:
        if len(subnode.values()) == 2:
            return subnode.text


def issue_price(node):
    for subnode in node:
        if subnode.tag == 'price':
            return float(subnode.text)


# yml parser
tree = etree.parse('1405344794565foi.xml')
# tree = etree.parse('minibase-lamoda.xml')
nodes = tree.xpath('/yml_catalog/shop/offers/offer')
folded_nodes = {}
prices = {}
sizes = {}
jsons = {}
issues_count=0
print(len(nodes))
fb = open("fullbase.py", "w")
fp = open("pictures.txt", "w")
fb.write("objects=[\n")
for i in range(len(nodes)):  # Перебираем элементы
    # print(node2json(nodes[i]))
    current = nodes[i].get('id')[:14]
    current_price = issue_price(nodes[i])
    current_size = issue_size(nodes[i])
    if current not in folded_nodes:
        issues_count+=1
        # if issues_count>200:
        #     break
        folded_nodes[current] = 1
        prices[current] = current_price
        sizes[current] = "'"+current_size+"'"
        jsons[current] = node2json(nodes[i])
    else:
        folded_nodes[current] += 1
        if current_price > prices[current]:
            print(current)
            prices[current] = current_price
        sizes[current] = sizes[current] + ",'" + current_size+"'"
    # print(current, issue_price(nodes[i]), issue_size(nodes[i]), jsons[current])  # nodes[i].get('id'),

# print(len(folded_nodes))
# print(folded_nodes)
# print(prices)
# print(sizes)
import pymongo
conn = pymongo.MongoClient('mongodb://ds015194.mlab.com',15194)
# выбираем базу данных
db = conn.shopeiro
db.authenticate('shopeiro','shopeiro')
# # БД можно выбрать и так db = conn['mydb']
# # выбираем коллекцию документов
coll = db.tools
coll.remove()

for current in folded_nodes.keys():
    json = jsons[current] + ",'price':'" + str(prices[current]) + "','sizes':[" + sizes[current] + "]}"
    # print(json)
    issue=eval(json)
    print(issue)
    coll.save(issue)

    if current != list(folded_nodes.keys())[-1]:
        fb.write(json + ",\n")
    else:
        fb.write(json + "\n")

fb.write("]")
fb.close()
fp.close()
