from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import random
from PIL import ImageTk, Image

root = Tk()
root.geometry("1300x680")
root.maxsize(1300, 680)
root.title("GeNamenator v 2.3")
root.iconbitmap('Groucho_Icon.ico')

conn = sqlite3.connect('GeName_DB_2.db')
curs = conn.cursor()

# Logo
logo_img = ImageTk.PhotoImage(Image.open('GNLogo_2_2.png'))
logo_label = Label(image=logo_img, padx=15, pady=15, relief=RIDGE)
logo_label.grid(row=10, column=0, columnspan=4, rowspan=5, sticky=W+N)


# Theme Options
curs.execute(""" SELECT * FROM themes """)
theme_list = curs.fetchone()
main_bg = theme_list[1]
button_bg = theme_list[2]
button_act_bg = theme_list[3]
frame_bg = theme_list[4]
text_color = theme_list[5]
entry_bg = theme_list[6]
main_font = theme_list[7]
output_font = theme_list[8]


def theme_green():
    curs.execute(""" UPDATE themes SET main_bg="#66cc99", button_bg="#66cc00", button_act_bg="#0b5345", frame_bg="#66cc33", 
    text_color="#000000", entry_bg="#ffffff", main_font="Helvetica", output_font="Times" WHERE thm_id=1""")
    conn.commit()


def theme_red():
    curs.execute(""" UPDATE themes SET main_bg="#c2240b", button_bg="#ae1f1f", button_act_bg="#5d0909", frame_bg="#c13323", 
    text_color="#000000", entry_bg="#ffffff", main_font="Helvetica", output_font="Times" WHERE thm_id=1""")
    conn.commit()


def theme_blue():
    curs.execute(""" UPDATE themes SET main_bg="#68d7ee", button_bg="#1db8de", button_act_bg="#11697e", frame_bg="#3c8afa", 
    text_color="#000000", entry_bg="#ffffff", main_font="Helvetica", output_font="Times" WHERE thm_id=1""")
    conn.commit()


def theme_purple():
    curs.execute(""" UPDATE themes SET main_bg="#c972f7", button_bg="#983dc8", button_act_bg="#441a5a", frame_bg="#ac5ed5", 
    text_color="#000000", entry_bg="#ffffff", main_font="Helvetica", output_font="Times" WHERE thm_id=1""")
    conn.commit()


def theme_gray():
    curs.execute(""" UPDATE themes SET main_bg="#737373", button_bg="#cdcdcd", button_act_bg="#666666", frame_bg="#e7e7e7", 
    text_color="#000000", entry_bg="#ffffff", main_font="Helvetica", output_font="Times" WHERE thm_id=1""")
    conn.commit()


def theme_dos():
    curs.execute(""" UPDATE themes SET main_bg="#000000", button_bg="#262626", button_act_bg="#000000", frame_bg="#222222", 
    text_color="#55ff00", entry_bg="#000000", main_font="System", output_font="System" WHERE thm_id=1""")
    conn.commit()


# Theme Buttons
theme_frame = LabelFrame(root, font=(main_font, 12), width=30, borderwidth=2, relief=RIDGE, fg=text_color, background=frame_bg)
theme_frame.grid(row=16, column=0, columnspan=6, rowspan=2, sticky=W+N)

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

ln_hyph = StringVar()
ln_hyph.set("HyphOff")

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
commonness = StringVar()
commonness.set("")

name_starts = ("A", "B", "C", "Ch", "D", "E", "F", "G", "Gr", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
               "S", "Sh", "St", "T", "Th", "U", "V", "W", "X", "Y", "Z")

# Gather last name origins for combobox
curs.execute(""" SELECT origin, origin_sec, origin_thrd FROM last_names """)
origin_list = curs.fetchall()
origin_set = set(origin_list)
ln_origin_list = list(origin_set)
ln_origin_list.remove(None)
ln_origin_list.insert(0, '')
ln_origin_list.sort()


# Error Messages
def index_error_popup():
    messagebox.showerror(title="INDEX ERROR", message="Not enough names in the database match that criteria.\n"
                     "Please change the alliteration settings\n"
                     "or expand the decade and commonness settings.")


def commonness_error():
    messagebox.showerror(title="INDEX ERROR", message="Please add commonness criteria.")


# Birth Decade Commonness
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


# Set default commonness when decade selected
def default_decom(event):
    chk_topten.set("Top Ten")
    chk_mostcommon.set("Most Common")
    chk_common.set("Common")


