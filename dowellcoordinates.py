from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests, json

url = "https://100074.pythonanywhere.com/get-coords/"

def dir(direction):
    direction_mapping = {
        'N': 'North',
        'E': 'East',
        'S': 'South',
        'W': 'West'
    }
    output_direction = direction_mapping.get(direction, direction)
    return output_direction

def coordinate():
    data = {"region":result.get()}
    headers = {'Content-Type': 'application/json'}
    info=requests.post(url=url,headers=headers, data=json.dumps(data))
    if info.status_code == 200:
        lat = info.json()['Coords']['lat'][-1]
        lng = info.json()['Coords']['lng'][-1]
        lab= ttk.Label(bootstyle="inverse-success", text=result.get()+" is in "+dir(lat)+"-"+dir(lng)+" direction.", font=('Roboto', 30, 'bold'))
    else:
        lab= ttk.Label(bootstyle="inverse-danger", text=info.json(), font=('Roboto', 30, 'bold'))
    lab.pack(side=ttk.TOP, fill=ttk.BOTH)

def toggler(event):
    fullScreenState = True
    root.attributes("-fullscreen", fullScreenState)


def exit(event):
    fullScreenState = False
    root.attributes("-fullscreen", fullScreenState)


root = ttk.Window(themename='yeti')
root.title("DowellCoordinates")
root.attributes('-fullscreen', True)
root.geometry('500x200')
root.configure()
style = ttk.Style()
root.bind("<F11>", toggler)
root.bind("<Escape>", exit)

innerbox = ttk.Frame(root, relief=RAISED, borderwidth=1)
innerbox.pack(fill=ttk.X, side=ttk.TOP, expand=True)

result = ttk.Entry(innerbox, justify="center", font=('Ariel 40 bold'))
result.pack(ipadx=30,side=ttk.TOP, fill=ttk.X, expand=True)

submit = ttk.Button(innerbox, text="Submit",
                    command=coordinate, style="success.outline.TButton")
style.configure('TButton', font=('Roboto', 50, 'bold'))
submit.pack(side=ttk.TOP, fill=ttk.BOTH)



root.mainloop()