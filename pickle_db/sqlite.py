#!/usr/bin/env python3

import sqlite3
import pickle

sqlite3.register_converter("pickle", pickle.loads)
sqlite3.register_adapter(list, pickle.dumps)
sqlite3.register_adapter(set, pickle.dumps)

class DB:

    schema_query = "CREATE TABLE items (id integer primary key not null, a pickle, b pickle)"
    insert_query = "INSERT into items (a, b) values (?, ?)"
    update_query = "UPDATE items SET a = ?, b = ? WHERE id = ?"
    select_query = "SELECT id, a, b FROM items WHERE id = ?"

    def __init__(self):
        self.conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
        self.conn.row_factory = sqlite3.Row

        self.execute(self.schema_query)

    def execute(self, query, params=None):
        with self.conn:
            if params is None:
                return self.conn.execute(query)
            return self.conn.execute(query, params)        

    def insert(self, obj):
        try:
            self.execute(self.insert_query, obj)
        except sqlite3.IntegrityError:
            print("Duplicate key")

    def update(self, obj):
        self.conn.execute(self.update_query, obj)

    def select(self, key):
        return self.execute(self.select_query, (key,)).fetchall()


db = DB()

some_object = ([1,2,3], set([1,2,3]))


db.insert(some_object)

for row in db.select(1):
    print(row[2])
