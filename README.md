# Auto-backup-repo

无依赖库。

在本仓库中的 repos.csv 中添加repo对应的 域名,用户名,仓库名 即可，如:`github.com,user,repo`。也可以直接填https地址，如：`https://github.com/user/repo`（链接不能以`/`结尾！！） ，会自动转换成`github.com,user,repo`一样的格式。

**脚本使用git更新自身和repos.csv，所以请Clone本仓库再在Clone的目录内运行main.py。**

本脚本使用裸版本库(`git clone --mirror`)存储备份的 Git 仓库，理由：

- 裸版本库没有工作区；
- 没有工作区，可以避免工作区文件/文件夹包含特殊文件名（~~说的就是你，NTFS~~）可能造成的问题；
- 没有工作区，存储空间占用会更小。
