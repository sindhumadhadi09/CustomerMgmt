Instructions to run the code:

Download the code from github link https://github.com/sindhumadhadi09/CustomerMgmt and go to location of the folder where this README.md file is present in CMD.
Follow the below steps in CMD prompt to run the customers management web app in Django. This uses SQLite DB.

:: Configure the Python virtual environment
py -3 -m venv customersenv
customersenv\scripts\activate

:: Install dependencies
pip install -r requirements.txt
:: Run Django migrations
python manage.py migrate
:: Run the dev server
python manage.py runserver
