#!/usr/bin/env python2.7

from os import rename, rmdir, walk
from os.path import exists, join as path_join, split as path_split

VALUE = "value.wsp"

top = "/opt/graphite/storage/whisper/collectd"

for dirpath, dirnames, filenames in walk(top):
    if filenames == [VALUE, ]:
        parent_dir, path = path_split(dirpath)
        new_name = path_join(parent_dir, "{0}.wsp".format(path))
        old_name = path_join(dirpath, VALUE)
        if exists(old_name):
            print "Renaming {0} -> {1}".format(old_name, new_name)
            rename(old_name, new_name)
            rmdir(dirpath)
