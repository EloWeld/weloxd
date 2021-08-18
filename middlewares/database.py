import sqlite3

from aiogram import types


class Database():
    def __init__(self, path_to_db="Data.db"):
        super(Database, self).__init__()
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_users(self):
        sql = 'CREATE TABLE users (id INTEGER, username varchar(255), subscription INTEGER, banned INTEGER);'
        self.execute(sql, commit=True)

    def add_user(self, user: types.User):
        sql = 'INSERT INTO users(id, username, subscription, banned) VALUES(?, ?, ?, ?)'
        params = (user.id, user.username, 0, 0)
        self.execute(sql, parameters=params, commit=True)

    def select_all_users(self):
        sql = 'SELECT DISTINCT * FROM users'
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f'{item} = ?' for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):
        sql = 'SELECT * FROM users WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def userturple_by_id(self, id):
        sql = 'SELECT * FROM users WHERE id=?'
        return self.execute(sql, parameters=(id,), fetchall=True)

    def userturple_by_username(self, username):
        sql = 'SELECT * FROM users WHERE username=?'
        return self.execute(sql, parameters=(username,), fetchall=True)

    def get_banned_users(self):
        return [user[0] for user in self.select_all_users() if user[3] != 0]

    def users_ids(self):
        return [item[0] for item in self.select_all_users()]

    def update_subscription(self, id, subscription):
        sql = "UPDATE users SET subscription=? WHERE id=?"
        return self.execute(sql, parameters=(subscription, id), commit=True)

    def update_ban(self, id, ban_count):
        sql = "UPDATE users SET banned=? WHERE id=?"
        return self.execute(sql, parameters=(ban_count, id), commit=True)

    def add_message(self, message : types.Message):
        sql = "INSERT INTO user_messages(id, message, date) VALUES(?, ?, ?)"
        params = (message.from_user.id, message.text, message.date)
        self.execute(sql, parameters=params, commit=True)

    def select_all_kitty(self):
        sql = 'SELECT * FROM cats'
        return self.execute(sql, fetchall=True)

    def count_all_kitty(self):
        sql = 'SELECT COUNT(link) FROM cats'
        return self.execute(sql, fetchall=True)

    def select_all_tracks(self):
        sql = 'SELECT * FROM music'
        return  self.execute(sql, fetchall=True)

    def count_all_tracks(self):
        sql = 'SELECT COUNT(*) FROM music'
        return  self.execute(sql, fetchall=True)


MainDB = Database()