#!/usr/bin/python3
"""deploys the archive into a server """


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['54.87.172.130', '52.204.105.20']


def do_deploy(archive_path):
    """ """
    if exists(archive_path) is False:
        return False
    arch = archive_path.split('/')[-1]
    arch_no_extension = '/data/web_static/releases/' + "{}".format(arch.split('.')[0])
    pat = "/tmp/" + arch
    remote_path = "/tmp/"

    try:
        put(archive_path, remote_path)
        run("mkdir -p {}/".format(arch_no_extension))
        run("tar -xzf {} -C {}/".format(pat, arch_no_extension))
        run("rm {}".format(pat))
        run("mv {}/web_static/* {}/".format(arch_no_extension, arch_no_extension))
        run("rm -rf {}/web_static".format(arch_no_extension))
        lnk = "/data/web_static/current"
        run(f"rm -rf {lnk}")
        run("ln -s {}/ {}".format(arch_no_extension, lnk))
        return True
    except:
        return False
