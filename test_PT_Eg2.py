"""
* Verifying assertion conditions
* Assertions are the conditions mentioned inside the methods
* If Assertion condition passes test passes
* _ _ eq _ _ (refers to equal to for strings)
* syntax: var1.--eq__(var2), " " for comments
* For giving comments in Assertion end the statement with ; and use " "
* comments which we give in Assertion are Assertion error, these Assertion
 errors will apear in the test results
* Only when the assertion fails the assertion errors or comments will get printed
for the passed conditions the messages wont get displayed in results
* pytest -k ass (keyword) will print all the 4 tests


"""

def test_ass1():
    a = 10
    b = 10
    assert a == b

def test_ass2():
    c = 20
    d = 30
    assert c < d

def test_ass3():
    e = 'vidya'
    f = 'nand'
    assert e.__eq__(f), "e is not equal to f "

def test_ass4():
    g = 'rita'
    h = 'rita'
    assert g.__eq__(h), "g is equal to h"




