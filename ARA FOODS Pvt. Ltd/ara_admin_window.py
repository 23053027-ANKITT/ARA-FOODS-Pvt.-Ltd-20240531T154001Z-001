from tkinter import *
from tkinter import ttk
import random as r
import random
from PIL import ImageTk
from PIL import Image
import math
import smtplib
import mysql.connector as ms
from last_win import loading_win_6

def ara_admin_function():

    #admin_win = adw
    adw = Tk()
    adw.title("Administrator Window")
    adw.iconbitmap("logo.ico")
    adw.geometry("850x550")
    adw.config(bg = "#C0C0C0")

    #=#
    global admin_username, admin_password
    admin_username = 'admin2ara'
    admin_password = 'fdsco@456'
    #=#

    #Create a main Frame
    main_frame_ad = Frame(adw)
    main_frame_ad.pack(fill = BOTH, expand = 1)

    #Create a Canvas
    my_canvas_ad = Canvas(main_frame_ad)
    my_canvas_ad.pack(side = LEFT, fill = BOTH, expand = 1)

    #Add a Scrollbar to the canvas
    my_scrollbar_ad = ttk.Scrollbar(main_frame_ad, orient = VERTICAL, command = my_canvas_ad.yview)
    my_scrollbar_ad.pack(side = RIGHT, fill = Y)

    #Configure the canvas
    my_canvas_ad.configure(yscrollcommand = my_scrollbar_ad.set)
    my_canvas_ad.bind('<Configure>', lambda e: my_canvas_ad.configure(scrollregion = my_canvas_ad.bbox('all')))

    #Create another frame inside canvas
    adw_frame_ad = Frame(my_canvas_ad)

    #Add that new frame into the window
    my_canvas_ad.create_window((0,0), window = adw_frame_ad, anchor = 'nw')

    #=#

    my_canvas_ad.config(bg = 'silver')
    adw_frame_ad.config(bg = 'silver')

    global adw_frame
    
    adw_frame = LabelFrame(adw_frame_ad, text = "Login as Administrator", font = ('Iron Blade', 30), bg = '#C0C0C0')
    adw_frame.pack(fill = BOTH, expand = True)

    global adw_entry_2, adw_entry_3

    adw_label_1 = Label(adw_frame, text = "Admin Username: ", font = ('Lucida Console', 20), bg = 'silver')
    adw_label_1.grid(row=0,column=0,pady=50)

    global adw_entry_1
    
    adw_entry_1 = Entry(adw_frame, width = 30, bg = 'black', fg = 'white', font = ('Times New Roman', 20))
    adw_entry_1.grid(row=0,column=1)

    
    adw_label_2 = Label(adw_frame, text = "Admin Email: ", font = ('Lucida Console', 20), bg = 'silver')
    adw_label_2.grid(row=1,column=0)

    adw_entry_2 = Entry(adw_frame, width = 30, font = ('Times New Roman', 20), bg = 'black', fg = 'white')
    adw_entry_2.grid(row=1,column=1)

    adw_label_3 = Label(adw_frame, text = "Enter OTP: ", font = ('Lucida Console', 20), bg = 'silver')
    adw_label_3.grid(row=2,column=0)

    adw_entry_3 = Entry(adw_frame, width = 30, font = ('Times New Roman', 20), bg = 'black', fg = 'white', show = '*')
    adw_entry_3.grid(row=2,column=1, pady=50)

    #==============#adw_entry_2 = Entry(adw_frame, width = 30, font = ('Times New Roman', 20), bg = 'blfjeje digeid , eodj "":dijdb rjjffjoj rikfbjhdibshwo mcoeoe dl dojdnek ofme, dbi  f imenrn )

    def otp_function_admin():

        #try:
        global adw_entry_2, adw_entry_3, OTP_admin

        digits="0123456789"
        OTP_admin=""
        for i in range(6):
            OTP_admin+=digits[math.floor(random.random()*10)]
        otp_admin = OTP_admin + " is your OTP for   < ADMIN LOGIN >\n\n\n(Don't share OTP to anyone)\n\n\n(Enter the OTP within 02:00 minutes)"
        msg = otp_admin
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("arafoodscompany@gmail.com", "fpch trvj kldg qxkp")
        emailid = adw_entry_2.get()
        s.sendmail('&&&&&&&&&&&',emailid,msg)

        global time_label_2
        
        time_label_2 = Label(adw_frame, text = "", font = ('Courier New', 20, 'bold'), bg = 'silver', fg = 'black')
        time_label_2.grid(row=3,column=0,padx=20)


            # timer =====
        
        global k
        k = 120
        
        def timer_admin():
                #lw.geometry("710x630")
            global k
            time_label_2.config(text = str(k) + " seconds left")
            k = k - 1
            time_label_2.after(1000, timer_admin)
            if k == -1:
                time_label_2.destroy()
                    #lw.geometry("570x630")
        
        timer_admin()

        #except:
        '''otp_error_admin = Tk()
            otp_error_admin.geometry("770x150")
            otp_error_admin.title("ERROR")
            otp_error_admin.iconbitmap("logo.ico")
            otp_error_admin.config(bg = 'black')
            label_error = Label(otp_error_admin, text = "\U0000274C" + " There was an unexpected error while generating the OTP" + "\n...Pls try again..." + "\n\n-Maybe try checking the internet connection-", bg = 'black', fg = 'red', font = ('Iron Blade', 20))
            label_error.pack(pady = 20)'''

    #==============#

    adw_sendotp = Button(adw_frame, text = "Send OTP to Email", bg = 'gold', font = ('Lucida Console', 20), command = otp_function_admin, cursor = 'hand2')
    adw_sendotp.grid(row=3,column=1)


    adw_cap_e = Entry(adw_frame, width = 30, font = ('Times New Roman', 20), bg = 'black', fg = 'white')
    adw_cap_e.grid(row=4,column=1, pady = 50)


    global cap_ad, cap_img_ad, rc_val

    rc_ad = r.randint(1,6)
    
    if rc_ad == 1:
        cap_img_ad = ImageTk.PhotoImage(Image.open("Captcha_1.png"), master = adw_frame)
        cap_ad = Label(adw_frame, image = cap_img_ad)
        cap_ad.grid(row=4,column=0, padx = 10, pady = 50)
        rc_val = 'a1dj80'
        
    elif rc_ad == 2:
        cap_img_ad = ImageTk.PhotoImage(Image.open("Captcha_2.png"), master = adw_frame)
        cap_ad = Label(adw_frame, image = cap_img_ad)
        cap_ad.grid(row=4,column=0, padx=10,pady = 50)
        rc_val = '5h09er'
        
    elif rc_ad == 3:
        cap_img_ad = ImageTk.PhotoImage(Image.open("Captcha_3.png"), master = adw_frame)
        cap_ad = Label(adw_frame, image = cap_img_ad)
        cap_ad.grid(row=4,column=0, padx=10,pady = 50)
        rc_val = 'f314fw'
        
    elif rc_ad == 4:
        cap_img_ad = ImageTk.PhotoImage(Image.open("Captcha_4.png"), master = adw_frame)
        cap_ad = Label(adw_frame, image = cap_img_ad)
        cap_ad.grid(row=4,column=0, padx=10,pady = 50)
        rc_val = 'kutr67'
        
    elif rc_ad == 5:
        cap_img_ad = ImageTk.PhotoImage(Image.open("Captcha_5.png"), master = adw_frame)
        cap_ad = Label(adw_frame, image = cap_img_ad)
        cap_ad.grid(row=4,column=0, padx=10,pady = 50)
        rc_val = 'dou78w'
        
    else:
        cap_img_ad = ImageTk.PhotoImage(Image.open("Captcha_6.png"), master = adw_frame)
        cap_ad = Label(adw_frame, image = cap_img_ad)
        cap_ad.grid(row=4,column=0, padx=10,pady = 50)
        rc_val = '69qwer'



    def reload_captcha_admin():
        
        rc_ad = r.randint(1,6)

        global cap_ad, rc_val
        
        if rc_ad == 1:
        
            cap_img_1_ad = ImageTk.PhotoImage(Image.open("Captcha_1.png"), master = adw_frame)
            cap_ad.config(image = cap_img_1_ad)
            cap_ad.image = cap_img_1_ad
            rc_val = 'a1dj80'
        
        elif rc_ad == 2:
            
            cap_img_1_ad = ImageTk.PhotoImage(Image.open("Captcha_2.png"), master = adw_frame)
            cap_ad.config(image = cap_img_1_ad)
            cap_ad.image = cap_img_1_ad
            rc_val = '5h09er'
        
        elif rc_ad == 3:
    
            cap_img_1_ad = ImageTk.PhotoImage(Image.open("Captcha_3.png"), master = adw_frame)
            cap_ad.config(image = cap_img_1_ad)
            cap_ad.image = cap_img_1_ad
            rc_val = 'f314fw'
        
        elif rc_ad == 4:
            
            cap_img_1_ad = ImageTk.PhotoImage(Image.open("Captcha_4.png"), master = adw_frame)
            cap_ad.config(image = cap_img_1_ad)
            cap_ad.image = cap_img_1_ad
            rc_val = 'kutr67'
        
        elif rc_ad == 5:
            
            cap_img_1_ad = ImageTk.PhotoImage(Image.open("Captcha_5.png"), master = adw_frame)
            cap_ad.config(image = cap_img_1_ad)
            cap_ad.image = cap_img_1_ad
            rc_val = 'dou78w'
        
        else:
            
            cap_img_1_ad = ImageTk.PhotoImage(Image.open("Captcha_6.png"), master = adw_frame)
            cap_ad.config(image = cap_img_1_ad)
            cap_ad.image = cap_img_1_ad
            rc_val = '69qwer'


    adw_cap_r = Button(adw_frame, text = "\U0001F501", font = 100, bg = 'green', fg = 'white', command = reload_captcha_admin, cursor = 'hand2')
    adw_cap_r.grid(row=4,column=2,padx=20)


    adw_label_4 = Label(adw_frame, text = "Admin Password: ", font = ('Lucida Console', 20), bg = 'silver')
    adw_label_4.grid(row=5,column=0,pady=20)

    adw_entry_4 = Entry(adw_frame, width = 30, font = ('Times New Roman', 20), bg = 'black', fg = 'white', show = '*')
    adw_entry_4.grid(row=5,column=1)


    def admin_check():

        admin_pass_var = 0

        a__1 = adw_entry_1.get()
        a__2 = adw_entry_3.get()
        a__3 = adw_entry_4.get()
        a__4 = adw_cap_e.get()
        
        if a__1.strip() == admin_username:
            if a__2.strip() == OTP_admin:
                if a__3.strip() == admin_password:
                    if a__4.strip() == rc_val:
                        if k > -1:
                            admin_pass_var = 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

        if admin_pass_var == 1: #NODAL
            
            adw.destroy()

            loading_win_6()
            
            '''ara_admin = Tk()
            ara_admin.title("ADMIN")
            ara_admin.iconbitmap("logo.ico")
            #ara_admin.geometry("500x500")
            ara_admin.state("zoomed")
            ara_admin.config(bg = '#003153')


            main_frame_ad_2 = Frame(ara_admin)
            main_frame_ad_2.pack(fill = BOTH, expand = True)
            main_frame_ad_2.config(bg = '#003153')


            my_canvas_ad_2 = Canvas(main_frame_ad_2)
            my_canvas_ad_2.pack(side = LEFT, fill = BOTH, expand = True)
            my_canvas_ad_2.config(bg = '#003153')

    
            my_scrollbar_ad_2 = ttk.Scrollbar(main_frame_ad_2, orient = VERTICAL, command = my_canvas_ad_2.yview)
            my_scrollbar_ad_2.pack(side = RIGHT, fill = Y)

    
            my_canvas_ad_2.configure(yscrollcommand = my_scrollbar_ad_2.set)
            my_canvas_ad_2.bind('<Configure>', lambda e: my_canvas_ad_2.configure(scrollregion = my_canvas_ad_2.bbox('all')))

    
            adw_frame_ad_2 = Frame(my_canvas_ad_2)

    
            my_canvas_ad_2.create_window((0,0), window = adw_frame_ad_2, anchor = 'nw')

            adw_frame_ad_2.config(bg = '#003153')

            #====================

            F_1_2 = Frame(ara_admin, bg = '#003153').pack(pady=20,padx=20)


            def var_fn():
                pass
            
            def vacad_fn():
                pass
                

            Button(F_1_2, text = "View all Restaurants", font = ('Courier New', 20, 'bold'), cursor = 'hand2', bg = 'orange', fg = 'black', command = var_fn).pack(pady=20)
            Button(F_1_2, text = "View all Customer account details", font = ('Courier New', 20, 'bold'), cursor = 'hand2', bg = 'orange', fg = 'black', command = vacad_fn).pack(padx=20)
'''
            #ara_conn = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            #ara_curr = ara_conn.cursor(buffered = True)
            #ara_conn.close()########
            
            
        else:
            #print("INCORRECT ADMIN LOGIN CREDENTIALS")

            sign_error = Tk()
            sign_error.title("ERROR")
            sign_error.iconbitmap("logo.ico")
            sign_error.geometry("500x100")
            sign_error.config(bg = "black")

            sign_error_label = Label(sign_error, text = "INCORRECT ADMIN LOGIN CREDENTIALS", font = ('Iron Blade', 20), bg = 'black', fg = 'red')
            sign_error_label.pack(pady=20)
        
    
    adw_submit = Button(adw_frame, text = "Login  as  Admin", bg = 'light blue', font = ('GodofThunder', 20), cursor = 'hand2', command = admin_check)
    adw_submit.grid(row=6,column=1, sticky = 'w', pady = 30)

#ara_admin_function()
