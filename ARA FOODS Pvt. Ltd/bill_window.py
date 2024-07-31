from tkinter import *
from tkinter import ttk
import mysql.connector as ms
import pickle as p
from PIL import ImageTk, Image
from datetime import datetime
from datetime import date
import random as r

#from dor_1 import dormammu_1
#from dor_2 import dormammu_2

def loading_win_5():

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
            bill_win_fn()
        
    timer_load()

def bill_win_fn():

    bill_win = Tk()
    bill_win.state('zoomed')
    bill_win.title("ARA FOODS - ORDER")
    bill_win.iconbitmap("logo.ico")
    #ord_win.attributes('-fullscreen', True)
    bill_win.config(bg = '#fc0398')

    main_frame = Frame(bill_win)
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


    f1 = LabelFrame(second_frame, bg = '#fc0398')
    f1.pack(padx=60)#place(x = 20, y = 20)

    f2 = LabelFrame(second_frame, bg = '#fc0398')
    f2.pack(pady=20)#place(x = 20, y = 200)

    f3 = LabelFrame(second_frame, bg = '#fc0398')
    f3.pack()#place(x = 20, y = 320)

    LL1 = Label(f1, text = "!  Yippee  !\nYour order has been placed successfully", font = ("Dollan Personal Use", 40), bg = '#fc0398', fg = 'yellow')
    LL1.pack()
    LL2 = Label(f2, text = "Thank You for using ARA FOODS", font = ("Jokerman", 30), bg = '#fc0398', fg = 'cyan')
    LL2.pack()

    bilx2 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    bily2 = bilx2.cursor(buffered = True)
    bily2.execute("select name, ph_no, address from order_bill order by id desc")
    global ronaldo
    ronaldo = bily2.fetchone()

    LL3 = Label(f3, text = "Customer name    :  " + ronaldo[0], font = ("High Tower Text", 20), bg = '#fc0398')
    LL3.pack()
    #Label(f3, text = "Customer ph_no   :  " + "XXXXXX" + str(ronaldo[1][6:]), font = ("High Tower Text", 20), bg = '#fc0398').pack()
    LL4 = Label(f3, text = "Customer address :  " + ronaldo[2], font = ("High Tower Text", 20), bg = '#fc0398')
    LL4.pack()

    fx = open("CART_DICTIONARIES.txt", 'rb')
    try:
        while True:
            data = p.load(fx)
    except EOFError:
        pass
    fx.close()

    ####
    f_bill = LabelFrame(second_frame, bg = 'white')
    f_bill.pack(pady=20)#place(x = 500, y = 200)

    L = Frame(f_bill, bg = "white")
    L.pack()
    Label(L, text = "ARA FOODS PVT. LTD.", font = ('Old English Text MT', 20), bg = 'white', fg = 'black').pack()
    Label(L, text = "---- Tax Invoice ----", font = ('Times New Roman', 18), bg = 'white', fg = 'black').pack()

    L2 = Frame(f_bill, bg = 'white')
    L2.pack()
    Label(L2, text = "Date: " + str(date.today().strftime("%d/%m/%y")), font = ('Times New Roman', 12), bg = 'white', fg = 'black').grid(row=0,column=0)
    Label(L2, text = "Bill No. : " + str(r.randint(100, 999)), font = ('Times New Roman', 12), bg = 'white', fg = 'black').grid(row=0,column=1,padx=5)

    Label(f_bill, text = "------------------------", font = ('Times New Roman', 12), bg = 'white', fg = 'black').pack()

    L3 = Frame(f_bill, bg = 'white')
    L3.pack()
    Label(L3, text = "Particulars",  font = ('Times New Roman', 15), bg = 'white', fg = 'black').grid(row=0,column=0,padx=50)
    Label(L3, text = "Qty",  font = ('Times New Roman', 15), bg = 'white', fg = 'black').grid(row=0,column=1)
    Label(L3, text = "Rate",  font = ('Times New Roman', 15), bg = 'white', fg = 'black').grid(row=0,column=2)
    Label(L3, text = "Amount",  font = ('Times New Roman', 15), bg = 'white', fg = 'black').grid(row=0,column=3)

    Label(f_bill, text = "------------------------", font = ('Times New Roman', 12), bg = 'white', fg = 'black').pack()

    total = 0

    u = 4
    for s in data:
        L_var = "L{}".format(u)
        globals()[L_var] = Frame(f_bill, bg = 'white')
        globals()[L_var].pack(pady=5)
        Label(globals()[L_var], text = str(s['Item']), font = ('Times New Roman', 12), bg = 'white', fg = 'black').grid(row=0,column=0,padx=10)
        Label(globals()[L_var], text = str(s['Qty']), font = ('Times New Roman', 12), bg = 'white', fg = 'black').grid(row=0,column=1,padx=5)
        Label(globals()[L_var], text = str(s['Price']), font = ('Times New Roman', 12), bg = 'white', fg = 'black').grid(row=0,column=2)
        Label(globals()[L_var], text = str(int(s['Qty'])*float(s['Price'])), font = ('Times New Roman', 12), bg = 'white', fg = 'black').grid(row=0,column=3,padx=5)
        total += float(s['Price'])*int(s['Qty'])
        u += 1

    Label(f_bill, text = "------------------------", font = ('Times New Roman', 12), bg = 'white', fg = 'black').pack()

    Label(f_bill, text = "Sub Total              :  " + str(total), font = ('Times New Roman', 15), bg = 'white', fg = 'black').pack()
    Label(f_bill, text = "GST (5%)               :  " + str(total * 0.05), font = ('Times New Roman', 15), bg = 'white', fg = 'black').pack()
    Label(f_bill, text = "Delivery Charges (25%) :  " + str(total * 0.25), font = ('Times New Roman', 15), bg = 'white', fg = 'black').pack()

    Label(f_bill, text = "------------------------", font = ('Times New Roman', 12), bg = 'white', fg = 'black').pack()

    Label(f_bill, text = "TOTAL :  " + str(total * 1.3), font = ('Times New Roman', 18, 'bold'), bg = 'white', fg = 'black').pack()

    Label(f_bill, text = "------------------------", font = ('Times New Roman', 12), bg = 'white', fg = 'black').pack()

    F1 = Frame(f_bill, bg = 'white')
    F1.pack()

    Label(F1, text = "FSSAI No. - " + str(r.randint(100000000000000000, 120000000000000000)), font = ('Times New Roman', 12), bg = 'white', fg = 'black').grid(row=0,column=0)
    Label(F1, text = "(" + str(datetime.now().strftime("%I:%M")) + " PM)", font = ('Times New Roman', 12), bg = 'white', fg = 'black').grid(row=0,column=1)

    Label(f_bill, text = "THANK YOU", font = ('Times New Roman', 20, 'bold'), bg = 'white', fg = 'black').pack()

    def RtHS():

        bill_win.destroy()

        #destruction
        #dormammu_1()
        #dormammu_2()
        #==========#

        global feedback
        feedback = Tk()
        feedback.title("ARA FOODS")
        feedback.iconbitmap("logo.ico")
        feedback.geometry("1075x330")
        feedback.config(bg = "cyan")

        Label(feedback, text = "How much would you like to rate us?", font = ('Ink Free', 30, 'bold'), bg = 'cyan', fg = 'black').grid(row=0,column=0,pady=25,columnspan=11)

        def rate(num):

            for ss in range(11):
                
                SB2_var = "SB_{}".format(ss)
                globals()[SB2_var].config(image = new_bg_2)

            for sss in range(num + 1):
                
                globals()["SB_{}".format(sss)].config(image = new_bg_1)

        #================
        global bg_1, bg_1_res, new_bg_1
        bg_1 = Image.open("Star_ON.png")
        bg_1_res = bg_1.resize((70, 70), Image.Resampling.LANCZOS)
        new_bg_1 = ImageTk.PhotoImage(bg_1_res, master = feedback)

        global bg_2, bg_2_res, new_bg_2
        bg_2 = Image.open("Star_OFF.png")
        bg_2_res = bg_2.resize((70, 70), Image.Resampling.LANCZOS)
        new_bg_2 = ImageTk.PhotoImage(bg_2_res, master = feedback)
        
        #================

        w = 0.0        
        for s in range(11):

            SB_var = "SB_{}".format(s)
            globals()[SB_var] = Button(feedback, image = new_bg_2, command = lambda num = s: rate(num))
            globals()[SB_var].grid(row=1,column=s,padx=10)

            Label(feedback, text = str(w), font = ('Avengeance', 15), bg = 'cyan').grid(row=2,column=s,padx=10)
            w = w + 0.5


        def rate_thnx():

            global thnx
            thnx = Tk()
            thnx.geometry("440x40")

            global t, tL
            t = 3
            tL = Label(thnx, text = "THANK YOU FOR RATING US !!!", font = ('Felix Titling', 20, 'bold'))
            tL.pack()

            def timer():
                global t
                t = t - 1
                tL.after(1000, timer)
                if t == -1:
                    thnx.destroy()
                    feedback.destroy()
                
            timer()

        Button(feedback, text = "RATE !", font = ('Felix Titling', 20), bg = 'black', fg = 'gold', command = rate_thnx).grid(row=3,column=5,pady=50)

    Button(second_frame, text = "Return to Home Screen", font = ('Iron Blade', 25), bg = 'black', fg = 'white', command = RtHS).pack(pady=20)

