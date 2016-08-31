import pymongo
from minibase7 import objects
conn = pymongo.MongoClient('mongodb://ds015194.mlab.com',15194)
# выбираем базу данных
db = conn.shopeiro
db.authenticate('stylist','stylist')
# # БД можно выбрать и так db = conn['mydb']
# # выбираем коллекцию документов
coll = db.tools
print(db.tools.distinct('typePrefix'))

# for issue in objects:
#     print(issue)


#coll.remove()
# for issue in coll.find():
#     print (issue)
# # альтернативный выбор коллекции документов coll = db['mycoll']
#
# # осуществляем добавление документа в коллекцию,
# # который содержит поля name и surname - имя и фамилия
# doc = {"name":"Иван", "surname":"Иванов"}
# coll.save(doc)
#
# # альтернативное добавление документа
# coll.save({"name":"Петр", "surname":"Петров"})
#
# # выводим все документы из коллекции coll

#
# # выводим фамилии людей с именем Петр
# for men in coll.find({"name": "Петр"})
#     print men["surname"]
#
# # подсчет количества людей с именем Петр
# print coll.find({"name": "Петр"}).count()
#
# # добавляем ко всем документам новое поле sex - пол
# coll.update({}, {"$set":{"sex": "мужской"}})
#
# # всем Петрам делаем фамилию Новосельцев и возраст 25 лет
# coll.update({"name": "Петр"}, {"surname": "Новосельцев", "age": 25})
#
# # увеличиваем всем Петрам возраст на 5 лет
# coll.update({"name": "Петр"}, {"$inc": {"age": 5}})
#
# # сбрасываем у всех документов поле name
# coll.update({}, {"$unset": {"name": 1}})
#
# # удаляем людей с возрастом более 20 лет
# # другие условия $gt - больше, $lt - меньше,
# # $lte - меньше или равно, $gte - больше или равно, $ne - не равно
# coll.remove({"age": {"$gt": 20}})
#
# # удаляем все документы коллекции
# coll.remove({})