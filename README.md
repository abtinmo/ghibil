#Ghibil API

clone the repo 

	git clone https://github.com/abtinmo/ghibil && cd ghibil

install virtualenv package:

	python3 -m pip install virtualenv

make new virtual env and activate it:

	python3 -m virtualenv .venv && source .venv/bin/activate

install requirements:

	pip install -r requirements/local.txt


run project with:

	python3 manage.py migrate
	python3 manage.py runserver



open [localhost:8000/movies](http://localhost:8000/movies) on browser


to run tests install and run tox package:
    
    pip install tox
    tox