# Inteior Name Functions
def create_first_name(gend_choice):
    global first_name
    global fn_pull
    global allit_end_string
    global dec
    global dec_string
    allitt_choice = allit.get()
    allit_input = allit_begin.get()
    dec = decade_menu.get()
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
            commonness_error()
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
    dec = decade_menu.get()
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
                if len(mid_pull) > 1:
                    mid_name = random.choice(fn_pull)
                    if mid_name != first_name:
                        break
                else:
                    index_error_popup()
        except IndexError:
            index_error_popup()
    elif allitt_choice == "AllitOn" and dec != "":
        try:
            while True:
                curs.execute(""" SELECT first_name FROM first_names WHERE gender = (?) AND first_name LIKE (?) AND """ + dec_string + """ IN """ + deccom_list,
                    (gend_choice, allit_end_string))
                mid_pull = curs.fetchall()
                if len(mid_pull) > 1:
                    mid_name = random.choice(fn_pull)
                    if mid_name != first_name:
                        break
                else:
                    index_error_popup()
        except IndexError:
            index_error_popup()


def create_last_name():
    global last_name
    global last_name_first
    global last_name_second
    global ln_pull
    allitt_choice = allit.get()
    lnhyph_choice = ln_hyph.get()
    ln_origin_choice = ln_origin_combo.get()
    if allitt_choice == "AllitOff":
        curs.execute(""" SELECT last_name FROM last_names """)
        ln_pull = curs.fetchall()
        if ln_origin_choice == "":
            if lnhyph_choice == "HyphOn":
                last_name_first = random.choice(ln_pull)
                while True:
                    last_name_second = random.choice(ln_pull)
                    if last_name_second != last_name_first:
                        break
                last_name = last_name_first + "-" + last_name_second
            else:
                last_name = random.choice(ln_pull)
        else:
            curs.execute(""" SELECT last_name FROM last_names WHERE origin=(?) OR origin_sec=(?) OR origin_thrd=(?)""",
                         (ln_origin_choice, ln_origin_choice, ln_origin_choice))
            ln_pull = curs.fetchall()
            if lnhyph_choice == "HyphOn":
                last_name_first = random.choice(ln_pull)
                while True:
                    last_name_second = random.choice(ln_pull)
                    if last_name_second != last_name_first:
                        break
                last_name = last_name_first + "-" + last_name_second
            else:
                last_name = random.choice(ln_pull)
    else:
        try:
            curs.execute(""" SELECT last_name FROM last_names WHERE last_name LIKE (?)""", (allit_end_string,))
            ln_pull = curs.fetchall()
            if ln_origin_choice == "":
                if lnhyph_choice == "HyphOn":
                    last_name_first = random.choice(ln_pull)
                    if len(ln_pull) > 1:
                        while True:
                            last_name_second = random.choice(ln_pull)
                            if last_name_second != last_name_first:
                                break
                        last_name = last_name_first + "-" + last_name_second
                    else:
                        index_error_popup()
                else:
                    last_name = random.choice(ln_pull)
            else:
                curs.execute(""" SELECT last_name FROM last_names WHERE last_name LIKE (?) AND origin=(?) OR origin_sec=(?) OR origin_thrd=(?)""",
                             (allit_end_string, ln_origin_choice, ln_origin_choice, ln_origin_choice))
                ln_pull = curs.fetchall()
                if lnhyph_choice == "HyphOn":
                    last_name_first = random.choice(ln_pull)
                    if len(ln_pull) > 1:
                        while True:
                            last_name_second = random.choice(ln_pull)
                            if last_name_second != last_name_first:
                                break
                        last_name = last_name_first + "-" + last_name_second
                    else:
                        index_error_popup()
                else:
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
        name_output['text'] = (first_name + " " + mid_name_last + " " + last_name)
        create_description()


# Output 1 and 2
output_frame = LabelFrame(root, fg=text_color, bg=main_bg)
output_frame.grid(row=0, column=0, rowspan=8, columnspan=4)

name_output = Label(output_frame, font=(output_font, 33, 'bold'), fg=text_color, bg=entry_bg, width=27, text="", borderwidth=7, relief=RAISED)
name_output.grid(row=0, column=0, padx=10, pady=10)

desc_output = Label(output_frame, font=(output_font, 33, 'bold'), fg=text_color, bg=entry_bg, width=27, text="", borderwidth=7, relief=RAISED)
desc_output.grid(row=1, column=0, padx=10, pady=10)


