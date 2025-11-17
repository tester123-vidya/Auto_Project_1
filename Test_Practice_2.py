"""
Mandatory:
import pytest
from pytest import mark

Decorators are the python features starts with @
Decorator pytest will import pytest '@pytest'
mark is an in-build application with in pytest
we need to import mark from pytest
@pytest.mark.in_build markers will appear which we can use direct above a method
@@pytest.mark.marker_name (if we give any specific marker name we need to register
it in conttext.py file. Else we may get warnings while test execution

***Notes:
1. There won't be any seperate @pytest.mark.xpass

If we mark a method as @pytest.mark.xfail and while test execution it passes
the result will be printed as 'xpass'

2. if xfail test passes the results will be printed as 'xpass'

3. If you mark a method as @pytest.mark.xpass, here the xpass is going to be a user
defined marked which need to get registered in conftest.ini file.
If the test passes the results will be printed as "PASSED"

4.@pytest.mark.skipif('condition','reason')

Eg: pytest.mark.skip (system defined)
Eg: pytest.mark.smoke (customised decorators)
Eg: pytest.mark.dontask (customised decorator)

"""
import sys

#user defined decorators

import pytest
from pytest import mark

class Test_flat:

    #This test will be skipped if the Python version is less than 8.4.2
    @pytest.mark.skipif(sys.version_info<(3,12,7),reason="Requires sys version 3.12.7 or Higher")

    def test_flat_1(self):
        print(sys.version_info)
        print(sys.version)
        print("pays maintenance on time")



f = Test_flat()
f.test_flat_1()
