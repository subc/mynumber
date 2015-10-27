# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from collections import defaultdict
import random

_MIN_BASE = 10000000000
_MAX_BASE = 99999990000


class MyNumber(object):
    def __iter__(self):
        """
        return My Number Duplicate Yes
        :rtype :int
        """
        while True:
            start_value = random.randint(_MIN_BASE, _MAX_BASE)
            assert len(str(start_value)) == 11
            start_value_reverse = MyNumber._revers_int(start_value)
            check_sum = MyNumber.get_check_sum(start_value_reverse)
            assert check_sum <= 9
            my_number = start_value * 10 + check_sum
            assert len(str(my_number)) == 12
            assert str(start_value) in str(my_number)
            assert MyNumber.validate(my_number)
            yield my_number

    @classmethod
    def gets(cls, count):
        """
        return My Number Duplicate No
        :param count:
        :return:
        """
        if count > 10000000:
            raise ValueError, "count is large value"

        # generate
        result = defaultdict(int)
        loop_count = 0
        for number in cls():
            result[number] += 1
            loop_count += 1

            if loop_count > 10000000 * 10:
                raise AssertionError
            if len(result) >= count:
                return result

    @classmethod
    def validate(cls, number):
        """
        validate number

        # My Number System Laws #5
        http://www.soumu.go.jp/main_content/000327387.pdf
        :param number: int
        :rtype : bool
        """
        cls._check(number)
        inspection, check_sum = cls.divide(number)
        return bool(cls.get_check_sum(inspection) == check_sum)

    @classmethod
    def get_check_sum(cls, inspection):
        """
        calc check sum from inspection
        :param inspection: int
        :rtype : int
        """
        def q(_n):
            if 1 <= _n <= 6:
                return n + 1
            if 7 <= _n <= 11:
                return _n - 5
            raise ValueError, "N is invalid data", _n

        n = 1
        _result = 0
        for p in list(str(inspection)):
            p = int(p)
            print p, n, q(n)
            _result += p * q(n)
            n += 1
        surplus = _result % 11
        if surplus <= 1:
            return 0
        return 11 - surplus

    @classmethod
    def divide(cls, number):
        """
        Divide My Number to inspection and check sum
        :param number: int
        :rtype : list(int, int)
        """
        # print "divide", number
        cls._check(number)
        check_sum = int(str(number)[11])
        _base = int(str(number)[0:11])
        print "divide", number, _base, check_sum
        inspection = cls._revers_int(_base)
        print "divide", number, _base, check_sum, inspection
        return inspection, check_sum

    @classmethod
    def _revers_int(cls, number):
        """
        from 123456 to 654321
        :param number: int
        :rtype : int
        """
        _base = list(str(number))
        _base.reverse()
        return int("".join(_base))

    @classmethod
    def _check(cls, number):
        if type(number) is not int:
            raise TypeError

        if len(str(number)) != 12:
            raise ValueError, "number must be 12-digit:{}".format(str(number))
