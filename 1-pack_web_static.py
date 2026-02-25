#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the web_static folder."""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Pack the contents of web_static into a .tgz archive.

    Creates a timestamped .tgz archive of the web_static directory and
    stores it in the versions/ folder. Returns the archive path on success,
    or None if the archive creation fails.
    """
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    print("Packing web_static to {}".format(archive_path))

    local("tar -cvzf {} web_static".format(archive_path))

    if os.path.exists(archive_path):
        size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, size))
        return archive_path

    return None
