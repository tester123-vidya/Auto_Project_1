#Part 8,9,10 :

"""
If we want to execute the tests only for a particular file
pytest -rA file_name.py
Eg: pytest -rA test_PT_Eg3.py

Note: cd folder_name we will get into that folder
cd.. enter -> we will get out from that folder to previous one
same as DOS

Generating Junit XML Report:

--junit-xml=path (this will create the junit-xml style report at given path
Terminal : pytest -rA --junit-xml="test_practice_1"
This creates "test_practice_1.xml" junit-xml file
right click on it and open in browser.

this junit_xml report is used if we want to customise the reports. But in real time
generally they don't do that

Part10: Generating HTML Reports

For generating HTML Reports we need to install
Terminal: pip install pytest-html

<Pytest_Practice_1> pip install pytest-html - Installed
Highlet the project 'Pytest_Practice_1' -> click on menu -> settings
-> Under the "Pytest_Practice_1" project -> Interpretter -> + ->
python-html -> install package -> ok

To generate the html report we have to run the below flag:
Terminal: pytest --html="test_practice_1.html"

Terminal : pytest -rA --html="test_practice_1.html"
this will generate the executed test results in html_reports
"""

def test_car():
    print("meeeavooo")

def test_dog():
    print ("bavbav")
