from git import *
import colorama

REPOS_LIST_FILE = 'repo.lst'
REPOS = []


def is_repo_dirty(path):
    repo = Repo(path)
    remote_url = ''
    try:
        remote_url = repo.remote().url
    except:
        remote_url = 'нет удаленного репозитория'
    return repo.is_dirty(), remote_url

def load_repo_path():
    for path in open(REPOS_LIST_FILE).readlines():
        path = path.rstrip('\n')
        REPOS.append(path)


def show_repo_status(path, is_dirty, remote_url):
    if is_dirty:
        color = colorama.Fore.RED
        status = 'DIRTY'
    else:
        color = colorama.Fore.GREEN
        status = 'CLEAR'
    print(f"{colorama.Fore.YELLOW}{path} {color}{status} {colorama.Fore.BLUE}({remote_url})")

if __name__ == '__main__':
    colorama.init()
    load_repo_path()
    for path in REPOS:
        is_dirty, remote_url = is_repo_dirty(path)
        show_repo_status(path, is_dirty, remote_url)