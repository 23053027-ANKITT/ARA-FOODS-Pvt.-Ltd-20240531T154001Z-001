from tkinter import *
from tkinter import ttk
import random as r
import random
from PIL import ImageTk
from PIL import Image
import math
import smtplib
import mysql.connector as ms

def last_fn_4():

    global ara_admin4
    ara_admin4 = Tk()
    ara_admin4.title("ADMIN")
    ara_admin4.iconbitmap("logo.ico")
    ara_admin4.state("zoomed")
    ara_admin4.config(bg = 'cyan')

    #====================
    
    #Create a main Frame
    main_frame = Frame(ara_admin4)
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

    second_frame.config(bg = 'cyan')
    main_frame.config(bg = 'cyan')
    my_canvas.config(bg = 'cyan')


    X_1 = Frame(second_frame, bg = 'cyan')
    X_1.pack(pady=20,padx=70)

    Label(X_1, text = "Name", font = ('Fighting Spirit turbo', 20), bg = 'cyan').grid(row=0,column=0)
    Label(X_1, text = "Phone Number", font = ('Fighting Spirit turbo', 20), bg = 'cyan').grid(row=0,column=1)
    Label(X_1, text = "Bill Total", font = ('Fighting Spirit turbo', 20), bg = 'cyan').grid(row=0,column=2)


    global ara_conn2, ara_curr2
    ara_conn2 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    ara_curr2 = ara_conn2.cursor(buffered = True)

    ara_curr2.execute("select name, ph_no from order_bill order by id desc")
    global datax2
    datax2 = ara_curr2.fetchall()

    ara_curr2.execute("select net_cost_1_3 from grand_cost order by id desc")
    global datay2
    datay2 = ara_curr2.fetchall()


    for i in range(len(datax2)):

        Label(X_1, text = str(datax2[i][0]), font = ('Times New Roman', 18, 'bold'), bg = 'cyan').grid(row = i + 1, column=0)

        Label(X_1, text = str(datax2[i][1]), font = ('Times New Roman', 18, 'bold'), bg = 'cyan').grid(row = i + 1,column=1, padx=50)

        Label(X_1, text = str(datay2[i][0]), font = ('Times New Roman', 18, 'bold'), bg = 'cyan').grid(row = i + 1,column=2,pady=30)
