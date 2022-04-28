The task was to write a test that runs from the main page to signup page.

I've extended this test a bit to fill the signup form, submit it and check if the onboarding page shown.
You may uncomment test_pitchme.py#L38-L40 to get this functionality.

In order to run the test run the following commands from the root of the project folder    

    python3 -m venv ../pitchme_venv
    
    source ../pitchme_venv/bin/activate

    pip3 install -r requirements.txt

    py.test  --alluredir=allure-report ./test_pitchme.py 
    
    allure serve allure-report