from tkinter import *
from tkinter import ttk
import random as r
import random
from PIL import ImageTk
from PIL import Image
import math
import smtplib
import mysql.connector as ms
from last_win_2 import last_fn_2
from last_win_3 import last_fn_3
from last_win_4 import last_fn_4

def loading_win_6():

    #Loading...

    loading = Tk()
    loading.title("ARA FOODS")
    loading.iconbitmap("logo.ico")
    loading.geometry("650x370")
    loading.config(bg = 'black')

    global load_1, load_1_res, new_load_1
    global load_2, load_2_res, new_load_2
    global load_3, load_3_res, new_load_3
    
    load_1 = Image.open("loading_1.png")
    load_1_res = load_1.resize((640, 360), Image.Resampling.LANCZOS)
    new_load_1 = ImageTk.PhotoImage(load_1_res, master = loading)

    load_2 = Image.open("loading_2.png")
    load_2_res = load_2.resize((640, 360), Image.Resampling.LANCZOS)
    new_load_2 = ImageTk.PhotoImage(load_2_res, master = loading)

    load_3 = Image.open("loading_3.png")
    load_3_res = load_3.resize((640, 360), Image.Resampling.LANCZOS)
    new_load_3 = ImageTk.PhotoImage(load_3_res, master = loading)

    label_load = Label(loading, image = new_load_1)
    label_load.pack()

    #label_load = Label(loading, text = "Loading", font = ('Dollan Personal Use', 50), bg = 'black', fg = 'white')
    #label_load.place(x=165,y=110)

    global unity
    unity = 0

    def timer_load():
        global unity
        unity = unity + 1
        if unity == 4:
            label_load.config(image = new_load_1)
        else:
            label_load.config(image = globals()["new_load_{}".format(unity)])
        label_load.after(1111, timer_load)
        if unity == 4:
            loading.destroy()
            last_fn()
        
    timer_load()

def last_fn():

    #global ara_admin, main_frame_ad_2, my_canvas_ad_2, my_scrollbar_ad_2, adw_frame_ad_2, F_1_2
    ara_admin = Tk()
    ara_admin.title("ADMIN")
    ara_admin.iconbitmap("logo.ico")
    ara_admin.state('zoomed')
    ara_admin.config(bg = '#003153')

    #====================
    
    #Create a main Frame
    main_frame = Frame(ara_admin)
    main_frame.pack(fill = BOTH, expand = True)

    #Create a Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill = BOTH, expand = True)

    #Add a Scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side = RIGHT, fill = Y)

    #my_scrollbar_2 = ttk.Scrollbar(main_frame, orient = HORIZONTAL, command = my_canvas.xview)
    #my_scrollbar_2.pack(side = BOTTOM, fill = X)

    #Configure the canvas
    my_canvas.configure(yscrollcommand = my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

    #my_canvas.configure(xscrollcommand = my_scrollbar_2.set)
    #my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

    #Create another frame inside canvas
    second_frame = Frame(my_canvas)

    #Add that new frame into the window
    my_canvas.create_window((0,0), window = second_frame, anchor = 'nw')

    second_frame.config(bg = '#003153')
    main_frame.config(bg = '#003153')
    my_canvas.config(bg = '#003153')

    #====================

    F_1_2 = LabelFrame(second_frame, bg = '#003153', text = 'ADMIN CONTROL OPTIONS', font = ('Iron Blade', 30), fg = 'white')
    F_1_2.pack(pady=200,padx=180)
    

    ara_conn = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    ara_curr = ara_conn.cursor(buffered = True)

    def var_fn():

        last_fn_2()

        '''ara_curr.execute("select name, area, type from restaurants order by id")
        datax = ara_curr.fetchall()

        for i in range(len(datax)):'''

            
            
    def vacad_fn():

        last_fn_3()

    def vaod_fn():

        last_fn_4()

    Button(F_1_2, text = "View all Restaurants", font = ('Courier New', 20, 'bold'), cursor = 'hand2', bg = 'orange', fg = 'black', command = var_fn).grid(row=0,column=0,pady=40)
    Button(F_1_2, text = "View all Customer account details", font = ('Courier New', 20, 'bold'), cursor = 'hand2', bg = 'orange', fg = 'black', command = vacad_fn).grid(row=0,column=1,padx=20)
    Button(F_1_2, text = "View all Order details", font = ('Courier New', 20, 'bold'), cursor = 'hand2', bg = 'orange', fg = 'black', command = vaod_fn).grid(row=1,column=0,columnspan=2)


    
    

    
    ara_conn.close()########

#last_fn()
