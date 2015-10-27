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
            seed = random.randint(_MIN_BASE, _MAX_BASE)
            seed_reverse = MyNumber._revers_int(seed)
            my_number = seed * 10 + MyNumber.get_check_sum(seed_reverse)
            yield my_number

    @classmethod
    def gets(cls, count):
        """
        return My Number Duplicate No
        :param count:
        :return:
        """
        _max = 10000000
        if count > _max:
            raise ValueError, "count is large value"

        # generate My Number by Duplicate No
        result = defaultdict(int)
        depth = 0
        for number in cls():
            result[number] += 1
            if len(result) >= count:
                return result
            if depth > _max * 100:
                raise ValueError
            else:
                depth += 1

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

        n = 12 - len(str(inspection))
        _result = 0
        for p in list(str(inspection)):
            _result += int(p) * q(n)
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
        cls._check(number)
        check_sum = int(str(number)[11])
        inspection = cls._revers_int(int(str(number)[0:11]))
        return inspection, check_sum

    @classmethod
    def _revers_int(cls, number):
        """
        from 123456 to 654321
        :param number: int
        :rtype : int
        """
        return int(str(number)[::-1])

    @classmethod
    def _check(cls, number):
        if type(number) is not int:
            raise TypeError

        if len(str(number)) != 12:
            raise ValueError, "number must be 12-digit:{}".format(str(number))
