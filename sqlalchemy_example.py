#!/usr/bin/env python
#conding:utf-8

from sqlalchemy import create_engine, Table, MetaData, desc
from sqlalchemy.sql import select, and_, or_, not_


MYSQL_HOST = '192.168.1.253'
MYSQL_USER = 'hwef'
MYSQL_PWD = 'hwewef'
MYSQL_DBN = 'thergata'

DRIVE_PRE = 'mysql+mysqldb'
#DRIVE_PRE = 'mysql+mysqlconnector'

engine = create_engine('%s://%s:%s@%s/%s'%(DRIVE_PRE, MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DBN), encoding='utf8', echo=0,)

conn = engine.connect()



tlod = Table('your_table_name', MetaData(), autoload=True, autoload_with=engine)


def flush_old():
    s = select([tlod]).where( and_( tlod.c.device_id == None, tlod.c.id >= sid ) ).limit(200)
    result = conn.execute(s)

    upd = tlod.update().values(device_id=devid).where(tlod.c.id == i.id)
    conn.execute(upd)

    s = select([tlod.c.user_id]).where(tlod.c.device_id == devid)
    result = conn.execute(s)


def offset():
    import time
    offs = 0
    STE = 3
    while 1:
        s = select([tlod]).where( tlod.c.id >= 1490015 ).limit(STE).offset(offs)
        result = conn.execute(s)
        print result.rowcount
        for _ in result:
            print _.id, _.order_id
        offs += STE
        time.sleep(1)


#s = select([spd]).order_by(desc(spd.c.id)).limit(1)
#exe = conn.execute(s)


if __name__ == '__main__':
    pass
    #offset()


