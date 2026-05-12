import os
from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError,  InvalidGitRepositoryError


from tkinter.messagebox import OK, INFO, showinfo

def check_git_repos():

    INSTALL_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        repo = Repo(INSTALL_DIR)
        info = repo.remotes.origin.fetch()

        
        if info[0].commit.count() > 0:
            print("УСПЕШНО: Программа обновлена до последней версии.")
            showinfo(title="Уведомление АИС", message="УСПЕШНО: Программа обновлена до последней версии.")
        else:
            showinfo(title="Уведомление АИС", message="Обновлений нет.")

    except InvalidGitRepositoryError:
        print("Ошибка: В этой папке нет Git-репозитория.")