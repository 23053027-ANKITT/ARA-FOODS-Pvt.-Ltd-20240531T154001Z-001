from tkinter import *
from tkinter import ttk
import mysql.connector as ms
import pickle as p
from PIL import ImageTk, Image
import math
import random
import smtplib
from bill_window import loading_win_5

def loading_win_4():

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
            ord_win_fn()
        
    timer_load()

def ord_win_fn():

    ord_win = Tk()
    ord_win.title("ARA FOODS - ORDER")
    ord_win.iconbitmap("logo.ico")
    #ord_win.attributes('-fullscreen', True)
    ord_win.config(bg = '#FFE5B4')

    main_frame = Frame(ord_win)
    main_frame.pack(fill = BOTH, expand = True)
    main_frame.config(bg = '#FFE5B4')

    #Create a Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill = BOTH, expand = True)
    my_canvas.config(bg = '#FFE5B4')

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

    sec_frame.config(bg = '#FFE5B4')


    boss_frame_1 = Frame(sec_frame, bg = '#FFE5B4')
    boss_frame_1.pack(pady=30)

    #global var2
    #var2 = 0
    #ord_win.geometry("1920x1080")
    ord_win.state('zoomed')

    '''def toggle2():
    
        global var2
        if var2 % 2 == 0:
            #ord_win.attributes('-fullscreen', False)
            #ord_win.state('zoomed')
            ord_win.geometry("1920x1080")
        else:
            ord_win.state('zoomed')
        var2 = var2 + 1'''

    def btr():
        ord_win.destroy()

    #toggle_btn = Button(boss_frame_1, text = 'Toggle Fullscreen  ON/OFF', font = ('Broadway', 15), bg = 'black', fg = 'pink', cursor = 'hand2', command = toggle2)
    #toggle_btn.grid(row=0,column=2,pady=20,padx=120)

    Label(boss_frame_1, text = 'Place Order', font = ('Algerian', 30), bg = '#FFE5B4').grid(row=0,column=1)

    back_to_root = Button(boss_frame_1, text = '< Back', font = ('Broadway', 15), bg = 'black', fg = 'pink', cursor = 'hand2', command = btr)
    back_to_root.grid(row=0,column=0,pady=20,padx=20)

    
    boss_frame_2 = Frame(sec_frame, bg = '#FFE5B4')
    boss_frame_2.pack(pady=10)

    Label(boss_frame_1, text = 'Your Cart Items', font = ('Algerian', 30), bg = '#FFE5B4').grid(row=1,column=1)

    try:
        f = open("CART_DICTIONARIES.txt", 'rb')
        while True:
            try:
                data = p.load(f)
            except:
                break
    except:
        sign_error = Tk()
        sign_error.title("ERROR")
        sign_error.iconbitmap("logo.ico")
        sign_error.geometry("500x100")
        sign_error.config(bg = "black")

        sign_error_label = Label(sign_error, text = "You haven't added anything in cart yet!", font = ('Iron Blade', 20), bg = 'black', fg = 'red')
        sign_error_label.pack(pady=20)

    ssl = []
    for i in data:
        ssl.append(i['Restaurant'] + '__' + i['Area'])
    ssll = list(set(ssl))

    t_list = []
    for j in range(len(ssll)):

        LB_var = "LB_{}".format(j + 1)
        t_list.append(str(LB_var))
        globals()[LB_var] = LabelFrame(boss_frame_2, text = ssll[j], font = ('Iron Blade', 20), bg = '#FFE5B4')
        globals()[LB_var].pack(pady=10)


    def del_fn(num):

        X1_var = "B1_{}".format(num + 1)
        X2_var = "B2_{}".format(num + 1)
        X3_var = "B3_{}".format(num + 1)
        X4_var = "B4_{}".format(num + 1)
        X_var = "B_{}".format(num + 1)
        ###
        yyy = globals()[X2_var].cget("text")
        ttt = globals()[X4_var].cget("text")

        grand2 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
        net2 = grand2.cursor(buffered = True)
        net2.execute("select id from grand_cost order by id desc")
        rcc2 = net2.fetchone()
        net2.execute("select * from grand_cost where id = {}".format(rcc2[0]))
        rcc3 = net2.fetchone()
        q1 = float(rcc3[1]) - float(float(yyy) * int(ttt))
        q2 = float(rcc3[2]) - 0.05 * float(float(yyy) * int(ttt))
        q3 = float(rcc3[3]) - 0.25 * float(float(yyy) * int(ttt))
        q4 = float(rcc3[4]) - 1.30 * float(float(yyy) * int(ttt))
        net2.execute("insert into grand_cost values({}, {}, {}, {}, {})".format(rcc2[0] + 1, q1, q2, q3, q4))
        grand2.commit()

        net2.execute("select * from grand_cost order by id desc")
        rcc4 = net2.fetchone()
        
        grand2.close()
        
        #global gra_l2, price_l2, delc_l2, tax_l2, net_cost

        f_1 = open("CART_DICTIONARIES.txt", 'rb')
        try:
            while True:
                d1 = p.load(f_1)
        except EOFError:
            pass
        f_1.close()

        #print(vars()[globals()[X1_var].].cget('text').split('__')[0])

        f_2 = open("CART_DICTIONARIES.txt", 'wb')
        for t in d1:
            if t['Item'] == globals()[X1_var].cget('text') and t['Price'] == globals()[X2_var].cget('text') and t['Veg/Non-veg'] == globals()[X3_var].cget('text') and t['Qty'] == globals()[X4_var].cget('text'):
                del d1[d1.index(t)]
        #print(d1)
        p.dump(d1, f_2)
        f_2.close()
        
        gra_l2.config(text = str(rcc4[4]))
        price_l2.config(text = str(rcc4[1]))
        delc_l2.config(text = str(rcc4[3]))
        tax_l2.config(text = str(rcc4[2]))
        ###
        globals()[X1_var].destroy()
        globals()[X2_var].destroy()
        globals()[X3_var].destroy()
        globals()[X4_var].destroy()
        globals()[X_var].destroy()
        
        
    for k in range(len(data)):
        LB_var = "LB_{}".format(k + 1)
        B1_var = "B1_{}".format(k + 1)
        B2_var = "B2_{}".format(k + 1)
        B3_var = "B3_{}".format(k + 1)
        B4_var = "B4_{}".format(k + 1)
        B_var = "B_{}".format(k + 1)
        
        
        if data[k]['Restaurant'] + '__' + data[k]['Area'] in ssll:
            iii = ssll.index(data[k]['Restaurant'] + '__' + data[k]['Area'])

            globals()[B1_var] = Label(globals()[t_list[iii]], text = data[k]['Item'], font = ('Century', 15), bg = 'yellow')
            globals()[B1_var].grid(row=k, column=0)
            
            globals()[B2_var] = Label(globals()[t_list[iii]], text = data[k]['Price'], font = ('Century', 15), bg = 'cyan')
            globals()[B2_var].grid(row=k, column=1,padx=10)

            if data[k]['Veg/Non-veg'] == 'v':
                globals()[B3_var] = Label(globals()[t_list[iii]], text = data[k]['Veg/Non-veg'], font = ('Century', 15), bg = '#00fc00')
                globals()[B3_var].grid(row=k, column=2)
                
            if data[k]['Veg/Non-veg'] == 'nv':
                globals()[B3_var] = Label(globals()[t_list[iii]], text = data[k]['Veg/Non-veg'], font = ('Century', 15), bg = '#fc0000')
                globals()[B3_var].grid(row=k, column=2)
            
            globals()[B4_var] = Label(globals()[t_list[iii]], text = data[k]['Qty'], font = ('Century', 15), bg = 'white')
            globals()[B4_var].grid(row=k, column=3,padx=10)

            globals()[B_var] = Button(globals()[t_list[iii]], text = 'x', font = ('Iron Blade', 15), bg = 'black', fg = 'white', command = lambda num = k: del_fn(num))
            globals()[B_var].grid(row=k,column=4)
        

    '''temp_list = []

    for i in range(len(data)):
        for j in data[i]:
            #print(data[i][j])
            temp_list.append(data[i][j])'''

    '''for x in range(len(temp_list)):
        for y in temp_list[x]:
            print(y)'''
    
        #E_var = "E_{}".format(i + 1)
        #LB_var = "LB_{}".format(i + 1)
        #Label(globals()[LB_var], text =

    #c = 0
    '''def del_fn(num):
        X1_var = "B_{}".format(num + 1)
        X2_var = "B1_{}".format(num + 1)
        X3_var = "B2_{}".format(num + 1)
        X4_var = "E_{}".format(num + 1)
        ###
        yyy = globals()[X3_var].cget("text")
        ttt = globals()[X4_var].get()
        #global gra_l2, price_l2, delc_l2, tax_l2, net_cost
        gra_l2.config(text = float(1.3 * net_cost) -  1.3 * (float(yyy) * int(ttt)))
        price_l2.config(text = float(net_cost) -  (float(yyy) * int(ttt)))
        delc_l2.config(text = float(0.25 * net_cost) -  0.25 * (float(yyy) * int(ttt)))
        tax_l2.config(text = float(0.05 * net_cost) -  0.05 * (float(yyy) * int(ttt)))
        ###
        globals()[X1_var].destroy()
        globals()[X2_var].destroy()
        globals()[X3_var].destroy()
        globals()[X4_var].destroy()'''
        
    
    '''for i in temp_list:
        for j in i:
            B_var = "B_{}".format(c + 1)
            B1_var = "B1_{}".format(c + 1)
            B2_var = "B2_{}".format(c + 1)
            E_var = "E_{}".format(c + 1)
            LB_var = "LB_{}".format(temp_list.index(i) + 1)
            globals()[B1_var] = Label(globals()[LB_var], text = j['Item'], font = ('Elephant', 18), bg = '#FFE5B4')
            globals()[B1_var].grid(row=c, column=0)
            globals()[B2_var] = Label(globals()[LB_var], text = j['Price'], font = ('Elephant', 18), bg = '#FFE5B4')
            globals()[B2_var].grid(row=c, column=1)
            globals()[E_var] = Entry(globals()[LB_var], width = 3, font = ('Times New Roman', 18), bg = 'white')
            globals()[E_var].insert(0, j['Qty'])
            globals()[E_var].grid(row=c, column=2)
            globals()[B_var] = Button(globals()[LB_var], text = 'x', font = ('Iron Blade', 18), bg = 'black', fg = 'white', command = lambda num = c: del_fn(num))
            globals()[B_var].grid(row=c,column=3)
            c = c + 1'''

    global number
    number = 0
    def coupon_check():
        if e.get() in ['LOT50', 'ARA30', 'EAT10']:
            global number
            number = 1
            e.config(state = DISABLED)
            b.config(state = DISABLED)
            v = Label(lb, text = 'Coupon Applied ' + u'\u2713', font = ('Times New Roman', 18), bg = 'cyan')
            v.grid(row=0,column=3)

            if e.get() == 'LOT50':

                x1 = gra_l2.cget('text')
                x2 = price_l2.cget('text')
                x3 = delc_l2.cget('text')
                x4 = tax_l2.cget('text')
                
                gra_l2.config(text = 0.5 * x1)
                price_l2.config(text = 0.5 * x2)
                delc_l2.config(text = 0.5 * x3)
                tax_l2.config(text = 0.5 * x4)

            elif e.get() == 'ARA30':

                x1 = gra_l2.cget('text')
                x2 = price_l2.cget('text')
                x3 = delc_l2.cget('text')
                x4 = tax_l2.cget('text')

                gra_l2.config(text = 0.7 * x1)
                price_l2.config(text = 0.7 * x2)
                delc_l2.config(text = 0.7 * x3)
                tax_l2.config(text = 0.7 * x4)

            elif e.get() == 'EAT10':

                x1 = gra_l2.cget('text')
                x2 = price_l2.cget('text')
                x3 = delc_l2.cget('text')
                x4 = tax_l2.cget('text')

                gra_l2.config(text = 0.9 * x1)
                price_l2.config(text = 0.9 * x2)
                delc_l2.config(text = 0.9 * x3)
                tax_l2.config(text = 0.9 * x4)

            else:
                pass

    global lb, e, b
    lb = LabelFrame(boss_frame_2, bg = '#FFE5B4')
    lb.pack(pady=10)
    l = Label(lb, text = "Enter Coupon:", font = ('Algerian', 18), bg = '#FFE5B4')
    l.grid(row=0,column=0)
    e = Entry(lb, width = 10)
    e.grid(row=0,column=1)
    b = Button(lb, text = 'Apply', font = ('Iron Blade', 18), bg = 'black', fg = 'white', command = coupon_check)
    b.grid(row=0,column=2)


    global net_cost
    net_cost = 0
    for i in data:
        net_cost += float(float(i['Price']) * int(i['Qty']))
        
    grand = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    net = grand.cursor(buffered = True)
    net.execute("select id from grand_cost order by id desc")
    rcc = net.fetchone()
    net.execute("insert into grand_cost values({}, {}, {}, {}, {})".format(rcc[0] + 1, net_cost, 0.05 * net_cost, 0.25 * net_cost, 1.30 * net_cost))
    grand.commit()
    grand.close()

    price_lb = LabelFrame(boss_frame_2, bg = '#FFE5B4')
    price_lb.pack(pady=10)

    global gra_l2, price_l2, delc_l2, tax_l2

    price_l = Label(price_lb, text = "Item Total:", font = ('Agency FB', 22, 'bold'), bg = '#FFE5B4', fg = 'black')
    price_l.grid(row=0,column=0)
    price_l2 = Label(price_lb, text = net_cost, font = ('Agency FB', 20, 'bold'), bg = '#FFE5B4', fg = 'black')
    price_l2.grid(row=0,column=1,padx=5)

    delc_l = Label(price_lb, text = "Delivary Charges (25%):", font = ('Agency FB', 20, 'bold'), bg = '#FFE5B4', fg = 'black')
    delc_l.grid(row=1,column=0,pady=5)
    delc_l2 = Label(price_lb, text = 0.25 * net_cost, font = ('Agency FB', 20, 'bold'), bg = '#FFE5B4', fg = 'black')
    delc_l2.grid(row=1,column=1,padx=5)

    tax_l = Label(price_lb, text = "Govt. Taxes (GST, Service Tax):", font = ('Agency FB', 20, 'bold'), bg = '#FFE5B4', fg = 'black')
    tax_l.grid(row=2,column=0,pady=5)
    tax_l2 = Label(price_lb, text = 0.05 * net_cost, font = ('Agency FB', 20, 'bold'), bg = '#FFE5B4', fg = 'black')
    tax_l2.grid(row=2,column=1,padx=5)
        
    gra_l = Label(price_lb, text = "GRAND TOTAL:", font = ('Agency FB', 25, 'bold'), bg = '#FFE5B4', fg = 'black')
    gra_l.grid(row=3,column=0,pady=5)
    gra_l2 = Label(price_lb, text = 1.3 * net_cost, font = ('Agency FB', 25, 'bold'), bg = '#FFE5B4', fg = 'black')
    gra_l2.grid(row=3,column=1,padx=5)
    

    details_lb = LabelFrame(boss_frame_2, bg = '#FFE5B4')
    details_lb.pack(pady=10)

    name = Label(details_lb, text = "Name:", font = ('Pricedown Bl', 20), bg = '#FFE5B4', fg = 'black')
    name.grid(row=0,column=0)
    ph_no = Label(details_lb, text = "Phone Number:", font = ('Pricedown Bl', 20), bg = '#FFE5B4', fg = 'black')
    ph_no.grid(row=1,column=0)
    address = Label(details_lb, text = "Address:", font = ('Pricedown Bl', 20), bg = '#FFE5B4', fg = 'black')
    address.grid(row=2,column=0)

    global name_e, ph_no_e, address_e
    name_e = Entry(details_lb, width = 15, font = ('Times New Roman', 20), bg = 'white', fg = 'black')
    name_e.grid(row=0,column=1)
    ph_no_e = Entry(details_lb, width = 15, font = ('Times New Roman', 20), bg = 'white', fg = 'black')
    ph_no_e.grid(row=1,column=1)
    address_e = Entry(details_lb, width = 30, font = ('Times New Roman', 20), bg = 'white', fg = 'black')
    address_e.grid(row=2,column=1)

    con_less = LabelFrame(boss_frame_2, text = "ARA FOODS' Contactless Delivery", font = ('GodofThunder', 25), bg = '#FFE5B4', fg = 'black')
    con_less.pack(pady=10)
    content = Label(con_less, text = "Restaurant's delivery partner will leave\nyour order outside the door, on a clean\nsurface (only applicable for online paid\norders)", font = ('Ink Free', 20, 'bold'), bg = '#FFE5B4', fg = 'black')
    content.grid(row=0,column=0,pady=5)

    #checkbox_var = IntVar()
    #checkbox_var.set(0)
    #global check_count
    #check_count = 0
    def check_changed():
        global chk
        if chk == 0:
            checkbtn.config(image = new_bg_2)
            chk = 1
        else:
            checkbtn.config(image = new_bg_1)
            chk = 0
            
    global bg_1, bg_2, new_bg_1, new_bg_2, bg_1_res, bg_2_res

    bg_1 = Image.open("cb_u.png")
    bg_1_res = bg_1.resize((100, 100), Image.Resampling.LANCZOS)
    new_bg_1 = ImageTk.PhotoImage(bg_1_res, master = con_less)

    bg_2 = Image.open("cb_c.png")
    bg_2_res = bg_2.resize((100, 100), Image.Resampling.LANCZOS)
    new_bg_2 = ImageTk.PhotoImage(bg_2_res, master = con_less)
    
    #img_1 = Image.open("cb_u.png")
    #bg_1_res = img_1.resize((1275, 715), Image.ANTIALIAS)
    #new_img_1 = ImageTk.PhotoImage(img_1, master = con_less)

    #img_2 = Image.open("cb_c.png")
    #bg_2_res = img_2.resize((1275, 715), Image.ANTIALIAS)
    #new_img_2 = ImageTk.PhotoImage(img_2, master = con_less)
    #img_11 = Label(con_less, image = new_bg_1, highlightcolor = '#FFD700', highlightbackground = '#FFD700', highlightthickness = 3)


    #img1 = ImageTk.PhotoImage(Image.open("cb_u.png"))
    #img2 = ImageTk.PhotoImage(Image.open("cb_c.png"))
    
    checkbtn = Button(con_less, image = new_bg_1, bg = 'white', font = ('Ink Free', 20, 'bold'), command = check_changed)
    checkbtn.grid(row=0,column=1)

    #=============================================================================================#

    global billing
    billing = LabelFrame(ord_win, text = "Billing", font = ('GodofThunder', 25), bg = '#FFE5B4')
    billing.place(x=770,y=144)

    bb1 = LabelFrame(billing, text = 'Cards', font = ('Algerian', 20), bg = '#FFE5B4')
    bb2 = LabelFrame(billing, text = 'UPI', font = ('Algerian', 20), bg = '#FFE5B4')
    bb3 = LabelFrame(billing, text = 'Wallets', font = ('Algerian', 20), bg = '#FFE5B4')
    bb4 = LabelFrame(billing, text = 'Netbanking', font = ('Algerian', 20), bg = '#FFE5B4')
    #bb5 = LabelFrame(billing, text = 'Pay Later', font = ('Algerian', 20), bg = '#FFE5B4')
    bb5 = LabelFrame(billing, text = 'Cash On Delivery', font = ('Algerian', 20), bg = '#FFE5B4')
    bb1.grid(row=0,column=0)
    bb2.grid(row=1,column=0)
    bb3.grid(row=2,column=0)
    bb4.grid(row=3,column=0)
    #bb5.grid(row=4,column=0)
    bb5.grid(row=4,column=0)

    def back_to_mode():

        try:
            xtra.destroy()
        except:
            pass
        
        try:
            gajini.destroy()
        except:
            pass

    def place_order_fn():

        alpha = ['b2-1','b3-1','b3-2','b1-1','b4-1','b5-1']
        beta = ['UPI', 'PayTM', 'PhonePe', 'Card', 'Netbanking', 'COD']

        if pay_var in alpha:

            '''for child in billing.winfo_children():
                print(child)
                #child.configure(state = DISABLED)'''

            global gajini
            gajini = Frame(ord_win, bg = '#FFE5B4', height = 600, width = 550)
            gajini.place(x=700, y=140)
            #for ghazi in range(60):            
                #Label(gajini, text = '  ', font = ('Times New Roman', 20), bg = '#FFE5B4', fg = '#FFE5B4').pack()

            global xtra
            xtra = LabelFrame(ord_win, bg = '#FFE5B4')
            xtra.place(x = 800, y = 300)
            '''m = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            u = m.cursor(buffered = True)
            u.execute("select net_cost_1_3 from grand_cost order by id desc")
            idu = u.fetchone()'''
            Label(xtra, text = "Final Amount: " + str(gra_l2.cget('text')), bg = "#FFE5B4", font = ('Times New Roman', 25, 'bold')).pack(pady=5,padx=5)
            #m.close()

            for pv in range(len(alpha)):
                if alpha[pv] == pay_var:
                    Label(xtra, text = "Mode of Payment: " + beta[pv], bg = "#FFE5B4", font = ('Times New Roman', 25, 'bold')).pack(padx=5)

            def final_order():

                fop = Tk()
                fop.title("Final Place Order")
                fop.iconbitmap("logo.ico")
                fop.geometry('400x300')

                global time_label
                time_label = Label(fop, text = '', font = ('Times New Roman', 60))
                time_label.pack(pady=50,padx=50)
                
                def cancel_order():
                    fop.destroy()
                cancel = Button(fop, text = "Cancel", font = ('Iron Blade', 30), bg = 'black', fg = 'white', command = cancel_order, cursor = 'hand2')
                cancel.pack(padx=100)

                #Label(fop, text = "(You can't cancel the order after count of 10 seconds)", font = ('Times New Roman', 20)).pack(pady=30,padx=150)
                

                global t
                t = 10
        
                def timer_admin():
                    global t
                    time_label.config(text = str(t))
                    t = t - 1
                    time_label.after(1000, timer_admin)
                    if t == -1:
                        time_label.destroy()
                        #print("ORDER CONFIRMED")
                        
                        bilx = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                        bily = bilx.cursor(buffered = True)
                        bily.execute("select id from order_bill order by id desc")
                        messi = bily.fetchone()
                        bily.execute("insert into order_bill values({}, '{}', {}, '{}')".format(int(messi[0]) + 1, str(name_e.get()), float(ph_no_e.get()), str(address_e.get())))
                        bilx.commit()
                        bilx.close()
                        
                        try:
                            fop.destroy()
                        except:
                            pass
                        try:
                            ord_win.destroy()
                        except:
                            pass
                        loading_win_5()
                        
        
                timer_admin()
                

            Button(xtra, text = "PLACE ORDER", font = ('Iron Blade', 20), bg = 'blue', fg = 'white', command = final_order).pack(pady=5,padx=5)
            Button(xtra, text = "Back", font = ('Iron Blade', 20), bg = 'red', command = back_to_mode).pack(pady=20,padx=10)

            
        

    global pay_var
    pay_var = None

    def bb2_l1():

        bb2_l1_win = Tk()
        bb2_l1_win.title("UPI")
        bb2_l1_win.iconbitmap("logo.ico")
        bb2_l1_win.geometry('300x300')
        bb2_l1_win.config(bg = "black")
        
        Label(bb2_l1_win, text = "Enter registered UPI ID:", font = ("Times New Roman", 20), fg = 'white', bg = 'black').grid(row=0,column=0)
        Entry(bb2_l1_win, width = 15, font = ("Times New Roman", 20)).grid(row=1,column=0,pady=10)
        
        def ee1b_fn():
            global pay_var
            pay_var = 'b2-1'
            bb2_l1_win.destroy()
            place_order_fn()
            
        Button(bb2_l1_win, text = "Continue >>>", font = ("Times New Roman", 20), fg = 'black', bg = 'white', command = ee1b_fn).grid(row=2,column=0)

    bb2_label_1 = Button(bb2, text = "Pay via UPI    " + u'\u2192', font = ('Avengeance', 18), bg = '#FFE5B4', command = bb2_l1)
    bb2_label_1.grid(row=0,column=0,columnspan=2)
    
    def bb3_l1():

        bb3_l1_win = Tk()
        bb3_l1_win.title("PayTM")
        bb3_l1_win.iconbitmap("logo.ico")
        bb3_l1_win.geometry('300x300')
        bb3_l1_win.config(bg = "black")

        def ee2b_fn():

            global jjj
            jjj = 0
            try:
                global OTP_admin

                digits="0123456789"
                OTP_admin=""
                for i in range(6):
                    OTP_admin+=digits[math.floor(random.random()*10)]
                otp_admin = OTP_admin + " is your OTP for   < PayTM Verification >\n\n\n(Don't share OTP to anyone)"
                msg = otp_admin
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("arafoodscompany@gmail.com", "fpch trvj kldg qxkp")
                emailid = ee2.get()
                s.sendmail('&&&&&&&&&&&',emailid,msg)
                jjj = 1

            except:
                otp_error_admin = Tk()
                otp_error_admin.geometry("770x150")
                otp_error_admin.title("ERROR")
                otp_error_admin.iconbitmap("logo.ico")
                otp_error_admin.config(bg = 'black')
                label_error = Label(otp_error_admin, text = "\U0000274C" + " There was an unexpected error while generating the OTP" + "\n...Pls try again..." + "\n\n-Maybe try checking the internet connection-", bg = 'black', fg = 'red', font = ('Iron Blade', 20))
                label_error.pack(pady = 20)
                jjj = 0

        def ee2bx_fn():
            
            if jjj == 1:

                if otp_e.get() == OTP_admin:
                    global pay_var
                    pay_var = 'b3-1'
                    bb3_l1_win.destroy()
                    place_order_fn()
                else:
                    otp_error_admin2 = Tk()
                    otp_error_admin2.geometry("770x150")
                    otp_error_admin2.title("ERROR")
                    otp_error_admin2.iconbitmap("logo.ico")
                    otp_error_admin2.config(bg = 'black')
                    label_error2 = Label(otp_error_admin2, text = "Incorrect OTP ... Try Again", bg = 'black', fg = 'red', font = ('Iron Blade', 20))
                    label_error2.pack(pady = 20)

        Label(bb3_l1_win, text = "Enter registered Email ID:", font = ("Times New Roman", 20), fg = 'white', bg = 'black').grid(row=0,column=0)
        global ee2
        ee2 = Entry(bb3_l1_win, width = 20, font = ("Times New Roman", 20))
        ee2.grid(row=1,column=0,pady=10)

        qFrame = Frame(bb3_l1_win, bg = 'black')
        qFrame.grid(row=2,column=0)
        global otp_e, otp_b
        otp_e = Entry(qFrame, width = 7, font = ("Times New Roman", 20), bg = 'white', fg = 'black')
        otp_e.grid(row=0,column=0)
        otp_b = Button(qFrame, text = "Send OTP", font = ('Times New Roman', 20), bg = 'white', fg = 'black', command = ee2b_fn)
        otp_b.grid(row=0,column=1,padx=5)

        Button(bb3_l1_win, text = "Continue >>>", font = ("Times New Roman", 20), fg = 'black', bg = 'white', command = ee2bx_fn).grid(row=3,column=0,pady=10)
        
    bb3_label_1 = Button(bb3, text = "Continue via PayTM    " + u'\u2192', font = ('Avengeance', 18), bg = '#FFE5B4', command = bb3_l1)
    bb3_label_1.grid(row=0,column=0)

    def bb3_l2():

        bb3_l2_win = Tk()
        bb3_l2_win.title("PhonePe")
        bb3_l2_win.iconbitmap("logo.ico")
        bb3_l2_win.geometry('300x300')
        bb3_l2_win.config(bg = "black")

        def ee3b_fn():

            global jjj2
            jjj2 = 0
            try:
                global OTP_admin2

                digits="0123456789"
                OTP_admin2=""
                for i in range(6):
                    OTP_admin2+=digits[math.floor(random.random()*10)]
                otp_admin = OTP_admin + " is your OTP for   < PayTM Verification >\n\n\n(Don't share OTP to anyone)"
                msg = otp_admin
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("arafoodscompany@gmail.com", "fpch trvj kldg qxkp")
                emailid = ee3.get()
                s.sendmail('&&&&&&&&&&&',emailid,msg)
                jjj2 = 1

            except:
                otp_error_admin = Tk()
                otp_error_admin.geometry("770x150")
                otp_error_admin.title("ERROR")
                otp_error_admin.iconbitmap("logo.ico")
                otp_error_admin.config(bg = 'black')
                label_error = Label(otp_error_admin, text = "\U0000274C" + " There was an unexpected error while generating the OTP" + "\n...Pls try again..." + "\n\n-Maybe try checking the internet connection-", bg = 'black', fg = 'red', font = ('Iron Blade', 20))
                label_error.pack(pady = 20)
                jjj2 = 0

        def ee3bx_fn():
            
            if jjj2 == 1:

                if otp2_e.get() == OTP_admin2:
                    global pay_var
                    pay_var = 'b3-2'
                    bb3_l2_win.destroy()
                    place_order_fn()
                else:
                    otp_error_admin2 = Tk()
                    otp_error_admin2.geometry("770x150")
                    otp_error_admin2.title("ERROR")
                    otp_error_admin2.iconbitmap("logo.ico")
                    otp_error_admin2.config(bg = 'black')
                    label_error2 = Label(otp_error_admin2, text = "Incorrect OTP ... Try Again", bg = 'black', fg = 'red', font = ('Iron Blade', 20))
                    label_error2.pack(pady = 20)

        Label(bb3_l2_win, text = "Enter registered Email ID:", font = ("Times New Roman", 20), fg = 'white', bg = 'black').grid(row=0,column=0)
        global ee3
        ee3 = Entry(bb3_l2_win, width = 20, font = ("Times New Roman", 20))
        ee3.grid(row=1,column=0,pady=10)

        qFrame2 = Frame(bb3_l2_win, bg = 'black')
        qFrame2.grid(row=2,column=0)
        global otp2_e, otp2_b
        otp2_e = Entry(qFrame2, width = 7, font = ("Times New Roman", 20), bg = 'white', fg = 'black')
        otp2_e.grid(row=0,column=0)
        otp2_b = Button(qFrame2, text = "Send OTP", font = ('Times New Roman', 20), bg = 'white', fg = 'black', command = ee3b_fn)
        otp2_b.grid(row=0,column=1,padx=5)

        Button(bb3_l2_win, text = "Continue >>>", font = ("Times New Roman", 20), fg = 'black', bg = 'white', command = ee3bx_fn).grid(row=3,column=0,pady=10)
        
        
    bb3_label_2 = Button(bb3, text = "Continue via PhonePe    " + u'\u2192', font = ('Avengeance', 18), bg = '#FFE5B4', command = bb3_l2)
    bb3_label_2.grid(row=0,column=2)

    def bb5_l1():
        #Label(bb5, text = u'\u2713', font = ("Times New Roman", 18, 'bold'), bg = '#FFE5B4').grid(row=0,column=1)
        #ee4 = Entry(bb3, width = 15, font = ("Times New Roman", 18), bg = '#FFE5B4')
        #ee4.grid(row=1,column=2)
        global pay_var
        pay_var = 'b5-1'
        place_order_fn()
        
    bb5_label_1 = Button(bb5, text = "Pay upon delivery at your doorstep", font = ('Avengeance', 18), bg = '#FFE5B4', command = bb5_l1)
    bb5_label_1.grid(row=0,column=0)

    def bb1_l1():

        bb1_l1_win = Tk()
        bb1_l1_win.title("Card")
        bb1_l1_win.iconbitmap("logo.ico")
        bb1_l1_win.geometry('600x400')
        bb1_l1_win.config(bg = "black")
        
        Label(bb1_l1_win, text = 'We accept Credit and Debit Cards from\nVisa, Mastercard, Sodexo, Diners,\nAmerican Express, Maestro, Rupay &\nDiscover.', font = ("Times New Roman", 20), bg = 'black', fg = 'white').grid(row=0,column=0, columnspan = 2)
        Label(bb1_l1_win, text = 'Name on card:  ', font = ("Times New Roman", 20), bg = 'black', fg = 'white').grid(row=1,column=0)
        ee4 = Entry(bb1_l1_win, width = 15, font = ("Times New Roman", 20))
        ee4.grid(row=1,column=1)
        Label(bb1_l1_win, text = 'Card number:  ', font = ("Times New Roman", 20), bg = 'black', fg = 'white').grid(row=2,column=0)
        ee5 = Entry(bb1_l1_win, width = 13, font = ("Times New Roman", 20))
        ee5.grid(row=2,column=1)
        Label(bb1_l1_win, text = 'Expiry date (MM/YY):  ', font = ("Times New Roman", 20), bg = 'black', fg = 'white').grid(row=3,column=0)
        ee6 = Entry(bb1_l1_win, width = 7, font = ("Times New Roman", 20))
        ee6.grid(row=3,column=1)

        def eee456b_fn():
            global pay_var
            pay_var = 'b1-1'
            bb1_l1_win.destroy()
            place_order_fn()

        Button(bb1_l1_win, text = "Continue >>>", font = ("Times New Roman", 20), command = eee456b_fn).grid(row=4,column=0)
        
    bb1_label_1 = Button(bb1, text = "Add a card    " + u'\u2192', font = ('Avengeance', 18), bg = '#FFE5B4', command = bb1_l1)
    bb1_label_1.grid(row=0,column=0)

    def bb4_l1():

        bb4_l1_win = Tk()
        bb4_l1_win.title("Net Banking")
        bb4_l1_win.iconbitmap("logo.ico")
        bb4_l1_win.geometry('650x550')
        bb4_l1_win.config(bg = "black")

        Label(bb4_l1_win, text = 'Choose bank (or) type:  ', font = ("Times New Roman", 20), bg = 'black', fg = 'white').grid(row=0,column=0)
        global loc_area_e
        loc_area_e = Entry(bb4_l1_win, width = 15, font = ("Times New Roman", 20))
        loc_area_e.grid(row=0,column=1)
        
