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
  def __init__(self, name, fullpath, size, atime, mtime, ctime, ats, owner, group):
    self.name = name
    self.fullpath = fullpath
    self.size = size
    self.atime = transform_datetime(atime)
    self.mtime = transform_datetime(mtime)
    self.ctime = transform_datetime(ctime)
    self.ats = ats
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
                        help='Mask fo files pattern (default: all files). List separated by ";"',
                        default='*',
                        required=False)
    parser.add_argument('-i',
                        dest='idx',
                        help='Index of element files array (default: all files)',
                        required=False)
    return parser.parse_args()

def init_config():
    args = parse_cli_args()
    config = Config(path=args.path,
                    mask=args.mask,
                    idx=args.idx)
    return config

def transform_datetime(s):
    try:
        return str(datetime.strptime(str(datetime.fromtimestamp(int(s))), "%Y-%m-%d %H:%M:%S"))
    except BaseException as e:
        raise str(e)

def get_files_list(config):
    files = []
    files_by_req_index = []

    for ptr in config.mask.split(';'):
       files_tmp = []
       for f in sorted(glob.glob(os.path.join(config.path + "/**/*" + ptr + "*"), recursive=True)):
          if os.path.isfile(f):
             stat = os.stat(f, dir_fd=None, follow_symlinks=False)
             f_attr = FileAttribute(Path(f).name, f, stat.st_size, stat.st_atime, stat.st_mtime, stat.st_ctime, int(stat.st_atime), Path(f).owner(), Path(f).group())
             fAttrDict = {
                'name': f_attr.name,
                'path' : f_attr.fullpath,
                'size': f_attr.size,
                'atime': f_attr.atime,
                'mtime' : f_attr.mtime,
                'ctime' : f_attr.ctime,
                'ats' : f_attr.ats,
                'owner' : f_attr.owner,
                'group' : f_attr.group
             }
             #files.append(dict(zip([Path(f).name],[fAttrDict])))
             files.append(fAttrDict)

             #files_tmp.append(dict(zip([Path(f).name],[fAttrDict])))
             files_tmp.append(fAttrDict)
       if config.idx:
          files_by_req_index.append(files_tmp[int(config.idx)])
    if config.idx:
       return json.dumps(files_by_req_index, indent=2)
    else:
       return json.dumps(files, indent=2)


if __name__ == '__main__':
    config = init_config()
    print(get_files_list(config))

