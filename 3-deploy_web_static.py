#!/usr/bin/python3
""" compresses a folder to an archive """


from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.87.172.130', '52.204.105.20']

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

def deploy():
    """ creates and distributes an archive to your web servers. """
    archv = do_pack()
    if exists(archv) is False:
        return False
    final = do_deploy(archv)
    return final
