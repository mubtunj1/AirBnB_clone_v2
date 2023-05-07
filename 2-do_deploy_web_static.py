#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers,
using the function
"""

from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ["54.146.66.65", "34.207.212.18"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Deploy web files to server"""
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive to server
        put(archive_path, '/tmp/')

        # create directory to uncompress files
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
            releases/web_static_{}/'.format(timestamp))

        # uncompress archive to new dir
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
            /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # delete archive from web server
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move files out of web_static dir
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove empty dir
        run('sudo rm -rf /data/web_static/releases/\
            web_static_{}/web_static'
            .format(timestamp))

        # delete old sym link
        run('sudo rm -rf /data/web_static/current')

        # create new sym link
        run('sudo ln -s /data/web_static/releases/\
        web_static_{}/ /data/web_static/current'.format(timestamp))
    except Exception:
        return False

        # return True if all operations successful
    return True
