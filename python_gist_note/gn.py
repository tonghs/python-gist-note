#! /usr/bin/env python
# -*- coding: utf-8 -*-


import os.path

import json
import requests
from os.path import expanduser


import sys
reload(sys)
sys.setdefaultencoding('utf8')


version = '0.2.4'

h = """

USAGE：
    1. 获取 gist 内容（写入到 file.py）：
    gn gist-id > file.py

    2. 新建 gist （根据 file.py 文件的内容）：
    gn [options] < file.py

    3. 完整参数：
    gn -f gist-test.py -m 'this is a test file' -u abc@def.com -p pwd < test.py

OPTIONS:
    --help, -h: 显示本帮助

    -f: 可选，新建 gist 时，新建的 gist 的文件名，默认为：gistfile1.txt

    -m: 可选，新建 gist 时，新建的 gist 描述，默认为空

    -u, -p: 用户名和密码

"""

API_HOST = 'https://api.github.com/'
GIST_HOST = 'https://gist.github.com/'
CONFIG_FILE = '{}/.config/.gn.conf'.format(expanduser("~"))


def _echo_info(r):
    """ 回显新建的 gist 的信息
    短地址
    id
    """
    d = json.loads(r)

    print d.get('html_url', '')
    print d.get('id', '')


def help():
    print h


def get(url_or_id):
    """ get gist content by gist id """

    url = ''
    if url_or_id.startswith(GIST_HOST):
        url_or_id = url_or_id.split('/')[-1]

    url = '{host}gists/{id}'.format(host=API_HOST, id=url_or_id)

    r = requests.get(url)
    files = json.loads(r.text).get('files', dict())
    if files:
        print files.values()[0].get('content', '')
    else:
        print 'Error: Bad gist id or url'
        help()


def get_auth(user=None, pwd=None):
    auth = None
    if user and pwd:
        auth = (user, pwd)
    else:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE) as f:
                for l in f:
                    if 'user:' in l:
                        user = l.split(':')[1].strip()
                    elif 'pwd' in l:
                        pwd = l.split(':')[1].strip()

                auth = (user, pwd)

    if user and pwd:
        print 'your gist account:', user, '\n'

    return auth


def create(filename='', desc='', content='', user=None, pwd=None):
    """ create gist file """

    if content:
        data = {
            "description": desc,
            "public": True,
            "files": {
                filename: {
                    "content": content
                }
            }
        }

        url = '{host}gists'.format(host=API_HOST)
        auth = get_auth(user=user, pwd=pwd) 
        r = requests.post(url, data=json.dumps(data), auth=auth)

        _echo_info(r.text)
    else:
        print 'this is a empty file ^_^'


def parse_args(argv):
    options = ['-f', '-m', '-u', '-p']

    filename = ''
    desc = ''
    user = ''
    pwd = ''

    removed_li = list()
    for i, arg in enumerate(argv):
        if arg in options:
            val = argv[i + 1]
            if val.startswith('-'):
                print '参数错误: {arg}'.format(arg=arg)
                help()
                return

            if arg == '-f':
                filename = val
            elif arg == '-m':
                desc = val
            elif arg == '-u':
                user = val
            elif arg == '-p':
                pwd = val

            removed_li.extend([arg, val])

    for o in removed_li:
        argv.remove(o)

    return dict(filename=filename, desc=desc,
                user=user, pwd=pwd), argv


def main():
    params, argv = parse_args(sys.argv)

    if len(argv) > 1:
        if argv[1] in ['--help', '-h']:
            help()
        elif argv[1] in ['--version', '-v']:
            print version
        else:
            get(argv[1])
    else:
        if sys.stdin.isatty():
            help()
        else:
            params.update(content = sys.stdin.read())
            create(**params)


if __name__ == '__main__':
    main()
