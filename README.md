1.  Git clone
    git clone git@github.com:lakshyasharma27/sms.git

2.  Create a python environment
    python3 -m pip install --user virtualenv
	python3 -m venv env
	source env/bin/activate
	
3.  Install python packages
    pip install -r requirements.txt

4.  Run makemigrations and migrate
    python manage.py makemigrations
    python manage.py migrate

5.  Run the server
    python manage.py runserver

'''
Basic Gits

    Adding new files
    1.  git add <file1> <file2>
    2.  git commit -m "message"
    3.  git push -u origin master

    Remove files
    1.  git rm <file1> <file2>
    2.  git commit -m "message"
    3.  git push -u origin master

    Pull Latest changes
    1. git pull origin master

git log
git status

'''