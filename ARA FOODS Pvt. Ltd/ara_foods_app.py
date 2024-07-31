#==#

from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import random as r
import os
import math
import random
import smtplib
from tkinter import messagebox
import time
from locality_dictionary import localities_blr
from food_genre_dict import food_genre
import urllib.request as ur
from search_window import loading_win_1
import mysql.connector as ms
from rrs_nw_function import rrs_new_window
from rrl_nw_function import rrl_new_window
from ara_admin_window import ara_admin_function
from search_window_2 import loading_win_2


#============================================================================================================

root = Tk()
root.title("ARA FOODS")
root.iconbitmap("logo.ico")
root.state('zoomed')
#root.attributes('-fullscreen', True)
root.config(bg = "#FED400")



#Create a main Frame
main_frame = Frame(root)
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


#========================================================================================================

var = 0

def toggle():
    
    global var
    if var % 2 == 0:
        #root.attributes('-fullscreen', False)
        root.geometry('1920x1080')
    else:
        root.state('zoomed')
        #root.attributes('-fullscreen', True)
    var = var + 1

#=============================================================================================================

#======================#
    
def search_new_window():

    def connect_net(host='http://google.com'):

        global con_var

        con_var = 0
    
        try:
            ur.urlopen(host) 
            con_var = 0
    
        except:
        
            con_var = 0


    connect_net()        

    global con_var

    if con_var == 0:

        if (len(search.get()) != 0) and (len(loc_area_e.get()) != 0):
            
            s_entry = search.get()
            mycon = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            mycur = mycon.cursor(buffered = True)
            mycur.execute("select sno from search_result_get order by sno desc")
            sno = mycur.fetchone()
            sno_int = sno[0]
            serial = sno_int + 1
            mycur.execute("insert into search_result_get values({}, '{}')".format(serial, s_entry))
            mycon.commit()
            mycon.close()

            mjolnir = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            thor = mjolnir.cursor(buffered = True)
            thor.execute("select pno from place_result_get order by pno desc")
            pno = thor.fetchone()
            pno_int = pno[0]
            perial = pno_int + 1
            thor.execute("insert into place_result_get values({}, '{}')".format(perial, loc_area_e.get()))
            mjolnir.commit()
            mjolnir.close()

            loading_win_1()

        else:

            len_error = Tk()
            len_error.title("Search Error")
            len_error.iconbitmap("logo.ico")
            len_error.geometry("600x100")
            len_error.config(bg = "black")

            error_label = Label(len_error, text = 'Either of the search (or area) fields are empty.\nPls type something to proceed.', bg = 'black', font = ('Times New Roamn', 20, 'bold'), fg = 'red')
            error_label.pack()

    else:

        con_error = Tk()
        con_error.title("Connection Error")
        con_error.iconbitmap("logo.ico")
        con_error.geometry("600x100")
        con_error.config(bg = "black")

        error_label = Label(con_error, text = 'There was an error in loading information.\nPls check internet connection', bg = 'black', font = ('Times New Roamn', 20, 'bold'), fg = 'red')
        error_label.pack()


def search_new_window_2():

    loading_win_2()
    
#======================#
        
def admin():

    ara_admin_function()

    '''#admin_win = adw
    adw = Tk()
    adw.title("Administrator Window")
    adw.iconbitmap("logo.ico")
    adw.geometry("850x550")
    adw.config(bg = "#C0C0C0")

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

    #==============#

    def otp_function_admin():

        try:
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

        except:
            otp_error_admin = Tk()
            otp_error_admin.geometry("770x150")
            otp_error_admin.title("ERROR")
            otp_error_admin.iconbitmap("logo.ico")
            otp_error_admin.config(bg = 'black')
            label_error = Label(otp_error_admin, text = "\U0000274C" + " There was an unexpected error while generating the OTP" + "\n...Pls try again..." + "\n\n-Maybe try checking the internet connection-", bg = 'black', fg = 'red', font = ('Iron Blade', 20))
            label_error.pack(pady = 20)

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

        if admin_pass_var == 1:
            #print("VERIFIED")

            ara_admin = Tk()
            ara_admin.title("ERROR")
            ara_admin.iconbitmap("logo.ico")
            ara_admin.geometry("500x500")
            ara_admin.config(bg = '#003153')

            ara_conn = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            ara_curr = ara_conn.cursor(buffered = True)

            ara_conn.close()########
            
            
        else:
            #print("INCORRECT ADMIN LOGIN CREDENTIALS")

            sign_error = Tk()
            sign_error.title("ERROR")
            sign_error.iconbitmap("logo.ico")
            sign_error.geometry("400x100")
            sign_error.config(bg = "black")

            sign_error_label = Label(sign_error, text = "INCORRECT ADMIN LOGIN CREDENTIALS", font = ('Iron Blade', 20), bg = 'black', fg = 'red')
            sign_error_label.pack(pady=20)
        
    
    adw_submit = Button(adw_frame, text = "Login  as  Admin", bg = 'light blue', font = ('GodofThunder', 20), cursor = 'hand2', command = admin_check)
    adw_submit.grid(row=6,column=1, sticky = 'w', pady = 30)'''


#=============================================================================================================


