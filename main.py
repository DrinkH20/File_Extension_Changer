from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import os
from to_docs import convert_docs
from doc_to_pdf import convert_pdf
import shutil
import time

time_start = time.time()


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.add_widget(self.inside)

        self.inside.add_widget(Label(text="File or Folder file/folder: "))
        self.file_or_folder = TextInput(multiline=False)
        self.inside.add_widget(self.file_or_folder)

        self.inside.add_widget(Label(text="Source Name: "))
        self.file_source = TextInput(multiline=False)
        self.inside.add_widget(self.file_source)

        self.inside.add_widget(Label(text="Convert to: "))
        self.type = TextInput(multiline=False)
        self.inside.add_widget(self.type)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        file_counter = 0
        path_folder = fr'{self.file_source.text}'
        new_ex = '.' + self.type.text

        file_or_folder = self.file_or_folder.text
        if file_or_folder == "folder":
            print(new_ex)
            with os.scandir(path_folder) as files_and_folder:
                for element in files_and_folder:
                    if element.is_file():
                        if new_ex.lower() != ".doc" and new_ex.lower() != ".pdf":
                            print(element.path)
                            root, ext = os.path.splitext(element.path)
                            if ext != ".py":
                                old_ex = ext
                                new_path = root + new_ex
                                os.rename(element.path, new_path)
                                file_counter += 1
                                print('Folder from {} to {}'.format(old_ex, new_ex, new_path))
                                # File copy part
                                copy_file = r"C:\Users\jones\OneDrive\Pictures\pngs_or_something\Copied files"
                                print(copy_file, "COPYING FILE...")
                                shutil.copy2(element.path, copy_file)
                                print("FILE COPIED!")

                        elif new_ex.lower() == ".doc":
                            print("This is the test")
                            convert_docs(element.path, new_ex)
                            copy_file = r"C:\Users\jones\OneDrive\Pictures\pngs_or_something\Copied files"
                            print(copy_file, "COPYING FILE...")
                            shutil.copy2(element.path, copy_file)
                            print("FILE COPIED!")

                        elif new_ex.lower() == ".pdf":
                            convert_pdf(element.path, new_ex)
                            copy_file = r"C:\Users\jones\OneDrive\Pictures\pngs_or_something\Copied files"
                            print(copy_file, "COPYING FILE...")
                            shutil.copy2(element.path, copy_file)
                            print("FILE COPIED!")

        elif file_or_folder == "file":
            root, ext = os.path.splitext(path_folder)
            print(new_ex)
            if new_ex != ".doc" and new_ex.lower() != ".pdf" and new_ex != ".docx":
                if ext != ".py":
                    old_ex = ext
                    new_path = root + new_ex
                    copy_file = r"C:\Users\jones\OneDrive\Pictures\pngs_or_something\Copied files"
                    print(copy_file, "not doc")
                    shutil.copy2(path_folder, copy_file)
                    os.rename(path_folder, new_path)
                    print('File from {} to {}'.format(old_ex, new_ex, new_path))
            elif new_ex == ".doc" or new_ex == ".docx":
                old_ex = ext
                new_path = root + new_ex
                print("This is the test")
                convert_docs(path_folder, new_ex)
                print('File from {} to {}'.format(old_ex, new_ex, new_path))
                print("converted!")
            elif new_ex.lower() == ".pdf":
                convert_pdf(path_folder, new_ex)
                copy_file = r"C:\Users\jones\OneDrive\Pictures\pngs_or_something\Copied files"
                print(copy_file, "COPYING FILE...")
                shutil.copy2(path_folder, copy_file)
                print("FILE COPIED!")
        else:
            print("Sorry, that is not a valid answer!")

        time_end = time.time()

        print(f'Time used for conversion {time_end - time_start}')


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
