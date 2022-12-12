
import pymongo


db_client = pymongo.MongoClient("mongodb://localhost:27017/")

current_db = db_client['board_db']

collection = current_db['bulletin_board']

first_board = {
    'user':
        {'first_name': 'John',
         'last_name': 'Jones'},
    'board':
        {'title': 'First board',
         'description': 'first_board',
         'price': '976452',
         'date_added': '2020-10-20',
         'date_delete': '2020-10-25'}
}

second_board = {
    'user':
        {'first_name': 'Mike',
         'last_name': 'Tyra'},
    'board':
        {'title': 'Second board',
         'description': 'second_board',
         'price': '368841',
         'date_added': '2020-11-18',
         'date_delete': '2020-12-20'}
}

third_board = {
    'user':
        {'first_name': 'Stevie',
         'last_name': 'Church'},
    'board':
        {'title': 'Third board',
         'description': 'third_board',
         'price': '324459',
         'date_added': '2020-10-11',
         'date_delete': '2020-10-15'}
}

ins_res1 = collection.insert_one(first_board)
ins_res2 = collection.insert_one(second_board)
ins_res3 = collection.insert_one(third_board)

#вывод всех объявлений
for board in collection.find():
    print(board)

collection.find({'user': {'first_name': 'Mike'}})
collection.find({'board': {'date_added': '2020-10-11'}})
collection.find({'board': {'date_delete': '2020-12-20'}})