'''def add():

    # add_window
    aw = Tk()
    aw.title("Add Restaurant")
    aw.iconbitmap("logo.ico")
    aw.geometry("900x550")
    aw.config(bg = "black")

    #global main_frame_2, my_canvas_2, my_scrollbar_2, aw_login

    #Create a main Frame
    main_frame_2 = Frame(master = aw)
    main_frame_2.pack(fill = BOTH, expand = 1)

    #Create a Canvas
    my_canvas_2 = Canvas(main_frame_2)
    my_canvas_2.pack(side = LEFT, fill = BOTH, expand = 1)

    #Add a Scrollbar to the canvas
    my_scrollbar_2 = ttk.Scrollbar(main_frame_2, orient = VERTICAL, command = my_canvas_2.yview)
    my_scrollbar_2.pack(side = RIGHT, fill = Y)

    #Configure the canvas
    my_canvas_2.configure(yscrollcommand = my_scrollbar_2.set)
    my_canvas_2.bind('<Configure>', lambda f: my_canvas_2.configure(scrollregion = my_canvas_2.bbox('all')))

    #Create another frame inside canvas
    aw_login = Frame(master = my_canvas_2)

    #Add that new frame into the window
    my_canvas_2.create_window((0,0), window = aw_login, anchor = 'nw')

    my_canvas_2.config(bg = 'black')
    aw_login.config(bg = 'black')

    global aw_new_bg_1
    
    aw_bg_1 = Image.open("add_img.png")
    aw_bg_1_res = aw_bg_1.resize((875, 325), Image.ANTIALIAS)
    aw_new_bg_1 = ImageTk.PhotoImage(aw_bg_1_res, master = aw_login)
    aw_bg_1_label = Label(master = aw_login, image = aw_new_bg_1)
    aw_bg_1_label.pack()

    business_label = Label(aw_login, text = "ARA FOODS\nfor business", font = ('Iron Blade', 15), bg = 'black', fg = 'gold')
    business_label.place(x=10,y=10)

    #========#

    def rrs_fn():

        aw.destroy()

        rrs_new_window()

    def rrl_fn():
        
        aw.destroy()

        rrl_new_window()

    #========#
    
    #register_restaurant_signin = rrs
    rrs = Button(aw_login, text = "Register your Restaurant", font = ('Times New Roman', 18), bg = 'light blue', cursor = 'hand2', command = rrs_fn)
    rrs.place(x=50,y=200)

    #register_restaurant_login = rrl
    rrl = Button(aw_login, text = "Restaurant already added? Login...", font = ('Times New Roman', 18), bg = 'light blue', cursor = 'hand2', command = rrl_fn)
    rrl.place(x=470,y=200)

    aw_space_1 = Label(aw_login, text = "", bg = 'black')
    aw_space_1.pack(pady=30)
        
    aw_info_label = Label(master = aw_login, text = "Why should you choose ARA FOODS ??", font = ('Castellar', 20), bg = 'black', fg = 'gold')
    aw_info_label.pack(pady = 60)

    aw_space_2 = Label(aw_login, text = "", bg = 'black')
    aw_space_2.pack()

    aw_info_frame = Frame(aw_login, bg = 'black')
    aw_info_frame.pack()

    aw_info_frame_1 = LabelFrame(aw_info_frame, bg = 'black')
    aw_info_frame_1.grid(row=0,column=0, pady = 5)

    aw_info_1a = Label(aw_info_frame_1, text = "100+ Restaurants", font = ('Old English Text MT', 20), bg = 'black', fg = 'light blue')
    aw_info_1b = Label(aw_info_frame_1, text = "listed so far...", font = ('Times New Roman', 15), bg = 'black', fg = 'light green')
    aw_info_1a.pack()
    aw_info_1b.pack()

    aw_info_frame_2 = LabelFrame(aw_info_frame, bg = 'black')
    aw_info_frame_2.grid(row=0,column=1, pady = 5, padx = 50)

    aw_info_2a = Label(aw_info_frame_2, text = "1.0 lakh+", font = ('Old English Text MT', 20), bg = 'black', fg = 'light blue')
    aw_info_2b = Label(aw_info_frame_2, text = "monthly orders", font = ('Times New Roman', 15), bg = 'black', fg = 'light green')
    aw_info_2a.pack()
    aw_info_2b.pack()

    aw_info_frame_3 = LabelFrame(aw_info_frame, bg = 'black')
    aw_info_frame_3.grid(row=0,column=2, pady = 5)

    aw_info_3a = Label(aw_info_frame_3, text = "60% more income", font = ('Old English Text MT', 20), bg = 'black', fg = 'light blue')
    aw_info_3b = Label(aw_info_frame_3, text = "2x new customers", font = ('Times New Roman', 15), bg = 'black', fg = 'light green')
    aw_info_3a.pack()
    aw_info_3b.pack()

    aw_space_3 = Label(aw_login, text = "", bg = 'black')
    aw_space_3.pack()

    aw__frame = LabelFrame(aw_login, text = "", bg = 'gold', fg = 'black')
    aw__frame.pack(pady = 100)

    aw_info_2_label = Label(aw__frame, text = "    Quite easy", bg = 'gold', fg = 'black', font = ('Old English Text MT', 30))
    aw_info_2_label.pack(pady = 30)
 
    #=============================================#

    aw_info_frame2 = Frame(aw__frame, bg = 'gold')
    aw_info_frame2.pack(pady = 50)

    aw_info_frame2_1 = LabelFrame(aw_info_frame2, bg = 'black')
    aw_info_frame2_1.grid(row=0,column=0, pady = 5)

    aw_info_21a = Label(aw_info_frame2_1, text = "Step - 1", font = ('Ink Free', 20), bg = 'black', fg = 'light blue')
    aw_info_21b = Label(aw_info_frame2_1, text = "Create your page on ARA FOODS", font = ('Times New Roman', 15), bg = 'black', fg = 'light green')
    aw_info_21a.pack()
    aw_info_21b.pack()

    aw_info_frame2_2 = LabelFrame(aw_info_frame2, bg = 'black')
    aw_info_frame2_2.grid(row=0,column=1, pady = 5, padx = 50)

    aw_info_22a = Label(aw_info_frame2_2, text = "Step - 2", font = ('Ink Free', 20), bg = 'black', fg = 'light blue')
    aw_info_22b = Label(aw_info_frame2_2, text = "Register for Online Ordering", font = ('Times New Roman', 15), bg = 'black', fg = 'light green')
    aw_info_22a.pack()
    aw_info_22b.pack()

    aw_info_frame2_3 = LabelFrame(aw_info_frame2, bg = 'black')
    aw_info_frame2_3.grid(row=0,column=2, pady = 5)

    aw_info_23a = Label(aw_info_frame2_3, text = "Step - 3", font = ('Ink Free', 20), bg = 'black', fg = 'light blue')
    aw_info_23b = Label(aw_info_frame2_3, text = "Start receiving orders online", font = ('Times New Roman', 15), bg = 'black', fg = 'light green')
    aw_info_23a.pack()
    aw_info_23b.pack()'''



