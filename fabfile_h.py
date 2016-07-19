from __future__ import with_statement
from fabric.api import local, env, settings, abort, run, cd, prefix
from fabric.operations import sudo
from fabric.contrib.console import confirm
from fabric.contrib.files import append, sed
import time
import os
env.hosts = ['127.0.0.1']
env.user = 'ubutnu'
env.key_filename = "~/Downloads/ankush.pem"
#fabfile

def system_info():
    local("echo SYSTEM")
    local("uname -a")
    local('pip install -r requirements.txt')
    local('sudo apt-get update')

def postgres_create_user():
    with settings(warn_only=True):
        local('sudo -u postgres createuser -P odyssey')
        local('sudo -u postgres createdb -O odyssey iote_odyssey')
        local('sudo -u postgres creatdeb -O odyssey testing_odyssey')
