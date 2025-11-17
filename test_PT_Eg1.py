#Pytest practice
# For Pytest 'test_' is mandatory for the file name and methods
# only if we give 'test_' the Pytest will pick up and execute the file
# Note: Only test_ (small case) not 'Test_' (Cap won't get picked up)
# Terminal : pytest (will execute the test and gives the result 3 pass)
# Terminal : pytest -rA (will give more description of the results)

def test_m1():
    print("methord1")

def test_m2():
    print("methord2")

def test_m3():
    print("methord3")

