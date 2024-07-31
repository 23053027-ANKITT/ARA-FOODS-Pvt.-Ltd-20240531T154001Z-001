from tkinter import *
from tkinter import ttk
import random as r
import random
from PIL import ImageTk
from PIL import Image
import math
import smtplib
import mysql.connector as ms
#from last_win import last_fn

def last_fn_2():

    #global ara_admin, main_frame_ad_2, my_canvas_ad_2, my_scrollbar_ad_2, adw_frame_ad_2, F_1_2
    global ara_admin2
    ara_admin2 = Tk()
    ara_admin2.title("ADMIN")
    ara_admin2.iconbitmap("logo.ico")
    ara_admin2.state("zoomed")
    ara_admin2.config(bg = '#003153')

    #====================
    
    #Create a main Frame
    main_frame = Frame(ara_admin2)
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

    #def back():
        #ara_admin2.destroy()
        #last_fn()

    #Button(second_frame, text = "< BACK", font = ('Elephant', 20), command = back).pack(pady=20,padx=20)

    X_1 = Frame(second_frame, bg = '#003153')
    X_1.pack(pady=20,padx=70)

    Label(X_1, text = "NAME", font = ('Fighting Spirit turbo', 20), bg = '#003153', fg = 'yellow').grid(row=0,column=0)
    Label(X_1, text = "AREA", font = ('Fighting Spirit turbo', 20), bg = '#003153', fg = 'yellow').grid(row=0,column=1)
    Label(X_1, text = "TYPE", font = ('Fighting Spirit turbo', 20), bg = '#003153', fg = 'yellow').grid(row=0,column=2)

    global ara_conn, ara_curr
    ara_conn = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    ara_curr = ara_conn.cursor(buffered = True)

    ara_curr.execute("select name, area, type from restaurants order by id")
    global datax
    datax = ara_curr.fetchall()

    def res_mod(num):

        global res_mod_win
        res_mod_win = Tk()
        res_mod_win.title("ADMIN")
        res_mod_win.iconbitmap("logo.ico")
        res_mod_win.state("zoomed")
        res_mod_win.config(bg = '#003153')

        main_frame = Frame(res_mod_win)
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

        #==========

        aa = "a_{}".format(num + 1)
        bb = "b_{}".format(num + 1)
        cc = "c_{}".format(num + 1)

        dF = LabelFrame(second_frame, bg = '#003153')
        dF.pack(pady=200,padx=200)

        Label(dF, text = "NAME", font = ('Times New Roman', 18, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=0)
        Label(dF, text = "AREA", font = ('Times New Roman', 18, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=1)
        Label(dF, text = "TYPE", font = ('Times New Roman', 18, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=2)

        global e1, e2, e3

        e1 = Entry(dF, width = 20, font = ('Times New Roman', 18))
        e1.grid(row=1,column=0)
        e1.insert(0, str(globals()[aa].cget('text')))

        e2 = Entry(dF, width = 20, font = ('Times New Roman', 18))
        e2.grid(row=1,column=1, padx = 30, pady = 40)
        e2.insert(0, str(globals()[bb].cget('text')))

        e3 = Entry(dF, width = 20, font = ('Times New Roman', 18))
        e3.grid(row=1,column=2)
        e3.insert(0, str(globals()[cc].cget('text')))

        def mod_fn():

            ara_curr.execute("update restaurants set name = '{}', area = '{}', type = '{}' where name = '{}' and area = '{}'".format(e1.get().strip(), e2.get().strip(), e3.get().strip(), globals()[aa].cget('text'), globals()[bb].cget('text')))
            ara_conn.commit()

            ara_curr.execute("create table " + e1.get().strip().replace(" ", "_") + "__" + e2.get().strip().replace(" ", "_") + " as select * from " + globals()[aa].cget('text').replace(" ", "_") + "__" + globals()[bb].cget('text').replace(" ", "_"))

            ara_curr.execute("drop table " + globals()[aa].cget('text').replace(" ", "_") + "__" + globals()[bb].cget('text').replace(" ", "_"))

            ara_admin2.destroy()
            last_fn_2()

            global L2
            L2 = Tk()
            L2.geometry("140x40")

            global t2, tL2
            t2 = 1
            tL2 = Label(L2, text = "SUCCESS!", font = ('Felix Titling', 20, 'bold'))
            tL2.pack()

            def timer2():
                global t2
                t2 = t2 - 1
                tL2.after(1000, timer2)
                if t2 == -1:
                    L2.destroy()
                    res_mod_win.destroy()
                
            timer2()
            

        def mod_fn_2():

            ara_curr.execute("delete from restaurants where name = '{}' and area = '{}'".format(str(globals()[aa].cget('text')), str(globals()[bb].cget('text'))))
            ara_conn.commit()

            ara_curr.execute("drop table " + globals()[aa].cget('text').replace(" ", "_") + "__" + globals()[bb].cget('text').replace(" ", "_"))

            ara_admin2.destroy()
            last_fn_2()

            global L1
            L1 = Tk()
            L1.geometry("140x40")

            global t1, tL1
            t1 = 1
            tL1 = Label(L1, text = "SUCCESS!", font = ('Felix Titling', 20, 'bold'))
            tL1.pack()

            def timer1():
                global t1
                t1 = t1 - 1
                tL1.after(1000, timer1)
                if t1 == -1:
                    L1.destroy()
                    res_mod_win.destroy()
                
            timer1()


        Button(dF, text = "UPDATE", font = ('Iron Blade', 20), bg = 'light green', command = mod_fn).grid(row=2,column=1)
        Button(dF, text = "DELETE This Restaurant", font = ('Iron Blade', 20), bg = 'light green', command = mod_fn_2).grid(row=3,column=1,pady=20)
        
        
    def res_menu(num):
        

        global res_menu_win
        res_menu_win = Tk()
        res_menu_win.title("ADMIN")
        res_menu_win.iconbitmap("logo.ico")
        res_menu_win.state("zoomed")
        res_menu_win.config(bg = '#003153')

        main_frame = Frame(res_menu_win)
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


        #==

        aa = "a_{}".format(num + 1)
        bb = "b_{}".format(num + 1)
        #cc = "c_{}".format(num + 1)

        dF = LabelFrame(second_frame, bg = '#003153')
        dF.pack(pady=20,padx=20)

        
        Label(dF, text = "Item", font = ('Times New Roman', 20, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=0)
        Label(dF, text = "Price", font = ('Times New Roman', 20, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=1)
        Label(dF, text = "Veg/Non-veg", font = ('Times New Roman', 20, 'bold'), bg = '#003153', fg = 'white').grid(row=0,column=2)

        ara_curr.execute("select items, price, vnv from " + str(globals()[aa].cget('text').replace(" ", "_")) + "__" + str(globals()[bb].cget('text').replace(" ", "_")))
        global datay
        datay = ara_curr.fetchall()

        def upd_menu(num):

            #aa = "a_{}".format(num - 1)
            #bb = "b_{}".format(num - 1)
            ae = "ae_{}".format(num + 1)
            be = "be_{}".format(num + 1)
            ce = "ce_{}".format(num + 1)

            #print(str(globals()[aa].cget('text').replace(" ", "_")) + "__" + str(globals()[bb].cget('text').replace(" ", "_")))
            #print(datax[num][0],datax[num][1])
            #print(globals()[ae].get())
            #print(int(globals()[be].get()))
            #print(globals()[ce].get())
            #print(datay[num][0])
            
            ara_curr.execute("update " + str(globals()[aa].cget('text').replace(" ", "_")) + "__" + str(globals()[bb].cget('text').replace(" ", "_")) + " set items = '{}', price = {}, vnv = '{}' where items = '{}'".format(globals()[ae].get(), int(globals()[be].get()), globals()[ce].get(), datay[num][0]))
            ara_conn.commit()

            res_menu_win.destroy()
            #done
            res_menu(int(aa[-1]) - 1)

            messi_1 = Tk()
            messi_1.title("ADMIN")
            messi_1.iconbitmap("logo.ico")
            messi_1.geometry("600x100")
            messi_1.config(bg = "black")

            messi_1_L = Label(messi_1, text = 'Modification completed successfully !!', bg = 'black', font = ('Iron Blade', 20, 'bold'), fg = 'cyan')
            messi_1_L.pack()

        def del_menu(num):

            ara_curr.execute("delete from " + str(globals()[aa].cget('text').replace(" ", "_")) + "__" + str(globals()[bb].cget('text').replace(" ", "_")) + " where items = '{}'".format(datay[num][0]))
            ara_conn.commit()

            res_menu_win.destroy()
            #done
            res_menu(int(aa[-1]) - 1)

            messi_2 = Tk()
            messi_2.title("ADMIN")
            messi_2.iconbitmap("logo.ico")
            messi_2.geometry("600x100")
            messi_2.config(bg = "black")

            messi_2_L = Label(messi_2, text = 'Deletion completed successfully !!', bg = 'black', font = ('Iron Blade', 20, 'bold'), fg = 'cyan')
            messi_2_L.pack()

        for j in range(len(datay)):

            ae = "ae_{}".format(j + 1)
            be = "be_{}".format(j + 1)
            ce = "ce_{}".format(j + 1)

            globals()[ae] = Entry(dF, width = 25, font = ('Times New Roman', 15), bg = 'cyan')
            globals()[ae].grid(row=j+1,column=0)
            globals()[ae].insert(0, str(datay[j][0]))

            globals()[be] = Entry(dF, width = 25, font = ('Times New Roman', 15), bg = 'cyan')
            globals()[be].grid(row=j+1,column=1,pady=50,padx=40)
            globals()[be].insert(0, str(datay[j][1]))

            globals()[ce] = Entry(dF, width = 25, font = ('Times New Roman', 15), bg = 'cyan')
            globals()[ce].grid(row=j+1,column=2)
            globals()[ce].insert(0, str(datay[j][2]))

            Button(dF, text = "Update", bg = 'pink', font = ('Iron Blade', 20), command = lambda num = j: upd_menu(num)).grid(row=j+1,column=3,padx=40)
            Button(dF, text = "Delete", bg = 'pink', font = ('Iron Blade', 20), command = lambda num = j: del_menu(num)).grid(row=j+1,column=4)            

        def add_menu():

            global maradona
            maradona = Tk()
            maradona.title("ADMIN")
            maradona.iconbitmap("logo.ico")
            maradona.geometry("820x220")
            maradona.config(bg = "#dedede")

            dF = LabelFrame(maradona, bg = '#dedede')
            dF.pack()

            Label(dF, text = "ITEM", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=0)
            Label(dF, text = "PRICE", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=1)
            Label(dF, text = "VEG/NON-VEG", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=2)

            global eee1, eee2, eee3

            eee1 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
            eee1.grid(row=1,column=0)
        #ee1.insert(0, str(globals()[aa].cget('text')))

            eee2 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
            eee2.grid(row=1,column=1, padx = 30, pady = 40)
        #ee2.insert(0, str(globals()[bb].cget('text')))

            eee3 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
            eee3.grid(row=1,column=2)
        #ee3.insert(0, str(globals()[cc].cget('text')))

            def add_final2():

                #ara_curr.execute("insert into restaurants values(NULL, '{}', '{}', '{}')".format(eee3.get().strip(), eee2.get().strip(), eee1.get().strip()))
                #ara_conn.commit()

                #ara_curr.execute("create table " + ee1.get().strip().replace(" ","_") + "__" + ee2.get().strip().replace(" ","_") + "(id int, items varchar(300), price int, vnv varchar(2))")

                ara_curr.execute("select id from " + globals()[aa].cget('text').replace(" ","_") + "__" + globals()[bb].cget('text').replace(" ","_") + " order by id desc")
                axe1 = ara_curr.fetchone()

                ara_curr.execute("insert into " + globals()[aa].cget('text').replace(" ","_") + "__" + globals()[bb].cget('text').replace(" ","_") + " values({}, '{}', {}, '{}')".format(int(axe1[0] + 1), str(eee1.get().strip()),int(eee2.get().strip()),str(eee3.get().strip())))
                ara_conn.commit()

                global done2
                done2 = Tk()
                done2.geometry("140x40")

                global t4, tL4
                t4 = 1
                tL4 = Label(done2, text = "SUCCESS!", font = ('Felix Titling', 20, 'bold'))
                tL4.pack()

                def timer4():
                    global t4
                    t4 = t4 - 1
                    tL4.after(1000, timer4)
                    if t4 == -1:
                        done2.destroy()
                        maradona.destroy()
                        res_menu_win.destroy()
                        res_menu(int(aa[-1]) - 1)
                
                timer4()

            Button(dF, text = "ADD", font = ('Courier New', 20, 'bold'), bg = 'black', fg = 'red', command = add_final2).grid(row=2,column=1)


        Button(dF, text = "Add Item [+]", font = ('Courier New', 20, 'bold'), bg = 'red', command = add_menu).grid(row=j+2,column=0,columnspan=3)

        #==========================
        

    for i in range(len(datax)):

        a_var = "a_{}".format(i + 1)
        b_var = "b_{}".format(i + 1)
        c_var = "c_{}".format(i + 1)
        d_var = "d_{}".format(i + 1)
        e_var = "e_{}".format(i + 1)

        globals()[a_var] = Label(X_1, text = str(datax[i][0]), font = ('Times New Roman', 18, 'bold'), bg = '#003153', fg = 'white')
        globals()[a_var].grid(row = i + 1, column=0)

        globals()[b_var] = Label(X_1, text = str(datax[i][1]), font = ('Times New Roman', 18, 'bold'), bg = '#003153', fg = 'white')
        globals()[b_var].grid(row = i + 1,column=1, padx=50)

        globals()[c_var] = Label(X_1, text = str(datax[i][2]), font = ('Times New Roman', 18, 'bold'), bg = '#003153', fg = 'white')
        globals()[c_var].grid(row = i + 1,column=2,pady=30)

        globals()[d_var] = Button(X_1, text = "Modify >>>", font = ('Times New Roman', 19), bg = 'yellow', command = lambda num = i: res_mod(num))
        globals()[d_var].grid(row = i + 1,column=3, padx=50)
    
        globals()[e_var] = Button(X_1, text = "View Menu >>>", font = ('Times New Roman', 19), bg = 'yellow', command = lambda num = i: res_menu(num))
        globals()[e_var].grid(row = i + 1,column=4)


    def add_res():

        global pele
        pele = Tk()
        pele.title("ADMIN")
        pele.iconbitmap("logo.ico")
        pele.geometry("820x220")
        pele.config(bg = "#dedede")

        dF = LabelFrame(pele, bg = '#dedede')
        dF.pack()

        Label(dF, text = "NAME", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=0)
        Label(dF, text = "AREA", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=1)
        Label(dF, text = "TYPE", font = ('Times New Roman', 18, 'bold'), bg = '#dedede').grid(row=0,column=2)

        global ee1, ee2, ee3

        ee1 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
        ee1.grid(row=1,column=0)
        #ee1.insert(0, str(globals()[aa].cget('text')))

        ee2 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
        ee2.grid(row=1,column=1, padx = 30, pady = 40)
        #ee2.insert(0, str(globals()[bb].cget('text')))

        ee3 = Entry(dF, width = 20, font = ('Times New Roman', 18), bg = 'black', fg = 'white')
        ee3.grid(row=1,column=2)
        #ee3.insert(0, str(globals()[cc].cget('text')))

        def add_final():

            ara_curr.execute("select id from restaurants order by id desc")
            axe2 = ara_curr.fetchone()

            ara_curr.execute("insert into restaurants values({}, '{}', '{}', '{}')".format(int(axe2[0] + 1), ee3.get().strip(), ee2.get().strip(), ee1.get().strip()))
            ara_conn.commit()

            ara_curr.execute("create table " + ee1.get().strip().replace(" ","_") + "__" + ee2.get().strip().replace(" ","_") + "(id int, items varchar(300), price int, vnv varchar(2))")

            global done
            done = Tk()
            done.geometry("140x40")

            global t3, tL3
            t3 = 1
            tL3 = Label(done, text = "SUCCESS!", font = ('Felix Titling', 20, 'bold'))
            tL3.pack()

            def timer3():
                global t3
                t3 = t3 - 1
                tL3.after(1000, timer3)
                if t3 == -1:
                    done.destroy()
                    pele.destroy()
                    ara_admin2.destroy()
                    last_fn_2()
                
            timer3()

        Button(dF, text = "ADD", font = ('Courier New', 20, 'bold'), bg = 'black', fg = 'red', command = add_final).grid(row=2,column=1)

    Button(X_1, text = "Add Restaurant [+]", font = ('Courier New', 20, 'bold'), bg = 'red', command = add_res).grid(row = i + 2, column = 0, columnspan = 3,pady=30)
    
    #ara_conn.close()########
