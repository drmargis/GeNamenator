from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import sqlite3
import random
from PIL import ImageTk, Image

root = Tk()
root.geometry("1020x600")
root.maxsize(1020, 600)
root.title("GeNamenator v 2.22")
root.iconbitmap('Groucho_Icon.ico')

conn = sqlite3.connect('GeName_DB_2.db')
curs = conn.cursor()

# Logo

logo_img = ImageTk.PhotoImage(Image.open('GNLogo_2_2.png'))
logo_label = Label(image=logo_img, padx=15, pady=15, relief=RIDGE)
logo_label.grid(row=5, column=0, columnspan=4, rowspan=2, sticky=W+N)


# Theme Options

curs.execute(""" SELECT * FROM themes """)
theme_list = curs.fetchone()
main_bg = theme_list[1]
button_bg = theme_list[2]
button_act_bg = theme_list[3]
frame_bg = theme_list[4]
text_color = theme_list[5]
entry_bg = theme_list[6]


def theme_green():
    main_bg = "#66cc99"
    button_bg = "#66cc00"
    button_act_bg = "#0b5345"
    frame_bg = "#66cc33"
    text_color = "#000000"
    entry_bg = "#ffffff"
    curs.execute(""" UPDATE themes SET main_bg=(?), button_bg=(?), button_act_bg=(?), frame_bg=(?), text_color=(?), entry_bg=(?) WHERE thm_id=1""",
                 (main_bg, button_bg, button_act_bg, frame_bg, text_color, entry_bg,))
    conn.commit()


def theme_red():
    main_bg = "#c2240b"
    button_bg = "#ae1f1f"
    button_act_bg = "#5d0909"
    frame_bg = "#c13323"
    text_color = "#000000"
    entry_bg = "#ffffff"
    curs.execute(""" UPDATE themes SET main_bg=(?), button_bg=(?), button_act_bg=(?), frame_bg=(?), text_color=(?), entry_bg=(?) WHERE thm_id=1""",
                 (main_bg, button_bg, button_act_bg, frame_bg, text_color, entry_bg,))
    conn.commit()


def theme_blue():
    main_bg = "#68d7ee"
    button_bg = "#1db8de"
    button_act_bg = "#11697e"
    frame_bg = "#3c8afa"
    text_color = "#000000"
    entry_bg = "#ffffff"
    curs.execute(""" UPDATE themes SET main_bg=(?), button_bg=(?), button_act_bg=(?), frame_bg=(?), text_color=(?), entry_bg=(?) WHERE thm_id=1""",
                 (main_bg, button_bg, button_act_bg, frame_bg, text_color, entry_bg,))
    conn.commit()


def theme_purple():
    main_bg = "#c972f7"
    button_bg = "#983dc8"
    button_act_bg = "#441a5a"
    frame_bg = "#ac5ed5"
    text_color = "#000000"
    entry_bg = "#ffffff"
    curs.execute(""" UPDATE themes SET main_bg=(?), button_bg=(?), button_act_bg=(?), frame_bg=(?), text_color=(?), entry_bg=(?) WHERE thm_id=1""",
                 (main_bg, button_bg, button_act_bg, frame_bg, text_color, entry_bg,))
    conn.commit()


def theme_gray():
    main_bg = "#737373"
    button_bg = "#cdcdcd"
    button_act_bg = "#666666"
    frame_bg = "#e7e7e7"
    text_color = "#000000"
    entry_bg = "#ffffff"
    curs.execute(""" UPDATE themes SET main_bg=(?), button_bg=(?), button_act_bg=(?), frame_bg=(?), text_color=(?), entry_bg=(?) WHERE thm_id=1""",
                 (main_bg, button_bg, button_act_bg, frame_bg, text_color, entry_bg,))
    conn.commit()


def theme_dos():
    main_bg = "#000000"
    button_bg = "#262626"
    button_act_bg = "#000000"
    frame_bg = "#222222"
    text_color = "#55ff00"
    entry_bg = "#000000"
    curs.execute(""" UPDATE themes SET main_bg=(?), button_bg=(?), button_act_bg=(?), frame_bg=(?), text_color=(?), entry_bg=(?) WHERE thm_id=1""",
                 (main_bg, button_bg, button_act_bg, frame_bg, text_color, entry_bg,))
    conn.commit()

# Theme Buttons

theme_frame = LabelFrame(root, font=("Calibri", 12), width=30, borderwidth=2, relief=RIDGE, fg=text_color, background=frame_bg)
theme_frame.grid(row=10, column=0, columnspan=6, sticky=W+N)

green_but = Button(theme_frame, text="Green Theme", padx=5, borderwidth=3, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, command=theme_green)
green_but.grid(row=0, column=0, sticky=W)

red_but = Button(theme_frame, text="Red Theme", padx=5, borderwidth=3, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, command=theme_red)
red_but.grid(row=0, column=1, sticky=W)

