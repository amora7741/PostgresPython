__author__ = 'DarkWeb'

import psycopg2
from psycopg2.extras import RealDictCursor

def connectDataBase():

    DB_NAME = "CPP"
    DB_USER = "postgres"
    DB_PASS = "123"
    DB_HOST = "localhost"
    DB_PORT = "5432"

    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT,
                                cursor_factory=RealDictCursor)
        return conn

    except:
        print("Database not connected successfully")

def createUser(cur, id, name, email):

    sql = "Insert into users (id, name, email) Values (%s, %s, %s)"

    recset = [id, name, email]
    cur.execute(sql, recset)

def updateUser(cur, id, name, email):

    sql = "Update users set name = %(name)s, email = %(email)s where id = " \
          "%(id)s"
    cur.execute(sql, {'name': name,
                      'email': email if email != '' else None,
                      'id': id})

def deleteUser(cur, id):

    sql = "Delete from comments where id_user = %(id)s"
    cur.execute(sql, {'id': id})

    sql = "Delete from users where id = %(id)s"
    cur.execute(sql, {'id': id})

def getUser(cur, nameUser):

    cur.execute("select * from users where name like %(nameUser)s",
                {'nameUser': '%{}%'.format(nameUser)})

    recset = cur.fetchall()

    if recset:
        return str(recset[0]['id']) + " | " + recset[0]['name'] + " | " + recset[0]['email']
    else:
        return []

def createComment(cur, id, id_user, text, datetime):

    sql = "Insert into comments (id, id_user, text, datetime) " \
          "Values (%s, %s, %s, %s)"

    recset = [id, id_user, text, datetime]

    cur.execute(sql, recset)

def updateComment(cur, id, text, datetime):

    sql = "Update comments set text = %(text)s, datetime = %(datetime)s where id = %(id)s"
    cur.execute(sql, {'text': text,
                     'datetime': datetime if datetime != '' else None,
                     'id': id})

def deleteComment(cur, id):

    sql = "Delete from comments where id = %(id)s"
    cur.execute(sql, {'id': id})

def getChat(cur):

    chat = ""

    cur.execute("SELECT users.name, comments.text, comments.datetime from comments inner join users on " 
                "comments.id_user = users.id order by datetime asc")

    recset = cur.fetchall()

    for rec in recset:
        chat += rec['name'] + " | " + rec['text'] + " | " + str(rec['datetime']) + "\n"

    return chat

def createTables(cur, conn):

    try:

        sql = "create table users(id integer not null, name character varying(255) not null, " \
              "email character varying(255) null, " \
              "constraint users_pk primary key (id))"
        cur.execute(sql)

        sql = "create table comments(id integer not null, id_user integer not null, " \
              "text character varying(255) not null, datetime timestamp(6) with time zone not null, " \
              "constraint comments_pk primary key (id), " \
              "constraint comments_users_id_fkey foreign key (id_user) references users (id))"
        cur.execute(sql)

        conn.commit()

    except:

        conn.rollback()
        print ("There was a problem during the database creation or the database already exists.")