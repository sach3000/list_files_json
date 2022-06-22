#!/usr/bin/env python3

import glob
import os
from datetime import date, datetime
from pathlib import Path
import json
import argparse


class Config:
    def __init__(self, **kwargs):
        # kwargs fields:
        #       path
        #       mask
        self.__dict__.update(kwargs)


class FileAttribute:
  def __init__(self, fullpath, size, atime, mtime, ctime, owner, group):
    self.fullpath = fullpath
    self.size = size
    self.atime = transform_datetime(atime)
    self.mtime = transform_datetime(mtime)
    self.ctime = transform_datetime(ctime)
    self.owner = owner
    self.group = group


def parse_cli_args():
    parser = argparse.ArgumentParser(description='Get listing files from Path by pattern and convert to json')
    parser.add_argument('-p',
                        dest='path',
                        help='Path to files',
                        required=True)
    parser.add_argument('-m',
                        dest='mask',
                        help='Mask fo files pattern (default: all files)',
                        default='*',
                        required=False)
    return parser.parse_args()

def init_config():
    args = parse_cli_args()
    config = Config(path=args.path,
                    mask=args.mask)
    return config

def transform_datetime(s):
    try:
        return str(datetime.strptime(str(datetime.fromtimestamp(int(s))), "%Y-%m-%d %H:%M:%S"))
    except BaseException as e:
        raise str(e)

def get_files_list(config):
    files = []
    for f in sorted(glob.glob(os.path.join(config.path + "/**/*" + config.mask + "*"), recursive=True)):
       if os.path.isfile(f):
          stat = os.stat(f, dir_fd=None, follow_symlinks=False)
          f_attr = FileAttribute(f, stat.st_size, stat.st_atime, stat.st_mtime, stat.st_ctime, Path(f).owner(), Path(f).group())
          fAttrDict = {
             'path' : f_attr.fullpath,
             'size': f_attr.size,
             'atime': f_attr.atime,
             'mtime' : f_attr.mtime,
             'ctime' : f_attr.ctime,
             'owner' : f_attr.owner,
             'group' : f_attr.group
          }
          files.append(dict(zip([Path(f).name],[fAttrDict])))
    return json.dumps(files, indent=2)


if __name__ == '__main__':
    config = init_config()
    print(get_files_list(config))

