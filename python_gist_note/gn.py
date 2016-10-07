#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import sys

import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')


version = '0.1.1'

h = """

USAGE：
    1. 获取 gist 内容（写入到 file.py）：
    gn gist-id > file.py

    2. 新建 gist （根据 file.py 文件的内容）：
    gn [options] < file.py

OPTIONS:
    --help, -h: 显示本帮助

    -f: 可选，新建 gist 时，新建的 gist 的文件名，默认为：gistfile1.txt

    -m: 可选，新建 gist 时，新建的 gist 描述，默认为空

"""

API_HOST = 'https://api.github.com/'
GIST_HOST = 'https://gist.github.com/'


def _echo_info(r):
    """ 回显新建的 gist 的信息
    短地址
    地址
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


def create(filename, desc, content):
    """ create gist file """

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
    r = requests.post(url, data=json.dumps(data))

    _echo_info(r.text)


def main():
    options = ['-f', '-m']
    argv = sys.argv

    filename = ''
    desc = ''
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
            removed_li.extend([arg, val])

    for o in removed_li:
        argv.remove(o)

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
            content = sys.stdin.read()
            create(filename, desc, content)


if __name__ == '__main__':
    main()
