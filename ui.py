import tkinter as tk
from tkinter import ttk
import ytbDL

# download path var
download_path = None


def download_video():
    video_url = stringEntry.get()
    ytbDL.download_video(video_url, download_path)


# TODO remove
def test():
    print(stringEntry.get())


# window
window = tk.Tk()
window.title("YtDl")
window.geometry('700x400')

# column config
window.columnconfigure(0, weight=1)
window.rowconfigure(8, weight=1)

# theme
window.call('source', 'Azure-ttk-theme-main/azure.tcl')
window.call('set_theme', 'dark')

s = ttk.Style()
s.configure('my.TButton', font=('ArialRoundedMTBold', 16))
s.configure('my2.TButton', font=('ArialRoundedMTBold', 12))

# DOWNLOAD
# title
t_label = ttk.Label(master=window, text='YouTube Link:', font='ArialRoundedMTBold 24')
t_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(25, 0))

# input field
input_frame = ttk.Frame(master=window)
input_frame.grid(row=1, column=0, padx=1, pady=0)

# ENTRY DOWNLOAD
stringEntry = tk.StringVar()
entry = ttk.Entry(master=input_frame, width=80, textvariable=stringEntry)
entry.grid(row=2, column=0, padx=10, pady=0)

# BUTTON DOWNLOAD
button = ttk.Button(master=input_frame, text='Download', style='my.TButton', command=download_video)
button.grid(row=3, column=0, padx=10, pady=(10, 35))

# LOCATION
# title
t_label2 = ttk.Label(master=window, text='Destination Path:', font='ArialRoundedMTBold 20')
t_label2.grid(row=5, column=0, columnspan=2, padx=10, pady=(25, 10))

# input field
input_frame2 = ttk.Frame(master=window)
input_frame2.grid(row=6, column=0, padx=10, pady=0)

# ENTRY LOCATION
stringEntry2 = tk.StringVar()
entry2 = ttk.Entry(master=input_frame2, width=50, textvariable=stringEntry2)
entry2.grid(row=7, column=0, padx=10, pady=0)

# CHECKBOX LOCATION
checkbutton_var = tk.BooleanVar(value=False)
checkbutton = tk.Checkbutton(input_frame2, variable=checkbutton_var, state=tk.DISABLED, padx=5, )
checkbutton.grid(row=7, column=1, sticky='e')


def confirm_button_actions():
    global checkbutton_var
    global download_path
    # check box if input
    condition = len(stringEntry2.get()) > 0
    checkbutton_var.set(condition)

    download_path = stringEntry2.get()


# BUTTON LOCATION
button2 = ttk.Button(master=window, text='Confirm', style='my2.TButton', command=confirm_button_actions)
button2.grid(row=8, column=0, padx=10, pady=10)

# TODO add path confirmed checkbox


# Image
image_path = "Image/blobicon.png"
photo = tk.PhotoImage(file=image_path)
resized_photo = photo.subsample(int(photo.width() / 75), int(photo.height() / 75))

image_label = tk.Label(window, image=resized_photo)
image_label.grid(row=4, column=0)

# run
window.mainloop()
