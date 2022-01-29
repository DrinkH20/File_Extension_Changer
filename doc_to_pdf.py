import os
import win32com.client
import time

format_code = 17

time_start = time.time()


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

    # file_input = os.path.abspath(root,"2" + exe)
    # file_output = os.path.abspath(root, "2", new_exe)
    # word_file = word_app.Documents.Open(file_input)
    # word_file.SaveAs(file_output, FileFormat=format_code)
    # word_file.Close()

    # close file and application
    word_app.Quit()

    time_end = time.time()

    print(f'Time used for conversion {time_end - time_start}')
