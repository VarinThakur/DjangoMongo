An app to show Django connecting with Mongo DB to plot graphs.

To run the app-

1. Ensure you're running python 3.11
    `python --version`

2. Install virtualenv to create a virtual environment
    `pip install virtualenv`

3. Create a virtual environment
    `virtualenv env`

4. Activate the virtual environment

    On Windows
    `\env\Scripts\activate`

    On Linux
    `env/Scripts/activate.sh`

5. Install the required dependencies
    `pip install -r requirements.txt`

6. Go to the djMon directory

    `cd djMon`

7. Initialise MongoDB database using MongoDB compass / mongosh

8. Run the App 

    `python manage.py runserver`