import os
import win32com.client

format_code = 17


def convert_pdf(file, new_exe):
    root, exe = os.path.splitext(file)
    # create the MS Word app
    word_app = win32com.client.Dispatch('Word.Application')
    word_app.Visible = False
    # conversion
    file_input = os.path.abspath(file)
    file_output = os.path.abspath(root + new_exe)
    word_file = word_app.Documents.Open(file_input)
    word_file.SaveAs(file_output, FileFormat=format_code)
    word_file.Close()

    word_app.Quit()