# Create Buttons
but_padx = 50
but_pady = 10
rando_button = Button(root, font=(main_font, 30, 'bold'), text="Create\nRandom", padx=but_padx, pady=but_pady, borderwidth=20, bg=button_bg, activebackground=button_act_bg, fg=text_color, relief=RAISED, command=create_random)
rando_button.grid(row=8, column=0, columnspan=2, rowspan=2)
crit_button = Button(root, font=(main_font, 30, 'bold'), text="Create by\nCriteria", padx=but_padx, pady=but_pady, borderwidth=20, bg=button_bg, activebackground=button_act_bg, fg=text_color, relief=RAISED, command=create_name)
crit_button.grid(row=8, column=2, columnspan=2, rowspan=2)


# Female/Male Options
f_m_frame = LabelFrame(root, width=20, borderwidth=2, fg=text_color, background=frame_bg, relief=RIDGE)
f_m_frame.grid(row=0, column=4, rowspan=4, padx=5, pady=5, sticky=N+S+E+W)
f_m_label = Label(f_m_frame, text="Gender", font=(main_font, 18, 'bold'), fg=text_color, bg=frame_bg)
f_m_label.grid(row=0, column=0, columnspan=2)
f_radio = Radiobutton(f_m_frame, font=(main_font, 15), text="Female", padx=5, variable=gender, value="Female", fg=text_color, bg=frame_bg)
f_radio.grid(row=1, column=0, sticky=W)
m_radio = Radiobutton(f_m_frame, font=(main_font, 15), text="Male", padx=5, variable=gender, value="Male", fg=text_color, bg=frame_bg)
m_radio.grid(row=2, column=0, sticky=W)
a_radio = Radiobutton(f_m_frame, font=(main_font, 15), text="Any", padx=5, variable=gender, value="Any", fg=text_color, bg=frame_bg)
a_radio.grid(row=3, column=0, sticky=W)


# Middle Name Options
middle_frame = LabelFrame(root, width=30, borderwidth=2, relief=RIDGE, fg=text_color, background=frame_bg)
middle_frame.grid(row=0, column=5, rowspan=4, padx=5, pady=5, sticky=N+S+E+W)
middle_label = Label(middle_frame, font=(main_font, 18, 'bold'), text="Middle Name", fg=text_color, bg=frame_bg)
middle_label.grid(row=0, column=0, columnspan=2)
middle_check = Checkbutton(middle_frame, padx=5, variable=middle, onvalue="MidOn", offvalue="MidOff", bg=frame_bg)
middle_check.grid(row=1, column=0)
middle_check_label = Label(middle_frame, font=(main_font, 15), text="Middle Name", fg=text_color, bg=frame_bg)
middle_check_label.grid(row=1, column=1, sticky=W)
midlast_check = Checkbutton(middle_frame, padx=5, variable=middle, onvalue="MidLastOn", offvalue="MidOff", bg=frame_bg)
midlast_check.grid(row=2, column=0)
midlast_check_label = Label(middle_frame, font=(main_font, 15), text="Last Name for\nMiddle Name", fg=text_color, bg=frame_bg)
midlast_check_label.grid(row=2, column=1, sticky=W)


# Last Name Options
ln_frame = LabelFrame(root, width=30, borderwidth=2, relief=RIDGE, background=frame_bg, fg=text_color)
ln_frame.grid(row=5, column=4, rowspan=2, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)
ln_label = Label(ln_frame, font=(main_font, 18, 'bold'), text="Last Name", fg=text_color, bg=frame_bg)
ln_label.grid(row=0, column=0, columnspan=2)
lnhyph_button = Checkbutton(ln_frame, padx=5, variable=ln_hyph, onvalue="HyphOn", offvalue="HyphOff", bg=frame_bg)
lnhyph_button.grid(row=1, column=0)
lnhyph_check_label = Label(ln_frame, font=(main_font, 15), text="Hyphenated", fg=text_color, bg=frame_bg)
lnhyph_check_label.grid(row=1, column=1, sticky=W)
ln_origin_combo = ttk.Combobox(ln_frame, font=(main_font, 15), width=12, value=ln_origin_list, state="readonly")
ln_origin_combo.current(0)
ln_origin_combo.grid(row=2, column=1, padx=5, pady=5)
ln_origin_label = Label(ln_frame, font=(main_font, 15), text="Origin", fg=text_color, bg=frame_bg)
ln_origin_label.grid(row=2, column=0)


