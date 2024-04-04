#!/usr/bin/python3
""" compresses a folder to an archive """


from fabric.api import *
from datetime import datetime
from os.path import exists


env.hosts = ['54.87.172.130', '52.204.105.20']

def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    remote_path = '/tmp/'
    final_path = '/data/web_static/releases' + f"{archive_path.split('.')[0]}"
    archive = archive_path.split('/')[-1]
    pat = remote_path + archive
    env.hosts = ['54.87.172.130', '52.204.105.20']
    try:
        put(archive_path, remote=remote_path)
        run(f'mkdir -p {final_path}')
        run(f'tar -xzf {pat} -C {final_path}')
        run(f"rm {pat}")
        run("mv {}/web_static/* {}/".format(final_path, final_path))
        run("rm -rf {}/web_static".format(final_path))
        lnk = '/data/web_static/current'
        run(f'rm {lnk}')
        run(f'ln -s {final_path} {lnk}')
        return True
    except Exception:
        return False