#=============================================================================================================


#================================================================================================================


def submit_signin():

    def connect_net2(host='http://google.com'):

        global con_var2

        con_var2 = 0
    
        try:
            ur.urlopen(host) 
            con_var2 = 0
    
        except:
        
            con_var2 = 0


    connect_net2()
    

    if con_var2 == 0:

        cap_score = 0
        pass_score = 0


        if cap_ent.get() == rc_val2:
            cap_score = 1


        if len(suw_pw.get()) >= 8:
            pass_score += 1


        U_count = 0
        L_count = 0
        D_count = 0
        S_count = 0
        
        for qi in suw_pw.get():
            
            if qi.isupper() == True:
                U_count += 1
                
            if qi.islower() == True:
                L_count += 1
                
            if qi in set('1234567890'):
                D_count += 1

            if qi in set('@#$'):
                S_count += 1


        if U_count >= 1:
            pass_score += 1

        if L_count >= 1:
            pass_score += 1

        if D_count >= 1:
            pass_score += 1
            
        if S_count >= 1:
            pass_score += 1


        ##
        final_score = 0

        if (cap_score != 1) or (pass_score != 5):
            global pass_error
            pass_error = Tk()
            pass_error.title("Password pattern incorrect")
            pass_error.iconbitmap("logo.ico")
            pass_error.geometry("600x200")
            pass_error.config(bg = "black")
            
        if cap_score == 1:
            final_score += 1
        else:
            pass_error_label_1 = Label(pass_error, text = "Your Captcha code is incorrect", font = ('Iron Blade', 20), bg = 'black', fg = 'red')
            pass_error_label_1.pack(pady=20)

        if pass_score == 5:
            final_score += 1
        else:
            pass_error_label_2 = Label(pass_error, text = "Pls follow the rules to set your Password", font = ('Iron Blade', 20), bg = 'black', fg = 'red')
            pass_error_label_2.pack(pady=20)


        if len(suw_un.get()) != 0:
            final_score += 1

        if len(suw_email.get()) != 0:
            final_score += 1

        #==================#
            
        if final_score == 4:
            
            try:
                pass_error.destroy()
            except:
                pass

            try:
                
                s_con = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                s_cur = s_con.cursor(buffered = True)

                s_cur.execute("select user_id from accounts order by user_id desc")
                s_id = s_cur.fetchone()
            
                s_cur.execute("insert into accounts values({},'{}','{}','{}')".format(s_id[0] + 1, suw_un.get(), suw_email.get(), suw_pw.get()))
                s_con.commit()

                s_con.close()


                try:
                    pass_error.destroy()
                except:
                    pass

                try:
                    s_error.destroy()
                except:
                    pass


                sign_success = Tk()
                sign_success.title("Sign In - Completed")
                sign_success.iconbitmap("logo.ico")
                sign_success.geometry("1000x200")
                sign_success.config(bg = "gold")

                sign_success_label = Label(sign_success, text = "Congratulations!!!\nYour account has been successfully created in ARA FOODS.", font = ('Cooper Black', 20), bg = 'gold', fg = 'black')
                sign_success_label.pack(pady=20)

                def close_sign():
                    try:
                        pass_error.destroy()
                    except:
                        pass
                    try:
                        s_error.destroy()
                    except:
                        pass
                    try:
                        sign_success.destroy()
                    except:
                        pass
                    try:
                        suw.destroy()
                    except:
                        pass
                    
                
                sign_button = Button(sign_success, text = "Close", font = ('Iron Blade', 30), bg = 'black', fg = 'gold', cursor = 'hand2', command = close_sign)
                sign_button.pack(pady=20)
                

            except:

                s_error = Tk()
                s_error.title("Sign In - ERROR")
                s_error.iconbitmap("logo.ico")
                s_error.geometry("700x100")
                s_error.config(bg = "gold")

                s_error_label = Label(s_error, text = "Unexpected error occured.\nTry changing Username/Password.", font = ('Cooper Black', 20), bg = 'gold', fg = 'black')
                s_error_label.pack(pady=20)

        else:

            s__error = Tk()
            s__error.title("Sign In - ERROR")
            s__error.iconbitmap("logo.ico")
            s__error.geometry("700x100")
            s__error.config(bg = "gold")

            s__error_label = Label(s__error, text = "Unexpected error occured.\nTry changing Username/Password.", font = ('Cooper Black', 20), bg = 'gold', fg = 'black')
            s__error_label.pack(pady=20)
            

    else:
         
        sign_error = Tk()
        sign_error.title("ERROR")
        sign_error.iconbitmap("logo.ico")
        sign_error.geometry("400x100")
        sign_error.config(bg = "black")

        sign_error_label = Label(sign_error, text = "Pls check Internet connection", font = ('Iron Blade', 20), bg = 'black', fg = 'red')
        sign_error_label.pack(pady=20)


        