#
        def update(data):
            blr_listbox.delete(0, END)
    
            for item in data:
                blr_listbox.insert(END, item)

        def fillout(e):
            loc_area_e.delete(0, END)

            loc_area_e.insert(0, blr_listbox.get(ACTIVE))

        def check(e):
            typed = loc_area_e.get()

            if typed == '':
                data = locality_list
            else:
                data = []
                for item in locality_list:
                    if typed.lower() in item.lower():
                        data.append(item)
            
                if len(data) == 0:
                    i_s = ["You can"]
                    i_s_2 = ["Proceed"]
                    data.append(i_s)
                    data.append(i_s_2)
                    data.append(l_s_3)
                
            update(data)


        blr_listbox = Listbox(bb4_l1_win, width = 10, bg = '#038cfc', font = ('Courier New', 20, 'bold'))
        blr_listbox.grid(row=1, column = 0, pady = 10)

        global locality_list
        locality_list = ['HDFC','Kotak','Axis','ICICI','SBI','Canara Bank','UBI']

        update(locality_list)

        blr_listbox.bind("<<ListboxSelect>>", fillout)

        loc_area_e.bind("<KeyRelease>", check)
#
        def eex_fn():
            global pay_var
            pay_var = 'b4-1'
            bb4_l1_win.destroy()
            place_order_fn()

        Label(bb4_l1_win, text = 'Enter registered mobile number:  ', font = ("Times New Roman", 20), bg = 'black', fg = 'white').grid(row=2,column=0)
        Entry(bb4_l1_win, width = 15, font = ("Times New Roman", 20)).grid(row=2,column=1)
        Button(bb4_l1_win, text = "Continue >>>", font = ("Times New Roman", 20), command = eex_fn).grid(row=3,column=0)
        
    bb4_label_1 = Button(bb4, text = "Select bank    " + u'\u2192', font = ('Avengeance', 18), bg = '#FFE5B4', command = bb4_l1)
    bb4_label_1.grid(row=0,column=0)



chk = 0
net_cost = 0
