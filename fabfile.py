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
    local('virtualenv venv')
    local('source venv/bin/activate')
    local('pip install -r requirements.txt')

