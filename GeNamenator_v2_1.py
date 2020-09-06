from tkinter import *
import sqlite3
import random
from PIL import ImageTk, Image

root = Tk()
root.configure(bg="#66cc99")
root.geometry("1000x510")
root.maxsize(1000, 510)
root.title("GeNamenator v 1.41")
root.iconbitmap(r"D:\Users\drmargis\Python Projects\Tkinter\Groucho_Icon.ico")

conn = sqlite3.connect(r'D:\Users\drmargis\Python Projects\Projects\GeNamenator\GeName_DB_2.db')
curs = conn.cursor()
curs.row_factory = lambda cursor, row: row[0]


# Logo

logo_img = ImageTk.PhotoImage(Image.open(r"D:\Users\drmargis\Python Projects\Projects\GeNamenator\GNLogo.png"))
logo_label = Label(image=logo_img, padx=15, pady=15, relief=RIDGE)
logo_label.grid(row=5, column=0, columnspan=4, sticky=W)


# Global Name Choice Variables

gender = StringVar()
gender.set("Any")

allit = StringVar()
allit.set("AllitOff")

middle = StringVar()
middle.set("MidOff")

decade = StringVar()
decade.set("")
dec_list =["", "1880s", "1890s", "1900s", "1910s", "1920s", "1930s", "1940s", "1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]

chk_topten = StringVar()
chk_topten.set("Off")
chk_mostcommon = StringVar()
chk_mostcommon.set("Off")
chk_common = StringVar()
chk_common.set("Off")
chk_lesscommon = StringVar()
chk_lesscommon.set("Off")
chk_rare = StringVar()
chk_rare.set("Off")
chk_exrare = StringVar()
chk_exrare.set("Off")
commonality = StringVar()
commonality.set("")

name_starts = ("A", "B", "C", "Ch", "D", "E", "F", "G", "Gr", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
               "S", "Sh", "St", "T", "Th", "U", "V", "W", "X", "Y", "Z")

global allit_begin


# Birth Decade Commonality

def decade_choice():
    global deccom_list
    dec = decade.get()
    topten = chk_topten.get()
    mostcommon = chk_mostcommon.get()
    common = chk_common.get()
    lesscommon = chk_lesscommon.get()
    rare = chk_rare.get()
    exrare = chk_exrare.get()
    deccom_list = [topten, mostcommon, common, lesscommon, rare, exrare]
    deccom_list = tuple(deccom_list)
    deccom_list = str(deccom_list)

# Inteior Name Functions

def create_first_name(gend_choice):
    global first_name
    global fn_pull
    global allit_end_string
    global dec
    global dec_string
    allitt_choice = allit.get()
    allit_input = allit_begin.get()
    dec = decade.get()
    dec_string = "\"" + dec + "\""
    if allit_input == "" or allit_input == "*:":
        rand_allit = random.choice(name_starts)
        allit_end_string = rand_allit + "%"
    else:
        allit_end_string = allit_input + "%"
    if allitt_choice == "AllitOff" and dec == "":
        curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) """, (gend_choice,))
        fn_pull = curs.fetchall()
        first_name = random.choice(fn_pull)
    elif allitt_choice == "AllitOff" and dec != "":
        decade_choice()
        curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND """ + dec_string + """ IN """ + deccom_list, (gend_choice,))
        fn_pull = curs.fetchall()
        first_name = random.choice(fn_pull)
    elif allitt_choice == "AllitOn" and dec == "":
        curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?)""", (gend_choice, allit_end_string))
        fn_pull = curs.fetchall()
        first_name = random.choice(fn_pull)
    elif allitt_choice == "AllitOn" and dec != "":
        decade_choice()
        curs.execute(
            """ SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?) AND """ + dec_string + """ IN """ + deccom_list,
            (gend_choice, allit_end_string))
        fn_pull = curs.fetchall()
        first_name = random.choice(fn_pull)


def create_middle_name(gend_choice):
    global mid_name
    global mid_pull
    global dec
    global dec_string
    allitt_choice = allit.get()
    dec = decade.get()
    if allitt_choice == "AllitOff" and dec == "":
        while True:
            curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) """, (gend_choice,))
            mid_pull = curs.fetchall()
            mid_name = random.choice(mid_pull)
            if mid_name != first_name:
                break
    elif allitt_choice == "AllitOff" and dec != "":
        while True:
            curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND """ + dec_string + """ IN """ + deccom_list, (gend_choice,))
            mid_pull = curs.fetchall()
            mid_name = random.choice(fn_pull)
            if mid_name != first_name:
                break
    elif allitt_choice == "AllitOn" and dec == "":
        while True:
            curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?)""", (gend_choice, allit_end_string))
            mid_pull = curs.fetchall()
            mid_name = random.choice(fn_pull)
            if mid_name != first_name:
                break
    elif allitt_choice == "AllitOn" and dec != "":
        while True:
            curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?) AND """ + dec_string + """ IN """ + deccom_list,
                (gend_choice, allit_end_string))
            mid_pull = curs.fetchall()
            mid_name = random.choice(fn_pull)
            if mid_name != first_name:
                break

def create_last_name():
    global last_name
    global ln_pull
    allitt_choice = allit.get()
    if allitt_choice == "AllitOff":
        curs.execute(""" SELECT last_name FROM last_names """)
        ln_pull = curs.fetchall()
        last_name = random.choice(ln_pull)
    else:
        curs.execute(""" SELECT last_name FROM last_names WHERE last_name LIKE (?)""", (allit_end_string,))
        ln_pull = curs.fetchall()
        last_name = random.choice(ln_pull)


def create_description():
    curs.execute(""" SELECT adjective FROM adjectives """)
    adj_pull = curs.fetchall()
    adject = random.choice(adj_pull)
    curs.execute(""" SELECT noun FROM nouns """)
    noun_pull = curs.fetchall()
    noun = random.choice(noun_pull)
    desc_output['text'] = ("The" + " " + adject + " " + noun)


# Create Name Functions

def create_random():
    randchoice = random.randrange(1, 42)
    if 1 <= randchoice <= 10:
        create_first_name('Female')
        create_last_name()
        name_output['text'] = (first_name + " " + last_name)
        create_description()
    elif 11 <= randchoice <= 20:
        create_first_name('Female')
        create_middle_name('Female')
        create_last_name()
        name_output['text'] = (first_name + " " + mid_name + " " + last_name)
        create_description()
    elif 21 <= randchoice <= 30:
        create_first_name('Male')
        create_last_name()
        name_output['text'] = (first_name + " " + last_name)
        create_description()
    elif 31 <= randchoice <= 40:
        create_first_name('Male')
        create_middle_name('Male')
        create_last_name()
        name_output['text'] = (first_name + " " + mid_name + " " + last_name)
        create_description()
    elif randchoice == 41:
        create_first_name('Female')
        create_last_name()
        while True:
            last_name_hyp = random.choice(ln_pull)
            if last_name_hyp != last_name:
                break
        name_output['text'] = (first_name + " " + last_name + "-" + last_name_hyp)
        create_description()
    elif randchoice == 42:
        create_first_name('Male')
        create_last_name()
        while True:
            last_name_hyp = random.choice(ln_pull)
            if last_name_hyp != last_name:
                break
        name_output['text'] = (first_name + " " + last_name + "-" + last_name_hyp)
        create_description()


def create_name():
    global gender
    gender.get()
    middle.get()
    choices = middle.get()
    randchoice = random.randrange(1, 10)
    if gender.get() != "Any":
        any_gend = gender.get()
    else:
        if randchoice >= 5:
            any_gend = "Female"
        else:
            any_gend = "Male"
    if choices == "MidOff":
        create_first_name(any_gend)
        create_last_name()
        name_output['text'] = (first_name + " " + last_name)
        create_description()
    elif choices == "MidOn":
        create_first_name(any_gend)
        create_middle_name(any_gend)
        create_last_name()
        name_output['text'] = (first_name + " " + mid_name + " " + last_name)
        create_description()
    elif choices == "MidLastOn":
        create_first_name(any_gend)
        create_last_name()
        while True:
            mid_name_last = random.choice(ln_pull)
            if mid_name_last != last_name:
                break
        name_output['text'] = (first_name + " " + last_name + " " + mid_name_last)
        create_description()



# Output 1 and 2

name_output = Label(root, font=("Calibri", 27), width=30, text="", borderwidth=4, relief=RAISED)
name_output.grid(row=0, column=0, columnspan=2)

desc_output = Label(root,  font=("Calibri", 27), width=30, text="", borderwidth=4, relief=RAISED)
desc_output.grid(row=1, column=0, columnspan=2)


# Create Buttons

but_padx = 40
but_pady = 30
rando_button = Button(root, font=("Calibri", 20), text="Create\nRandom", padx=but_padx, pady=but_pady, bg="#66cc00", activebackground="#0b5345", command=create_random)
rando_button.grid(row=2, column=0)
crit_button = Button(root, font=("Calibri", 20), text="Create by\nCriteria", padx=but_padx, pady=but_pady, bg="#66cc00", activebackground="#0b5345", command=create_name)
crit_button.grid(row=2, column=1)


# Female/Male Options

def gender_func():
    gender.get()

f_m_frame = LabelFrame(root, font=("Calibri", 15), width=20, borderwidth=2, background="#66cc33", relief=RIDGE)
f_m_frame.grid(row=0, column=2, rowspan=2)
f_m_label = Label(f_m_frame, text="Gender", font=("Calibri", 15), bg="#66cc33")
f_m_label.grid(row=0, column=0, columnspan=2)
f_radio = Radiobutton(f_m_frame, font=("Calibri", 13), text="Female", padx=5, variable=gender, value="Female", bg="#66cc33")
f_radio.grid(row=1, column=0, sticky=W)
m_radio = Radiobutton(f_m_frame, font=("Calibri", 13), text="Male", padx=5, variable=gender, value="Male", bg="#66cc33")
m_radio.grid(row=2, column=0, sticky=W)
a_radio = Radiobutton(f_m_frame, font=("Calibri", 13), text="Any", padx=5, variable=gender, value="Any", bg="#66cc33")
a_radio.grid(row=3, column=0, sticky=W)


# Alliterative Options

def allit_func():
    pass

allit_frame = LabelFrame(root, font=("Calibri", 15), width=30, borderwidth=2, relief=RIDGE, background="#66cc33")
allit_frame.grid(row=0, column=3)
allit_label = Label(allit_frame, font=("Calibri", 15), text="Alliteration", bg="#66cc33")
allit_label.grid(row=0, column=0, columnspan=2)
allit_button = Checkbutton(allit_frame, padx=5, variable=allit, onvalue="AllitOn", offvalue="AllitOff", bg="#66cc33")
allit_button.grid(row=1, column=0)
allit_check_label = Label(allit_frame, font=("Calibri", 13), text="Alliterative Name", bg="#66cc33")
allit_check_label.grid(row=1, column=1, sticky=W)
allit_begin = Entry(allit_frame, font=("Calibri", 13), width=3, borderwidth=5)
allit_begin.grid(row=2, column=0)
allit_label = Label(allit_frame, font=("Calibri", 13), text="Name starts with", bg="#66cc33")
allit_label.grid(row=2, column=1, sticky=W)


# Middle Name Options

def midname_func():
    pass

middle_frame = LabelFrame(root, font=("Calibri", 15), width=30, borderwidth=2, relief=RIDGE, background="#66cc33")
middle_frame.grid(row=2, column=2)
middle_label = Label(middle_frame, font=("Calibri", 15), text="Middle Name", bg="#66cc33")
middle_label.grid(row=0, column=0, columnspan=2)
middle_check = Checkbutton(middle_frame, padx=5, variable=middle, onvalue="MidOn", offvalue="MidOff", bg="#66cc33")
middle_check.grid(row=1, column=0)
middle_check_label = Label(middle_frame, font=("Calibri", 13), text="Middle Name", bg="#66cc33")
middle_check_label.grid(row=1, column=1, sticky=W)
midlast_check = Checkbutton(middle_frame, padx=5, variable=middle, onvalue="MidLastOn", offvalue="MidOff", bg="#66cc33")
midlast_check.grid(row=2, column=0)
midlast_check_label = Label(middle_frame, font=("Calibri", 13), text="Last Name for Middle Name", bg="#66cc33")
midlast_check_label.grid(row=2, column=1, sticky=W)


# Decade and Commonality Options

def decade_common():
    pass

decade_frame = LabelFrame(root, font=("Calibri", 15), width=50, borderwidth=2, relief=RIDGE, background="#66cc33")
decade_frame.grid(row=1, column=3, rowspan=2)
decade_label = Label(decade_frame, font=("Calibri", 15), text="Birth Decade", bg="#66cc33")
decade_label.grid(row=0, column=0, columnspan=2)
decade_menu = OptionMenu(decade_frame, decade, *dec_list)
decade_menu.grid(row=1, column=1)
decade_menu_label = Label(decade_frame, font=("Calibri", 13), text="Decade", bg="#66cc33")
decade_menu_label.grid(row=1, column=0)
commonality_label = Label(decade_frame, font=("Calibri", 15), text="Commonality", bg="#66cc33")
commonality_label.grid(row=2, column=0, columnspan=2)

topten = Checkbutton(decade_frame, variable=chk_topten, onvalue="Top Ten", offvalue="Off", bg="#66cc33")
topten.grid(row=3, column=0)
topten_label = Label(decade_frame, font=("Calibri", 13), text="Top Ten", bg="#66cc33")
topten_label.grid(row=3, column=1, sticky=W)

mostcommon = Checkbutton(decade_frame, variable=chk_mostcommon, onvalue="Most Common", offvalue="Off", bg="#66cc33")
mostcommon.grid(row=4, column=0)
mostcommon_label = Label(decade_frame, font=("Calibri", 13), text="Most Common", bg="#66cc33")
mostcommon_label.grid(row=4, column=1, sticky=W)

common = Checkbutton(decade_frame, variable=chk_common, onvalue="Common", offvalue="Off", bg="#66cc33")
common.grid(row=5, column=0)
common_label = Label(decade_frame, font=("Calibri", 13), text="Common", bg="#66cc33")
common_label.grid(row=5, column=1, sticky=W)

lesscommon = Checkbutton(decade_frame, variable=chk_lesscommon, onvalue="Less Common", offvalue="Off", bg="#66cc33")
lesscommon.grid(row=6, column=0)
lesscommon_label = Label(decade_frame, font=("Calibri", 13), text="Less Common", bg="#66cc33")
lesscommon_label.grid(row=6, column=1, sticky=W)

rare = Checkbutton(decade_frame, variable=chk_rare, onvalue="Rare", offvalue="Off", bg="#66cc33")
rare.grid(row=7, column=0)
rare_label = Label(decade_frame, font=("Calibri", 13), text="Rare", bg="#66cc33")
rare_label.grid(row=7, column=1, sticky=W)

exrare = Checkbutton(decade_frame, variable=chk_exrare, onvalue="Extremely Rare", offvalue="Off", bg="#66cc33")
exrare.grid(row=8, column=0)
exrare_label = Label(decade_frame, font=("Calibri", 13), text="Extremely Rare", bg="#66cc33")
exrare_label.grid(row=8, column=1, sticky=W)



root.mainloop()