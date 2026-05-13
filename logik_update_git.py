import os
from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError,  InvalidGitRepositoryError


from tkinter.messagebox import OK, INFO, showinfo

def check_git_repos():
    INSTALL_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        repo = Repo(INSTALL_DIR)
        changes = repo.index.diff("origin/main")
        
        if len(changes) > 0:
            showinfo(title="Уведомление АИС", message="Найдены обновления! вы можете их установить!")
            
        else:
            showinfo(title="Уведомление АИС", message="Обновлений нет.")

    except InvalidGitRepositoryError:
        showinfo(title="Ошибка АИС", message="Ошибка: Репозиторий не найден.")
    except Exception as e:
        showinfo(title="Ошибка АИС", message="Не удалось проверить обновления.")


#загрузка обновлений из репозитория       
def download_update_system():
    INSTALL_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        repo = Repo(INSTALL_DIR)
        origin = repo.remotes.origin
        info_pull = origin.pull()
        showinfo(title="Уведомление АИС", message="УСПЕШНО: Программа обновлена.\nПерезапустите приложение.")
            

    except InvalidGitRepositoryError:
        showinfo(title="Ошибка АИС", message="Ошибка: Репозиторий не найден.")
    except Exception as e:
        showinfo(title="Ошибка АИС", message="Не удалось проверить обновления.")