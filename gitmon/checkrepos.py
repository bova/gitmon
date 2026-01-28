from git import *
import colorama

REPOS_LIST_FILE = 'repo.lst'
REPOS = []


def is_repo_dirty(path):
	repo = Repo(path)
	return repo.is_dirty()

def load_repo_path():
	for path in open(REPOS_LIST_FILE).readlines():
		path = path.rstrip('\n')
		REPOS.append(path)


def show_repo_status(path, is_dirty):
	if is_dirty:
		color = colorama.Fore.RED
		status = 'DIRTY'
	else:
		color = colorama.Fore.GREEN
		status = 'CLEAR'
	print(colorama.Fore.YELLOW + path + ' ' + color + status)

if __name__ == '__main__':
	colorama.init()
	load_repo_path()
	for path in REPOS:
		is_dirty = is_repo_dirty(path)
		show_repo_status(path, is_dirty)