blue_but = Button(theme_frame, text="Blue Theme", padx=5, borderwidth=3, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, command=theme_blue)
blue_but.grid(row=0, column=2, sticky=W)

purple_but = Button(theme_frame, text="Purple Theme", padx=5, borderwidth=3, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, command=theme_purple)
purple_but.grid(row=0, column=3, sticky=W)

gray_but = Button(theme_frame, text="Gray Theme", padx=5, borderwidth=3, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, command=theme_gray)
gray_but.grid(row=0, column=4, sticky=W)

dos_but = Button(theme_frame, text="DOS Theme", padx=5, borderwidth=3, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, command=theme_dos)
dos_but.grid(row=0, column=5, sticky=W)


root.configure(bg=main_bg)

# Allows names to be selected as items from the query lists

curs.row_factory = lambda cursor, row: row[0]

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
chk_topten.set("Top Ten")
chk_mostcommon = StringVar()
chk_mostcommon.set("Most Common")
chk_common = StringVar()
chk_common.set("Common")
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


# Error Messages

def index_error_popup():
    messagebox.showerror(title="INDEX ERROR", message="Not enough names in the database match that criteria.\n"
                     "Please change the alliteration settings\n"
                     "or expand the decade and commonality settings.")


def commonality_error():
    messagebox.showerror(title="INDEX ERROR", message="Please add commonality criteria.")


# Birth Decade Commonality

def decade_choice():
    global deccom_list
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
        try:
            decade_choice()
            curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND """ + dec_string + """ IN """ + deccom_list, (gend_choice,))
            fn_pull = curs.fetchall()
            first_name = random.choice(fn_pull)
        except IndexError:
            commonality_error()
    elif allitt_choice == "AllitOn" and dec == "":
        try:
            curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?)""", (gend_choice, allit_end_string))
            fn_pull = curs.fetchall()
            first_name = random.choice(fn_pull)
        except IndexError:
            index_error_popup()
    elif allitt_choice == "AllitOn" and dec != "":
        try:
            decade_choice()
            curs.execute(
                """ SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?) AND """ + dec_string + """ IN """ + deccom_list,
                (gend_choice, allit_end_string))
            fn_pull = curs.fetchall()
            first_name = random.choice(fn_pull)
        except IndexError:
            index_error_popup()


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
        try:
            while True:
                curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?)""", (gend_choice, allit_end_string))
                mid_pull = curs.fetchall()
                mid_name = random.choice(fn_pull)
                if mid_name != first_name:
                    break
        except IndexError:
            index_error_popup()
    elif allitt_choice == "AllitOn" and dec != "":
        try:
            while True:
                curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?) AND """ + dec_string + """ IN """ + deccom_list,
                    (gend_choice, allit_end_string))
                mid_pull = curs.fetchall()
                mid_name = random.choice(fn_pull)
                if mid_name != first_name:
                    break
        except IndexError:
            index_error_popup()


def create_last_name():
    global last_name
    global ln_pull
    allitt_choice = allit.get()
    if allitt_choice == "AllitOff":
        curs.execute(""" SELECT last_name FROM last_names """)
        ln_pull = curs.fetchall()
        last_name = random.choice(ln_pull)
    else:
        try:
            curs.execute(""" SELECT last_name FROM last_names WHERE last_name LIKE (?)""", (allit_end_string,))
            ln_pull = curs.fetchall()
            last_name = random.choice(ln_pull)
        except IndexError:
            index_error_popup()


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

name_output = Label(root, font=("Calibri", 27), fg=text_color, bg=entry_bg, width=30, text="", borderwidth=5, relief=RAISED)
name_output.grid(row=0, column=0, columnspan=2)

desc_output = Label(root,  font=("Calibri", 27), fg=text_color, bg=entry_bg, width=30, text="", borderwidth=5, relief=RAISED)
desc_output.grid(row=1, column=0, columnspan=2)


# Create Buttons

but_padx = 40
but_pady = 30
rando_button = Button(root, font=("Calibri", 30, 'bold'), text="Create\nRandom", padx=but_padx, pady=but_pady, borderwidth=5, bg=button_bg, activebackground=button_act_bg, fg=text_color, relief=RAISED, command=create_random)
rando_button.grid(row=2, column=0, sticky=N+S+E+W)
crit_button = Button(root, font=("Calibri", 30, 'bold'), text="Create by\nCriteria", padx=but_padx, pady=but_pady, borderwidth=5, bg=button_bg, activebackground=button_act_bg, fg=text_color, relief=RAISED, command=create_name)
crit_button.grid(row=2, column=1, sticky=N+S+E+W)


# Female/Male Options

