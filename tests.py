# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from mynumber import MyNumber


def test_divide():
    num = 123456789018
    inspection, check_sum = MyNumber.divide(num)
    assert inspection == 10987654321
    assert check_sum == 8


def test_validate():
    num = 123456789018
    assert MyNumber.validate(num), MyNumber.validate(num)


def test_iter():
    ct = 1
    for m in MyNumber():
        ct += 1
        assert MyNumber.validate(m), m
        if ct > 1000:
            return
    raise


def test_gets():
    count = 1000
    numbers = MyNumber.gets(count)
    assert len(numbers) == count

    for num in numbers:
        print num
        assert MyNumber.validate(num), num
