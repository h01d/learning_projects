# Search bar that generates the top 6 images in google for what you search
# -tkinter gui
# -button to select a photo and download it
from tkinter import *

root = Tk()
root.title("Image Search")


class Imagesearch:
    def __init__(self, master):
        frame_label = Frame(master)
        frame_entry = Frame(master)
        frame_search = Frame(master)
        self.frame_results = Frame(master)

        self.greeting = Label(master=frame_label, text="Enter what you would like to search for:")
        self.greeting.pack()

        self.user_entry = Entry(master=frame_entry)
        self.user_entry.pack()

        self.search = Button(master=frame_search, text="Search", command=self.on_button)
        self.search.pack()

        frame_label.pack()
        frame_entry.pack()
        frame_search.pack()

    def on_button(self):
        user_results = self.user_entry.get()
        search_results = Label(master=self.frame_results, text=user_results)
        search_results.pack()
        self.frame_results.pack()
        self.user_entry.configure(state="disabled")


if __name__ == "__main__":
    Image = Imagesearch(root)
    root.mainloop()
