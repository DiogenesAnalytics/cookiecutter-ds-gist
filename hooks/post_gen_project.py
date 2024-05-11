"""Execute after main templating completes."""

import os
import pathlib
import shutil

def move_contents_and_cleanup():
    """Move contents of template files directory to current directory."""
    # get paths
    src = pathlib.Path(os.getcwd())
    dst = src.parent

    # copy files
    for item in src.iterdir():
        shutil.copy(item, dst)

    # remove template_files directory
    shutil.rmtree(src)

move_contents_and_cleanup()
