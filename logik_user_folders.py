import os

def open_attendance_folder():
    folder_path = "Посещаемость"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        os.startfile(folder_path)
        

def open_grade_folder():
    folder_path = "Успеваемость"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        os.startfile(folder_path)