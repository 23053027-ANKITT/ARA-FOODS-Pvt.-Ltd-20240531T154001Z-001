from tkinter import *
from tkinter import ttk
import mysql.connector as ms
import pickle as p
#import json as j
from order_window import loading_win_4
from PIL import ImageTk
from PIL import Image

def loading_win_3():

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
            menu_window_frame()
        
    timer_load()

def menu_window_frame():

    menu_win = Tk()
    menu_win.title("ARA FOODS - MENU")
    menu_win.iconbitmap("logo.ico")
    menu_win.state('zoomed')
    menu_win.config(bg = '#3cfa02')

    main_frame = Frame(menu_win)
    main_frame.pack(fill = BOTH, expand = True)
    main_frame.config(bg = '#3cfa02')

    #Create a Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill = BOTH, expand = True)
    my_canvas.config(bg = '#3cfa02')

    #Add a Scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side = RIGHT, fill = Y)

    #Configure the canvas
    my_canvas.configure(yscrollcommand = my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

    #Create another frame inside canvas
    sec_frame = Frame(my_canvas)

    #Add that new frame into the window
    my_canvas.create_window((0,0), window = sec_frame, anchor = 'nw')

    sec_frame.config(bg = '#3cfa02')

    ####
    boss_frame_1 = Frame(sec_frame, bg = '#3cfa02')
    boss_frame_1.pack(pady=30)

    global var2
    var2 = 0

    def toggle2():
    
        global var2
        if var2 % 2 == 0:
            menu_win.geometry('1920x1080')
        else:
            menu_win.state('zoomed')
        var2 = var2 + 1

    def btr():
        menu_win.destroy()

    toggle_btn = Button(boss_frame_1, text = 'Toggle Fullscreen  ON/OFF', font = ('Broadway', 15), bg = 'black', fg = 'pink', cursor = 'hand2', command = toggle2)
    #toggle_btn.grid(row=0,column=2,pady=20,padx=120)

    back_to_root = Button(boss_frame_1, text = '< Back', font = ('Broadway', 15), bg = 'black', fg = 'pink', cursor = 'hand2', command = btr)
    back_to_root.grid(row=0,column=0,pady=20,padx=20)

    mycon = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    mycur = mycon.cursor(buffered = True)
    mycur.execute("select id from rest_result_get order by id desc")
    myres1 = mycur.fetchone()
    mycur.execute("select id_rest from rest_result_get where id = {}".format(int(myres1[0])))
    myres2 = mycur.fetchone()
    mycur.execute("select name, area, type from restaurants where id = {}".format(int(myres2[0])))
    global myres3
    myres3 = mycur.fetchone()
    #print("myres3 ", myres3)

    bass1 = Label(boss_frame_1, text = myres3[0].upper(), bg = '#3cfa02', font = ('GodofThunder', 50))
    bass1.grid(row=1,column=1, sticky = 'w')

    bass2 = Label(boss_frame_1, text = myres3[1], bg = '#3cfa02', font = ('Iron Blade', 30))
    bass2.grid(row=2,column=1, sticky = 'w')

    bass3 = Label(boss_frame_1, text = myres3[2], bg = '#3cfa02', font = ('Ink Free', 20, 'bold'))
    bass3.grid(row=3,column=1, sticky = 'w')

    #
    boss_frame_0 = LabelFrame(sec_frame, bg = '#3cfa02')
    boss_frame_0.pack(pady=20)

    global boss_frame_2
    boss_frame_2 = LabelFrame(sec_frame, bg = '#3cfa02')
    boss_frame_2.pack(pady=30, padx = 100)
    

    def cart_fn_4(num):

        global cart_list
        if int(globals()["E_{}".format(num + 1)].get()) != 0:

            cart_dict = {'Restaurant' : myres3[0], 'Area' : myres3[1], 'Item' : str(p2res[num][1]), 'Price' : str(p2res[num][2]), 'Qty' : str(globals()["E_{}".format(num + 1)].get()), 'Veg/Non-veg' : str(p2res[num][3])}
            cart_list.append(cart_dict)

            f = open("CART_DICTIONARIES.txt", 'wb')
            p.dump(cart_list, f)
            f.close()

        '''global LF_win, L_F
        try:
            LF_win.destroy()
        except:
            pass
        LF_win = Tk()
        LF_win.title("CART")
        LF_win.iconbitmap("logo.ico")
        LF_win.geometry('700x300')
        LF_win.config(bg = 'silver')

        for item in LF_win.winfo_children():
            item.destroy()

        #res_list.clear()
        #res2_list.clear()


        for item_x in cart_list:
            Label(LF_win, text = item_x, font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)'''

        global LF_win, L_F
        try:
            LF_win.destroy()
        except:
            pass
        LF_win = Tk()
        LF_win.title("CART")
        LF_win.iconbitmap("logo.ico")
        LF_win.geometry('700x300')
        LF_win.config(bg = 'silver')

        #
        main_frame_22 = Frame(LF_win)
        main_frame_22.pack(fill = BOTH, expand = True)

        my_canvas_22 = Canvas(main_frame_22)
        my_canvas_22.pack(side = LEFT, fill = BOTH, expand = True)

        my_scrollbar_22 = ttk.Scrollbar(main_frame_22, orient = VERTICAL, command = my_canvas_22.yview)
        my_scrollbar_22.pack(side = RIGHT, fill = Y)

        my_canvas_22.configure(yscrollcommand = my_scrollbar_22.set)
        my_canvas_22.bind('<Configure>', lambda e: my_canvas_22.configure(scrollregion = my_canvas_22.bbox('all')))

        second_frame_22 = Frame(my_canvas_22)

        my_canvas_22.create_window((0,0), window = second_frame_22, anchor = 'nw')
        #

        for item in second_frame_22.winfo_children():
            item.destroy()


        for item_x in cart_list:
            Label(second_frame_22, text = "Restaurant Name: " + item_x['Restaurant'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Item: " + item_x['Item'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)            
            Label(second_frame_22, text = "Price: " + item_x['Price'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Qty: " + item_x['Qty'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Veg/Non-veg: " + item_x['Veg/Non-veg'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "----------", font = ('Times New Roman', 25), bg = 'silver').pack(padx=5,pady=5)

        Button(second_frame_22, text = "Proceed to Place Order", bg = 'black', fg = 'white', font = ('Courier New', 25), cursor = 'hand2', command = order_fn).pack(padx=5,pady=10)   

        

    def cart_fn_3(num):
        
        global cart_list
        if int(globals()["E_{}".format(num + 1)].get()) != 0:

            cart_dict = {'Restaurant' : myres3[0], 'Area' : myres3[1], 'Item' : str(pres[num][1]), 'Price' : str(pres[num][2]), 'Qty' : str(globals()["E_{}".format(num + 1)].get()), 'Veg/Non-veg' : str(pres[num][3])}
            cart_list.append(cart_dict)

            f = open("CART_DICTIONARIES.txt", 'wb')
            p.dump(cart_list, f)
            f.close()

        '''global LF_win, L_F
        try:
            LF_win.destroy()
        except:
            pass
        LF_win = Tk()
        LF_win.title("CART")
        LF_win.iconbitmap("logo.ico")
        LF_win.geometry('700x300')
        LF_win.config(bg = 'silver')

        for item in LF_win.winfo_children():
            item.destroy()

        #res_list.clear()
        #res2_list.clear()


        for item_x in cart_list:
            Label(LF_win, text = item_x, font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)'''

        global LF_win, L_F
        try:
            LF_win.destroy()
        except:
            pass
        LF_win = Tk()
        LF_win.title("CART")
        LF_win.iconbitmap("logo.ico")
        LF_win.geometry('700x300')
        LF_win.config(bg = 'silver')

        #
        main_frame_22 = Frame(LF_win)
        main_frame_22.pack(fill = BOTH, expand = True)

        my_canvas_22 = Canvas(main_frame_22)
        my_canvas_22.pack(side = LEFT, fill = BOTH, expand = True)

        my_scrollbar_22 = ttk.Scrollbar(main_frame_22, orient = VERTICAL, command = my_canvas_22.yview)
        my_scrollbar_22.pack(side = RIGHT, fill = Y)

        my_canvas_22.configure(yscrollcommand = my_scrollbar_22.set)
        my_canvas_22.bind('<Configure>', lambda e: my_canvas_22.configure(scrollregion = my_canvas_22.bbox('all')))

        second_frame_22 = Frame(my_canvas_22)

        my_canvas_22.create_window((0,0), window = second_frame_22, anchor = 'nw')
        #

        for item in second_frame_22.winfo_children():
            item.destroy()


        for item_x in cart_list:
            Label(second_frame_22, text = "Restaurant Name: " + item_x['Restaurant'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Item: " + item_x['Item'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)            
            Label(second_frame_22, text = "Price: " + item_x['Price'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Qty: " + item_x['Qty'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Veg/Non-veg: " + item_x['Veg/Non-veg'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "----------", font = ('Times New Roman', 25), bg = 'silver').pack(padx=5,pady=5)

        Button(second_frame_22, text = "Proceed to Place Order", bg = 'black', fg = 'white', font = ('Courier New', 25), cursor = 'hand2', command = order_fn).pack(padx=5,pady=10)   


    def cart_fn_2(num):
        
        global cart_list
        if int(globals()["E_{}".format(num + 1)].get()) != 0:

            cart_dict = {'Restaurant' : myres3[0], 'Area' : myres3[1], 'Item' : str(vres[num][1]), 'Price' : str(vres[num][2]), 'Qty' : str(globals()["E_{}".format(num + 1)].get()), 'Veg/Non-veg' : str(vres[num][3])}
            cart_list.append(cart_dict)

            f = open("CART_DICTIONARIES.txt", 'wb')
            p.dump(cart_list, f)
            f.close()

        '''global LF_win, L_F
        try:
            LF_win.destroy()
        except:
            pass
        LF_win = Tk()
        LF_win.title("CART")
        LF_win.iconbitmap("logo.ico")
        LF_win.geometry('700x300')
        LF_win.config(bg = 'silver')

        for item in LF_win.winfo_children():
            item.destroy()

        #res_list.clear()
        #res2_list.clear()


        for item_x in cart_list:
            Label(LF_win, text = item_x, font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)'''

        global LF_win, L_F
        try:
            LF_win.destroy()
        except:
            pass
        LF_win = Tk()
        LF_win.title("CART")
        LF_win.iconbitmap("logo.ico")
        LF_win.geometry('700x300')
        LF_win.config(bg = 'silver')

        #
        main_frame_22 = Frame(LF_win)
        main_frame_22.pack(fill = BOTH, expand = True)

        my_canvas_22 = Canvas(main_frame_22)
        my_canvas_22.pack(side = LEFT, fill = BOTH, expand = True)

        my_scrollbar_22 = ttk.Scrollbar(main_frame_22, orient = VERTICAL, command = my_canvas_22.yview)
        my_scrollbar_22.pack(side = RIGHT, fill = Y)

        my_canvas_22.configure(yscrollcommand = my_scrollbar_22.set)
        my_canvas_22.bind('<Configure>', lambda e: my_canvas_22.configure(scrollregion = my_canvas_22.bbox('all')))

        second_frame_22 = Frame(my_canvas_22)

        my_canvas_22.create_window((0,0), window = second_frame_22, anchor = 'nw')
        #

        for item in second_frame_22.winfo_children():
            item.destroy()


        for item_x in cart_list:
            Label(second_frame_22, text = "Restaurant Name: " + item_x['Restaurant'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Item: " + item_x['Item'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)            
            Label(second_frame_22, text = "Price: " + item_x['Price'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Qty: " + item_x['Qty'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Veg/Non-veg: " + item_x['Veg/Non-veg'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "----------", font = ('Times New Roman', 25), bg = 'silver').pack(padx=5,pady=5)

        Button(second_frame_22, text = "Proceed to Place Order", bg = 'black', fg = 'white', font = ('Courier New', 25), cursor = 'hand2', command = order_fn).pack(padx=5,pady=10)   


    def filter_price():
        p = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
        p0 = p.cursor(buffered = True)
        p0.execute("select * from " + myres3[0].replace(" ", "_") + "__" + myres3[1].replace(" ", "_") + " order by price")
        global pres
        pres = p0.fetchall()
        p.close()

        for item in boss_frame_2.winfo_children():
            item.destroy()

        for w in range(len(pres)):

            Btn_var = "Btn_{}".format(w + 1)
            E_var = "E_{}".format(w + 1)

            Label(boss_frame_2, text = pres[w][0], bg = '#3cfa02', font = ("Garamond", 15, 'bold')).grid(row=w,column=0,padx=10,pady=10)
            Label(boss_frame_2, text = pres[w][1], bg = '#3cfa02', font = ("Garamond", 15)).grid(row=w,column=1,padx=10,pady=10)
            Label(boss_frame_2, text = pres[w][2], bg = '#3cfa02', fg = 'blue', font = ("Garamond", 15)).grid(row=w,column=2,padx=10,pady=10)

            try:
                if pres[w][3] == 'v':
                    Label(boss_frame_2, text = "Veg", bg = '#3cfa02', fg = 'green', font = ("Garamond", 15)).grid(row=w,column=3,padx=10,pady=10)
                if pres[w][3] == 'nv':
                    Label(boss_frame_2, text = "Non-Veg", bg = '#3cfa02', fg = 'red', font = ("Garamond", 15)).grid(row=w,column=3,padx=10,pady=10)
            except:
                pass

            Label(boss_frame_2, text = "Qty:", bg = '#3cfa02', font = ("Garamond", 15)).grid(row=w,column=4,padx=10,pady=10)

            globals()[E_var] = Entry(boss_frame_2, width = 3, bg = 'yellow', font = ('Garamond', 15))
            globals()[E_var].grid(row=w,column=5,padx=10)
            globals()[E_var].insert(0, '0')

            globals()[Btn_var] = Button(boss_frame_2, text = "Add to Cart", fg = '#c203fc', bg = 'black', font = ('Matura MT Script Capitals', 15), cursor = 'hand2', command = lambda num = w: cart_fn_3(num))
            globals()[Btn_var].grid(row=w,column=6,padx=10)


    def filter_price_2():
        p2 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
        p20 = p2.cursor(buffered = True)
        p20.execute("select * from " + myres3[0].replace(" ", "_") + "__" + myres3[1].replace(" ", "_") + " order by price desc")
        global p2res
        p2res = p20.fetchall()
        p2.close()

        for item in boss_frame_2.winfo_children():
            item.destroy()

        for e in range(len(p2res)):

            Btn_var = "Btn_{}".format(e + 1)
            E_var = "E_{}".format(e + 1)

            Label(boss_frame_2, text = p2res[e][0], bg = '#3cfa02', font = ("Garamond", 15, 'bold')).grid(row=e,column=0,padx=10,pady=10)
            Label(boss_frame_2, text = p2res[e][1], bg = '#3cfa02', font = ("Garamond", 15)).grid(row=e,column=1,padx=10,pady=10)
            Label(boss_frame_2, text = p2res[e][2], bg = '#3cfa02', fg = 'blue', font = ("Garamond", 15)).grid(row=e,column=2,padx=10,pady=10)

            try:
                if p2res[e][3] == 'v':
                    Label(boss_frame_2, text = "Veg", bg = '#3cfa02', fg = 'green', font = ("Garamond", 15)).grid(row=e,column=3,padx=10,pady=10)
                if p2res[e][3] == 'nv':
                    Label(boss_frame_2, text = "Non-Veg", bg = '#3cfa02', fg = 'red', font = ("Garamond", 15)).grid(row=e,column=3,padx=10,pady=10)
            except:
                pass

            Label(boss_frame_2, text = "Qty:", bg = '#3cfa02', font = ("Garamond", 15)).grid(row=e,column=4,padx=10,pady=10)

            globals()[E_var] = Entry(boss_frame_2, width = 3, bg = 'yellow', font = ('Garamond', 15))
            globals()[E_var].grid(row=e,column=5,padx=10)
            globals()[E_var].insert(0, '0')

            globals()[Btn_var] = Button(boss_frame_2, text = "Add to Cart", fg = '#c203fc', bg = 'black', font = ('Matura MT Script Capitals', 15), cursor = 'hand2', command = lambda num = e: cart_fn_4(num))
            globals()[Btn_var].grid(row=e,column=6,padx=10)
    
    def filter_vnv():
        vnv = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
        vnv0 = vnv.cursor(buffered = True)
        vnv0.execute("select * from " + myres3[0].replace(" ", "_") + "__" + myres3[1].replace(" ", "_") + " where vnv = 'v'")
        global vres
        vres = vnv0.fetchall()
        vnv.close()

        for item in boss_frame_2.winfo_children():
            item.destroy()

        for q in range(len(vres)):
            
            Btn_var = "Btn_{}".format(q + 1)
            E_var = "E_{}".format(q + 1)

            Label(boss_frame_2, text = vres[q][0], bg = '#3cfa02', font = ("Garamond", 15, 'bold')).grid(row=q,column=0,padx=10,pady=10)
            Label(boss_frame_2, text = vres[q][1], bg = '#3cfa02', font = ("Garamond", 15)).grid(row=q,column=1,padx=10,pady=10)
            Label(boss_frame_2, text = vres[q][2], bg = '#3cfa02', fg = 'blue', font = ("Garamond", 15)).grid(row=q,column=2,padx=10,pady=10)

            try:
                if vres[q][3] == 'v':
                    Label(boss_frame_2, text = "Veg", bg = '#3cfa02', fg = 'green', font = ("Garamond", 15)).grid(row=q,column=3,padx=10,pady=10)
            except:
                pass

            Label(boss_frame_2, text = "Qty:", bg = '#3cfa02', font = ("Garamond", 15)).grid(row=q,column=4,padx=10,pady=10)

            globals()[E_var] = Entry(boss_frame_2, width = 3, bg = 'yellow', font = ('Garamond', 15))
            globals()[E_var].grid(row=q,column=5,padx=10)
            globals()[E_var].insert(0, '0')

            globals()[Btn_var] = Button(boss_frame_2, text = "Add to Cart", fg = '#c203fc', bg = 'black', font = ('Matura MT Script Capitals', 15), cursor = 'hand2', command = lambda num = q: cart_fn_2(num))
            globals()[Btn_var].grid(row=q,column=6,padx=10)


    def cart_fn(num):
        
        global cart_list
        if int(globals()["E_{}".format(num + 1)].get()) != 0:

            cart_dict = {'Restaurant' : myres3[0], 'Area' : myres3[1], 'Item' : str(myres4[num][1]), 'Price' : str(myres4[num][2]), 'Qty' : str(globals()["E_{}".format(num + 1)].get()), 'Veg/Non-veg' : str(myres4[num][3])}
            cart_list.append(cart_dict)

            f = open("CART_DICTIONARIES.txt", 'wb')
            p.dump(cart_list, f)
            f.close()

        global LF_win, L_F
        try:
            LF_win.destroy()
        except:
            pass
        LF_win = Tk()
        LF_win.title("CART")
        LF_win.iconbitmap("logo.ico")
        LF_win.geometry('700x300')
        LF_win.config(bg = 'silver')

        #
        main_frame_22 = Frame(LF_win)
        main_frame_22.pack(fill = BOTH, expand = True)

        my_canvas_22 = Canvas(main_frame_22)
        my_canvas_22.pack(side = LEFT, fill = BOTH, expand = True)

        my_scrollbar_22 = ttk.Scrollbar(main_frame_22, orient = VERTICAL, command = my_canvas_22.yview)
        my_scrollbar_22.pack(side = RIGHT, fill = Y)

        my_canvas_22.configure(yscrollcommand = my_scrollbar_22.set)
        my_canvas_22.bind('<Configure>', lambda e: my_canvas_22.configure(scrollregion = my_canvas_22.bbox('all')))

        second_frame_22 = Frame(my_canvas_22)

        my_canvas_22.create_window((0,0), window = second_frame_22, anchor = 'nw')
        #

        for item in second_frame_22.winfo_children():
            item.destroy()


        for item_x in cart_list:
            Label(second_frame_22, text = "Restaurant Name: " + item_x['Restaurant'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Item: " + item_x['Item'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)            
            Label(second_frame_22, text = "Price: " + item_x['Price'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Qty: " + item_x['Qty'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "Veg/Non-veg: " + item_x['Veg/Non-veg'], font = ('Times New Roman', 15), bg = 'silver').pack(padx=5,pady=5)
            Label(second_frame_22, text = "----------", font = ('Times New Roman', 25), bg = 'silver').pack(padx=5,pady=5)

        Button(second_frame_22, text = "Proceed to Place Order", bg = 'black', fg = 'white', font = ('Courier New', 25), cursor = 'hand2', command = order_fn).pack(padx=5,pady=10)   
        

    def filter_reset():

        for r in range(len(myres4)):

            Btn_var = "Btn_{}".format(r + 1)
            E_var = "E_{}".format(r + 1)

            Label(boss_frame_2, text = myres4[r][0], bg = '#3cfa02', font = ("Garamond", 15, 'bold')).grid(row=r,column=0,padx=10,pady=10)
            Label(boss_frame_2, text = myres4[r][1], bg = '#3cfa02', font = ("Garamond", 15)).grid(row=r,column=1,padx=10,pady=10)
            Label(boss_frame_2, text = myres4[r][2], bg = '#3cfa02', fg = 'blue', font = ("Garamond", 15)).grid(row=r,column=2,padx=10,pady=10)

            try:
                if myres4[r][3] == 'v':
                    Label(boss_frame_2, text = "Veg", bg = '#3cfa02', fg = 'green', font = ("Garamond", 15)).grid(row=r,column=3,padx=10,pady=10)
                if myres4[r][3] == 'nv':
                    Label(boss_frame_2, text = "Non-Veg", bg = '#3cfa02', fg = 'red', font = ("Garamond", 15)).grid(row=r,column=3,padx=10,pady=10)
            except:
                pass

            Label(boss_frame_2, text = "Qty:", bg = '#3cfa02', font = ("Garamond", 15)).grid(row=r,column=4,padx=10,pady=10)

            globals()[E_var] = Entry(boss_frame_2, width = 3, bg = 'yellow', font = ('Garamond', 15))
            globals()[E_var].grid(row=r,column=5,padx=10)
            globals()[E_var].insert(0, '0')

            globals()[Btn_var] = Button(boss_frame_2, text = "Add to Cart", fg = '#c203fc', bg = 'black', font = ('Matura MT Script Capitals', 15), cursor = 'hand2', command = lambda num = r: cart_fn(num))
            globals()[Btn_var].grid(row=r,column=6,padx=10)
    

    reorder_btn_price_1 = Button(boss_frame_0, text = "Filter by price (ascending)", bg = 'black', fg = '#3cfa02', font = ('Algerian', 15), command = filter_price)
    reorder_btn_price_1.grid(row=0,column=0)

    reorder_btn_price_2 = Button(boss_frame_0, text = "Filter by price (descending)", bg = 'black', fg = '#3cfa02', font = ('Algerian', 15), command = filter_price_2)
    reorder_btn_price_2.grid(row=0,column=1,padx=5)

    reorder_btn_vnv = Button(boss_frame_0, text = "Filter by Veg only", bg = 'black', fg = '#3cfa02', font = ('Algerian', 15), command = filter_vnv)
    reorder_btn_vnv.grid(row=0,column=2)

    reorder_btn_reset = Button(boss_frame_0, text = "Reset", bg = 'black', fg = '#3cfa02', font = ('Algerian', 15), command = filter_reset)
    reorder_btn_reset.grid(row=0,column=3,padx=5)
    #

    mycur.execute("select * from " + myres3[0].replace(" ", "_") + "__" + myres3[1].replace(" ", "_") + "")
    myres4 = mycur.fetchall()
    

    #global cart_list
    #cart_list = []


    for i in range(len(myres4)):

        Btn_var = "Btn_{}".format(i + 1)
        E_var = "E_{}".format(i + 1)

        Label(boss_frame_2, text = myres4[i][0], bg = '#3cfa02', font = ("Garamond", 15, 'bold')).grid(row=i,column=0,padx=10,pady=10)
        Label(boss_frame_2, text = myres4[i][1], bg = '#3cfa02', font = ("Garamond", 15)).grid(row=i,column=1,padx=10,pady=10)
        Label(boss_frame_2, text = myres4[i][2], bg = '#3cfa02', fg = 'blue', font = ("Garamond", 15)).grid(row=i,column=2,padx=10,pady=10)

        try:
            if myres4[i][3] == 'v':
                Label(boss_frame_2, text = "Veg", bg = '#3cfa02', fg = 'green', font = ("Garamond", 15)).grid(row=i,column=3,padx=10,pady=10)
            if myres4[i][3] == 'nv':
                Label(boss_frame_2, text = "Non-Veg", bg = '#3cfa02', fg = 'red', font = ("Garamond", 15)).grid(row=i,column=3,padx=10,pady=10)
        except:
            pass

        '''LF = LabelFrame(boss_frame_2, bg = '#3cfa02')
        LF.grid(row=i,column=4)
        Button(LF, text = "-", bg = 'black', fg = 'white', font = ('Garamond', 20), command = less_fn()).pack(side = LEFT)
        Label(LF, text = '\r' + str(qty_num), font = ('Garamond', 20)).pack(side = RIGHT)
        Button(LF, text = "+", bg = 'black', fg = 'white', font = ('Garamond', 20), command = more_fn()).pack(side = RIGHT)'''

        Label(boss_frame_2, text = "Qty:", bg = '#3cfa02', font = ("Garamond", 15)).grid(row=i,column=4,padx=10,pady=10)

        globals()[E_var] = Entry(boss_frame_2, width = 3, bg = 'yellow', font = ('Garamond', 15))
        globals()[E_var].grid(row=i,column=5,padx=10)
        globals()[E_var].insert(0, '0')

        globals()[Btn_var] = Button(boss_frame_2, text = "Add to Cart", fg = '#c203fc', bg = 'black', font = ('Matura MT Script Capitals', 15), cursor = 'hand2', command = lambda num = i: cart_fn(num))
        globals()[Btn_var].grid(row=i,column=6,padx=10)
        

    def order_fn():
        try:
            LF_win.destroy()
        except:
            pass
        menu_win.destroy()
        loading_win_4()


    btn_frame = Frame(sec_frame, bg = '#3cfa02')
    btn_frame.pack(pady=20,padx=20)

    order_btn = Button(btn_frame, text = "Proceed to Place Order", bg = 'black', fg = '#c203fc', font = ('Cocogoose Pro', 25), cursor = 'hand2', command = order_fn)
    order_btn.grid(row=0,column=1,padx=5)

    global LF_win, L_F

global cart_list, res_list, res2_list
cart_list = []
res_list = []
res2_list = []

def m_destroy():

    menu_win.destroy()
