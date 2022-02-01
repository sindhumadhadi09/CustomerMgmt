**Instructions to run the code:**

Download the code from github link https://github.com/sindhumadhadi09/CustomerMgmt and go to location of the folder where this README.md file is present in CMD.
Follow the below steps in CMD prompt to run the customers management web app in Django. This uses SQLite DB.
The instructions below are for Windows.

**step 1: Configure the Python virtual environment**

py -3 -m venv customersenv 

**Step2 : Activate Environment**

customersenv\scripts\activate

**step3 :Install dependencies**

pip install -r requirements.txt

**step4:Run Django migrations**

python manage.py migrate

**step5:Run the dev server**

python manage.py runserver
