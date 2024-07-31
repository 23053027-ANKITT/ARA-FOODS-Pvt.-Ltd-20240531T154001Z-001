#= At last, we can try to modify the MENU Tab (by adding [+]) =#

from tkinter import *
from tkinter import ttk
import urllib.request as ur
import mysql.connector as ms

def rrs_new_window():

    rrs_nw = Tk()
    rrs_nw.title("Register your restaurant")
    rrs_nw.iconbitmap("logo.ico")
    rrs_nw.state('zoomed')
    rrs_nw.config(bg = "black")

    
    #Create a main Frame
    main_frame_rrs = Frame(rrs_nw)
    main_frame_rrs.pack(fill = BOTH, expand = True)

    #Create a Canvas
    my_canvas_rrs = Canvas(main_frame_rrs)
    my_canvas_rrs.pack(side = LEFT, fill = BOTH, expand = True)

    #Add a Scrollbar to the canvas
    my_scrollbar_rrs = ttk.Scrollbar(main_frame_rrs, orient = VERTICAL, command = my_canvas_rrs.yview)
    my_scrollbar_rrs.pack(side = RIGHT, fill = Y)

    #Configure the canvas
    my_canvas_rrs.configure(yscrollcommand = my_scrollbar_rrs.set)
    my_canvas_rrs.bind('<Configure>', lambda e: my_canvas_rrs.configure(scrollregion = my_canvas_rrs.bbox('all')))

    #Create another frame inside canvas
    rrs_nwin = Frame(my_canvas_rrs)

    #Add that new frame into the window
    my_canvas_rrs.create_window((0,0), window = rrs_nwin, anchor = 'nw')


    main_frame_rrs.config(bg = 'black')

    my_canvas_rrs.config(bg = 'black')

    rrs_nwin.config(bg = 'black')
    
    #
    global e_unit1, e_unit0, e_unit2, e_unit3, e_unit5, e_unit7, pass_rrs_e
    #
    
    rrs_frame1 = LabelFrame(rrs_nwin, text = 'Restaurant Details', font = ('Broadway', 30), bg = 'black', fg = 'white')
    rrs_frame1.pack(pady = 20)

    unit1 = Label(rrs_frame1, text = 'Restaurant Name: ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'yellow')
    unit1.grid(row=0,column=0, pady = 20, padx = 10)

    e_unit1 = Entry(rrs_frame1, width = 25, font = ('Times New Roman', 20))
    e_unit1.grid(row=0,column=1, padx = 10)

    unit0 = Label(rrs_frame1, text = 'Restaurant Type: ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'yellow')
    unit0.grid(row=3,column=0)
    
    e_unit0 = Entry(rrs_frame1, width = 25, font = ('Times New Roman', 20))
    e_unit0.grid(row=3,column=1,pady=20)

    eg_unit0 = Label(rrs_frame1, text = 'like - sweets, tandoori, pure-veg', font = ('Centaur', 15, 'bold'), bg = 'black', fg = 'white')
    eg_unit0.grid(row=3,column=2)

    unit2 = Label(rrs_frame1, text = 'Location (with Street no. and name): ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'pink')
    unit2.grid(row=1,column=0, pady = 20, padx = 10)

    unit3 = Label(rrs_frame1, text = 'Area/Locality (in Bangalore Urban): ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'pink')
    unit3.grid(row=2,column=0, pady = 20, padx = 10)

    e_unit2 = Entry(rrs_frame1, width = 25, font = ('Times New Roman', 20))
    e_unit2.grid(row=1,column=1, padx = 10)

    e_unit3 = Entry(rrs_frame1, width = 25, font = ('Times New Roman', 20))
    e_unit3.grid(row=2,column=1, padx = 10)

    label4 = Label(rrs_frame1, text = "Don't use quote(s).\nDon't use space(s).", font = ('Centaur', 15), bg = 'black', fg = 'white')
    label4.grid(row=0,column=2)

    #=#
    rrs_frame2 = LabelFrame(rrs_nwin, text = 'Personal Details', font = ('Broadway', 30), bg = 'black', fg = 'white')
    rrs_frame2.pack(pady = 20)

    unit4 = Label(rrs_frame2, text = 'Mobile no. of Owner: ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'yellow')
    unit4.grid(row=1,column=0, pady = 20, padx=10)

    e_unit4 = Entry(rrs_frame2, width = 25, font = ('Times New Roman', 20))
    e_unit4.grid(row=1,column=1, padx=10)

    unit5 = Label(rrs_frame2, text = 'Telephone/Mobile No. at restaurant: ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'pink')
    unit5.grid(row=2,column=0, pady = 20, padx=10)

    e_unit5 = Entry(rrs_frame2, width = 25, font = ('Times New Roman', 20))
    e_unit5.grid(row=2,column=1, padx=10)

    unit6 = Label(rrs_frame2, text = 'Email ID of Owner: ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'yellow')
    unit6.grid(row=3,column=0, pady = 20, padx=10)

    e_unit6 = Entry(rrs_frame2, width = 25, font = ('Times New Roman', 20))
    e_unit6.grid(row=3,column=1, padx=10)

    unit7 = Label(rrs_frame2, text = 'Name of Owner: ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'light green')
    unit7.grid(row=0,column=0,pady=20)

    e_unit7 = Entry(rrs_frame2, width = 25, font = ('Times New Roman', 20))
    e_unit7.grid(row=0,column=1)

    #
    rrs_frame0 = LabelFrame(rrs_nwin, text = 'Account Access', fg = 'white', bg = 'black', font = ('Broadway', 30))
    rrs_frame0.pack()

    pass_rrs_l = Label(rrs_frame0, text = 'Set a password: ', font = ('Centaur', 20, 'bold'), bg = 'black', fg = 'light blue')
    pass_rrs_l.grid(row=0,column=0,pady=20,padx=20)

    pass_rrs_e = Entry(rrs_frame0, width = 25, font = ('Times New Roman', 20), show = '*')
    pass_rrs_e.grid(row=0,column=1,padx=20)
    #
    
    
    #=#

    rrs_frame4 = LabelFrame(rrs_nwin, text = "Timings", bg = 'black', fg = 'white', font = ('Broadway', 30), width = 1000)
    rrs_frame4.pack(pady = 50)

    tup1 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    
    for j in range(len(tup1)):
        Label(rrs_frame4, text = tup1[j], font = ('Times New Roman', 20), bg = 'black', fg = 'yellow').grid(row=j,column=0, pady = 20)


    global day
    day = ['AM', 'PM']
    
    def drop1_fn(event):

        global day

        if drop1.get() == options[0]:

            global combo1

            combo1 = Frame(rrs_frame4, bg = 'black')
            combo1.grid(row=0,column=2)

            e1a = Entry(combo1, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e1a.grid(row=0,column=0,padx=20)

            com1a = ttk.Combobox(combo1, value = day, font = ('Times New Roman', 15))
            com1a.current(0)
            com1a.grid(row=0,column=1,padx=20)
            
            Label(combo1, text = 'to', font = ('Times New Roman', 15), bg = 'black', fg = 'white').grid(row=0,column=2,padx=30)

            e1b = Entry(combo1, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e1b.grid(row=0,column=3,padx=20)

            com1b = ttk.Combobox(combo1, value = day, font = ('Times New Roman', 15))
            com1b.current(1)
            com1b.grid(row=0,column=4,padx=20)

        else:

            combo1.destroy()
    
    def drop2_fn(event):

        global day

        if drop2.get() == options[0]:

            global combo2

            combo2 = Frame(rrs_frame4, bg = 'black')
            combo2.grid(row=1,column=2)

            e2a = Entry(combo2, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e2a.grid(row=0,column=0,padx=20)

            com2a = ttk.Combobox(combo2, value = day, font = ('Times New Roman', 15))
            com2a.current(0)
            com2a.grid(row=0,column=1,padx=20)
            
            Label(combo2, text = 'to', font = ('Times New Roman', 15), bg = 'black', fg = 'white').grid(row=0,column=2,padx=30)

            e2b = Entry(combo2, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e2b.grid(row=0,column=3,padx=20)

            com2b = ttk.Combobox(combo2, value = day, font = ('Times New Roman', 15))
            com2b.current(1)
            com2b.grid(row=0,column=4,padx=20)

        else:

            combo2.destroy()
    
    def drop3_fn(event):

        global day

        if drop3.get() == options[0]:

            global combo3

            combo3 = Frame(rrs_frame4, bg = 'black')
            combo3.grid(row=2,column=2)

            e3a = Entry(combo3, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e3a.grid(row=0,column=0,padx=20)

            com3a = ttk.Combobox(combo3, value = day, font = ('Times New Roman', 15))
            com3a.current(0)
            com3a.grid(row=0,column=1,padx=20)
            
            Label(combo3, text = 'to', font = ('Times New Roman', 15), bg = 'black', fg = 'white').grid(row=0,column=2,padx=30)

            e3b = Entry(combo3, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e3b.grid(row=0,column=3,padx=20)

            com3b = ttk.Combobox(combo3, value = day, font = ('Times New Roman', 15))
            com3b.current(1)
            com3b.grid(row=0,column=4,padx=20)

        else:

            combo3.destroy()
    
    def drop4_fn(event):

        global day

        if drop4.get() == options[0]:

            global combo4

            combo4 = Frame(rrs_frame4, bg = 'black')
            combo4.grid(row=3,column=2)

            e4a = Entry(combo4, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e4a.grid(row=0,column=0,padx=20)

            com4a = ttk.Combobox(combo4, value = day, font = ('Times New Roman', 15))
            com4a.current(0)
            com4a.grid(row=0,column=1,padx=20)
            
            Label(combo4, text = 'to', font = ('Times New Roman', 15), bg = 'black', fg = 'white').grid(row=0,column=2,padx=30)

            e4b = Entry(combo4, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e4b.grid(row=0,column=3,padx=20)

            com4b = ttk.Combobox(combo4, value = day, font = ('Times New Roman', 15))
            com4b.current(1)
            com4b.grid(row=0,column=4,padx=20)

        else:

            combo4.destroy()
    
    def drop5_fn(event):

        global day

        if drop5.get() == options[0]:

            global combo5

            combo5 = Frame(rrs_frame4, bg = 'black')
            combo5.grid(row=4,column=2)

            e5a = Entry(combo5, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e5a.grid(row=0,column=0,padx=20)

            com5a = ttk.Combobox(combo5, value = day, font = ('Times New Roman', 15))
            com5a.current(0)
            com5a.grid(row=0,column=1,padx=20)
            
            Label(combo5, text = 'to', font = ('Times New Roman', 15), bg = 'black', fg = 'white').grid(row=0,column=2,padx=30)

            e5b = Entry(combo5, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e5b.grid(row=0,column=3,padx=20)

            com5b = ttk.Combobox(combo5, value = day, font = ('Times New Roman', 15))
            com5b.current(1)
            com5b.grid(row=0,column=4,padx=20)

        else:

            combo5.destroy()
    
    def drop6_fn(event):

        global day

        if drop6.get() == options[0]:

            global combo6

            combo6 = Frame(rrs_frame4, bg = 'black')
            combo6.grid(row=5,column=2)

            e6a = Entry(combo6, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e6a.grid(row=0,column=0,padx=20)

            com6a = ttk.Combobox(combo6, value = day, font = ('Times New Roman', 15))
            com6a.current(0)
            com6a.grid(row=0,column=1,padx=20)
            
            Label(combo6, text = 'to', font = ('Times New Roman', 15), bg = 'black', fg = 'white').grid(row=0,column=2,padx=30)

            e6b = Entry(combo6, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e6b.grid(row=0,column=3,padx=20)

            com6b = ttk.Combobox(combo6, value = day, font = ('Times New Roman', 15))
            com6b.current(1)
            com6b.grid(row=0,column=4,padx=20)

        else:

            combo6.destroy()
    
    def drop7_fn(event):

        global day

        if drop7.get() == options[0]:

            global combo7

            combo7 = Frame(rrs_frame4, bg = 'black')
            combo7.grid(row=6,column=2)

            e7a = Entry(combo7, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e7a.grid(row=0,column=0,padx=20)

            com7a = ttk.Combobox(combo7, value = day, font = ('Times New Roman', 15))
            com7a.current(0)
            com7a.grid(row=0,column=1,padx=20)
            
            Label(combo7, text = 'to', font = ('Times New Roman', 15), bg = 'black', fg = 'white').grid(row=0,column=2,padx=30)

            e7b = Entry(combo7, width = 3, font = ('Times New Roman', 15), bg = 'pink')
            e7b.grid(row=0,column=3,padx=20)

            com7b = ttk.Combobox(combo7, value = day, font = ('Times New Roman', 15))
            com7b.current(1)
            com7b.grid(row=0,column=4,padx=20)

        else:

            combo7.destroy()
            
    
        
    options = ['Opened', 'Closed']

    #click1 = StringVar()
    #click1.set("Choose: ")

    drop1 = ttk.Combobox(rrs_frame4, value = options, font = ('Times New Roman', 15))
    drop1.current(1)
    drop1.bind("<<ComboboxSelected>>", drop1_fn)
    drop1.grid(row=0,column=1, padx = 20)

    #click2 = StringVar()
    #click2.set("Choose: ")

    drop2 = ttk.Combobox(rrs_frame4, value = options, font = ('Times New Roman', 15))
    drop2.current(1)
    drop2.bind("<<ComboboxSelected>>", drop2_fn)
    drop2.grid(row=1,column=1, padx = 20)

    #click3 = StringVar()
    #click3.set("Choose: ")

    drop3 = ttk.Combobox(rrs_frame4, value = options, font = ('Times New Roman', 15))
    drop3.current(1)
    drop3.bind("<<ComboboxSelected>>", drop3_fn)
    drop3.grid(row=2,column=1, padx = 20)

    #click4 = StringVar()
    #click4.set("Choose: ")

    drop4 = ttk.Combobox(rrs_frame4, value = options, font = ('Times New Roman', 15))
    drop4.current(1)
    drop4.bind("<<ComboboxSelected>>", drop4_fn)
    drop4.grid(row=3,column=1, padx = 20)

    #click5 = StringVar()
    #click5.set("Choose: ")

    drop5 = ttk.Combobox(rrs_frame4, value = options, font = ('Times New Roman', 15))
    drop5.current(1)
    drop5.bind("<<ComboboxSelected>>", drop5_fn)
    drop5.grid(row=4,column=1, padx = 20)

    #click6 = StringVar()
    #click6.set("Choose: ")

    drop6 = ttk.Combobox(rrs_frame4, value = options, font = ('Times New Roman', 15))
    drop6.current(1)
    drop6.bind("<<ComboboxSelected>>", drop6_fn)
    drop6.grid(row=5,column=1, padx = 20)

    #click7 = StringVar()
    #click7.set("Choose: ")

    drop7 = ttk.Combobox(rrs_frame4, value = options, font = ('Times New Roman', 15))
    drop7.current(1)
    drop7.bind("<<ComboboxSelected>>", drop7_fn)
    drop7.grid(row=6,column=1, padx = 20)


 
    #=#

    def insert_new_row():
        
        global sss
        sss = ent.get()
        
        for i in range(1, int(sss) + 1):

            Label(rrs_frame3, text = i, font = ('Times New Roman', 20), bg = 'black', fg = 'white').grid(row = i, column = 0)

        qframe.destroy()


        for xi in range(1, int(sss) + 1):

            menu_var1 = 'menu_name{}'.format(xi)
            menu_var2 = 'menu_vnv{}'.format(xi)
            menu_var3 = 'menu_price{}'.format(xi)

            globals()[menu_var1] = Entry(rrs_frame3, width = 25, font = ('Times New Roman', 20))
            globals()[menu_var1].grid(row = xi, column=1,pady=10)
            
            globals()[menu_var2] = Entry(rrs_frame3, width = 5, font = ('Times New Roman', 20))
            globals()[menu_var2].grid(row = xi, column=3, padx=20,pady=10)
            
            globals()[menu_var3] = Entry(rrs_frame3, width = 10, font = ('Times New Roman', 20))
            globals()[menu_var3].grid(row = xi, column=4, padx=20,pady=10)
        

        
    rrs_frame3 = LabelFrame(rrs_nwin, text = 'Menu', font = ('Broadway', 30), bg = 'black', fg = 'white')
    rrs_frame3.pack(pady = 20, padx = 50)

    name1 = Label(rrs_frame3, text = 'S.NO.', font = ('Centaur', 15, 'bold'), bg = 'black', fg = 'light blue')
    name1.grid(row=0,column=0, padx = 50)

    name2 = Label(rrs_frame3, text = 'ITEM NAME', font = ('Centaur', 15, 'bold'), bg = 'black', fg = 'light blue')
    name2.grid(row=0,column=1, padx = 50)

    name3 = Label(rrs_frame3, text = 'VEG or NON-VEG\nveg: (v) | non-veg: (nv)', font = ('Centaur', 15, 'bold'), bg = 'black', fg = 'light blue')
    name3.grid(row=0,column=3,padx = 20)

    name4 = Label(rrs_frame3, text = 'PRICE', font = ('Centaur', 15, 'bold'), bg = 'black', fg = 'light blue')
    name4.grid(row=0,column=4)
    

    qframe = Frame(rrs_nwin, bg = 'black')
    qframe.pack(pady=20,padx=50)

    ask = Label(qframe, text = 'How many records to insert? ', font = ('Times New Roman', 20), bg = 'black', fg = 'gold')
    ask.grid(row=0,column=0,padx=10)

    ent = Entry(qframe, width = 5, font = ('Times New Roman', 20))
    ent.grid(row=0,column=1,padx=10)

    insert = Button(qframe, text = 'Insert', font = ('Times New Roman', 20), bg = 'gold', command = insert_new_row)
    insert.grid(row=0,column=2,padx=15)
    


    def rrs_register():

        def connect_net_rrs(host='http://google.com'):

            global con_var
            con_var = 0
    
            try:
                ur.urlopen(host) 
                con_var = 0
    
            except:
        
                con_var = 0

        connect_net_rrs()

        global con_var

        rrs_pass = 0

        if con_var == 0:

            if (len(e_unit1.get()) > 0) and (len(e_unit2.get()) > 0) and (len(e_unit3.get()) > 0):
                if (len(e_unit4.get()) > 0) and (len(e_unit5.get()) > 0) and (len(e_unit6.get()) > 0):
                    rrs_pass = 1
            else:
                rrs_pass = 0
                
        else:

            rrs_error = Tk()
            rrs_error.title("Error")
            rrs_error.iconbitmap("logo.ico")
            rrs_error.geometry('600x100')
            rrs_error.config(bg = "black")

            error_label = Label(rrs_error, text = 'There was an error in registering your restaurant.\nPls check internet connection', bg = 'black', font = ('Times New Roamn', 20, 'bold'), fg = 'red')
            error_label.pack()


        if rrs_pass == 1:

            mycon2 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            mycur2 = mycon2.cursor(buffered = True)

            mycur2.execute("select id from restaurants order by id desc")
            data_x = mycur2.fetchone()
            print(data_x[0])

            #try:
                
            mycur2.execute("insert into restaurants values({}, '{}', {}, '{}', '{}', '{}', '{}', '{}')".format(int(data_x[0] + 1)), e_unit7.get(), int(e_unit5.get()), e_unit0.get(), e_unit2.get(), e_unit3.get(), e_unit1.get(), pass_rrs_e.get())
            mycon2.commit()

                #try:
                
            mycur.execute("create table {}(id int primary key, items varchar(300), vnv varchar(3), price decimal(12,2))".format(e_unit1.get()))            

            '''except:

                    mycon.close()

                    table_error = Tk()
                    table_error.title("Restaurant already taken")
                    table_error.iconbitmap("C:/Users/lenovo/Desktop/ARA FOODS Pvt. Ltd/logo.ico")
                    table_error.geometry("600x100")
                    table_error.config(bg = "black")

                    error_label = Label(table_error, text = 'Restaurant already taken.\nPls try another name.', bg = 'black', font = ('Times New Roamn', 20, 'bold'), fg = 'red')
                    error_label.pack()'''

            '''except:

                table__error = Tk()
                table__error.title("Restaurant already taken")
                table__error.iconbitmap("C:/Users/lenovo/Desktop/ARA FOODS Pvt. Ltd/logo.ico")
                table__error.geometry("600x100")
                table__error.config(bg = "black")

                error__label = Label(table__error, text = 'Restaurant already taken.\nPls try another name.', bg = 'black', font = ('Times New Roamn', 20, 'bold'), fg = 'red')
                error__label.pack()'''

            mycon2.close()

            mycon = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            mycur = mycon.cursor(buffered = True)

            
                
            try:

                for ix in range(1, int(sss) + 1):

                    menu_var1 = 'menu_name{}'.format(ix)
                    menu_var2 = 'menu_vnv{}'.format(ix)
                    menu_var3 = 'menu_price{}'.format(ix)

                    mycur.execute("insert into {} values({},'{}','{}',{})".format(e_unit1.get(), ix, globals()[menu_var1].get(), globals()[menu_var2].get(), float(globals()[menu_var3].get())))
                    mycon.commit()


                mycon.close()

                s__t = Tk()
                s__t.title("Restaurant successfully registered")
                s__t.iconbitmap("logo.ico")
                s__t.geometry("1000x100")
                s__t.config(bg = "#38F800")

                success_label = Label(s__t, text = 'Your restaurant has been successfully registered with ARA FOODS Pvt. Ltd.\n...Thank You for choosing ARA FOODS...', bg = '#38F800', font = ('Colonna MT', 20, 'bold'), fg = 'black')
                success_label.pack()

            except:
                mycon.close()
            
            
        else:
            pass
        

    reg = Button(rrs_nwin, text = "Register", font = ('Iron Blade', 30), bg = 'light green', cursor = 'hand2', command = rrs_register)
    reg.pack(pady = 30)

    
