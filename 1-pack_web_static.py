#!/usr/bin/python3
""" compresses a folder to an archive """


from fabric.api import *
from datetime import datetime


def do_pack():
    """ the function to generate the archive """
    local("sudo mkdir -p versions")
    formt = datetime.now().strftime("%Y%m%d%H%M%S")
    arch = "versions/web_static_{}.tgz".format(formt)
    rez = local("sudo tar -cvzf {} web_static".format(arch))
    if rez.succeeded:
        return arch
    else:
        return None
