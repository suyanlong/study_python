import unittest


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s:%s' % self.__name, self.__score

    def __str__(self):
        return 'Student object (name:%s)' % self.__name

    def __call__(self):
        return 'Student object (name:%s)' % self.__name


if __name__ == '__main__':
    type(123)
    s = Student("suyanlong", 12)
    print s
    print s()
else:
    pass
