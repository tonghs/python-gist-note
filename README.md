# This is a simple note based on gist.

基于 gist 的简易 note 工具，可以很方便和你的小伙伴分享代码片段。

### 安装

```
sudo pip install python-gist-note
```

### 使用

USAGE：

    1. 获取 gist 内容（写入到 file.py）：
    gn gist-id-or-url > file.py

    2. 新建 gist （根据 file.py 文件的内容）：
    gn [options] < file.py

OPTIONS:

    --help, -h: 显示本帮助

    -f: 可选，新建 gist 时，新建的 gist 的文件名，默认为：gistfile1.txt

    -m: 可选，新建 gist 时，新建的 gist 描述，默认为空

使用场景举例：

李雷想把自己机器上的 app.py 分享给韩梅梅，李雷操作如下：

```
$ gn -f app.py -m 'this is a test python file' < app.py
https://gist.github.com/38821b0f84959c525379edb258f0243f
38821b0f84959c525379edb258f0243f
```

李雷将获得的 gist id 或 url 发送给韩梅梅，然后韩梅梅操作如下：

```
$ gn 38821b0f84959c525379edb258f0243fc > app.py
```
