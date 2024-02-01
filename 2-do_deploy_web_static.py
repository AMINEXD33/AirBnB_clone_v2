#!/usr/bin/python3
"""distribute the package to all servers"""
from fabric.api import *
import os.path


env.user = 'ubuntu'
env.hosts = ["54.242.176.4", "54.162.88.196"]
env.key_filename = "my_ssh_private_key"


def do_deploy(archive_path):
    """do_deploy
    this function deployes the archive passed to all
    server hosts
    """
    # check if archive exists
    if not os.path.exists(archive_path):
        return False

    try:
        ar = archive_path.split("/")
        bs = archive_path[1].strip('.tgz')

        # upload to host
        put(archive_path, '/tmp/')
        # make a new dir in the hosts
        sudo(f'mkdir -p /data/web_static/releases/{bs}')

        path = f"/data/web_static/releases/{bs}"
        sudo('rm /tmp/{}'.format(ar[1]))
        sudo('mv {}/web_static/* {}/'.format(path, path))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(path))
        return True
    except:
        return False
