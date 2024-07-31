from tkinter import *
from tkinter import ttk
import mysql.connector as ms2
import mysql.connector as ms
from menu_window import loading_win_3
from PIL import ImageTk
from PIL import Image

def loading_win_2():

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
            s_new_window_2()
        
    timer_load()

def s_new_window_2():

    global sn_win
    sn_win = Tk()
    sn_win.title("ARA FOODS - SEARCH")
    sn_win.iconbitmap("logo.ico")
    #sn_win.attributes('-fullscreen', True)
    sn_win.state('zoomed')
    sn_win.config(bg = 'gold')

    ####
    #Create a main Frame
    main_frame = Frame(sn_win)
    main_frame.pack(fill = BOTH, expand = True)
    main_frame.config(bg = 'gold')

    #Create a Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill = BOTH, expand = True)
    my_canvas.config(bg = 'gold')

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

    sec_frame.config(bg = 'gold')

    ####
    boss_frame_1 = Frame(sec_frame, bg = 'gold')
    boss_frame_1.pack(pady=30,padx=30)
    ####

    global var2
    var2 = 0

    def toggle2():
    
        global var2
        if var2 % 2 == 0:
            sn_win.geometry('1920x1080')
        else:
            sn_win.state('zoomed')
            #sn_win.attributes('-fullscreen', True)
        var2 = var2 + 1

    def btr():
        sn_win.destroy()

    toggle_btn = Button(boss_frame_1, text = 'Toggle Fullscreen  ON/OFF', font = ('Broadway', 20), bg = 'light blue', cursor = 'hand2', command = toggle2)
    #toggle_btn.grid(row=0,column=2,pady=20,padx=40)

    back_to_root = Button(boss_frame_1, text = '< Back', font = ('Broadway', 20), bg = 'light blue', cursor = 'hand2', command = btr)
    back_to_root.grid(row=0,column=0,pady=20,padx=20)

    mycon = ms2.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')

    mycur = mycon.cursor(buffered = True)



    main_frame_search = Frame(sec_frame, bg = 'gold')
    main_frame_search.pack(pady=50)



    mycur.execute("select name, area, type from restaurants")
    global res6
    res6 = mycur.fetchall()

    val = int(len(res6)/3)

        #try:

    global h1, h2, h3
    
    for h1 in range(val):
                
        ser_la_fr_var4 = 'ser_la_fr4_{}'.format(h1 + 1)
        label_a_var4 = 'label_a4_{}'.format(h1 + 1)
        label_b_var4 = 'label_b4_{}'.format(h1 + 1)
        label_c_var4 = 'label_c4_{}'.format(h1 + 1)

            
        globals()[ser_la_fr_var4] = LabelFrame(main_frame_search, bg = '#3cfa02')
        globals()[ser_la_fr_var4].grid(row=h1,column=0,padx=50,pady=20)

        globals()[label_a_var4] = Label(globals()[ser_la_fr_var4], text = res6[h1][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
        globals()[label_a_var4].grid(row=0,column=0,sticky='w')

        globals()[label_b_var4] = Label(globals()[ser_la_fr_var4], text = res6[h1][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
        globals()[label_b_var4].grid(row=1,column=0,sticky='w')

        globals()[label_c_var4] = Label(globals()[ser_la_fr_var4], text = res6[h1][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
        globals()[label_c_var4].grid(row=2,column=0,sticky='w')

    for h2 in range(val, val * 2):
                
        ser_la_fr_var4 = 'ser_la_fr4_{}'.format(h2 + 1)
        label_a_var4 = 'label_a4_{}'.format(h2 + 1)
        label_b_var4 = 'label_b4_{}'.format(h2 + 1)
        label_c_var4 = 'label_c4_{}'.format(h2 + 1)

            
        globals()[ser_la_fr_var4] = LabelFrame(main_frame_search, bg = '#3cfa02')
        globals()[ser_la_fr_var4].grid(row=h2 - val,column=1,padx=50,pady=20)

        globals()[label_a_var4] = Label(globals()[ser_la_fr_var4], text = res6[h2][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
        globals()[label_a_var4].grid(row=0,column=0,sticky='w')

        globals()[label_b_var4] = Label(globals()[ser_la_fr_var4], text = res6[h2][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
        globals()[label_b_var4].grid(row=1,column=0,sticky='w')

        globals()[label_c_var4] = Label(globals()[ser_la_fr_var4], text = res6[h2][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
        globals()[label_c_var4].grid(row=2,column=0,sticky='w')

    for h3 in range(val * 2, len(res6)):
                
        ser_la_fr_var4 = 'ser_la_fr4_{}'.format(h3 + 1)
        label_a_var4 = 'label_a4_{}'.format(h3 + 1)
        label_b_var4 = 'label_b4_{}'.format(h3 + 1)
        label_c_var4 = 'label_c4_{}'.format(h3 + 1)

            
        globals()[ser_la_fr_var4] = LabelFrame(main_frame_search, bg = '#3cfa02')
        globals()[ser_la_fr_var4].grid(row=h3 - 2 * val,column=2,padx=50,pady=20)

        globals()[label_a_var4] = Label(globals()[ser_la_fr_var4], text = res6[h3][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
        globals()[label_a_var4].grid(row=0,column=0,sticky='w')

        globals()[label_b_var4] = Label(globals()[ser_la_fr_var4], text = res6[h3][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
        globals()[label_b_var4].grid(row=1,column=0,sticky='w')

        globals()[label_c_var4] = Label(globals()[ser_la_fr_var4], text = res6[h3][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
        globals()[label_c_var4].grid(row=2,column=0,sticky='w')


    def function_btn_a4(num):
            #print(res3[num])
        b3 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
        ab3 = b3.cursor(buffered = True)
        ab3.execute("select id from restaurants where name = '{}' and area = '{}'".format(res6[num][0], res6[num][1]))
        ooo3 = ab3.fetchone()
        ab3.execute("select id from rest_result_get order by id desc")
        ww3 = ab3.fetchone()
        ab3.execute("insert into rest_result_get values({}, {})".format(int(ww3[0]) + 1, int(ooo3[0])))
        b3.commit()
        b3.close()
        sn_win.destroy()
        loading_win_3()
        #sn_win.destroy()
            
    for x_i in range(len(res6)):

        ser_la_fr_varz = 'ser_la_fr4_{}'.format(x_i + 1)
    
        btn_x_i = Button(globals()[ser_la_fr_varz], text = 'Continue...', font = ('Iron Blade', 20), bg = 'black', fg = '#3cfa02', cursor = 'hand2', command = lambda num = x_i: function_btn_a4(num))
        btn_x_i.grid(row=3,column=0,pady=5)

    #==#
    mycon.close()
