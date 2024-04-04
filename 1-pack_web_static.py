#!/usr/bin/python3
"""
This module generates a.tgz archive.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Compresses a folder to a .tgz archive"""

    fold = 'web_static'
    arch = f'web_static_{datetime.now().strftime("%Y%m%d%H%M%S")}.tgz'
    local('mkdir -p versions')
    fin = local(f'tar -cvzf versions/{arch} {fold}')
    if fin.succeeded:
        return f'versions/{arch}'
    else:
        return None
