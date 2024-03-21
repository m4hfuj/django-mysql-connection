# Django MySQL Connection
Connecting Django with MySQL localhost, 127.0.0.1

### Essential Dependencies to install in Ubuntu:

    sudo apt-get install libmysqlclient-dev
    sudo apt-get install python3-dev

### Dependencies for Python:

    pip install mysqlclient
    export MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
    export MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

#### Setting.py

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

### XAMPP Installation:

Ensure XAMPP is installed on your system and the MySQL service is running. You can download XAMPP from the official website and start the MySQL service from the XAMPP control panel.


### Creating a MySQL Database:

Before running migrations, create a MySQL database using phpMyAdmin or any MySQL client. You can create a database named 'django_test' using phpMyAdmin or the MySQL command line.


### Run migrations:
    python manage.py makemigrations
    python manage.py migrate

Note that the database user should have full access rights on the database.</s>


### Start Server:
    python manage.py runserver

Then run Xampp mysql server and you are good to go.
