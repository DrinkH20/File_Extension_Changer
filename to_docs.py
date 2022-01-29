import win32com.client
import os


def convert_docs(path, ex):
    # INPUT/OUTPUT PATH
    pdf_path = fr"""{path}"""
    output_path = fr"""{path}"""

    word = win32com.client.Dispatch("Word.Application")
    word.visible = 1

    # GET FILE NAME AND NORMALIZED PATH
    filename = pdf_path.split('\\')[-1]
    in_file = os.path.abspath(pdf_path)

    # CONVERT PDF TO DOCX AND SAVE IT ON THE OUTPUT PATH WITH THE SAME INPUT FILE NAME
    print(path)
    root, ext = os.path.splitext(path)
    out_file = os.path.abspath(root + '' + ex)
    wb = word.Documents.Open(in_file)
    print(out_file)
    wb.SaveAs2(out_file, FileFormat=16)
    wb.Close()
    word.Quit()