f_m_frame = LabelFrame(root, font=("Calibri", 15), width=20, borderwidth=2, fg=text_color, background=frame_bg, relief=RIDGE)
f_m_frame.grid(row=0, column=2, rowspan=2)
f_m_label = Label(f_m_frame, text="Gender", font=("Calibri", 15), fg=text_color, bg=frame_bg)
f_m_label.grid(row=0, column=0, columnspan=2)
f_radio = Radiobutton(f_m_frame, font=("Calibri", 13), text="Female", padx=5, variable=gender, value="Female", fg=text_color, bg=frame_bg)
f_radio.grid(row=1, column=0, sticky=W)
m_radio = Radiobutton(f_m_frame, font=("Calibri", 13), text="Male", padx=5, variable=gender, value="Male", fg=text_color, bg=frame_bg)
m_radio.grid(row=2, column=0, sticky=W)
a_radio = Radiobutton(f_m_frame, font=("Calibri", 13), text="Any", padx=5, variable=gender, value="Any", fg=text_color, bg=frame_bg)
a_radio.grid(row=3, column=0, sticky=W)


# Alliterative Options

allit_frame = LabelFrame(root, font=("Calibri", 15), width=30, borderwidth=2, relief=RIDGE, background=frame_bg, fg=text_color)
allit_frame.grid(row=0, column=3)
allit_label = Label(allit_frame, font=("Calibri", 15), text="Alliteration", fg=text_color, bg=frame_bg)
allit_label.grid(row=0, column=0, columnspan=2)
allit_button = Checkbutton(allit_frame, padx=5, variable=allit, onvalue="AllitOn", offvalue="AllitOff", bg=frame_bg)
allit_button.grid(row=1, column=0)
allit_check_label = Label(allit_frame, font=("Calibri", 13), text="Alliterative Name", fg=text_color, bg=frame_bg)
allit_check_label.grid(row=1, column=1, sticky=W)
allit_begin = Entry(allit_frame, font=("Calibri", 13), width=3, borderwidth=5)
allit_begin.grid(row=2, column=0)
allit_label = Label(allit_frame, font=("Calibri", 13), text="Name starts with", fg=text_color, bg=frame_bg)
allit_label.grid(row=2, column=1, sticky=W)


# Middle Name Options

middle_frame = LabelFrame(root, font=("Calibri", 15), width=30, borderwidth=2, relief=RIDGE, fg=text_color, background=frame_bg)
middle_frame.grid(row=2, column=2)
middle_label = Label(middle_frame, font=("Calibri", 15), text="Middle Name", fg=text_color, bg=frame_bg)
middle_label.grid(row=0, column=0, columnspan=2)
middle_check = Checkbutton(middle_frame, padx=5, variable=middle, onvalue="MidOn", offvalue="MidOff", bg=frame_bg)
middle_check.grid(row=1, column=0)
middle_check_label = Label(middle_frame, font=("Calibri", 13), text="Middle Name", fg=text_color, bg=frame_bg)
middle_check_label.grid(row=1, column=1, sticky=W)
midlast_check = Checkbutton(middle_frame, padx=5, variable=middle, onvalue="MidLastOn", offvalue="MidOff", bg=frame_bg)
midlast_check.grid(row=2, column=0)
midlast_check_label = Label(middle_frame, font=("Calibri", 13), text="Last Name for Middle Name", fg=text_color, bg=frame_bg)
midlast_check_label.grid(row=2, column=1, sticky=W)


# Decade and Commonality Options

decade_frame = LabelFrame(root, font=("Calibri", 15), width=50, borderwidth=2, relief=RIDGE, fg=text_color, background=frame_bg)
decade_frame.grid(row=1, column=3, rowspan=2)
decade_label = Label(decade_frame, font=("Calibri", 15), text="Birth Decade", fg=text_color, bg=frame_bg)
decade_label.grid(row=0, column=0, columnspan=2)
decade_menu = OptionMenu(decade_frame, decade, *dec_list)
decade_menu.grid(row=1, column=1)
decade_menu_label = Label(decade_frame, font=("Calibri", 13), text="Decade", fg=text_color, bg=frame_bg)
decade_menu_label.grid(row=1, column=0)
commonality_label = Label(decade_frame, font=("Calibri", 15), text="Commonality", fg=text_color, bg=frame_bg)
commonality_label.grid(row=2, column=0, columnspan=2)

topten = Checkbutton(decade_frame, variable=chk_topten, onvalue="Top Ten", offvalue="Off", bg=frame_bg)
topten.grid(row=3, column=0)
topten_label = Label(decade_frame, font=("Calibri", 13), text="Top Ten", fg=text_color, bg=frame_bg)
topten_label.grid(row=3, column=1, sticky=W)

mostcommon = Checkbutton(decade_frame, variable=chk_mostcommon, onvalue="Most Common", offvalue="Off", bg=frame_bg)
mostcommon.grid(row=4, column=0)
mostcommon_label = Label(decade_frame, font=("Calibri", 13), text="Most Common", fg=text_color, bg=frame_bg)
mostcommon_label.grid(row=4, column=1, sticky=W)

