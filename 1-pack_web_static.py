#!/usr/bin/python3
"""web server distribution
    """
from fabric.api import local
import tarfile
import os.path
import re
from datetime import datetime


def do_pack():
    """do_pack
    pack the content of the webstatic dir into a .tgz file
    in the versions dir , that this function will also create
    """
    target = local("mkdir -p versions")
    name = str(datetime.now()).replace(" ", '')
    opt = re.sub(r'[^\w\s]', '', name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(opt))
    if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(opt))
    else:
        return None
