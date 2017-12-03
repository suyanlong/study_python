#! /usr/bin/env python2
# -*- coding:utf-8 -*-


# pip install leveldb

import leveldb

# python版本的leveldb接口比较少，就几个增删查改，以及批量操作，使用比较简单。
def single():
    db = leveldb.LevelDB('./data')
    db.Put('foo', 'suyanlong')
    print(db.Get('foo'))
    db.Delete('foo')
    print(db.Get('foo'))


def clear_db():
    db = leveldb.LevelDB('./data')
    db.Put('foo', 'suyanlong')
    db.Put('foo1', 'suyanlong')
    db.Put('foo2', 'suyanlong')
    db.Put('foo3', 'suyanlong')
    db.Put('foo4', 'suyanlong')
    b = leveldb.WriteBatch()
    for k in db.RangeIter(include_value = False, reverse = True):
        print(k)
        b.Delete(k)
    db.Write(b)


if __name__ == '__main__':
    # single()
    clear_db()