# Alliterative Options
allit_frame = LabelFrame(root, width=30, borderwidth=2, relief=RIDGE, background=frame_bg, fg=text_color)
allit_frame.grid(row=8, column=4, rowspan=2, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)
allit_label = Label(allit_frame, font=(main_font, 18, 'bold'), text="Alliteration", fg=text_color, bg=frame_bg)
allit_label.grid(row=0, column=0, columnspan=2)
allit_button = Checkbutton(allit_frame, padx=5, variable=allit, onvalue="AllitOn", offvalue="AllitOff", bg=frame_bg)
allit_button.grid(row=1, column=0)
allit_check_label = Label(allit_frame, font=(main_font, 15), text="Alliterative Name", fg=text_color, bg=frame_bg)
allit_check_label.grid(row=1, column=1, sticky=W)
allit_begin = Entry(allit_frame, font=(main_font, 15), width=3, borderwidth=5)
allit_begin.grid(row=2, column=0, padx=5, pady=5)
allit_label = Label(allit_frame, font=(main_font, 15), text="Name starts with", fg=text_color, bg=frame_bg)
allit_label.grid(row=2, column=1, sticky=W)


# Decade and Commonness Options
decade_frame = LabelFrame(root, width=50, borderwidth=2, relief=RIDGE, fg=text_color, background=frame_bg)
decade_frame.grid(row=0, column=6, rowspan=9, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)
decade_label = Label(decade_frame, font=(main_font, 18, 'bold'), text="Birth Decade", fg=text_color, bg=frame_bg)
decade_label.grid(row=0, column=0, columnspan=2)
decade_menu = ttk.Combobox(decade_frame, font=(main_font, 15), width=10, value=dec_list, state="readonly")
decade_menu.current(0)
decade_menu.bind("<<ComboboxSelected>>", default_decom)
decade_menu.grid(row=1, column=1)
decade_menu_label = Label(decade_frame, font=(main_font, 15), text="Decade", fg=text_color, bg=frame_bg)
decade_menu_label.grid(row=1, column=0)
commonness_label = Label(decade_frame, font=(main_font, 18, 'bold'), text="Commonness", fg=text_color, bg=frame_bg)
commonness_label.grid(row=2, column=0, columnspan=2)

topten = Checkbutton(decade_frame, variable=chk_topten, onvalue="Top Ten", offvalue="Off", bg=frame_bg)
topten.grid(row=3, column=0)
topten_label = Label(decade_frame, font=(main_font, 15), text="Top Ten", fg=text_color, bg=frame_bg)
topten_label.grid(row=3, column=1, sticky=W)

mostcommon = Checkbutton(decade_frame, variable=chk_mostcommon, onvalue="Most Common", offvalue="Off", bg=frame_bg)
mostcommon.grid(row=4, column=0)
mostcommon_label = Label(decade_frame, font=(main_font, 15), text="Most Common", fg=text_color, bg=frame_bg)
mostcommon_label.grid(row=4, column=1, sticky=W)

common = Checkbutton(decade_frame, variable=chk_common, onvalue="Common", offvalue="Off", bg=frame_bg)
common.grid(row=5, column=0)
common_label = Label(decade_frame, font=(main_font, 15), text="Common", fg=text_color, bg=frame_bg)
common_label.grid(row=5, column=1, sticky=W)

lesscommon = Checkbutton(decade_frame, variable=chk_lesscommon, onvalue="Less Common", offvalue="Off", bg=frame_bg)
lesscommon.grid(row=6, column=0)
lesscommon_label = Label(decade_frame, font=(main_font, 15), text="Less Common", fg=text_color, bg=frame_bg)
lesscommon_label.grid(row=6, column=1, sticky=W)

rare = Checkbutton(decade_frame, variable=chk_rare, onvalue="Rare", offvalue="Off", bg=frame_bg)
rare.grid(row=7, column=0)
rare_label = Label(decade_frame, font=(main_font, 15), text="Rare", fg=text_color, bg=frame_bg)
rare_label.grid(row=7, column=1, sticky=W)

exrare = Checkbutton(decade_frame, variable=chk_exrare, onvalue="Extremely Rare", offvalue="Off", bg=frame_bg)
exrare.grid(row=8, column=0)
exrare_label = Label(decade_frame, font=(main_font, 15), text="Extremely Rare", fg=text_color, bg=frame_bg)
exrare_label.grid(row=8, column=1, sticky=W)


