import os

with open('repos.csv', 'r') as f:
  file = f.read()
lines = file.splitlines()
lines = set(lines)
lines.discard('')
lines = list(lines)
lines.sort()

with open('repos.csv', 'w') as f:
  for line in lines:
    f.write(line.replace("/", ",")+'\n')

with open('repos.csv', 'r') as f:
  file = f.read()
lines = file.splitlines()
print('----------------')

for line in lines:
  repo_inf = line.split(',')
  print('['+repo_inf[1]+'/'+repo_inf[2]+'.git]',end = "--")
  isrepo = os.path.isfile('./repos_data/'+repo_inf[1]+'/'+repo_inf[2]+'.git/config')
  if isrepo == False:
    print('Git目录不存在，开始Clone...')
    repo_url = 'https://saveweb:fake_password@'+repo_inf[0]+'/'+repo_inf[1]+'/'+repo_inf[2]
    clone_command = 'git clone --mirror '+repo_url+' repos_data/'+repo_inf[1]+'/'+repo_inf[2]+'.git'
    log = os.system(clone_command)
    if log == 0:
      print('成功Clone!')
    else:
      print('Clone时发生未知错误，返回值:'+log)
  if isrepo == True:
    print('Git目录存在，开始Update...')
    repo_dir = './'+'repos_data/'+repo_inf[1]+'/'+repo_inf[2]+'.git'
    git_update = 'git remote update'
    update_command = 'cd '+repo_dir+' ; '+git_update
    log1 = os.system(update_command)
    if log1 == 0:
      print('已更新: '+repo_inf[1]+'/'+repo_inf[2]+'.git')
    else:
      print('出错，无法Update: '+repo_inf[1]+'/'+repo_inf[2]+'.git')