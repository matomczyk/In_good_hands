
# In good hands
The purpose of this project is to create space where everyone can donate things they don't use anymore to various institutions. 
People often have things in their houses they would like to donate, but the process is often too complicated and requires a lot of effort. In good hands allows user to easily choose what they want to donate, how many items they want to donate and choose a convenient day and time for the courier to pick up the items from their chosen location.



## Setup


To install requirements of the project execute the following command:

    $ pip install -r requirements.txt

Establish connection to a database of your choice. I used PostgreSQL for this project. Create migrations and migrate:

    $ python manage.py makemigrations then $ python manage.py migrate

To start the app:

    $ python manage.py runserver
## License

[MIT](https://choosealicense.com/licenses/mit/)