# Clear Options

def clear():
    gender.set("Any")
    allit.set("AllitOff")
    allit_begin.delete(0, END)
    allit_begin.insert(0, "")
    middle.set("MidOff")
    ln_hyph.set("HyphOff")
    ln_origin_combo.current(0)
    decade_menu.current(0)
    chk_topten.set("Off")
    chk_mostcommon.set("Off")
    chk_common.set("Off")
    chk_lesscommon.set("Off")
    chk_rare.set("Off")
    chk_exrare.set("Off")
    commonness.set("")
    name_output['text'] = ""
    desc_output['text'] = ""


clear_all = Button(root, font=(main_font, 23, 'bold'), text="Clear", padx=25, pady=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, borderwidth=20, command=clear)
clear_all.grid(row=9, column=6, rowspan=1, columnspan=2, sticky=N+S+E+W)


# Database Management Module

def database():
    dbwin = Tk()
    dbwin.geometry("855x835")
    # dbwin.maxsize(990, 820)
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

    # Combobox Lists
    gend_comb = ["", "Female", "Male"]
    deccom_comb = ["", "Top Ten", "Most Common", "Common", "Less Common", "Rare", "Extremely Rare"]
    lncom_comb = ["", "Most Common", "Common", "Less Common", "Rare"]
    ntype_comb = ["", "Occupation", "Personality"]

    # Search Functions
    def fn_search():
        fn_edit.delete(0, END)
        gender_edit.current(0)
        d1880s_edit.current(0)
        d1890s_edit.current(0)
        d1900s_edit.current(0)
        d1910s_edit.current(0)
        d1920s_edit.current(0)
        d1930s_edit.current(0)
        d1940s_edit.current(0)
        d1950s_edit.current(0)
        d1960s_edit.current(0)
        d1970s_edit.current(0)
        d1980s_edit.current(0)
        d1990s_edit.current(0)
        d2000s_edit.current(0)
        d2010s_edit.current(0)
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
        try: # convert index from SQL search into index of gender/deccom lists
            fn_edit.insert(0, fn_sql[1])
            sql_gend = gend_comb.index(fn_sql[2])
            gender_edit.current(sql_gend)
            sql_d1880s = deccom_comb.index(fn_sql[3])
            d1880s_edit.current(sql_d1880s)
            sql_d1890s = deccom_comb.index(fn_sql[4])
            d1890s_edit.current(sql_d1890s)
            sql_d1900s = deccom_comb.index(fn_sql[5])
            d1900s_edit.current(sql_d1900s)
            sql_d1910s = deccom_comb.index(fn_sql[6])
            d1910s_edit.current(sql_d1910s)
            sql_d1920s = deccom_comb.index(fn_sql[7])
            d1920s_edit.current(sql_d1920s)
            sql_d1930s = deccom_comb.index(fn_sql[8])
            d1930s_edit.current(sql_d1930s)
            sql_d1940s = deccom_comb.index(fn_sql[9])
            d1940s_edit.current(sql_d1940s)
            sql_d1950s = deccom_comb.index(fn_sql[10])
            d1950s_edit.current(sql_d1950s)
            sql_d1960s = deccom_comb.index(fn_sql[11])
            d1960s_edit.current(sql_d1960s)
            sql_d1970s = deccom_comb.index(fn_sql[12])
            d1970s_edit.current(sql_d1970s)
            sql_d1980s = deccom_comb.index(fn_sql[13])
            d1980s_edit.current(sql_d1980s)
            sql_d1990s = deccom_comb.index(fn_sql[14])
            d1990s_edit.current(sql_d1990s)
            sql_d2000s = deccom_comb.index(fn_sql[15])
            d2000s_edit.current(sql_d2000s)
            sql_d2010s = deccom_comb.index(fn_sql[16])
            d2010s_edit.current(sql_d2010s)
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
        ln_common_edit.current(0)
        origin_1_edit.delete(0, END)
        origin_2_edit.delete(0, END)
        origin_3_edit.delete(0, END)
        ln = ln_getbox.get()
        curs.execute(""" SELECT * FROM last_names WHERE last_name = (?) """, (ln,))
        ln_sql = curs.fetchone()
        try:
            ln_edit.insert(0, ln_sql[1])
            sql_lncom = lncom_comb.index(ln_sql[2])
            ln_common_edit.current(sql_lncom)
            origin_1_edit.insert(0, ln_sql[3])
            origin_2_edit.insert(0, ln_sql[4])
            origin_3_edit.insert(0, ln_sql[5])
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
            curs.execute(""" INSERT INTO last_names VALUES (:ln_id, :last_name, :commonness, :origin_1, :origin_2, :origin_3) """,
                         {
                             'ln_id': None,
                             'last_name': ln_edit.get(),
                             'commonness': ln_common_edit.get(),
                             'origin_1': origin_1_edit.get(),
                             'origin_2': origin_2_edit.get(),
                             'origin_3': origin_3_edit.get()})
            conn.commit()
            messagebox.showinfo(title="Name Created", message=name + " has been added to the database")
        else:
            update_yn = messagebox.askyesno(title="Name Already Exists",
                                            message="That name already exists in the database.\nWould you like to update it?")
            if update_yn:
                curs.execute(
                    """ UPDATE last_names SET last_name=(?), commonness=(?), origin_1=(?) WHERE last_name=(?) """,
                    (ln_edit.get(), ln_common_edit.get(), origin_1_edit.get(), name))
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
            sql_ntype = ntype_comb.index(nns_sql[2])
            ntype_edit.current(sql_ntype)
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
        gender_edit.current(0)
        d1880s_edit.current(0)
        d1890s_edit.current(0)
        d1900s_edit.current(0)
        d1910s_edit.current(0)
        d1920s_edit.current(0)
        d1930s_edit.current(0)
        d1940s_edit.current(0)
        d1950s_edit.current(0)
        d1960s_edit.current(0)
        d1970s_edit.current(0)
        d1980s_edit.current(0)
        d1990s_edit.current(0)
        d2000s_edit.current(0)
        d2010s_edit.current(0)
        ln_getbox.delete(0, END)
        ln_edit.delete(0, END)
        ln_common_edit.current(0)
        origin_1_edit.delete(0, END)
        origin_2_edit.delete(0, END)
        origin_3_edit.delete(0, END)
        adj_getbox.delete(0, END)
        adj_edit.delete(0, END)
        nns_getbox.delete(0, END)
        nns_edit.delete(0, END)
        ntype_edit.current(0)

    # Padding
    set_padx = 3
    set_pady = 3

    # First Name
    fn_frame = LabelFrame(dbwin, font=(main_font, 15), borderwidth=5, fg=text_color, background=frame_bg, relief=RIDGE)
    fn_frame.grid(row=0, column=0, rowspan=5, columnspan=2, sticky=N)
    fn_label = Label(fn_frame, text="First Names", font=(main_font, 15, 'bold'), fg=text_color, bg=frame_bg)
    fn_label.grid(row=0, column=0, columnspan=2, pady=5)

    fn_getbox = Entry(fn_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    fn_getbox.grid(row=1, column=1, padx=5)
    fn_getbox_but = Button(fn_frame, font=(main_font, 15, 'bold'), text="Search", width=10, borderwidth=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=fn_search)
    fn_getbox_but.grid(row=1, column=0, padx=5)

    fn_edit = Entry(fn_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    fn_edit.grid(row=2, column=1, padx=5)
    fn_edit_label = Label(fn_frame, text="First Name", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    fn_edit_label.grid(row=2, column=0)

    gender_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=gend_comb, state="readonly")
    gender_edit.current(0)
    gender_edit.grid(row=3, column=1)
    gender_edit_label = Label(fn_frame, text="Gender", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    gender_edit_label.grid(row=3, column=0)

    d1880s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1880s_edit.current(0)
    d1880s_edit.grid(row=4, column=1)
    d1880s_edit_label = Label(fn_frame, text="1880s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1880s_edit_label.grid(row=4, column=0)

    d1890s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1890s_edit.current(0)
    d1890s_edit.grid(row=5, column=1)
    d1890s_edit_label = Label(fn_frame, text="1890s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1890s_edit_label.grid(row=5, column=0)

    d1900s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1900s_edit.current(0)
    d1900s_edit.grid(row=6, column=1)
    d1900s_edit_label = Label(fn_frame, text="1900s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1900s_edit_label.grid(row=6, column=0)

    d1910s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1910s_edit.current(0)
    d1910s_edit.grid(row=7, column=1)
    d1910s_edit_label = Label(fn_frame, text="1910s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1910s_edit_label.grid(row=7, column=0)

    d1920s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1920s_edit.current(0)
    d1920s_edit.grid(row=8, column=1)
    d1920s_edit_label = Label(fn_frame, text="1920s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1920s_edit_label.grid(row=8, column=0)

    d1930s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1930s_edit.current(0)
    d1930s_edit.grid(row=9, column=1)
    d1930s_edit_label = Label(fn_frame, text="1930s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1930s_edit_label.grid(row=9, column=0)

    d1940s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1940s_edit.current(0)
    d1940s_edit.grid(row=10, column=1)
    d1940s_edit_label = Label(fn_frame, text="1940s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1940s_edit_label.grid(row=10, column=0)

    d1950s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1950s_edit.current(0)
    d1950s_edit.grid(row=11, column=1)
    d1950s_edit_label = Label(fn_frame, text="1950s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1950s_edit_label.grid(row=11, column=0)

    d1960s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1960s_edit.current(0)
    d1960s_edit.grid(row=12, column=1)
    d1960s_edit_label = Label(fn_frame, text="1960s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1960s_edit_label.grid(row=12, column=0)

    d1970s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1970s_edit.current(0)
    d1970s_edit.grid(row=13, column=1)
    d1970s_edit_label = Label(fn_frame, text="1970s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1970s_edit_label.grid(row=13, column=0)

    d1980s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1980s_edit.current(0)
    d1980s_edit.grid(row=14, column=1)
    d1980s_edit_label = Label(fn_frame, text="1980s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1980s_edit_label.grid(row=14, column=0)

    d1990s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d1990s_edit.current(0)
    d1990s_edit.grid(row=15, column=1)
    d1990s_edit_label = Label(fn_frame, text="1990s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d1990s_edit_label.grid(row=15, column=0)

    d2000s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d2000s_edit.current(0)
    d2000s_edit.grid(row=16, column=1)
    d2000s_edit_label = Label(fn_frame, text="2000s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d2000s_edit_label.grid(row=16, column=0)

    d2010s_edit = ttk.Combobox(fn_frame, font=(main_font, 15), width=18, value=deccom_comb, state="readonly")
    d2010s_edit.current(0)
    d2010s_edit.grid(row=17, column=1)
    d2010s_edit_label = Label(fn_frame, text="2010s", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    d2010s_edit_label.grid(row=17, column=0)

    fn_submit_but = Button(fn_frame, font=(main_font, 15, 'bold'), text="Submit", width=10, pady=3, borderwidth=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=fn_submit)
    fn_submit_but.grid(row=18, column=0, pady=5, columnspan=2)

    # Last Names

    ln_frame = LabelFrame(dbwin, font=(main_font, 15), borderwidth=5, padx=5, pady=5, fg=text_color, background=frame_bg, relief=RIDGE)
    ln_frame.grid(row=0, column=2, rowspan=2, columnspan=2, sticky=N)
    ln_label = Label(ln_frame, text="Last Names", font=(main_font, 15, 'bold'), fg=text_color, bg=frame_bg)
    ln_label.grid(row=0, column=0, columnspan=2, pady=5)

    ln_getbox = Entry(ln_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    ln_getbox.grid(row=1, column=1, padx=5)
    ln_getbox_but = Button(ln_frame, font=(main_font, 15, 'bold'), text="Search", width=10, borderwidth=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=ln_search)
    ln_getbox_but.grid(row=1, column=0, padx=5)

    ln_edit = Entry(ln_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    ln_edit.grid(row=2, column=1)
    ln_edit_label = Label(ln_frame, text="Last Name", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    ln_edit_label.grid(row=2, column=0)

    ln_common_edit = ttk.Combobox(ln_frame, font=(main_font, 15), width=18, value=lncom_comb, state="readonly")
    ln_common_edit.current(0)
    ln_common_edit.grid(row=3, column=1)
    ln_common_edit_label = Label(ln_frame, text="Commonness", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    ln_common_edit_label.grid(row=3, column=0)

    origin_1_edit = Entry(ln_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    origin_1_edit.grid(row=4, column=1)
    origin_1_edit_label = Label(ln_frame, text="Origin 1", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    origin_1_edit_label.grid(row=4, column=0)

    origin_2_edit = Entry(ln_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    origin_2_edit.grid(row=5, column=1)
    origin_2_edit_label = Label(ln_frame, text="Origin 2", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    origin_2_edit_label.grid(row=5, column=0)

    origin_3_edit = Entry(ln_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    origin_3_edit.grid(row=6, column=1)
    origin_3_edit_label = Label(ln_frame, text="Origin 3", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    origin_3_edit_label.grid(row=6, column=0)

    ln_submit_but = Button(ln_frame, font=(main_font, 15, 'bold'), text="Submit", width=10, pady=3, borderwidth=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=ln_submit)
    ln_submit_but.grid(row=20, column=0, pady=5, columnspan=2)

    # Adjectives

    adj_frame = LabelFrame(dbwin, font=(main_font, 15), borderwidth=5, padx=5, pady=5, fg=text_color, background=frame_bg, relief=RIDGE)
    adj_frame.grid(row=2, column=2, columnspan=2, sticky=N)
    adj_label = Label(adj_frame, text="Adjectives", font=(main_font, 15, 'bold'), fg=text_color, bg=frame_bg)
    adj_label.grid(row=0, column=0, columnspan=2, pady=5)

    adj_getbox = Entry(adj_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    adj_getbox.grid(row=1, column=1, padx=5)
    adj_getbox_but = Button(adj_frame, font=(main_font, 15, 'bold'), text="Search", width=10, borderwidth=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=adj_search)
    adj_getbox_but.grid(row=1, column=0, padx=5)

    adj_edit = Entry(adj_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    adj_edit.grid(row=2, column=1)
    adj_edit_label = Label(adj_frame, text="Adjective", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg,  padx=set_padx, pady=set_pady)
    adj_edit_label.grid(row=2, column=0)

    adj_submit_but = Button(adj_frame, font=(main_font, 15, 'bold'), text="Submit", width=10, pady=3, borderwidth=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=adj_submit)
    adj_submit_but.grid(row=18, column=0, pady=5, columnspan=2)

    # Nouns

    nns_frame = LabelFrame(dbwin, font=(main_font, 15), borderwidth=5, padx=5, pady=5, fg=text_color, background=frame_bg, relief=RIDGE)
    nns_frame.grid(row=3, column=2, columnspan=2, sticky=N)
    nns_label = Label(nns_frame, text="Nouns", font=(main_font, 15, 'bold'), fg=text_color, bg=frame_bg)
    nns_label.grid(row=0, column=0, columnspan=2, pady=5)

    nns_getbox = Entry(nns_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    nns_getbox.grid(row=1, column=1, padx=5)
    nns_getbox_but = Button(nns_frame, font=(main_font, 15, 'bold'), text="Search", width=10, borderwidth=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=nns_search)
    nns_getbox_but.grid(row=1, column=0, padx=5)

    nns_edit = Entry(nns_frame, font=(main_font, 15), width=20, fg=text_color, bg=entry_bg)
    nns_edit.grid(row=2, column=1)
    nns_edit_label = Label(nns_frame, text="Noun", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    nns_edit_label.grid(row=2, column=0)

    ntype_edit = ttk.Combobox(nns_frame, font=(main_font, 15), width=18, value=ntype_comb, state="readonly")
    ntype_edit.current(0)
    ntype_edit.grid(row=3, column=1)
    ntype_edit_label = Label(nns_frame, text="Type", font=(main_font, 15), width=10, fg=text_color, bg=frame_bg, padx=set_padx, pady=set_pady)
    ntype_edit_label.grid(row=3, column=0)

    nns_submit_but = Button(nns_frame, font=(main_font, 15, 'bold'), text="Submit", width=10, pady=3, borderwidth=10, fg=text_color, bg=button_bg, activebackground=button_act_bg, command=nns_submit)
    nns_submit_but.grid(row=18, column=0, pady=5, columnspan=2)

    # Main Buttons

    clear_but = Button(dbwin, font=(main_font, 24, 'bold'), text="Clear", width=8, borderwidth=20, padx=5, pady=10, fg=text_color, background=frame_bg, relief=RAISED, command=clear_all)
    clear_but.grid(row=3, column=0, sticky=S)
    close_but = Button(dbwin, font=(main_font, 24, 'bold'), text="Close", width=8, borderwidth=20, padx=5, pady=10, fg=text_color, background=frame_bg, relief=RAISED, command=dbwin.destroy)
    close_but.grid(row=3, column=1, sticky=S)

    dbwin.mainloop()


db_button = Button(root, font=(main_font, 23, 'bold'), text="Database\nManagement", fg=text_color, bg=button_bg, activebackground=button_act_bg, relief=RAISED, borderwidth=20, command=database)
db_button.grid(row=10, column=6, rowspan=4, columnspan=2, sticky=N+S+E+W)

root.mainloop()