#!/usr/bin/python3
""" deploys archives to a server """


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['54.87.172.130', '52.204.105.20']


def do_deploy(archive_path):
    """ distributes archives to web servers
    """
    if exists(archive_path) is False:
        return False
    filen = archive_path.split('/')[-1]
    no_ext = '/data/web_static/releases/' + "{}".format(filen.split('.')[0])
    temp = "/tmp/" + filen

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_ext))
        run("tar -xzf {} -C {}/".format(temp, no_ext))
        run("rm {}".format(temp))
        run("mv {}/web_static/* {}/".format(no_ext, no_ext))
        run("rm -rf {}/web_static".format(no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_ext))
        return True
    except:
        return False