common = Checkbutton(decade_frame, variable=chk_common, onvalue="Common", offvalue="Off", bg=frame_bg)
common.grid(row=5, column=0)
common_label = Label(decade_frame, font=("Calibri", 13), text="Common", fg=text_color, bg=frame_bg)
common_label.grid(row=5, column=1, sticky=W)

lesscommon = Checkbutton(decade_frame, variable=chk_lesscommon, onvalue="Less Common", offvalue="Off", bg=frame_bg)
lesscommon.grid(row=6, column=0)
lesscommon_label = Label(decade_frame, font=("Calibri", 13), text="Less Common", fg=text_color, bg=frame_bg)
lesscommon_label.grid(row=6, column=1, sticky=W)

rare = Checkbutton(decade_frame, variable=chk_rare, onvalue="Rare", offvalue="Off", bg=frame_bg)
rare.grid(row=7, column=0)
rare_label = Label(decade_frame, font=("Calibri", 13), text="Rare", fg=text_color, bg=frame_bg)
rare_label.grid(row=7, column=1, sticky=W)

exrare = Checkbutton(decade_frame, variable=chk_exrare, onvalue="Extremely Rare", offvalue="Off", bg=frame_bg)
exrare.grid(row=8, column=0)
exrare_label = Label(decade_frame, font=("Calibri", 13), text="Extremely Rare", fg=text_color, bg=frame_bg)
exrare_label.grid(row=8, column=1, sticky=W)


# Clear Options

def clear():
    gender.set("Any")
    allit.set("AllitOff")
    allit_begin.delete(0, END)
    allit_begin.insert(0, "")
    middle.set("MidOff")
    decade.set("")
    chk_topten.set("Top Ten")
    chk_mostcommon.set("Most Common")
    chk_common.set("Common")
    chk_lesscommon.set("Off")
    chk_rare.set("Off")
    chk_exrare.set("Off")
    commonality.set("")
    name_output['text'] = ""
    desc_output['text'] = ""


clear_all = Button(root, font=("Calibri", 23, 'bold'), text="Clear", padx=25, pady=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, command=clear)
clear_all.grid(row=5, column=3, sticky=N+S+E+W)


# Database Management Module

