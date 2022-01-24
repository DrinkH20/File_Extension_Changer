import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import os


# Trying to implement the code above so i can make this into a mobile app
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.add_widget(self.inside)

        self.inside.add_widget(Label(text="File or Folder fi/fo: "))
        self.fileorfolder = TextInput(multiline=False)
        self.inside.add_widget(self.fileorfolder)

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
        fileorfolder = self.fileorfolder.text
        if fileorfolder == "fo":
            with os.scandir(path_folder) as files_and_folder:
                for element in files_and_folder:
                    if element.is_file():
                        root, ext = os.path.splitext(element.path)
                        if ext != ".py":
                            old_ex = ext
                            new_path = root + new_ex
                            os.rename(element.path, new_path)
                            file_counter += 1
                            print('Folder from {} to {}'.format(old_ex, new_ex, new_path))
        elif fileorfolder == "fi":
            root, ext = os.path.splitext(path_folder)
            if ext != ".py":
                old_ex = ext
                new_path = root + new_ex
                os.rename(path_folder, new_path)
                print('File from {} to {}'.format(old_ex, new_ex, new_path))


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
