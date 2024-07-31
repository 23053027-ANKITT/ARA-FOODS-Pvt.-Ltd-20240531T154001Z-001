from tkinter import *
from tkinter import ttk
import mysql.connector as ms

def rrl_new_window():

    rrl_win = Tk()
    rrl_win.title("Restaurant Login")
    rrl_win.iconbitmap("logo.ico")
    rrl_win.geometry('800x400')
    rrl_win.config(bg = "silver")

    root = LabelFrame(rrl_win, text = "Restaurant Login", font = ('Broadway', 30), bg = 'silver')
    root.pack(pady=20)

    global r_name_e, r_pass_e, r_area_e
    r_name = Label(root, text = "Name of Restaurant: ", font = ('Dubai', 20), bg = 'silver')
    r_name.grid(row=0,column=0,pady=20)

    r_name_e = Entry(root, width = 25, font = ('Times New Roman', 20))
    r_name_e.grid(row=0,column=1)

    r_pass = Label(root, text = "Password: ", font = ('Dubai', 20), bg = 'silver')
    r_pass.grid(row=2,column=0)

    r_pass_e = Entry(root, width = 25, font = ('Times New Roman', 20), show = '*')
    r_pass_e.grid(row=2,column=1)

    r_area = Label(root, text = "Area/Locality: ", font = ('Dubai', 20), bg = 'silver')
    r_area.grid(row=1,column=0)

    r_area_e = Entry(root, width = 25, font = ('Times New Roman', 20))
    r_area_e.grid(row=1,column=1)

    def r_fn():
        
        con1 = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
        cur1 = con1.cursor()

        cur1.execute("select name, area, passwd from restaurants") 
        data1 = cur1.fetchall()

        con1.close()

        t = 0
        for i in data1:
            if (r_name_e.get().lower() == i[0]) and (r_area_e.get().lower() == i[1]) and (r_pass_e.get() == i[2]):
                t = 1
                yyhs = i[2]

        if t == 1:

            #=====================================================================================================#

            root.destroy()

            rrl_win.geometry("500x400")

            def b1_fn():

                rrl_win.geometry("500x400")
                
                for widgets in frame.winfo_children():
                    widgets.destroy()
                    
                frame_1 = Frame(frame, bg = 'silver')
                frame_1.pack(side = LEFT,pady=20)

                def b1_a_fn():

                    ba = ms.connect(host='localhost', user='root', passwd='dpsbn', database='arafoodsdb')
                    bac = ba.cursor()
                    bac.execute("update restaurants set name = '{}' where name = '{}'".format(e1.get().lower(), mjolnir[0][0]))
                    ba.commit()
                    ba.close()
                    
                def b1_b_fn():

                    bb = ms.connect(host='localhost', user='root', passwd='dpsbn', database='arafoodsdb')
                    bbc = bb.cursor()
                    bbc.execute("update restaurants set owner = '{}' where owner = '{}'".format(e2.get().lower(), mjolnir[0][1]))
                    bb.commit()
                    bb.close()
                    
                def b1_c_fn():

                    bc = ms.connect(host='localhost', user='root', passwd='dpsbn', database='arafoodsdb')
                    bcc = bc.cursor()
                    bcc.execute("update restaurants set type = '{}' where type = '{}'".format(e3.get().lower(), mjolnir[0][2]))
                    bc.commit()
                    bc.close()
                    
                def b1_d_fn():

                    bd = ms.connect(host='localhost', user='root', passwd='dpsbn', database='arafoodsdb')
                    bdc = bd.cursor()
                    bdc.execute("update restaurants set ph_no = '{}' where ph_no = '{}'".format(e4.get().lower(), mjolnir[0][3]))
                    bd.commit()
                    bd.close()
                    
                def b1_e_fn():

                    be = ms.connect(host='localhost', user='root', passwd='dpsbn', database='arafoodsdb')
                    bec = be.cursor()
                    bec.execute("update restaurants set location = '{}' where location = '{}'".format(e5.get().lower(), mjolnir[0][4]))
                    be.commit()
                    be.close()
                    
                def b1_f_fn():
                    bf = ms.connect(host='localhost', user='root', passwd='dpsbn', database='arafoodsdb')
                    bfc = bf.cursor()
                    bfc.execute("update restaurants set area = '{}' where area = '{}'".format(e6.get().lower(), mjolnir[0][5]))
                    bf.commit()
                    bf.close()
                    
                def b1_g_fn():

                    bg = ms.connect(host='localhost', user='root', passwd='dpsbn', database='arafoodsdb')
                    bgc = bg.cursor()
                    bgc.execute("update restaurants set passwd = '{}' where passwd = '{}'".format(e7.get().lower(), mjolnir[0][6]))
                    bg.commit()
                    bg.close()
                    

                def b1_1_fn():
                    global e1
                    for widgets in framex.winfo_children():
                        widgets.destroy()
                    e1 = Entry(framex, width = 20, bg = 'yellow', fg = 'black', font = ('Times New Roman', 10))
                    e1.insert(0, mjolnir[0][0])
                    e1.pack(pady=20)
                    b1_a = Button(framex, text = 'Update', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_a_fn)
                    b1_a.pack()
                def b1_2_fn():
                    global e2
                    for widgets in framex.winfo_children():
                        widgets.destroy()
                    e2 = Entry(framex, width = 20, bg = 'yellow', fg = 'black', font = ('Times New Roman', 10))
                    e2.insert(0, mjolnir[0][1])
                    e2.pack(pady=20)
                    b1_b = Button(framex, text = 'Update', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_b_fn)
                    b1_b.pack()
                def b1_3_fn():
                    global e3
                    for widgets in framex.winfo_children():
                        widgets.destroy()
                    e3 = Entry(framex, width = 20, bg = 'yellow', fg = 'black', font = ('Times New Roman', 10))
                    e3.insert(0, mjolnir[0][2])
                    e3.pack(pady=20)
                    b1_c = Button(framex, text = 'Update', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_c_fn)
                    b1_c.pack()
                def b1_4_fn():
                    global e4
                    for widgets in framex.winfo_children():
                        widgets.destroy()
                    e4 = Entry(framex, width = 20, bg = 'yellow', fg = 'black', font = ('Times New Roman', 10))
                    e4.insert(0, mjolnir[0][3])
                    e4.pack(pady=20)
                    b1_d = Button(framex, text = 'Update', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_d_fn)
                    b1_d.pack()
                def b1_5_fn():
                    global e5
                    for widgets in framex.winfo_children():
                        widgets.destroy()
                    e5 = Entry(framex, width = 20, bg = 'yellow', fg = 'black', font = ('Times New Roman', 10))
                    e5.insert(0, mjolnir[0][4])
                    e5.pack(pady=20)
                    b1_e = Button(framex, text = 'Update', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_e_fn)
                    b1_e.pack()
                def b1_6_fn():
                    global e6
                    for widgets in framex.winfo_children():
                        widgets.destroy()
                    e6 = Entry(framex, width = 20, bg = 'yellow', fg = 'black', font = ('Times New Roman', 10))
                    e6.insert(0, mjolnir[0][5])
                    e6.pack(pady=20)
                    b1_f = Button(framex, text = 'Update', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_f_fn)
                    b1_f.pack()
                def b1_7_fn():
                    global e7
                    for widgets in framex.winfo_children():
                        widgets.destroy()
                    e7 = Entry(framex, width = 20, bg = 'yellow', fg = 'black', font = ('Times New Roman', 10))
                    e7.insert(0, mjolnir[0][6])
                    e7.pack(pady=20)
                    b1_g = Button(framex, text = 'Update', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_g_fn)
                    b1_g.pack()
                

                b1_1 = Button(frame_1, text = 'Restaurant Name  ', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_1_fn)
                b1_1.grid(row=0,column=0)

                b1_2 = Button(frame_1, text = 'Owner Name     ', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_2_fn)
                b1_2.grid(row=0,column=1)

                b1_3 = Button(frame_1, text = 'Restaurant Type', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_3_fn)
                b1_3.grid(row=1,column=1)

                b1_4 = Button(frame_1, text = 'Restaurant Ph.No.', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_4_fn)
                b1_4.grid(row=1,column=0)

                b1_5 = Button(frame_1, text = 'Detailed Location', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_5_fn)
                b1_5.grid(row=2,column=0)

                b1_6 = Button(frame_1, text = 'Area/Locality  ', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_6_fn)
                b1_6.grid(row=2,column=1)

                b1_7 = Button(frame_1, text = 'Password', font = ('Courier New', 10), bg = 'black', fg = 'white', command = b1_7_fn)
                b1_7.grid(row=3,column=0,columnspan=2)

                framex = Frame(frame, bg = 'silver')
                framex.pack(padx=30,pady=10)

            def b2_fn():

                rrl_win.geometry("800x400")

                for widgets in frame.winfo_children():
                    widgets.destroy()   
                    
                frame_2 = Frame(frame, bg = 'silver')
                frame_2.pack()

                label_1 = Label(frame_2, text = "Do you really want to Withdraw Consent and leave ARA Foods Pvt. Ltd. ??", bg = 'silver', fg = 'black', font = ('Matura MT Script Capitals', 15))
                label_1.pack(pady=20)

                def btn_1_fn():

                    #bi = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                    #st = bi.cursor(buffered = True)

                    #st.execute("delete from restaurants where name ")
                    
                    rrl_win.destroy()#still left

                btn_1 = Button(frame_2, text = "Yes - Continue -->", font = ('Matura MT Script Capitals', 15), bg = 'black', fg = 'white', command = btn_1_fn)
                btn_1.pack()
                
                

            b1 = Button(rrl_win, text = 'Update Details', font = ('Courier New', 15), bg = 'black', fg = 'white', command = b1_fn)
            b1.grid(row=0,column=0)

            b2 = Button(rrl_win, text = 'Withdraw Consent', font = ('Courier New', 15), bg = 'black', fg = 'white', command = b2_fn)
            b2.grid(row=0,column=1,padx=7)

            frame = Frame(rrl_win, bg = 'silver')
            frame.grid(row=1,column=0,columnspan=2)


            #bifrost
            dark = ms.connect(host='localhost', user='root', passwd='dpsbn', database='arafoodsdb')
            kurse = dark.cursor()

            kurse.execute("select name, owner, type, ph_no, location, area, passwd from restaurants where passwd = '{}'".format(yyhs))
            mjolnir = kurse.fetchall()


            
            '''#note = ttk.Notebook(rrl_win)
            #note.pack(expand = True, fill = BOTH)

            #tab_1 = ttk.Frame(note)
            #note.add(tab_1, text = 'Update Details')

            #note0 = ttk.Notebook(tab_1)
            #note0.pack(expand = True, fill = BOTH)

            #taba = ttk.Frame(note0)
            #note0.add(taba, text = 'Restaurant Name')

            #res_name_1 = Label(taba, text = 'Restaurant Name: ', font = ('Broadway', 20), bg = 'silver')
            #res_name_1.grid(row=0,column=0,pady=20,padx=20)

            res_name_2 = Entry(taba, width = 25, font = ('Times New Roman', 20))
            res_name_2.grid(row=0,column=1,pady=20,padx=20)

            update_1 = Button(taba, text = 'Update', font = ('Iron Blade', 20), bg = 'gold')
            update_1.grid(row=1,column=1,sticky='w',pady=20)

            tabb = ttk.Frame(note0)
            note0.add(tabb, text = 'Owner Name')

            own_name_1 = Label(tabb, text = 'Owner Name: ', font = ('Broadway', 20), bg = 'silver')
            own_name_1.grid(row=0,column=0,pady=20,padx=20)

            own_name_2 = Entry(tabb, width = 25, font = ('Times New Roman', 20))
            own_name_2.grid(row=0,column=1,pady=20,padx=20)

            update_2 = Button(tabb, text = 'Update', font = ('Iron Blade', 20), bg = 'gold')
            update_2.grid(row=1,column=1,sticky='w',pady=20)

            tabc = ttk.Frame(note0)
            note0.add(tabc, text = 'Restaurant Type')

            res_type_1 = Label(tabc, text = 'Restaurant Type: ', font = ('Broadway', 20), bg = 'silver')
            res_type_1.grid(row=0,column=0,pady=20,padx=20)

            res_type_2 = Entry(tabc, width = 25, font = ('Times New Roman', 20))
            res_type_2.grid(row=0,column=1,pady=20,padx=20)

            update_3 = Button(tabc, text = 'Update', font = ('Iron Blade', 20), bg = 'gold')
            update_3.grid(row=1,column=1,sticky='w',pady=20)

            tabd = ttk.Frame(note0)
            note0.add(tabd, text = 'Restaurant Ph.No.')

            res_no_1 = Label(tabd, text = 'Restaurant Ph.No.: ', font = ('Broadway', 20), bg = 'silver')
            res_no_1.grid(row=0,column=0,pady=20,padx=20)

            res_no_2 = Entry(tabd, width = 25, font = ('Times New Roman', 20))
            res_no_2.grid(row=0,column=1,pady=20,padx=20)

            update_4 = Button(tabd, text = 'Update', font = ('Iron Blade', 20), bg = 'gold')
            update_4.grid(row=1,column=1,sticky='w',pady=20)

            tabe = ttk.Frame(note0)
            note0.add(tabe, text = 'Detailed Location')

            loc_1 = Label(tabe, text = 'Detailed Location: ', font = ('Broadway', 20), bg = 'silver')
            loc_1.grid(row=0,column=0,pady=20,padx=20)

            loc_2 = Entry(tabe, width = 25, font = ('Times New Roman', 20))
            loc_2.grid(row=0,column=1,pady=20,padx=20)

            update_5 = Button(tabe, text = 'Update', font = ('Iron Blade', 20), bg = 'gold')
            update_5.grid(row=1,column=1,sticky='w',pady=20)

            tabf = ttk.Frame(note0)
            note0.add(tabf, text = 'Area/Locality')

            area_1 = Label(tabf, text = 'Area/Locality: ', font = ('Broadway', 20), bg = 'silver')
            area_1.grid(row=0,column=0,pady=20,padx=20)

            area_2 = Entry(tabf, width = 25, font = ('Times New Roman', 20))
            area_2.grid(row=0,column=1,pady=20,padx=20)

            update_6 = Button(tabf, text = 'Update', font = ('Iron Blade', 20), bg = 'gold')
            update_6.grid(row=1,column=1,sticky='w',pady=20)

            tabg = ttk.Frame(note0)
            note0.add(tabg, text = 'Password')

            pass_1 = Label(tabg, text = 'Password: ', font = ('Broadway', 20), bg = 'silver')
            pass_1.grid(row=0,column=0,pady=20,padx=20)

            pass_2 = Entry(tabg, width = 25, font = ('Times New Roman', 20))
            pass_2.grid(row=0,column=1,pady=20,padx=20)

            update_7 = Button(tabg, text = 'Update', font = ('Iron Blade', 20), bg = 'gold')
            update_7.grid(row=1,column=1,sticky='w',pady=20)

            #==#

            #mj = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb3')
            #beat = mj.cursor(buffered = True)

            #beat.execute("select * from restaurants where id = {}".format(id_var))
            #it = beat.fetchall()'''

            

            
            
            #==#

            #tab_2 = ttk.Frame(note)
            #note.add(tab_2, text = 'Withdraw Consent')
            
            #=====================================================================================================#

    r_btn = Button(root, text = "Login", font = ('Iron Blade', 20), bg = 'gold', cursor = 'hand2', command = r_fn)
    r_btn.grid(row=3,column=1,pady=20,stick = 'w')
    
    
    
