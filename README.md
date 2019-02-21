# Django Dynamic Form

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

"Django Dynamic Form" enables inserting a form within a form. 

### Quick install
Assuming django and pipenv is installed:
```sh
$ git clone https://github.com/alvarolloret/django_dynamic_form
$ cd django_dynamic_form
$ pipenv install
$ python manage.py migrate
$ python manage.py runserver
```

### Usage 

|  N | Step  | Image  |
| ---|:------| -----|
| 1. | Go to [http://127.0.0.1:8000/backtest/dynamic/](http://127.0.0.1:8000/backtest/dynamic/). The following webpage should show: | <img src="https://github.com/alvarolloret/django_dynamic_form/blob/master/static/images/index.PNG" width="60%"></img> |
| 2. | It is possible to modify the details dynamically when clicking on the button "Modify details": |  <img src="https://github.com/alvarolloret/django_dynamic_form/blob/master/static/images/modify_details.PNG" width="60%"></img> |
| 3. | Finally, the data is saved in the following form:  |  <img src="https://github.com/alvarolloret/django_dynamic_form/blob/master/static/images/database.PNG" width="100%"></img>|


