#Class test not getting executed may be due to fixtures confusion
import pytest
from pytest import mark
from allure_commons import fixture


class Test_1:


    def test_m1(self):
        print('testing1')

    def test_m2(self):
        print('testing2')

a = Test_1()
a.test_m1()
a.test_m2()
