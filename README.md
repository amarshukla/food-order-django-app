## Clone the source code on target system/server
1. git clone https://github.com/amarshukla/food-order-django-app.git
2. cd food-order-django-app
3. Activate your virtual enviornment (Preferable), ignore this step if you prefer to work without virtualenv.
4. pip install -r requirements.txt
5. python manage.py makemigrations
6. python manage.py makemigrations
7. python manage.py runserver

* in case you want to run the server in sucha way that it can be accessed over network, please replace step 7 with below step:
python manage.py runserver 0.0.0.0:8000
* You are free to run the server on any of the unreserve port. 8000 is just default port in practice.

### Developer information
Name - Amar Shukla
Email  - amarshukla123@gmail.com
Linkedin - https://www.linkedin.com/in/amarshukla123/
