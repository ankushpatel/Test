from __future__ import with_statement
from fabric.api import local, env, settings, abort, local, cd, prefix
from fabric.operations import sudo
from fabric.contrib.console import confirm
from fabric.contrib.files import append, sed
import time
import os
env.hosts = ['127.0.0.1']
env.user = 'ubuntu'
env.key_filename = "~/Downloads/ankush.pem"


def update_apt_get():
    local('sudo apt-get update')


def install_pip():
    with settings(warn_only=True):
        local("wget https://bootstrap.pypa.io/get-pip.py")
        local("sudp python get-pip.py")
        local('pip -V')


def install_postgres_all_components():
    local('sudo apt-get install postgresql -y')
    local('sudo apt-get install postgresql-9.3-postgis-2.1 postgresql-contrib-9.3 postgresql-server-dev-9.3 -y')


def install_python_utils():
    local('sudo apt-get install python-pip python-dev build-essential -y')


def install_virtualenv():
    local('sudo pip install virtualenv')


def install_gunicorn():
    local('sudo pip install gunicorn psycopg2')


def install_git():
    local('sudo apt-get install git -y')


# def git_clone_and_setup():
#     with settings(warn_only=True)
#         with cd('~'):
#             local("git clone https://github.com/bhiwalakhil/odyssey.git")
#         with cd('~/odyssey'):
#             local('pip install -r requirements.txt')


def setup_timezone_to_ist():
    local("sudo timedatectl set-timezone 'Asia/Kolkata'")


def postgres_create_user():
    with settings(warn_only=True):
        local('sudo -u postgres createuser -P odyssey')
        local('sudo -u postgres createdb -O odyssey iote_odyssey')
        local('sudo -u postgres creatdeb -O odyssey testing_odyssey')


def install_all():
    update_apt_get()
    install_pip()
    install_python_utils()
    install_virtualenv()
    install_git()
    install_postgres_all_components()
    local('echo ****Installation Done****')


def setup_all():
    # git_clone_and_setup()
    local('pip install -r requirements.txt')
    postgres_create_user()
    setup_timezone_to_ist()
    test_mode()
    local('echo ****Setup Done****')


def test_mode():
    local('pwd')
    local('cd ./tests')
    local('python test_models.py')


def run_server():
    local('sh runserver.sh &')


def run_curl():
    local('curl http://54.169.175.156/')
