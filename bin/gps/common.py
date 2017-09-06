#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sqlite3
from ..common import open_gps_database
from ..common import logger


def open_database():
    return open_gps_database()


area_alias = []

room_alias = {
    "地下暗室": 2158,
    "小木屋": 2048,
}

def fixup_area(desc):
    for [k, v] in area_alias:
        if re.match("^%s" % (k), desc):
            if not re.match("^%s" % (v), desc) or k.startswith(v):
                desc = "%s%s" % (v, desc[len(k):])
                break
    return desc


def fixup_room(zone, room, desc, exits):
    return zone, room, desc, exits


def get_zone(conn, room):
    sql = "select zone from mud_room where roomno = %d" % (room)
    row = conn.execute(sql).fetchone()
    if row:
        return row[0]
    else:
        return "nil"


def normalize_exits(exits):
    exits = exits.strip(";").split(";")
    exits.sort()
    return ";".join(exits)
