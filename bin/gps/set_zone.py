#!/usr/bin/env python3
import sqlite3
import os
import sys
from .common import open_database
from .insert_room import insert_room

def set_zone (conn, roomno, zone):
    sql = "update mud_room set zone2 = '%s' where roomno = %d" % (zone, roomno)
    conn.execute(sql)
    conn.commit()

if __name__ == "__main__":
    conn = open_database()
    set_zone (conn, int(sys.argv[1]), sys.argv[2])
    conn.close()
