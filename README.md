# Django MySQL Connection
Connecting Django with MySQL localhost, 127.0.0.1

### Essential Dependencies to install in Ubuntu:
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install python3-dev

### Dependencies for Python:
    pip install mysqlclient
    export MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
    export MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

### XAMPP Installation:
Ensure XAMPP is installed on your system and the MySQL service is running. You can download XAMPP from the official website and start the MySQL service from the XAMPP control panel.

### Start Xampp Server
    sudo service mysql stop
    sudo /opt/lampp/manager-linux-x64.run

#### If Apache server not working

For Ubuntu:

    sudo systemctl stop apache2

### Creating a MySQL Database:
Before running migrations, create a MySQL database using phpMyAdmin or any MySQL client. You can create a database named 'django_test' using phpMyAdmin or the MySQL command line.

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

Note that the database user should have full access rights on the database.</s>

### Run migrations:
    python manage.py makemigrations
    python manage.py migrate

### Start Django Server:
    python manage.py runserver


