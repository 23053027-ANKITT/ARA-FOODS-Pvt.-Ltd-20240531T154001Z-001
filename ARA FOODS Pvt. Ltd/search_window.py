from tkinter import *
from tkinter import ttk
import mysql.connector as ms
import mysql.connector as ms2
from menu_window import loading_win_3
from PIL import ImageTk
from PIL import Image


def loading_win_1():

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
            s_new_window()
        
    timer_load()


def s_new_window():

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

    #toggle_btn = Button(boss_frame_1, text = 'Toggle Fullscreen  ON/OFF', font = ('Broadway', 20), bg = 'light blue', cursor = 'hand2', command = toggle2)
    #toggle_btn.grid(row=0,column=2,pady=20,padx=40)

    back_to_root = Button(boss_frame_1, text = '< Back', font = ('Broadway', 20), bg = 'light blue', cursor = 'hand2', command = btr)
    back_to_root.grid(row=0,column=0,pady=20,padx=20)

    mycon2 = ms2.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')

    mycur2 = mycon2.cursor(buffered = True)

    mycur2.execute("select search from search_result_get order by sno desc")

    result = mycur2.fetchone()
    res_str = result[0]

    search_result = Label(boss_frame_1, text = "Search results for " + "\U000027BE  " + res_str, font = ('Bell MT', 20, 'bold'), bg = 'gold', fg = 'brown')
    search_result.grid(row=1,column=1,pady=60)

    mycon2.close()


    tele = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    port = tele.cursor()
    port.execute("select place from place_result_get order by pno desc")
    uuu = port.fetchone()
    uuu_str = uuu[0]

    place_result = Label(boss_frame_1, text = "Search results for area/locality " + "\U000027BE  " + uuu_str, font = ('Bell MT', 20, 'bold'), bg = 'gold', fg = 'brown')
    place_result.grid(row=2,column=1)


    ####

    main_frame_search = Frame(sec_frame, bg = 'gold')
    main_frame_search.pack(pady=50)

    mycon = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
    mycur = mycon.cursor(buffered = True)

    mycur.execute("select search from search_result_get order by sno desc")
    res2 = mycur.fetchone()
    res2_str = res2[0]

    #=========================#
    mycur.execute("select name, area, type from restaurants where type like '%" + res2_str.strip().lower() + "%' and area like '%" + uuu_str.strip().lower() + "%'")
    global res3
    res3 = mycur.fetchall()


    #===#

    if len(res3) != 0:
        
        try:

            global k
    
            for k in range(len(res3)):
                
                ser_la_fr_var = 'ser_la_fr_{}'.format(k + 1)
                label_a_var = 'label_a_{}'.format(k + 1)
                label_b_var = 'label_b_{}'.format(k + 1)
                label_c_var = 'label_c_{}'.format(k + 1)

                globals()[ser_la_fr_var] = LabelFrame(main_frame_search, bg = '#3cfa02')
                globals()[ser_la_fr_var].grid(row=k,column=0,padx=50,pady=20)

                globals()[label_a_var] = Label(globals()[ser_la_fr_var], text = res3[k][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
                globals()[label_a_var].grid(row=0,column=0,sticky='w')

                globals()[label_b_var] = Label(globals()[ser_la_fr_var], text = res3[k][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
                globals()[label_b_var].grid(row=1,column=0,sticky='w')

                globals()[label_c_var] = Label(globals()[ser_la_fr_var], text = res3[k][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
                globals()[label_c_var].grid(row=2,column=0,sticky='w')


            def function_btn_a(num):
            #print(res3[num])
                b3 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                ab3 = b3.cursor(buffered = True)
                ab3.execute("select id from restaurants where name = '{}' and area = '{}'".format(res3[num][0], res3[num][1]))
                ooo3 = ab3.fetchone()
                ab3.execute("select id from rest_result_get order by id desc")
                ww3 = ab3.fetchone()
                ab3.execute("insert into rest_result_get values({}, {})".format(int(ww3[0]) + 1, int(ooo3[0])))
                b3.commit()
                b3.close()
                sn_win.destroy()
                loading_win_3()
                #sn_win.destroy()
            
            for x_i in range(len(res3)):

                ser_la_fr_varx = 'ser_la_fr_{}'.format(x_i + 1)
    
                btn_x_i = Button(globals()[ser_la_fr_varx], text = 'Continue...', font = ('Iron Blade', 20), bg = 'black', fg = '#3cfa02', cursor = 'hand2', command = lambda num = x_i: function_btn_a(num))
                btn_x_i.grid(row=3,column=0,pady=5)

        except:
            pass
        

    
    #=========================#

    mycur.execute("select name, area, type from restaurants where name like '%" + res2_str.strip().lower() + "%' and area like '%" + uuu_str.strip().lower() + "%'")
    global res4
    res4 = mycur.fetchall()

    #

    #try:

    if len(res4) != 0:
        
        try:

            global g
    
            for g in range(len(res4)):
                
                ser_la_fr_var2 = 'ser_la_fr2_{}'.format(g + 1)
                label_a_var2 = 'label_a2_{}'.format(g + 1)
                label_b_var2 = 'label_b2_{}'.format(g + 1)
                label_c_var2 = 'label_c2_{}'.format(g + 1)

                globals()[ser_la_fr_var2] = LabelFrame(main_frame_search, bg = '#3cfa02')
                globals()[ser_la_fr_var2].grid(row=g,column=1,padx=50,pady=20)

                globals()[label_a_var2] = Label(globals()[ser_la_fr_var2], text = res4[g][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
                globals()[label_a_var2].grid(row=0,column=0,sticky='w')

                globals()[label_b_var2] = Label(globals()[ser_la_fr_var2], text = res4[g][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
                globals()[label_b_var2].grid(row=1,column=0,sticky='w')

                globals()[label_c_var2] = Label(globals()[ser_la_fr_var2], text = res4[g][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
                globals()[label_c_var2].grid(row=2,column=0,sticky='w')


            def function_btn_a2(num):
            #print(res3[num])
                b3 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                ab3 = b3.cursor(buffered = True)
                ab3.execute("select id from restaurants where name = '{}' and area = '{}'".format(res4[num][0], res4[num][1]))
                ooo3 = ab3.fetchone()
                ab3.execute("select id from rest_result_get order by id desc")
                ww3 = ab3.fetchone()
                ab3.execute("insert into rest_result_get values({}, {})".format(int(ww3[0]) + 1, int(ooo3[0])))
                b3.commit()
                b3.close()
                sn_win.destroy()
                loading_win_3()
                #sn_win.destroy()
            
            for x_i in range(len(res4)):

                ser_la_fr_vary = 'ser_la_fr2_{}'.format(x_i + 1)
    
                btn_x_i = Button(globals()[ser_la_fr_vary], text = 'Continue...', font = ('Iron Blade', 20), bg = 'black', fg = '#3cfa02', cursor = 'hand2', command = lambda num = x_i: function_btn_a2(num))
                btn_x_i.grid(row=3,column=0,pady=5)

        except:
            pass

    #====================

    #print(len(res3))
    #print(len(res4))

    #remove try-except and check
    if len(res3) == 0 and len(res4) == 0:

        mycur.execute("select name, area, type from restaurants where area like '%" + uuu_str.strip().lower() + "%'")
        global res5
        res5 = mycur.fetchall()

        #try:

        global f
    
        for f in range(len(res5)):
                
            ser_la_fr_var3 = 'ser_la_fr3_{}'.format(f + 1)
            label_a_var3 = 'label_a3_{}'.format(f + 1)
            label_b_var3 = 'label_b3_{}'.format(f + 1)
            label_c_var3 = 'label_c3_{}'.format(f + 1)

            globals()[ser_la_fr_var3] = LabelFrame(main_frame_search, bg = '#3cfa02')
            globals()[ser_la_fr_var3].grid(row=f,column=0,padx=50,pady=20)

            globals()[label_a_var3] = Label(globals()[ser_la_fr_var3], text = res5[f][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
            globals()[label_a_var3].grid(row=0,column=0,sticky='w')

            globals()[label_b_var3] = Label(globals()[ser_la_fr_var3], text = res5[f][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
            globals()[label_b_var3].grid(row=1,column=0,sticky='w')

            globals()[label_c_var3] = Label(globals()[ser_la_fr_var3], text = res5[f][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
            globals()[label_c_var3].grid(row=2,column=0,sticky='w')


        def function_btn_a3(num):
            #print(res3[num])
            b3 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            ab3 = b3.cursor(buffered = True)
            ab3.execute("select id from restaurants where name = '{}' and area = '{}'".format(res5[num][0], res5[num][1]))
            ooo3 = ab3.fetchone()
            ab3.execute("select id from rest_result_get order by id desc")
            ww3 = ab3.fetchone()
            ab3.execute("insert into rest_result_get values({}, {})".format(int(ww3[0]) + 1, int(ooo3[0])))
            b3.commit()
            b3.close()
            sn_win.destroy()
            loading_win_3()
            #sn_win.destroy()
            
        for x_i in range(len(res5)):

            ser_la_fr_varz = 'ser_la_fr3_{}'.format(x_i + 1)
    
            btn_x_i = Button(globals()[ser_la_fr_varz], text = 'Continue...', font = ('Iron Blade', 20), bg = 'black', fg = '#3cfa02', cursor = 'hand2', command = lambda num = x_i: function_btn_a3(num))
            btn_x_i.grid(row=3,column=0,pady=5)

        #except:
            #pass
    
    #====================

    '''global t

    for t in range(len(res4)):
                
        ser_la_fr_b_var = 'ser_la_fr_b_{}'.format(t + 1)
        label_d_var = 'label_d_{}'.format(t + 1)
        label_e_var = 'label_e_{}'.format(t + 1)
        label_f_var = 'label_f_{}'.format(t + 1)

        globals()[ser_la_fr_b_var] = LabelFrame(main_frame_search, bg = '#3cfa02')
        globals()[ser_la_fr_b_var].grid(row=t,column=1, padx = 50)

        globals()[label_d_var] = Label(globals()[ser_la_fr_b_var], text = res4[t][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
        globals()[label_d_var].grid(row=0,column=0,sticky='w')

        globals()[label_e_var] = Label(globals()[ser_la_fr_b_var], text = res4[t][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
        globals()[label_e_var].grid(row=1,column=0,sticky='w')
                
        globals()[label_f_var] = Label(globals()[ser_la_fr_b_var], text = res4[t][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
        globals()[label_f_var].grid(row=2,column=0,sticky='w')

    def function_btn_b(num):
        #print(res4[num])
        b2 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
        ab2 = b2.cursor(buffered = True)
        ab2.execute("select id from restaurants where name = '{}' and area = '{}'".format(res4[num][0], res4[num][1]))
        ooo2 = ab2.fetchone()
        ab2.execute("select id from rest_result_get order by id desc")
        ww2 = ab2.fetchone()
        ab2.execute("insert into rest_result_get values({}, {})".format(int(ww2[0]) + 1, int(ooo2[0])))
        b2.commit()
        b2.close()
        sn_win.destroy()
        menu_window_frame()

    for y_i in range(len(res4)):

        ser_la_fr__b_var = 'ser_la_fr_b_{}'.format(y_i + 1)
            
        btn_y_i = Button(globals()[ser_la_fr_b_var], text = 'Continue...', font = ('Iron Blade', 20), bg = 'black', fg = '#3cfa02', cursor = 'hand2', command = lambda num = y_i: function_btn_b(num))
        btn_y_i.grid(row=3,column=0,pady=5)'''

    #except:
        #pass

    #mycon.close()

    if len(res3) == 0 and len(res4) == 0 and len(res5) == 0:

        '''ser_err = Tk()
        ser_err.title("Search Error")
        ser_err.iconbitmap("logo.ico")
        ser_err.geometry("900x100")
        ser_err.config(bg = "black")

        error_label = Label(ser_err, text = "No related search was found in the area you have typed.\nTry changing the area typed.", bg = 'black', font = ('Courier New', 20, 'bold'), fg = 'red')
        error_label.pack()'''

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

    '''if len(res3) == 0:

        for i in food_category: #searching among keys
            for j in food_category[i]:         #searching through related searches
                if res2_str in j:   #if given search is found

                    con3 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                    cur3 = con3.cursor()
                    cur3.execute("select name, area, type from restaurants where type = '{}'".format(i))
                    global out3
                    out3 = cur3.fetchall()
                    con3.close()

                    #try:

                    global s

                    for s in range(len(out3)):
                                
                        ser_la_fr_c_var = 'ser_la_fr_c_{}'.format(s + 1)
                        label_g_var = 'label_g_{}'.format(s + 1)
                        label_h_var = 'label_h_{}'.format(s + 1)
                        label_i_var = 'label_i_{}'.format(s + 1)

                        globals()[ser_la_fr_c_var] = LabelFrame(main_frame_search, bg = '#3cfa02')
                        globals()[ser_la_fr_c_var].grid(row=s,column=2,padx=50)

                        globals()[label_g_var] = Label(globals()[ser_la_fr_c_var], text = out3[s][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
                        globals()[label_g_var].grid(row=0,column=0,sticky='w')

                        globals()[label_h_var] = Label(globals()[ser_la_fr_c_var], text = out3[s][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
                        globals()[label_h_var].grid(row=1,column=0,sticky='w')
    
                        globals()[label_i_var] = Label(globals()[ser_la_fr_c_var], text = out3[s][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
                        globals()[label_i_var].grid(row=2,column=0,sticky='w')

                    def function_btn_c(num):
                        #print(out3[num])
                        b1 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                        ab1 = b1.cursor(buffered = True)
                        ab1.execute("select id from restaurants where name = '{}' and area = '{}'".format(out3[num][0], out3[num][1]))
                        ooo1 = ab1.fetchone()
                        ab1.execute("select id from rest_result_get order by id desc")
                        ww1 = ab1.fetchone()
                        ab1.execute("insert into rest_result_get values({}, {})".format(int(ww1[0]) + 1, int(ooo1[0])))
                        b1.commit()
                        b1.close()
                        sn_win.destroy()
                        menu_window_frame()

                    for z_i in range(len(out3)):

                        ser_la_fr_c_var = 'ser_la_fr_c_{}'.format(z_i + 1)

                        btn_z_i = Button(globals()[ser_la_fr_c_var], text = 'Continue...', font = ('Iron Blade', 20), bg = 'black', fg = '#3cfa02', cursor = 'hand2', command = lambda num = z_i: function_btn_c(num))
                        btn_z_i.grid(row=3,column=0)

                    #except:
                        #pass


    
    
        
        try:
            
            if len(res3) == 0 and len(res4) == 0 and len(out3) == 0:

                len_error = Tk()
                len_error.title("Empty Search")
                len_error.iconbitmap("logo.ico")
                len_error.geometry("600x100")
                len_error.config(bg = "black")

                try:

                    xyz = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                    abc = xyz.cursor(buffered = True)
                    abc.execute("select name, area, type from restaurants where area like '%" + str(uuu_str) + "'")
                    rex = abc.fetchall()
                    xyz.close()

                    global qvb
                    
                    for qvb in range(len(rex)):

                        ser_la_fr_var = 'ser_la_fr_{}'.format(qvb + 1)
                        label_a_var = 'label_a_{}'.format(qvb + 1)
                        label_b_var = 'label_b_{}'.format(qvb + 1)
                        label_c_var = 'label_c_{}'.format(qvb + 1)

                        globals()[ser_la_fr_var] = LabelFrame(main_frame_search, bg = '#3cfa02')
                        globals()[ser_la_fr_var].grid(row=qvb,column=0,padx=50)

                        globals()[label_a_var] = Label(globals()[ser_la_fr_var], text = rex[qvb][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
                        globals()[label_a_var].grid(row=0,column=0,sticky='w')

                        globals()[label_b_var] = Label(globals()[ser_la_fr_var], text = rex[qvb][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
                        globals()[label_b_var].grid(row=1,column=0,sticky='w')

                        globals()[label_c_var] = Label(globals()[ser_la_fr_var], text = rex[qvb][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
                        globals()[label_c_var].grid(row=2,column=0,sticky='w')

                    def function_btn_q(num):
            
                        b3 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                        ab3 = b3.cursor(buffered = True)
                        ab3.execute("select id from restaurants where name = '{}' and area = '{}'".format(rex[num][0], rex[num][1]))
                        ooo3 = ab3.fetchone()
                        ab3.execute("select id from rest_result_get order by id desc")
                        ww3 = ab3.fetchone()
                        ab3.execute("insert into rest_result_get values({}, {})".format(int(ww3[0]) + 1, int(ooo3[0])))
                        b3.commit()
                        b3.close()
                        sn_win.destroy()
                        menu_window_frame()
            
                    for x_q in range(len(rex)):

                        ser_la_fr_var = 'ser_la_fr_{}'.format(x_q + 1)
    
                        btn_x_i = Button(globals()[ser_la_fr_var], text = 'Continue...', font = ('Iron Blade', 20), bg = 'black', fg = '#3cfa02', cursor = 'hand2', command = lambda num = x_q: function_btn_q(num))
                        btn_x_i.grid(row=3,column=0,pady=5)
                    
                except:
                    
                    error_label = Label(len_error, text = 'No related search results found...\nPls try with other keywords...', bg = 'black', font = ('Times New Roamn', 20, 'bold'), fg = 'red')
                    error_label.pack()

                    sn_win.destroy()
            
        except:

            #
            try:

                    xyz = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                    abc = xyz.cursor(buffered = True)
                    abc.execute("select name, area, type from restaurants where area like '%" + str(uuu_str) + "'")
                    rex = abc.fetchall()
                    xyz.close()

                    #global qvb
                    
                    for qvb in range(len(rex)):

                        ser_la_fr_var = 'ser_la_fr_{}'.format(qvb + 1)
                        label_a_var = 'label_a_{}'.format(qvb + 1)
                        label_b_var = 'label_b_{}'.format(qvb + 1)
                        label_c_var = 'label_c_{}'.format(qvb + 1)

                        globals()[ser_la_fr_var] = LabelFrame(main_frame_search, bg = '#3cfa02')
                        globals()[ser_la_fr_var].grid(row=qvb,column=0,padx=50)

                        globals()[label_a_var] = Label(globals()[ser_la_fr_var], text = rex[qvb][0], font = ('Matura MT Script Capitals', 40), bg = '#3cfa02')
                        globals()[label_a_var].grid(row=0,column=0,sticky='w')

                        globals()[label_b_var] = Label(globals()[ser_la_fr_var], text = rex[qvb][1], font = ('Harrington', 30, 'bold'), bg = '#3cfa02')
                        globals()[label_b_var].grid(row=1,column=0,sticky='w')

                        globals()[label_c_var] = Label(globals()[ser_la_fr_var], text = rex[qvb][2], font = ('Stencil', 20), bg = 'black', fg = 'gold')
                        globals()[label_c_var].grid(row=2,column=0,sticky='w')

                    def function_btn_q(num):
            
                        b3 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                        ab3 = b3.cursor(buffered = True)
                        ab3.execute("select id from restaurants where name = '{}' and area = '{}'".format(rex[num][0], rex[num][1]))
                        ooo3 = ab3.fetchone()
                        ab3.execute("select id from rest_result_get order by id desc")
                        ww3 = ab3.fetchone()
                        ab3.execute("insert into rest_result_get values({}, {})".format(int(ww3[0]) + 1, int(ooo3[0])))
                        b3.commit()
                        b3.close()
                        sn_win.destroy()
                        menu_window_frame()
            
                    for x_q in range(len(rex)):

                        ser_la_fr_var = 'ser_la_fr_{}'.format(x_q + 1)
    
                        btn_x_i = Button(globals()[ser_la_fr_var], text = 'Continue...', font = ('Iron Blade', 20), bg = 'black', fg = '#3cfa02', cursor = 'hand2', command = lambda num = x_q: function_btn_q(num))
                        btn_x_i.grid(row=3,column=0,pady=5)
            #
            except:
                
                len_error = Tk()
                len_error.title("Empty Search")
                len_error.iconbitmap("logo.ico")
                len_error.geometry("600x100")
                len_error.config(bg = "black")

                error_label = Label(len_error, text = 'No related search results found...\nPls try with other keywords...', bg = 'black', font = ('Times New Roamn', 20, 'bold'), fg = 'red')
                error_label.pack()
        
                sn_win.destroy()


    #sn_win.mainloop()'''

def s_destroy():

    sn_win.destroy()

#======================

#s_new_window()


