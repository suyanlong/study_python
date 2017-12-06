#! /usr/bin/env python2
# -*- coding:utf-8 -*-

class Student(object):
    name = 'student'


s = Student()
print(s.name)
print(Student.name)

s.name = "s.name"
print(s.name)
print(Student.name)

del s.name
print(s.name)
print(Student.name)

del Student.name
print(s.name)
print(Student.name)



