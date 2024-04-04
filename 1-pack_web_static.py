#!/usr/bin/python3
"""
This module generates a.tgz archive.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Compresses a folder to a .tgz archive"""
    local("sudo mkdir -p versions")
    archive = f"versions/web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
    fin = local(f"sudo tar-cvzf {archive} web_static")
    if fin.succeed:
        return archive
    else:
        return None
