Japan 'My Number' validate module[マイナンバー検査用モジュール]
========================================================================


日本語ドキュメント: `Japanese Document`_


Installation
-----------------

.. code-block:: bash

    $ pip install japan_holiday

Sample Code
-----------------

.. code-block:: python

    # -*- coding: utf-8 -*-
    from __future__ import absolute_import, unicode_literals
    from mynumber import MyNumber

    # Validate
    my_number = 123456789018
    print MyNumber.validate(my_number)

    # Validate MyNumber. Duplicate Disable
    for my_number in MyNumber.gets(1000):
        assert MyNumber.validate(my_number)

    # Validate MyNumber by iterator. Duplicate Enable
    for my_number in MyNumber():
        assert MyNumber.validate(my_number)


Documentation
-----------------

- `My Number Law`_
- 日本語ドキュメント: `Japanese Document`_

.. _`GoogleAPI token`: http://www.php-factory.net/calendar_form/google_api.php
.. _`White Paper`: http://qiita.com/haminiku/items/3c8f0d43d82c0d58d7da
.. _`Japanese Document`: http://qiita.com/haminiku/items/3c8f0d43d82c0d58d7da
.. _`My Number Law`: http://www.soumu.go.jp/main_content/000327387.pdf
