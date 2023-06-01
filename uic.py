import json
import ytbDL
import tkinter as tk
from tkinter import ttk

# download path var
download_path = None


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title('YouTube Dl')
        self.geometry('800x450')
        self.minsize(700, 400)

        # Section setup
        # Download
        self.download = DownloadSec(self)
        # Location
        self.location = LocationSec(self)

        # Column config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(8, weight=1)

        # Theme
        self.call('source', 'Azure-ttk-theme-main/azure.tcl')
        self.call('set_theme', 'dark')

        # Style
        s = ttk.Style()
        s.configure('my.TButton', font=('ArialRoundedMTBold', 16))
        s.configure('my2.TButton', font=('ArialRoundedMTBold', 12))

        # Image
        image_path = "Image/blobicon.png"
        photo = tk.PhotoImage(file=image_path)
        resized_photo = photo.subsample(int(photo.width() / 75), int(photo.height() / 75))

        tk.Label(self, image=resized_photo) \
            .grid(row=4, column=0)

        # Run
        self.mainloop()


class DownloadSec(ttk.Frame):
    string_entry = None

    def __init__(self, parent):
        # Frame setup
        super().__init__(parent)
        self.grid(row=1, column=0, padx=1, pady=0)

        # Label
        ttk.Label(master=parent, text='YouTube Link:', font='ArialRoundedMTBold 24') \
            .grid(row=0, column=0, columnspan=2, padx=10, pady=(25, 0))

        # Entry
        self.string_entry = tk.StringVar()
        ttk.Entry(master=self, width=80, textvariable=self.string_entry) \
            .grid(row=2, column=0, padx=10, pady=0)

        # Button
        ttk.Button(master=self, text='Download', style='my.TButton', command=self.download_video) \
            .grid(row=3, column=0, padx=10, pady=(10, 35))

    def download_video(self):
        video_url = self.string_entry.get()
        ytbDL.download_video(video_url, download_path)


def load_paths():
    try:
        with open("Path/paths.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return


def save_path(path):
    with open("Path/paths.json", "w") as file:
        json.dump(path, file, indent=4)


def add_download_path(path):
    path_json = load_paths()
    paths = path_json['paths']

    # check if path already exists
    if path not in paths:
        paths.append(path)
        save_path(path_json)


class LocationSec(ttk.Frame):
    string_entry2 = None
    checkbutton_var = None

    def __init__(self, parent):
        # Frame setup
        super().__init__(parent)
        self.grid(row=6, column=0, padx=10, pady=0)

        # Label
        ttk.Label(master=parent, text='Destination Path:', font='ArialRoundedMTBold 20') \
            .grid(row=5, column=0, columnspan=2, padx=10, pady=(25, 10))

        # Dropdown
        self.string_entry2 = tk.StringVar()
        combo_values = load_paths()["paths"]
        ttk.Combobox(master=self, width=50, textvariable=self.string_entry2, values=combo_values) \
            .grid(row=7, column=0, padx=10, pady=0)

        # Checkbox
        self.checkbutton_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self, variable=self.checkbutton_var, state=tk.DISABLED, padx=5) \
            .grid(row=7, column=1, sticky='e')

        # Button
        ttk.Button(master=parent, text='Confirm', style='my2.TButton', command=self.confirm_button_actions) \
            .grid(row=8, column=0, padx=10, pady=10)

    def confirm_button_actions(self):
        global download_path
        path_input = self.string_entry2.get()
        # check box if input
        condition = len(path_input) > 0
        self.checkbutton_var.set(condition)
        download_path = path_input
        # Add new path to json
        if condition:
            add_download_path(path_input)
