#!/usr/bin/env python3
import sqlite3
import os
import sys
from .common import open_database
from ..common import Tintin


def insert_room(conn, room, desc, exits, zone):
    sql = "insert into mud_room values (NULL, '%s', '%s', '%s', '%s', NULL, NULL, NULL)" % (
        room, desc, exits, zone)
    conn.execute(sql)
    conn.commit()
    sql = "select roomno from mud_room where zone = '%s' and roomname = '%s' and description = '%s' and exits = '%s'" % (
        zone, room, desc, exits)
    row = conn.execute(sql).fetchone()
    if row:
        return row[0]
    return -1

if __name__ == "__main__":
    conn = open_database()
    roomno = insert_room(conn, sys.argv[1], sys.argv[2], sys.argv[3],
                         sys.argv[4])
    conn.close()
    tt = Tintin()
    tt.write("#var gps.roomno %d;" % (roomno))
