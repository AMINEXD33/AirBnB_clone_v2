#!/usr/bin/python3
"""distribute the package to all servers"""
from fabric.api import *
import os.path


env.user = 'ubuntu'
env.hosts = ["54.242.176.4", "54.162.88.196"]
env.key_filename = "~/id_rsa"


def do_deploy(archive_path):
    """do_deploy
    this function deployes the archive passed to all
    server hosts
    """
    # check if archive exists
    if not os.path.exists(archive_path):
        return False
    try:
        arc = archive_path.split("/")
        base = arc[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(base))
        main = "/data/web_static/releases/{}".format(base)
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main))
        sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True
    except:
        return False
