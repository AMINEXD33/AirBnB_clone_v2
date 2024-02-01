#!/usr/bin/python3
"""
   just a simple use case of fabric to run some tasks
"""
from fabric import task
import datetime


def get_date_formated():
    """get_date_formated
    return the string that represent
    Year month day hour minuts seconds
    """
    formated = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return (formated)


@task
def do_pack(c):
    """do_pack
    pack the content of the webstatic dir into a .tgz file
    in the versions dir , that this function will also create
    """
    file_name = f"web_static_{get_date_formated()}.tgz"
    c.local("mkdir versions")
    c.local(f"tar -cvzf /versions/{file_name} web_static")
    return (f"/versions/{file_name}")