#================================================================================================================

def close_info():
        global info
        try:
            info.destroy()
        except:
            pass

def sign_up():
    
    # sign_up_window = suw
    global suw
    suw = Tk()
    suw.title("Sign Up")
    suw.iconbitmap("logo.ico")
    suw.geometry("750x550")
    suw.config(bg = "black")

    suw_frame = LabelFrame(suw, text = "Sign Up", font = ('Iron Blade', 30), bg = 'black', fg = 'white')
    suw_frame.pack(fill = BOTH, expand = True)

    def popup():
        global info
        info = Tk()
        info.geometry("400x200")
        info.title("PASSWORD - INFO")
        info.iconbitmap("logo.ico")
        info.config(bg = "black")

        mb = Label(master = info,
                   text = "Password should be minimumn of 8 characters,\nwith atleast 1 upper-case letter,\nwith atleast 1 lower-case letter,\nwith atleast 1 numeric,\n& should contain atleast 1 of these: [ @ , # , $ ]",
                   font = ('Times New Roman', 15), bg = 'black', fg = 'white')
        mb.grid(row=0,column=0)

        mb_btn = Button(info, text = "CLOSE", font = ('Iron Blade', 15), bg = 'red', command = close_info, cursor = "hand2")
        mb_btn.grid(row=1,column=0, pady=15)

        root.after(15000, close_info)

    
    # user_name = un
    global suw_un
    suw_un_label = Label(suw_frame, text = "User Name - ", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    suw_un_label.grid(row=0,column=0,padx=20,pady=50)
    suw_un = Entry(suw_frame, width = 25, font = ('Times New Roman', 20), bg = 'yellow')
    suw_un.grid(row=0,column=1)

    global suw_email
    suw_email_label = Label(suw_frame, text = "Email - ", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    suw_email_label.grid(row=1,column=0)
    suw_email = Entry(suw_frame, width = 25, font = ('Times New Roman', 20), bg = 'yellow')
    suw_email.grid(row=1,column=1)

    # password = pw
    global suw_pw
    suw_pw_label = Label(suw_frame, text = "Password - ", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    suw_pw_label.grid(row=2,column=0)
    suw_pw = Entry(suw_frame, width = 25, font = ('Times New Roman', 20), bg = 'yellow', show = '*')
    suw_pw.grid(row=2,column=1, pady=50)

    info_mb = Button(suw_frame, text = "\U000026A0", command = popup, font = 100, bg = 'green', fg = 'white', cursor = "hand2").grid(row=2,column=2, padx = 20)

    global cap, rc_val2

    rc = r.randint(1,6)
    
    if rc == 1:
        cap_img = ImageTk.PhotoImage(Image.open("Captcha_1.png"), master = suw_frame)
        cap = Label(suw_frame, image = cap_img)
        cap.grid(row=3,column=0, padx = 10)
        rc_val2 = 'a1dj80'
        
    elif rc == 2:
        cap_img = ImageTk.PhotoImage(Image.open("Captcha_2.png"), master = suw_frame)
        cap = Label(suw_frame, image = cap_img)
        cap.grid(row=3,column=0, padx=10)
        rc_val2 = '5h09er'
        
    elif rc == 3:
        cap_img = ImageTk.PhotoImage(Image.open("Captcha_3.png"), master = suw_frame)
        cap = Label(suw_frame, image = cap_img)
        cap.grid(row=3,column=0, padx=10)
        rc_val2 = 'f314fw'
        
    elif rc == 4:
        cap_img = ImageTk.PhotoImage(Image.open("Captcha_4.png"), master = suw_frame)
        cap = Label(suw_frame, image = cap_img)
        cap.grid(row=3,column=0, padx=10)
        rc_val2 = 'kutr67'
        
    elif rc == 5:
        cap_img = ImageTk.PhotoImage(Image.open("Captcha_5.png"), master = suw_frame)
        cap = Label(suw_frame, image = cap_img)
        cap.grid(row=3,column=0, padx=10)
        rc_val2 = 'dou78w'
        
    else:
        cap_img = ImageTk.PhotoImage(Image.open("Captcha_6.png"), master = suw_frame)
        cap = Label(suw_frame, image = cap_img)
        cap.grid(row=3,column=0, padx=10)
        rc_val2 = '69qwer'


    #def submit_signin():
        #pass

    def reload_captcha():
        
        rc = r.randint(1,6)

        global cap, rc_val2
        
        if rc == 1:
        
            cap_img_1 = ImageTk.PhotoImage(Image.open("Captcha_1.png"), master = suw_frame)
            cap.config(image = cap_img_1)
            cap.image = cap_img_1
            rc_val2 = 'a1dj80'
        
        elif rc == 2:
            
            cap_img_1 = ImageTk.PhotoImage(Image.open("Captcha_2.png"), master = suw_frame)
            cap.config(image = cap_img_1)
            cap.image = cap_img_1
            rc_val2 = '5h09er'
        
        elif rc == 3:
    
            cap_img_1 = ImageTk.PhotoImage(Image.open("Captcha_3.png"), master = suw_frame)
            cap.config(image = cap_img_1)
            cap.image = cap_img_1
            rc_val2 = 'f314fw'
        
        elif rc == 4:
            
            cap_img_1 = ImageTk.PhotoImage(Image.open("Captcha_4.png"), master = suw_frame)
            cap.config(image = cap_img_1)
            cap.image = cap_img_1
            rc_val2 = 'kutr67'
        
        elif rc == 5:
            
            cap_img_1 = ImageTk.PhotoImage(Image.open("Captcha_5.png"), master = suw_frame)
            cap.config(image = cap_img_1)
            cap.image = cap_img_1
            rc_val2 = 'dou78w'
        
        else:
            
            cap_img_1 = ImageTk.PhotoImage(Image.open("Captcha_6.png"), master = suw_frame)
            cap.config(image = cap_img_1)
            cap.image = cap_img_1
            rc_val2 = '69qwer'


    rel = Button(suw_frame, text = "\U0001F501", font = 100, bg = 'green', fg = 'white', cursor = "hand2", command = reload_captcha)
    rel.grid(row=4,column=0, pady = 30)

    global cap_ent

    cap_ent = Entry(suw_frame, width = 25, font = ('Times New Roman', 20), bg = 'yellow')
    cap_ent.grid(row=3, column=1)
    

    submit = Button(suw_frame, text = "SIGN UP", font = ('Iron Blade', 30), bg = 'orange', command = submit_signin, cursor = "hand2")
    submit.grid(row=4, column=1)

    suw.mainloop()
    
    
    #=======================================================================================================================
    
def login():
    
    # login_window = lw
    global lw
    lw = Tk()
    lw.title("Login")
    lw.iconbitmap("logo.ico")
    lw.geometry("570x630")
    lw.config(bg = "black")

    lw_frame = LabelFrame(lw, text = "Login", font = ('Iron Blade', 30), bg = 'black', fg = 'white')
    lw_frame.pack(fill = BOTH, expand = True)

    lw_un_label = Label(lw_frame, text = "User Name - ", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    lw_un_label.grid(row=0,column=0,padx=20,pady=40)

    global lw_un
    lw_un = Entry(lw_frame, width = 25, font = ('Times New Roman', 20), bg = 'yellow')
    lw_un.grid(row=0,column=1)

    lw_f = LabelFrame(lw_frame, bg = 'black', fg = 'white')
    lw_f.grid(row=1, column=0, columnspan=2)

    

    # password = pw

    global lw_em, otp_entry
    
    lw_pw_label = Label(lw_f, text = "Password - ", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    lw_pw_label.grid(row=0,column=0, padx = 10)

    global lw_pw
    lw_pw = Entry(lw_f, width = 25, font = ('Times New Roman', 20), bg = 'yellow', show = '*')
    lw_pw.grid(row=0,column=1, pady=20, padx = 20)

    lw_space = Label(lw_f, text = " ", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    lw_space.grid(row=1,column=0, padx = 10, pady=30)

    lw_or = Label(lw_f, text = "__ OR __", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    lw_or.place(x=240,y=100)

    lw_em_label = Label(lw_f, text = "Email - ", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    lw_em_label.grid(row=2,column=0, pady = 20)
    
    lw_em = Entry(lw_f, width = 25, font = ('Times New Roman', 20), bg = 'yellow')
    lw_em.grid(row=2,column=1)

    #timer and otp

    lw_otp_label = Label(lw_f, text = "Enter OTP - ", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
    lw_otp_label.grid(row=3,column=0)

    otp_entry = Entry(lw_f, width = 25, font = ('Times New Roman', 20), bg = 'yellow', show = '*')
    otp_entry.grid(row=3,column=1)

    def otp_function():

        try:
            global lw_em, otp_entry, OTP

            digits="0123456789"
            OTP=""
            for i in range(6):
                OTP+=digits[math.floor(random.random()*10)]
            otp = OTP + " is your OTP for   < LOGIN >\n\n\n(Don't share OTP to anyone)\n\n\n(Enter the OTP within 02:00 minutes)"
            msg = otp
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("arafoodscompany@gmail.com", "fpch trvj kldg qxkp")
            emailid = lw_em.get()
            s.sendmail('&&&&&&&&&&&',emailid,msg)

            global time_label_1
        
            time_label_1 = Label(lw_f, text = "", font = ('Courier New', 20, 'bold'), bg = 'black', fg = 'white')
            time_label_1.grid(row=4,column=0, padx = 20)


            # timer =====
        
            global j
            j = 120
        
            def timer():
                lw.geometry("710x630")
                global j
                time_label_1.config(text = str(j) + " seconds left")
                j = j - 1
                time_label_1.after(1000, timer)
                if j == -1:
                    time_label_1.destroy()
                    lw.geometry("570x630")
        
            timer()

        except:
            otp_error = Tk()
            otp_error.geometry("770x150")
            otp_error.title("ERROR")
            otp_error.iconbitmap("logo.ico")
            otp_error.config(bg = 'black')
            label_error = Label(otp_error, text = "\U0000274C" + " There was an unexpected error while generating the OTP" + "\n...Pls try again..." + "\n\n-Maybe try checking the internet connection-", bg = 'black', fg = 'red', font = ('Iron Blade', 20))
            label_error.pack(pady = 20)
            

    def login_pass():
        
        global OTP, otp_entry

        def connect_net3(host='http://google.com'):

            global con_var3

            con_var3 = 0
    
            try:
                ur.urlopen(host) 
                con_var3 = 0
    
            except:
        
                con_var3 = 0


        connect_net3()

        if con_var3 == 0:

            log_con = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
            log_cur = log_con.cursor()

            log_cur.execute("select username from accounts")
            data1 = log_cur.fetchall()


            log_score = 0

            for xe in data1:
                if lw_un.get() == xe[0]:
                    log_score += 1

            if (len(lw_pw.get()) != 0) and (len(lw_em.get()) == 0):

                log_cur.execute("select password from accounts")
                data2 = log_cur.fetchall()

                for ex in data2:
                    if lw_pw.get() == ex[0]:
                        log_score += 1

            if (len(lw_pw.get()) == 0) and (len(lw_em.get()) != 0) and (j > -1):

                if otp_entry.get() == str(OTP.strip()):
                    log_score += 1

            if log_score == 2:

                log_success = Tk()
                log_success.title("Logged In - Successfully")
                log_success.iconbitmap("logo.ico")
                log_success.geometry("1000x200")
                log_success.config(bg = "silver")

                log_success_label = Label(log_success, text = "Yippee!!!\nYou have logged in into your account.", font = ('Cooper Black', 20), bg = 'silver', fg = 'black')
                log_success_label.pack(pady=20)

                global login_btn, signup_btn, login_side_tab
                login_btn.destroy()
                signup_btn.destroy()
                
                login_side_tab = LabelFrame(second_frame, text = 'My Profile', font = ('Iron Blade', 20), bg = '#9403fc')
                login_side_tab.place(x=1050,y=42.5)

                global profile_img, profile_label
                profile_img = ImageTk.PhotoImage(Image.open("User_icon.png"), master = login_side_tab)
                profile_imglabel = Label(master = login_side_tab, image = profile_img)
                profile_imglabel.grid(row=0,column=0,pady=20)

                profile_label = Label(master = login_side_tab, text = lw_un.get(), font = ('Iron Blade', 20), bg = '#9403fc', fg = 'white')
                profile_label.grid(row=1,column=0)


                options_list = ['Settings', 'Logout']

                def drop_1_fn(event):

                    '''if drop_1.get() == options_list[0]:

                        orders = Tk()
                        orders.title("My Orders")
                        orders.iconbitmap("logo.ico")
                        orders.geometry("400x400")
                        orders.config(bg = "yellow")'''

                        # To be continued...

                    if drop_1.get() == options_list[0]:

                        sets = Tk()
                        sets.title("Settings")
                        sets.iconbitmap("logo.ico")
                        sets.geometry("690x310")
                        sets.config(bg = "light blue")

                        name_s = Label(sets, text = "Name: ", font = ('Broadway', 20), bg = 'light blue')
                        email_s = Label(sets, text = 'Email ID: ', font = ('Broadway', 20), bg = 'light blue')
                        passwd_s = Label(sets, text = 'Password: ', font = ('Broadway', 20), bg = 'light blue')

                        global name_se, email_se, passwd_se
                        name_se = Entry(sets, width = 30, font = ('Times New Roman', 20))
                        email_se = Entry(sets, width = 30, font = ('Times New Roman', 20))
                        passwd_se = Entry(sets, width = 30, font = ('Times New Roman', 20))

                        name_s.grid(row=0,column=0,pady=30,padx=20)
                        email_s.grid(row=1,column=0,padx=20)
                        passwd_s.grid(row=2,column=0,pady=30,padx=20)
                        name_se.grid(row=0,column=1)
                        email_se.grid(row=1,column=1)
                        passwd_se.grid(row=2,column=1)

                        bifrost = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                        froid = bifrost.cursor()

                        froid.execute("select username, email, password from accounts where user_id = {}".format(name_x))
                        global datax
                        datax = froid.fetchall()
                        
                        name_se.insert(0, datax[0][0])
                        email_se.insert(0, datax[0][1])
                        passwd_se.insert(0, datax[0][2])

                        def update_sets(): 

                            if (len(name_se.get()) != 0) and (len(email_se.get()) != 0) and (len(passwd_se.get()) != 0):
                                if ".com" in email_se.get():
                                    if len(passwd_se.get()) >= 8:
                                        U_count = 0
                                        L_count = 0
                                        D_count = 0
                                        S_count = 0
                                        for xex in passwd_se.get():
                                            if xex.isupper() == True:
                                                U_count += 1
                                            if xex.islower() == True:
                                                L_count += 1
                                            if xex in set('1234567890'):
                                                D_count += 1
                                            if xex in set('@#$'):
                                                S_count += 1

                            try:
                                
                                if U_count >= 1 and L_count >= 1 and D_count >= 1 and S_count >= 1:

                                    upd_con = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                                    upd_cur = upd_con.cursor()

                                    upd_cur.execute("update accounts set username = '{}', email = '{}', password = '{}' where user_id = {}".format(name_se.get(), email_se.get(), passwd_se.get(), name_x))
                                    upd_con.commit()

                                    upd_con.close()

                                    bi_log = Tk()
                                    bi_log.title("ERROR")
                                    bi_log.iconbitmap("logo.ico")
                                    bi_log.geometry("600x100")
                                    bi_log.config(bg = "black")

                                    bi_log_label = Label(bi_log, text = "The credentials have been successfully updated.", font = ('Iron Blade', 20), bg = 'black', fg = '#13ff03')
                                    bi_log_label.pack(pady=20)

                                    profile_label.config(text = name_se.get())

                                else:

                                    bilog = Tk()
                                    bilog.title("ERROR")
                                    bilog.iconbitmap("logo.ico")
                                    bilog.geometry("600x100")
                                    bilog.config(bg = "black")

                                    bilog_label = Label(bilog, text = "There was an error in updating the credentials.", font = ('Iron Blade', 20), bg = 'black', fg = 'red')
                                    bilog_label.pack(pady=20)

                            except:
                                pass

                        update_btn = Button(sets, text = "UPDATE", font = ('Broadway', 25), bg = 'blue', fg = 'white', cursor = 'hand2', command = update_sets)
                        update_btn.grid(row=3,column=1)

                    if drop_1.get() == options_list[1]:

                        login_side_tab.destroy()

                        logout_success = Tk()
                        logout_success.title("Logout - Success")
                        logout_success.iconbitmap("logo.ico")
                        logout_success.geometry("700x100")
                        logout_success.config(bg = "black")

                        logout_success_label = Label(logout_success, text = "You have successfully logged out of your account.", font = ('Iron Blade', 20), bg = 'black', fg = 'white')
                        logout_success_label.pack(pady=20)
                        
                        global login_btn, signup_btn
                        login_btn = Button(second_frame, text = "LOGIN", bg = 'black', fg = 'white', font = ("Iron Blade", 30), cursor = 'hand2', command = login )
                        login_btn.place(x=900,y=30)

                        signup_btn = Button(second_frame, text = "Sign Up", bg = 'black', fg = 'white', font = ("Iron Blade", 30), cursor = 'hand2', command = sign_up)
                        signup_btn.place(x=1100,y=30)
                        

                drop_1 = ttk.Combobox(master = login_side_tab, value = options_list, font = ('Iron Blade', 15))
                drop_1.current(0)
                drop_1.bind("<<ComboboxSelected>>", drop_1_fn)
                drop_1.grid(row=2,column=0,pady=10)


                def close_log():
                    try:
                        log_success.destroy()
                    except:
                        pass

                    try:
                        lw.destroy()
                    except:
                        pass


                groot_con = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
                groot_cur = groot_con.cursor()

                groot_cur.execute("select user_id from accounts where username = '{}'".format(lw_un.get()))
                groot_data = groot_cur.fetchone()

                global name_x
                name_x = groot_data[0]

                groot_con.close()
                
                log_button = Button(log_success, text = "Close", font = ('Iron Blade', 30), bg = 'black', fg = 'silver', cursor = 'hand2', command = close_log)
                log_button.pack(pady=20)

                log_con.close()

        else:

            log_error = Tk()
            log_error.title("ERROR")
            log_error.iconbitmap("logo.ico")
            log_error.geometry("400x100")
            log_error.config(bg = "black")

            log_error_label = Label(log_error, text = "Pls check Internet connection", font = ('Iron Blade', 20), bg = 'black', fg = 'red')
            log_error_label.pack(pady=20)
            

    
            
    
    send_btn = Button(lw_f, text = "Send OTP", font = ('Iron Blade', 20), bg = 'blue', fg = 'white', cursor = 'hand2', command = otp_function)
    send_btn.grid(row=4,column=1, pady = 20)

    lw_login_btn = Button(lw_frame, text = "LOGIN", font = ('Iron Blade', 30), bg = 'orange', cursor = 'hand2', command = login_pass)
    lw_login_btn.grid(row=2,column=1, pady = 30, sticky = 'w')

    
        
#============================================================================================================================



second_frame.config(bg = '#FED400')

bg_1 = Image.open("FOODS_2.png")
#bg_1_res = bg_1.resize((1275, 715), resample = Image.Resampling.LANCZOS)
bg_1_res = bg_1.resize((1275, 715), Image.Resampling.LANCZOS)
new_bg_1 = ImageTk.PhotoImage(bg_1_res, master = second_frame)
bg_1_label = Label(second_frame, image = new_bg_1, highlightcolor = '#FFD700', highlightbackground = '#FFD700', highlightthickness = 3)
bg_1_label.pack()

loc_ser_frame = Frame(second_frame, bg = '#FFD700', width = 1200, height = 600)
loc_ser_frame.pack(pady = 100)

#loc_house_e = Entry(loc_ser_frame, width = 50, font  = ('Times New Roman', 20), bg = 'white')
#loc_house_e.grid(row=1,column=1)

#loc_label  = Label(loc_ser_frame, text = "Enter Location: ", font = ('Cocogoose Pro', 23), bg = '#FFD700')
#loc_label.grid(row=0,column=1, sticky = 'w', pady = 30)

#loc_house = Label(loc_ser_frame, text = "House No.: ", font = ('Cocogoose Pro', 23), bg = '#FFD700')
#loc_house.grid(row=1,column=0)

#loc_name = Label(loc_ser_frame, text = "House Name: ", font = ('Cocogoose Pro', 23), bg = '#FFD700')
#loc_name.grid(row=2, column=0)

#loc_name_e = Entry(loc_ser_frame, width = 50, font = ('Times New Roman', 20), bg = 'white')
#loc_name_e.grid(row=2, column=1)

loc_area = Label(loc_ser_frame, text = "Area/Region: ", font = ('Cocogoose Pro', 23), bg = '#FFD700')
loc_area.place(x=75,y=-5)#grid(row=3,column=0)

frame_y = Frame(loc_ser_frame, bg = '#FFD700')
frame_y.grid(row=3,column=1)

loc_area_e = Entry(frame_y, width = 50, font = ('Times New Roman', 20), bg = 'white')
loc_area_e.grid(row=0,column=0)

#loc_info_label = Label(loc_ser_frame, text = "You can skip\nHouse No and\nHouse Name\nas of now", font = ('Iron Blade', 20), bg = "#FFD700", fg = 'blue')
#loc_info_label.grid(row=4,column=0)

frame_x = Frame(loc_ser_frame, bg = '#FFD700')
frame_x.grid(row=5,column=1,pady=50)

search = Entry(frame_x, width = 50, font  = ('Times New Roman', 20), bg = 'white')
search.grid(row=0,column=0)

ser_label  = Label(loc_ser_frame, text = "Search Food/Restaurant: ", font = ('Cocogoose Pro', 23), bg = '#FFD700')
ser_label.place(x=-5,y=405)

ser_label  = Label(loc_ser_frame, text = "Search Food/Restaurant: ", font = ('Cocogoose Pro', 23), bg = '#FFD700', fg = '#FFD700')
ser_label.grid(row=5,column=0)

#search_info_label = Label(loc_ser_frame, text = "Trending  searches ", font = ('GodofThunder', 20), bg = '#FFD700', fg = 'dark green')
#search_info_label.grid(row=6,column=0)


loc_ser_btn = Button(loc_ser_frame, text = "SEARCH", font = ('Iron Blade', 30), bg = '#68FE00', cursor = 'hand2', command = search_new_window)
loc_ser_btn.grid(row=7,column=1, sticky = 'w', pady = 50)

loc_ser_btn2 = Button(loc_ser_frame, text = "View All Restaurants", font = ('Iron Blade', 30), bg = 'cyan', cursor = 'hand2', command = search_new_window_2)
loc_ser_btn2.grid(row=8,column=1, sticky = 'w')

switch = Button(second_frame, text = "Toggle FullScreen - ON/OFF", bg = 'black', fg = 'white', font = ('Iron Blade', 20), cursor = 'hand2', command = toggle)
#switch.place(x=475, y=42.5)


login_btn = Button(second_frame, text = "LOGIN", bg = 'black', fg = 'white', font = ("Iron Blade", 30), cursor = 'hand2', command = login)
login_btn.place(x=900,y=30)

signup_btn = Button(second_frame, text = "Sign Up", bg = 'black', fg = 'white', font = ("Iron Blade", 30), cursor = 'hand2', command = sign_up)
signup_btn.place(x=1100,y=30)

admin_btn = Button(second_frame, text = "Administrator", bg = 'black', fg = 'white', font = ('Iron Blade', 30), cursor = 'hand2', command = admin)
admin_btn.place(x=40,y=575)

#add_btn = Button(second_frame, text = "Add Restaurant", bg = 'black', fg = 'white', font = ('Iron Blade', 30), cursor = 'hand2', command = add)
#add_btn.place(x=910,y=575)


#==============================#


def update(data):
    blr_listbox.delete(0, END)
    
    for item in data:
        blr_listbox.insert(END, item)

def fillout(e):
    loc_area_e.delete(0, END)

    loc_area_e.insert(0, blr_listbox.get(ACTIVE))

def check(e):
    global i_s
    typed = loc_area_e.get()

    if typed == '':
        data = locality_list
    else:
        data = []
        for item in locality_list:
            if typed.lower() in item.lower():
                data.append(item)
            
        if len(data) == 0:
            i_s = ["Not found"]
            i_s_2 = ["We don't deliver here"]
            l_s_3 = ["Type something else"]
            data.append(i_s)
            data.append(i_s_2)
            data.append(l_s_3)
                
    update(data)


blr_listbox = Listbox(frame_y, width = 23, bg = 'black', font = ('Courier New', 20, 'bold'), fg = 'cyan')
blr_listbox.grid(row = 1, column = 0, sticky = 'w')

#====================#

mycony = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
mycury = mycony.cursor(buffered = True)

mycury.execute('select distinct area from restaurants')
food_tup3 = mycury.fetchall()

mycony.close()

locality_list = []

for dict_var in food_tup3:
    locality_list.append(dict_var[0])


#====================#

update(locality_list)

blr_listbox.bind("<<ListboxSelect>>", fillout)

loc_area_e.bind("<KeyRelease>", check)



#============================================================================


def update_2(data):
    gen_listbox.delete(0, END)
    
    for item in data:
        gen_listbox.insert(END, item)

def fillout_2(e):
    search.delete(0, END)

    search.insert(0, gen_listbox.get(ACTIVE))

def check_2(e):
    typed = search.get()

    if typed == '':
        data = food_list
    else:
        data = []
        for item in food_list:
            if typed.lower() in item.lower():
                data.append(item)

        if len(data) == 0:
            hhh = ['Search anything']
            data.append(hhh)
                
    update_2(data)


gen_listbox = Listbox(frame_x, width = 17, bg = 'black', font = ('Courier New', 20, 'bold'), fg = 'yellow')
gen_listbox.grid(row = 1, column = 0, sticky = 'w')

#====================#

myconx = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
mycurx = myconx.cursor(buffered = True)

mycurx.execute('select distinct name from restaurants')
food_tup1 = mycurx.fetchall()
mycurx.execute('select distinct type from restaurants')
food_tup2 = mycurx.fetchall()

myconx.close()

food_list = []

for tup_var1 in food_tup1:
    food_list.append(tup_var1[0])

for tup_var2 in food_tup2:
    food_list.append(tup_var2[0])

#====================#

update_2(food_list)

gen_listbox.bind("<<ListboxSelect>>", fillout_2)

search.bind("<KeyRelease>", check_2)





root.mainloop()