def database():
    dbwin = Tk()
    dbwin.geometry("890x670")
    dbwin.maxsize(890, 670)
    dbwin.iconbitmap('Groucho_Icon.ico')

    dbwin.title("GeNamenator Database Manager")

    conn = sqlite3.connect('GeName_DB_2.db')
    curs = conn.cursor()

    # Database Window Theme
    curs.execute(""" SELECT * FROM themes """)

    theme_list = curs.fetchone()
    main_bg = theme_list[1]
    button_bg = theme_list[2]
    button_act_bg = theme_list[3]
    frame_bg = theme_list[4]
    text_color = theme_list[5]
    entry_bg = theme_list[6]

    dbwin.configure(bg=main_bg)

    # Search Functions
    def fn_search():
        fn_edit.delete(0, END)
        gender_edit.delete(0, END)
        d1880s_edit.delete(0, END)
        d1890s_edit.delete(0, END)
        d1900s_edit.delete(0, END)
        d1910s_edit.delete(0, END)
        d1920s_edit.delete(0, END)
        d1930s_edit.delete(0, END)
        d1940s_edit.delete(0, END)
        d1950s_edit.delete(0, END)
        d1960s_edit.delete(0, END)
        d1970s_edit.delete(0, END)
        d1980s_edit.delete(0, END)
        d1990s_edit.delete(0, END)
        d2000s_edit.delete(0, END)
        d2010s_edit.delete(0, END)
        fn = fn_getbox.get()
        curs.execute(""" SELECT COUNT (first_name) FROM first_names WHERE first_name = (?)  """, (fn,))
        fn_count = curs.fetchall()
        if fn_count[0][0] == 2:
            fm_choice = messagebox.askyesno(title="Two Names Found",
                                            message="That name exists as both female and male.\nChoose yes to retrieve the female name and no to retrieve male.")
            if fm_choice:
                curs.execute(""" SELECT * FROM first_names WHERE first_name = (?) AND gender="Female" """, (fn,))
                fn_sql = curs.fetchone()
            else:
                curs.execute(""" SELECT * FROM first_names WHERE first_name = (?) AND gender="Male" """, (fn,))
                fn_sql = curs.fetchone()
        else:
            curs.execute(""" SELECT * FROM first_names WHERE first_name = (?) """, (fn,))
            fn_sql = curs.fetchone()
        try:
            fn_edit.insert(0, fn_sql[1])
            gender_edit.insert(0, fn_sql[2])
            d1880s_edit.insert(0, fn_sql[3])
            d1890s_edit.insert(0, fn_sql[4])
            d1900s_edit.insert(0, fn_sql[5])
            d1910s_edit.insert(0, fn_sql[6])
            d1920s_edit.insert(0, fn_sql[7])
            d1930s_edit.insert(0, fn_sql[8])
            d1940s_edit.insert(0, fn_sql[9])
            d1950s_edit.insert(0, fn_sql[10])
            d1960s_edit.insert(0, fn_sql[11])
            d1970s_edit.insert(0, fn_sql[12])
            d1980s_edit.insert(0, fn_sql[13])
            d1990s_edit.insert(0, fn_sql[14])
            d2000s_edit.insert(0, fn_sql[15])
            d2010s_edit.insert(0, fn_sql[16])
        except TypeError:
            messagebox.showerror(title="Name does not exist", message=fn + " is not in the database.")

    def fn_submit():
        name = fn_edit.get()
        gend = gender_edit.get()
        # Checks if a name with that gender is already in the database
        curs.execute(""" SELECT first_name, gender FROM first_names WHERE first_name=(?) AND gender = (?) """,
                     (name, gend))
        dupe_check_result = curs.fetchone()
        if name == "":
            messagebox.showerror(title="Fields Blank", message="Please fill out fields before submitting")
        elif not dupe_check_result:
            curs.execute(
                """ INSERT INTO first_names VALUES (:fn_id, :first_name, :gender, :1880s, :1890s, :1900s, :1910s, :1920s, :1930s, :1940s, :1950s, :1960s, :1970s, :1980s, :1990s, :2000s, :2010s)""",
                {
                    'fn_id': None,
                    'first_name': fn_edit.get(),
                    'gender': gender_edit.get(),
                    '1880s': d1880s_edit.get(),
                    '1890s': d1890s_edit.get(),
                    '1900s': d1900s_edit.get(),
                    '1910s': d1910s_edit.get(),
                    '1920s': d1920s_edit.get(),
                    '1930s': d1930s_edit.get(),
                    '1940s': d1940s_edit.get(),
                    '1950s': d1950s_edit.get(),
                    '1960s': d1960s_edit.get(),
                    '1970s': d1970s_edit.get(),
                    '1980s': d1980s_edit.get(),
                    '1990s': d1990s_edit.get(),
                    '2000s': d2000s_edit.get(),
                    '2010s': d2010s_edit.get()})
            conn.commit()
            messagebox.showinfo(title="Name Created", message=name + " has been added to the database")
        else:
            update_yn = messagebox.askyesno(title="Name Already Exists",
                                            message="That name already exists in the database.\nWould you like to update it?")
            if update_yn:
                curs.execute(
                    "UPDATE first_names SET first_name=(?), gender=(?), '1880s'=(?), '1890s'=(?), '1900s'=(?), '1910s'=(?), "
                    "'1920s'=(?), '1930s'=(?), '1940s'=(?), '1950s'=(?), '1960s'=(?), '1970s'=(?), '1980s'=(?), '1990s'=(?), "
                    "'2000s'=(?), '2010s'=(?) WHERE first_name=(?) AND gender=(?)",
                    (fn_edit.get(), gender_edit.get(), d1880s_edit.get(), d1890s_edit.get(),
                     d1900s_edit.get(), d1910s_edit.get(), d1920s_edit.get(), d1930s_edit.get(),
                     d1940s_edit.get(), d1950s_edit.get(), d1960s_edit.get(), d1970s_edit.get(),
                     d1980s_edit.get(), d1990s_edit.get(), d2000s_edit.get(), d2010s_edit.get(),
                     name, gend,))
                conn.commit()
                messagebox.showinfo(title="Name Created", message=name + " has has been updated")
            else:
                messagebox.showinfo(title="Name Not Updated", message=name + " has not been updated.")

    def ln_search():
        ln_edit.delete(0, END)
        common_edit.delete(0, END)
        origin_edit.delete(0, END)
        ln = ln_getbox.get()
        curs.execute(""" SELECT * FROM last_names WHERE last_name = (?) """, (ln,))
        fn_sql = curs.fetchone()
        try:
            ln_edit.insert(0, fn_sql[1])
            common_edit.insert(0, fn_sql[2])
            origin_edit.insert(0, fn_sql[3])
        except TypeError:
            messagebox.showerror(title="Name does not exist", message=ln + " is not in the database.")

    def ln_submit():
        name = ln_edit.get()
        # Check if that surname is already in the database
        curs.execute(""" SELECT * FROM last_names WHERE last_name = (?) """, (name,))
        dupe_check_result = curs.fetchone()
        if name == "":
            messagebox.showerror(title="Fields Blank", message="Please fill out fields before submitting")
        elif not dupe_check_result:
            curs.execute(""" INSERT INTO last_names VALUES (:ln_id, :last_name, :commonality, :origin) """,
                         {
                             'ln_id': None,
                             'last_name': ln_edit.get(),
                             'commonality': common_edit.get(),
                             'origin': origin_edit.get()})
            conn.commit()
            messagebox.showinfo(title="Name Created", message=name + " has been added to the database")
        else:
            update_yn = messagebox.askyesno(title="Name Already Exists",
                                            message="That name already exists in the database.\nWould you like to update it?")
            if update_yn:
                curs.execute(
                    """ UPDATE last_names SET last_name=(?), commonality=(?), origin=(?) WHERE last_name=(?) """,
                    (ln_edit.get(), common_edit.get(), origin_edit.get(), name))
                conn.commit()
                messagebox.showinfo(title="Name Created", message=name + " has has been updated")
            else:
                messagebox.showinfo(title="Name Not Updated", message=name + " has not been updated.")

    def adj_search():
        adj_edit.delete(0, END)
        adj = adj_getbox.get()
        curs.execute(""" SELECT * FROM adjectives WHERE adjective = (?) """, (adj,))
        adj_sql = curs.fetchone()
        try:
            adj_edit.insert(0, adj_sql[1])
        except TypeError:
            messagebox.showerror(title="Adjective does not exist", message=adj + " is not in the database.")

    def adj_submit():
        adj = adj_edit.get()
        # Check if that adjective is already in the database
        curs.execute(""" SELECT * FROM adjectives WHERE adjective = (?) """, (adj,))
        dupe_check_result = curs.fetchone()
        if adj == "":
            messagebox.showerror(title="Fields Blank", message="Please fill out fields before submitting")
        elif not dupe_check_result:
            curs.execute(""" INSERT INTO adjectives VALUES (:adj_id, :adjective) """,
                         {
                             'adj_id': None,
                             'adjective': adj_edit.get()})
            conn.commit()
            messagebox.showinfo(title="Adjective Created", message=adj + " has been added to the database")
        else:
            update_yn = messagebox.askyesno(title="Adjective Already Exists",
                                            message="That adjective already exists in the database.\nWould you like to update it?")
            if update_yn:
                curs.execute(""" UPDATE adjectives SET adjective=(?) WHERE adjective=(?) """,
                             (adj_edit.get(), adj))
                conn.commit()
                messagebox.showinfo(title="Adjective Created", message=adj + " has has been updated")
            else:
                messagebox.showinfo(title="Adjective Not Updated", message=adj + " has not been updated.")

    def nns_search():
        nns_edit.delete(0, END)
        nns = nns_getbox.get()
        curs.execute(""" SELECT * FROM nouns WHERE noun = (?) """, (nns,))
        nns_sql = curs.fetchone()
        try:
            nns_edit.insert(0, nns_sql[1])
            ntype_edit.insert(0, nns_sql[2])
        except TypeError:
            messagebox.showerror(title="Noun does not exist", message=nns + " is not in the database.")

    def nns_submit():
        nns = nns_edit.get()
        # Check if that noun is already in the database
        curs.execute(""" SELECT * FROM nouns WHERE noun = (?) """, (nns,))
        dupe_check_result = curs.fetchone()
        if nns == "":
            messagebox.showerror(title="Fields Blank", message="Please fill out fields before submitting")
        elif not dupe_check_result:
            curs.execute(""" INSERT INTO nouns VALUES (:nns_id, :noun, :type) """,
                         {
                             'nns_id': None,
                             'noun': nns_edit.get(),
                             'type': ntype_edit.get()})
            conn.commit()
            messagebox.showinfo(title="Noun Created", message=nns + " has been added to the database")
        else:
            update_yn = messagebox.askyesno(title="Noun Already Exists",
                                            message="That noun already exists in the database.\nWould you like to update it?")
            if update_yn:
                curs.execute(""" UPDATE nouns SET noun=(?), type=(?) WHERE noun=(?) """,
                             (nns_edit.get(), ntype_edit.get(), nns))
                conn.commit()
                messagebox.showinfo(title="Noun Created", message=nns + " has has been updated")
            else:
                messagebox.showinfo(title="Noun Not Updated", message=nns + " has not been updated.")

    def clear_all():
        fn_getbox.delete(0, END)
        fn_edit.delete(0, END)
        gender_edit.delete(0, END)
        d1880s_edit.delete(0, END)
        d1890s_edit.delete(0, END)
        d1900s_edit.delete(0, END)
        d1910s_edit.delete(0, END)
        d1920s_edit.delete(0, END)
        d1930s_edit.delete(0, END)
        d1940s_edit.delete(0, END)
        d1950s_edit.delete(0, END)
        d1960s_edit.delete(0, END)
        d1970s_edit.delete(0, END)
        d1980s_edit.delete(0, END)
        d1990s_edit.delete(0, END)
        d2000s_edit.delete(0, END)
        d2010s_edit.delete(0, END)
        ln_getbox.delete(0, END)
        ln_edit.delete(0, END)
        common_edit.delete(0, END)
        origin_edit.delete(0, END)
        adj_getbox.delete(0, END)
        adj_edit.delete(0, END)
        nns_getbox.delete(0, END)
        nns_edit.delete(0, END)
        ntype_edit.delete(0, END)

    # Option Menus
    gend_menu = ["Female", "Male"]
    dec_com_menu = ["", "Top Ten", "Most Common", "Common", "Less Common", "Rare", "Extremely Rare"]

    # Padding
    set_padx = 3
    set_pady = 3

    # First Name
    fn_frame = LabelFrame(dbwin, font=("Calibri", 15), width=30, borderwidth=5, padx=5, pady=5, fg=text_color, background=frame_bg, relief=RIDGE)
    fn_frame.grid(row=0, column=0, rowspan=5, sticky=N)
    fn_label = Label(fn_frame, text="First Names", font=("Calibri", 15), fg=text_color, bg=frame_bg)
    fn_label.grid(row=0, column=0)

    fn_getbox = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    fn_getbox.grid(row=1, column=1)
    fn_getbox_but = Button(fn_frame, font=("Calibri", 13, 'bold'), text="Search", width=15, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=fn_search)
    fn_getbox_but.grid(row=1, column=0)

    fn_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    fn_edit.grid(row=2, column=1)
    fn_edit_label = Label(fn_frame, text="First Name", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    fn_edit_label.grid(row=2, column=0)

    gender_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    gender_edit.grid(row=3, column=1)
    gender_edit_label = Label(fn_frame, text="Gender", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    gender_edit_label.grid(row=3, column=0)

    d1880s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1880s_edit.grid(row=4, column=1)
    d1880s_edit_label = Label(fn_frame, text="1880s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1880s_edit_label.grid(row=4, column=0)

    d1890s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1890s_edit.grid(row=5, column=1)
    d1890s_edit_label = Label(fn_frame, text="1890s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1890s_edit_label.grid(row=5, column=0)

    d1900s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1900s_edit.grid(row=6, column=1)
    d1900s_edit_label = Label(fn_frame, text="1900s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1900s_edit_label.grid(row=6, column=0)

    d1910s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1910s_edit.grid(row=7, column=1)
    d1910s_edit_label = Label(fn_frame, text="1910s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1910s_edit_label.grid(row=7, column=0)

    d1920s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1920s_edit.grid(row=8, column=1)
    d1920s_edit_label = Label(fn_frame, text="1920s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1920s_edit_label.grid(row=8, column=0)

    d1930s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1930s_edit.grid(row=9, column=1)
    d1930s_edit_label = Label(fn_frame, text="1930s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1930s_edit_label.grid(row=9, column=0)

    d1940s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1940s_edit.grid(row=10, column=1)
    d1940s_edit_label = Label(fn_frame, text="1940s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1940s_edit_label.grid(row=10, column=0)

    d1950s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1950s_edit.grid(row=11, column=1)
    d1950s_edit_label = Label(fn_frame, text="1950s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1950s_edit_label.grid(row=11, column=0)

    d1960s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1960s_edit.grid(row=12, column=1)
    d1960s_edit_label = Label(fn_frame, text="1960s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1960s_edit_label.grid(row=12, column=0)

    d1970s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1970s_edit.grid(row=13, column=1)
    d1970s_edit_label = Label(fn_frame, text="1970s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1970s_edit_label.grid(row=13, column=0)

    d1980s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1980s_edit.grid(row=14, column=1)
    d1980s_edit_label = Label(fn_frame, text="1980s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1980s_edit_label.grid(row=14, column=0)

    d1990s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d1990s_edit.grid(row=15, column=1)
    d1990s_edit_label = Label(fn_frame, text="1990s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1990s_edit_label.grid(row=15, column=0)

    d2000s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d2000s_edit.grid(row=16, column=1)
    d2000s_edit_label = Label(fn_frame, text="2000s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d2000s_edit_label.grid(row=16, column=0)

    d2010s_edit = Entry(fn_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    d2010s_edit.grid(row=17, column=1)
    d2010s_edit_label = Label(fn_frame, text="2010s", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d2010s_edit_label.grid(row=17, column=0)

    fn_submit_but = Button(fn_frame, font=("Calibri", 13, 'bold'), text="Submit", width=15, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=fn_submit)
    fn_submit_but.grid(row=18, column=0, columnspan=2)

    # Last Names

    ln_frame = LabelFrame(dbwin, font=("Calibri", 15), width=30, borderwidth=5, padx=5, pady=5, fg=text_color, background=frame_bg, relief=RIDGE)
    ln_frame.grid(row=0, column=1, rowspan=2, columnspan=2, sticky=N)
    ln_label = Label(ln_frame, text="Last Names", font=("Calibri", 15), fg=text_color, bg=frame_bg)
    ln_label.grid(row=0, column=0)

    ln_getbox = Entry(ln_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    ln_getbox.grid(row=1, column=1)
    ln_getbox_but = Button(ln_frame, font=("Calibri", 13, 'bold'), text="Search", width=15, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=ln_search)
    ln_getbox_but.grid(row=1, column=0)

    ln_edit = Entry(ln_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    ln_edit.grid(row=2, column=1)
    ln_edit_label = Label(ln_frame, text="Last Name", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    ln_edit_label.grid(row=2, column=0)

    common_edit = Entry(ln_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    common_edit.grid(row=3, column=1)
    common_edit_label = Label(ln_frame, text="Commonality", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    common_edit_label.grid(row=3, column=0)

    origin_edit = Entry(ln_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    origin_edit.grid(row=4, column=1)
    origin_edit_label = Label(ln_frame, text="Origin", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    origin_edit_label.grid(row=4, column=0)

    ln_submit_but = Button(ln_frame, font=("Calibri", 13, 'bold'), text="Submit", width=15, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=ln_submit)
    ln_submit_but.grid(row=5, column=0, columnspan=2)

    # Adjectives

    adj_frame = LabelFrame(dbwin, font=("Calibri", 15), width=30, borderwidth=5, padx=5, pady=5, fg=text_color, background=frame_bg, relief=RIDGE)
    adj_frame.grid(row=2, column=1, columnspan=2, sticky=N)
    adj_label = Label(adj_frame, text="Adjectives", font=("Calibri", 15), fg=text_color, bg=frame_bg)
    adj_label.grid(row=0, column=0)

    adj_getbox = Entry(adj_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    adj_getbox.grid(row=1, column=1)
    adj_getbox_but = Button(adj_frame, font=("Calibri", 13, 'bold'), text="Search", width=15, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=adj_search)
    adj_getbox_but.grid(row=1, column=0)

    adj_edit = Entry(adj_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    adj_edit.grid(row=2, column=1)
    adj_edit_label = Label(adj_frame, text="Adjective", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg,  padx=set_padx, pady=set_pady)
    adj_edit_label.grid(row=2, column=0)

    adj_submit_but = Button(adj_frame, font=("Calibri", 13, 'bold'), text="Submit", width=15, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=adj_submit)
    adj_submit_but.grid(row=3, column=0, columnspan=2)

    # Nouns

    nns_frame = LabelFrame(dbwin, font=("Calibri", 15), width=30, borderwidth=5, padx=5, pady=5, fg=text_color, background=frame_bg, relief=RIDGE)
    nns_frame.grid(row=3, column=1, columnspan=2, sticky=N)
    nns_label = Label(nns_frame, text="Nouns", font=("Calibri", 15), fg=text_color, bg=frame_bg)
    nns_label.grid(row=0, column=0)

    nns_getbox = Entry(nns_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    nns_getbox.grid(row=1, column=1)
    nns_getbox_but = Button(nns_frame, font=("Calibri", 13, 'bold'), text="Search", width=15, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=nns_search)
    nns_getbox_but.grid(row=1, column=0)

    nns_edit = Entry(nns_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    nns_edit.grid(row=2, column=1)
    nns_edit_label = Label(nns_frame, text="Noun", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    nns_edit_label.grid(row=2, column=0)

    ntype_edit = Entry(nns_frame, font=("Calibri", 15), width=20, fg=text_color, bg=entry_bg)
    ntype_edit.grid(row=3, column=1)
    ntype_edit_label = Label(nns_frame, text="Type", font=("Calibri", 15), width=20, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    ntype_edit_label.grid(row=3, column=0)

    nns_submit_but = Button(nns_frame, font=("Calibri", 13, 'bold'), text="Submit", width=15, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=nns_submit)
    nns_submit_but.grid(row=4, column=0, columnspan=2)

    # Main Buttons

    clear_but = Button(dbwin, font=("Calibri", 24, 'bold'), text="Clear", width=12, borderwidth=5, padx=5, pady=10, fg=text_color, background=frame_bg, relief=RAISED, command=clear_all)
    clear_but.grid(row=4, column=1, sticky=NW)
    close_but = Button(dbwin, font=("Calibri", 24, 'bold'), text="Close", width=12, borderwidth=5, padx=5, pady=10, fg=text_color, background=frame_bg, relief=RAISED, command=dbwin.destroy)
    close_but.grid(row=4, column=2, sticky=NW)

    dbwin.mainloop()


db_button = Button(root, font=("Calibri", 23, 'bold'), text="Database\nManagement", padx=25, pady=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, command=database)
db_button.grid(row=6, column=3, sticky=N+S+E+W)

root.mainloop()