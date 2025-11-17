"""
reason="" prints the given reason in results
reason="" can be given in arguments
@pytest.mark.skipif(condition, reason="")

"""


import pytest

class Test_flats_1:

    @pytest.mark.xfail(reason="build not ready")
    def test_flat_101(self):
        print("flat_101")

    @pytest.mark.skipif(pytest.__version__== (8,4,2),reason="the version should be 8.4.2")
    def test_flat_102(self):
        print("flat_102")
        print(pytest.version_tuple)
        print(pytest.__version__)

    @pytest.mark.skip(reason="This test is already covered in another test")
    def test_flat_103(self):
        print("flat_103")

f = Test_flats_1()
f.test_flat_101()
f.test_flat_102()
f.test_flat_103()

