#!/usr/bin/python3
"""Fabric script that distributes a .tgz archive to web servers."""

from fabric.api import env, put, run
import os

# Define target web servers
env.hosts = ['98.93.145.166', '18.208.133.10']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy an archive to the web servers.

    Uploads the archive to /tmp/, extracts it to the releases directory,
    removes the archive, and updates the symbolic link to point to the
    new release. Returns True on success, False otherwise.

    Args:
        archive_path (str): Local path to the .tgz archive to deploy.
    """
    # Check if the archive file exists locally
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract filename and name without extension
        filename = os.path.basename(archive_path)
        name = filename.replace(".tgz", "")
        release_dir = "/data/web_static/releases/{}/".format(name)

        # 1. Upload archive to /tmp/ on the remote server
        put(archive_path, "/tmp/{}".format(filename))

        # 2. Create target release directory
        run("mkdir -p {}".format(release_dir))

        # 3. Extract the archive into the release directory
        run("tar -xzf /tmp/{} -C {}".format(filename, release_dir))

        # 4. Remove the archive from the server
        run("rm /tmp/{}".format(filename))

        # 5. Move contents out of the nested web_static/ subfolder
        run("mv {}web_static/* {}".format(release_dir, release_dir))

        # 6. Remove the now-empty web_static subfolder
        run("rm -rf {}web_static".format(release_dir))

        # 7. Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # 8. Create new symbolic link pointing to the new release
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True

    except Exception:
        return False
