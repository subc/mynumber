# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from mynumber import MyNumber


def test_divide():
    num = 123456789018
    inspection, check_sum = MyNumber.divide(num)
    assert inspection == 10987654321
    assert check_sum == 8


def test_validate():
    num_group = [
        123456789018,
        190852597007,
        664559681879,
        317115269465,
        636234891610,
        759492641118,
        653148356959,
        712502608231,
        845344637296,
        626150900081,
        250059391352,
        220009988475,
        518472892796,
        971973656959,
        142943093120,
        661945516417,
        275391807883,
        422468354448,
        345381273668,
        282612367782,
        993274102186,
        101951472043,
        288204947884,
        459810701741,
        673630519726,
        428367052872,
        656861725106,
        559958524339,
        727514382775,
        858986774968,
        633284231620,
        457474026230,
    ]

    for num in num_group:
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
