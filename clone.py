import os
import subprocess

from github import Github
from dotenv import dotenv_values

config = dotenv_values('.env')
github = Github(config['ACCESS_TOKEN'])

for repo in github.get_user().get_repos():
    try:
        os.makedirs("{}\\{}".format(config['PATH'], repo.name))
        subprocess.run("git -C {}\\{} clone {}".format(config['PATH'], repo.name, repo.ssh_url).split(' '))
    except:
        pass