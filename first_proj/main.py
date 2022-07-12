# library importation
import os
import glob
import tkinter as tk


# function definitions
def dir_to_desk():
    # making the folder on desktop to contain files
    output_dir = os.path.expanduser("~/Desktop/my_files")
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    return output_dir


def create_file(output_dir):
    # adding files to folder path
    for file in range(5):
        filepath = os.path.join(output_dir, "file" + str(file + 1) + ".txt")
        f = open(filepath, "x")
    for file in range(2):
        filepath = os.path.join(output_dir, "file" + str(file + 1) + ".doc")
        f = open(filepath, "x")


def read_txt():
    # gathering the txt files
    txt = []
    files = glob.glob('/Users/jarodcrush/Desktop/my_files/**/*.txt', recursive=True)
    for file in files:
        txt.append(file)
    return txt



def read_doc():
    # gathering the doc files
    doc = []
    documents = glob.glob('/Users/jarodcrush/Desktop/my_files/**/*.doc', recursive=True)
    for document in documents:
        doc.append(document)
    return doc



def display_files(files):
    # displaying the paths for both file types
    info_files = tk.Label(text='\n'.join(map(str, files)))
    info_files.pack()


# main
if __name__ == '__main__':
    output_dir = dir_to_desk()
    create_file(output_dir)
    txt = read_txt()
    doc = read_doc()
    doc_txt = doc + txt

# establishing GUI
    window = tk.Tk()
    greeting = tk.Label(text="Hello, would you like to display your files?")
    button = tk.Button(text="Yes!", command=lambda: display_files(doc_txt))
    greeting.pack()
    button.pack()
    window.mainloop()