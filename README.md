# Auto-backup-repo

无依赖库。

在本仓库中的 repos.csv 中添加repo对应的 域名,用户名,仓库名 即可，如:`github.com,user,repo`。也可以直接填https地址，如：`https://github.com/user/repo`（链接不能以`/`结尾！！） ，会自动转换成`github.com,user,repo`一样的格式。

**脚本使用git更新自身和repos.csv，所以请Clone本仓库再在Clone的目录内运行main.py。**
