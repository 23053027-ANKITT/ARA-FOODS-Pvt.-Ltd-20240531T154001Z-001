from tkinter import *
from tkinter import ttk
import random as r
import random
from PIL import ImageTk
from PIL import Image
import math
import smtplib
import mysql.connector as ms

def last_fn_3():

    global ara_admin3
    ara_admin3 = Tk()
    ara_admin3.title("ADMIN")
    ara_admin3.iconbitmap("logo.ico")
    ara_admin3.state("zoomed")
    ara_admin3.config(bg = '#f5fca4')

    #====================
    
    #Create a main Frame
    main_frame = Frame(ara_admin3)
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

    second_frame.config(bg = '#f5fca4')
    main_frame.config(bg = '#f5fca4')
    my_canvas.config(bg = '#f5fca4')

    #========================================================================

    X_1 = Frame(second_frame, bg = '#f5fca4')
    X_1.pack(pady=20,padx=70)

    Label(X_1, text = "Username", font = ('Fighting Spirit turbo', 20), bg = '#f5fca4').grid(row=0,column=0)
    Label(X_1, text = "Email ID", font = ('Fighting Spirit turbo', 20), bg = '#f5fca4').grid(row=0,column=1)
    Label(X_1, text = "Password", font = ('Fighting Spirit turbo', 20), bg = '#f5fca4').grid(row=0,column=2)

    ###
    global ara_conn2, ara_curr2
    ara_conn2 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    ara_curr2 = ara_conn2.cursor(buffered = True)

    ara_curr2.execute("select username, email, password from accounts")
    global datax2
    datax2 = ara_curr2.fetchall()

    #============================

    def cus_mod(num):

        global res_menu_win2
        res_menu_win2 = Tk()
        res_menu_win2.title("ADMIN")
        res_menu_win2.iconbitmap("logo.ico")
        res_menu_win2.state("zoomed")
        res_menu_win2.config(bg = '#003153')

        main_frame = Frame(res_menu_win2)
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


        aa = "a_{}".format(num + 1)
        bb = "b_{}".format(num + 1)
        cc = "c_{}".format(num + 1)

        dF = LabelFrame(second_frame, bg = '#003153')
        dF.pack(pady=20,padx=20)

        
        Label(dF, text = "Username", font = ('Times New Roman', 20, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=0)
        Label(dF, text = "Email ID", font = ('Times New Roman', 20, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=1)
        Label(dF, text = "Password", font = ('Times New Roman', 20, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=2)

        #ara_curr.execute("select items, price, vnv from " + str(globals()[aa].cget('text').replace(" ", "_")) + "__" + str(globals()[bb].cget('text').replace(" ", "_")))
        #global datay
        #datay = ara_curr.fetchall()

        global ee1, ee2, ee3

        ee1 = Entry(dF, width = 20, font = ('Times New Roman', 18))
        ee1.grid(row=1,column=0)
        ee1.insert(0, str(globals()[aa].cget('text')))

        ee2 = Entry(dF, width = 20, font = ('Times New Roman', 18))
        ee2.grid(row=1,column=1, padx = 30, pady = 40)
        ee2.insert(0, str(globals()[bb].cget('text')))

        ee3 = Entry(dF, width = 20, font = ('Times New Roman', 18))
        ee3.grid(row=1,column=2)
        ee3.insert(0, str(globals()[cc].cget('text')))

        def cus_fn_1():

            ara_curr2.execute("update accounts set username = '{}', email = '{}', password = '{}' where username = '{}' and email = '{}' and password = '{}'".format(str(ee1.get().strip()), str(ee2.get().strip()), str(ee3.get().strip()), str(globals()[aa].cget('text')), str(globals()[bb].cget('text')), str(globals()[cc].cget('text'))))
            ara_conn2.commit()

            global g
            g = Tk()
            g.geometry("140x40")

            global g1, gL1
            g1 = 1
            gL1 = Label(g, text = "SUCCESS!", font = ('Felix Titling', 20, 'bold'))
            gL1.pack()

            def timer_2():
                global g1
                g1 = g1 - 1
                gL1.after(1000, timer_2)
                if g1 == -1:
                    g.destroy()
                    res_menu_win2.destroy()
                    ara_admin3.destroy()
                    last_fn_3()
                
            timer_2()          
    

        def cus_fn_2():

            #print(str(globals()[aa].cget('text')))
            #print(str(globals()[bb].cget('text')))
            #print(str(globals()[cc].cget('text')))

            ara_curr2.execute("delete from accounts where username = '{}' and password = '{}'".format(str(globals()[aa].cget('text')), str(globals()[cc].cget('text'))))
            ara_conn2.commit()

            global ra
            ra = Tk()
            ra.geometry("140x40")

            global r1, rL1
            r1 = 1
            rL1 = Label(ra, text = "SUCCESS!", font = ('Felix Titling', 20, 'bold'))
            rL1.pack()

            def timer_1():
                global r1
                r1 = r1 - 1
                rL1.after(1000, timer_1)
                if r1 == -1:
                    ra.destroy()
                    res_menu_win2.destroy()
                    ara_admin3.destroy()
                    last_fn_3()
                
            timer_1()


        Button(dF, text = "Update", font = ('Courier New', 20, 'bold'), bg = 'light green', command = cus_fn_1).grid(row = 2, column = 1, pady=30)
        Button(dF, text = "Delete", font = ('Courier New', 20, 'bold'), bg = 'light green', command = cus_fn_2).grid(row = 3, column = 1)
        

        #=========================================

    for i in range(len(datax2)):

        a_var = "a_{}".format(i + 1)
        b_var = "b_{}".format(i + 1)
        c_var = "c_{}".format(i + 1)
        d_var = "d_{}".format(i + 1)
        e_var = "e_{}".format(i + 1)

        globals()[a_var] = Label(X_1, text = str(datax2[i][0]), font = ('Times New Roman', 18, 'bold'), bg = '#f5fca4')
        globals()[a_var].grid(row = i + 1, column=0)

        globals()[b_var] = Label(X_1, text = str(datax2[i][1]), font = ('Times New Roman', 18, 'bold'), bg = '#f5fca4')
        globals()[b_var].grid(row = i + 1,column=1, padx=50)

        globals()[c_var] = Label(X_1, text = str(datax2[i][2]), font = ('Times New Roman', 18, 'bold'), bg = '#f5fca4')
        globals()[c_var].grid(row = i + 1,column=2,pady=30)

        globals()[d_var] = Button(X_1, text = "Modify >>>", font = ('Times New Roman', 19), bg = 'black', fg = 'white', command = lambda num = i: cus_mod(num))
        globals()[d_var].grid(row = i + 1,column=3, padx=50)

    def add_cus_acc():

        global pele2
        pele2 = Tk()
        pele2.title("ADMIN")
        pele2.iconbitmap("logo.ico")
        pele2.geometry("820x220")
        pele2.config(bg = "#dedede")

        dF = LabelFrame(pele2, bg = '#dedede')
        dF.pack()

        Label(dF, text = "Username", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=0)
        Label(dF, text = "Email ID", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=1)
        Label(dF, text = "Password", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=2)

        global ee_1, ee_2, ee_3

        ee_1 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
        ee_1.grid(row=1,column=0)
        #ee1.insert(0, str(globals()[aa].cget('text')))

        ee_2 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
        ee_2.grid(row=1,column=1, padx = 30, pady = 40)
        #ee2.insert(0, str(globals()[bb].cget('text')))

        ee_3 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
        ee_3.grid(row=1,column=2)
        #ee3.insert(0, str(globals()[cc].cget('text')))

        def add_final_cus():

            ara_curr2.execute("select user_id from accounts order by user_id desc")
            axe3 = ara_curr2.fetchone()

            ara_curr2.execute("insert into accounts values({}, '{}', '{}', '{}')".format(int(axe3[0] + 1), ee_1.get().strip(), ee_2.get().strip(), ee_3.get().strip()))
            ara_conn2.commit()

            #ara_curr.execute("create table " + ee1.get().strip().replace(" ","_") + "__" + ee2.get().strip().replace(" ","_") + "(id int, items varchar(300), price int, vnv varchar(2))")

            global done0
            done0 = Tk()
            done0.geometry("140x40")

            global t30, tL30
            t30 = 1
            tL30 = Label(done0, text = "SUCCESS!", font = ('Felix Titling', 20, 'bold'))
            tL30.pack()

            def timer30():
                global t30
                t30 = t30 - 1
                tL30.after(1000, timer30)
                if t30 == -1:
                    done0.destroy()
                    pele2.destroy()
                    ara_admin3.destroy()
                    last_fn_3()
                
            timer30()

        Button(dF, text = "ADD", font = ('Courier New', 20, 'bold'), bg = 'black', fg = 'red', command = add_final_cus).grid(row=2,column=1)


    Button(X_1, text = "Add Customer Account [+]", font = ('Courier New', 20, 'bold'), bg = 'magenta', command = add_cus_acc).grid(row = i + 2, column = 0, columnspan = 3,pady=30)
    
        #globals()[e_var] = Button(X_1, text = "View Menu >>>", font = ('Times New Roman', 19), bg = 'black', fg = 'white', command = lambda num = i: res_menu(num))
        #globals()[e_var].grid(row = i + 1,column=4)
