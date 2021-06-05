import random as r
#import pymysql
#from config import host, password, user, db_name

def probability():
    return r.random()

def YorN():
    x = r.random()
    if 0 < x < 0.25:
        return 'Absolutely no'
    elif 0.25 < x < 0.5:
        return 'No'
    elif 0.5 < x < 0.75:
        return 'Yes'
    elif 0.75 < x < 1:
        return 'Absolutely yes'
    elif x == 0.5:
        return '50/50'
    elif x == 0:
        return 'Critical no'
    elif x == 1:
        return 'Critical yes'

# def magicBall(type):
#     return config.type[r.randint(0,7)]

# def send_to_DB(data):
#     try:
#         connection = pymysql.connect(
#             host=host,
#             port=3306,
#             user=user,
#             password=password,
#             database=db_name,
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         print("Connection was sucsessful...")
#         print('#' * 30)
#         try:
#             with connection.cursor() as cursor:
#                 create_table_query = f"CREATE TABLE `message_holder`(id int AUTO_INCREMENT," \
#                                      "user_id varchar(32), chat_id varchar(32), message_number varchar(32)," \
#                                      " message_text varchar(255), PRIMARY KEY (id))"
#                 cursor.execute(create_table_query)

#                 insert_query = f"INSERT INTO `{user}`(user_id, chat_id, message_number, message_text) VALUES"\
#                                 "({data.chat.id}, {data.from_user.id}, {data.message_id},{data.chat.text});"
#                 cursor.execute(insert_query)
#                 connection.commit()
#                 print('Process ended sucsessfully...')
#                 print('#' * 30)
#         finally:
#             connection.close()
#
#     except Exception as ex:
#         print('Connection refused...')
#         print(ex)