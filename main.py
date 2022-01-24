import os

fileorfolder = input("is this a file or a folders? fi/fo")

if fileorfolder == "y":
    path_folder = f'{input("file location?")}'
else:
    path_folder = fr'{input("file location?")}'

old_ex = '.' + input("OLD STUF ")
new_ex = '.' + input("NEW STUF ")

file_counter = 0

if fileorfolder == "fo":
    with os.scandir(path_folder) as files_and_folder:
            for element in files_and_folder:
                if element.is_file():
                    root, ext = os.path.splitext(element.path)
                    if ext != ".py":
                        new_path = root + new_ex
                        os.rename(element.path, new_path)
                        file_counter += 1
elif fileorfolder == "fi":
    root, ext = os.path.splitext(path_folder)
    if ext != ".py":
        new_path = root + new_ex
        os.rename(path_folder, new_path)
print('Ex from {} to {}'.format(old_ex, new_ex, new_path))
