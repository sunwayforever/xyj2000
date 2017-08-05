#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import os
import sys
from .common import open_database
from .common import normalize_exits

if __name__ == "__main__":
    conn = open_database()
    sql = "select * from mud_room"
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
        sql = "update mud_room set exits='%s' where roomno=%d" % (normalize_exits(row[3]), row[0])
        conn.execute(sql)
        conn.commit()
