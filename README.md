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


Then run Xampp mysql server and you are good to go.
