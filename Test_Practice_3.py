"""
Marked the methods as xtestfail and executed.
As all the tests are passed we will get xPass results
Terminal : pytest Test_Practice_3.py -rX

"""

import pytest


class Test_flats:

    @pytest.mark.xfail
    def test_flat_301(self):
        print("flat_301")

    @pytest.mark.xfail
    def test_flat_302(self):
        print("flat_302")

    @pytest.mark.xfail
    def test_flat_303(self):
        print("flat_303")

flats = Test_flats()
flats.test_flat_301()
flats.test_flat_302()
flats.test_flat_303()


