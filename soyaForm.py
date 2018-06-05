import tkinter as tk
from soya import *
from PIL import Image, ImageTk

"""Define global value
"""
entry = None
response_area = None
lb = None
action = None
soya = Soya('soya')

def putlog(str):
    lb.insert(tk.END, str)

def prompt():
    s = soya.name
    if (action.get())==0:
        s += ':' + soya.responder.name
    return s +'> '


def talk():
    value = entry.get()
    if not value:
        response_area.configure(text='何？')
    else:
        response = soya.dialogue(value)
        response_area.configure(text=response)
        putlog('> ' + value)
        putlog(prompt() + response)
        entry.delete(0, tk.END)

#====================
#describe view
#====================

def run():
    global entry, response_area, lb, action

    #make the main window
    root = tk.Tk()
    root.geometry('880x560')
    root.title('Intelligent Agent : ')
    font=('Helevetica', 11)

    # make a menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    # file menu
    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Close', command=root.destroy)
    # option menu
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label='option', menu=optionmenu)
    optionmenu.add_radiobutton(
        label='display Responder',
        variable = action,
        value = 0
    )
    optionmenu.add_radiobutton(
        label='Hide Responder',
        variable=action,
        value = 0
    )

    # make canvas
    canvas = tk.Canvas(
        root,
        width = 500,
        height = 300,
        relief = tk.RIDGE,
        bd=2
    )
    canvas.place(x=370, y=0)

    image=Image.open('port.jpg')
    img=ImageTk.PhotoImage(image)
    canvas.create_image(
        0,
        0,
        image = img,
        anchor = tk.NW
    )

    # make response area
    response_area = tk.Label(
        root,
        width =50,
        height = 10,
        bg='salmon',
        font=font,
        relief=tk.RIDGE,
        bd=2,
    )
    response_area.place(x=370, y=305)


    # make frame
    frame = tk.Frame(
        root,
        relief=tk.RIDGE,
        borderwidth=4
    )

    # entry box
    entry = tk.Entry(
        frame,
        width=70,
        font=font
    )
    entry.pack(side = tk.LEFT)
    entry.focus_set()

    # buttons
    button = tk.Button(
        frame,
        width=15,
        text='Talk',
        command=talk
    )
    button.pack(side = tk.LEFT)
    frame.place(x=30, y=520)


    # make listbox
    lb = tk.Listbox(
        root,
        width=42,
        height=30,
        font=font
    )

    #make scrollbar
    sb1 = tk.Scrollbar(
        root,
        orient = tk.VERTICAL,
        command = lb.yview
    )

    sb2 =tk.Scrollbar(
        root,
        orient = tk.HORIZONTAL,
        command = lb.xview
    )

    lb.configure(yscrollcommand = sb1.set)
    lb.configure(xscrollcommand = sb2.set)

    lb.grid(row = 0, column = 0)
    sb1.grid(row = 0, column = 1, sticky = tk.NS)
    sb2.grid(row = 1, column = 0, sticky = tk.EW)

    root.mainloop()

if __name__ == '__main__':
    run()
