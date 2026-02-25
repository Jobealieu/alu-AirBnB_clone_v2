#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers."""

from fabric.api import env, put, run, local
from datetime import datetime
import os

env.hosts = ['98.93.145.166', '18.208.133.10']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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

    web_static_path = "/home/jobealieu/alu-AirBnB_clone"
    local("cd {} && tar -cvzf ~/alu-AirBnB_clone_v2/{} web_static".format(
        web_static_path, archive_path))

    if os.path.exists(archive_path):
        size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, size))
        return archive_path

    return None


def do_deploy(archive_path):
    """Deploy an archive to the web servers.

    Uploads the archive to /tmp/, extracts it to the releases directory,
    removes the archive, and updates the symbolic link to point to the
    new release. Returns True on success, False otherwise.

    Args:
        archive_path (str): Local path to the .tgz archive to deploy.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        name = filename.replace(".tgz", "")
        release_dir = "/data/web_static/releases/{}/".format(name)

        put(archive_path, "/tmp/{}".format(filename))
        run("mkdir -p {}".format(release_dir))
        run("tar -xzf /tmp/{} -C {}".format(filename, release_dir))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(release_dir, release_dir))
        run("rm -rf {}web_static".format(release_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True

    except Exception:
        return False


def deploy():
    """Create and distribute an archive to the web servers.

    Calls do_pack() to generate a new archive, then calls do_deploy() to
    upload and activate it on both web servers. Returns True on full success,
    False if packing or deployment fails.
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
