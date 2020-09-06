import random
import sqlite3

genamenator_db = sqlite3.connect('GeNamenator_DB.db')
cursor = genamenator_db.cursor()
cursor.row_factory = lambda cursor, row: row[0]

name_starts = ("A", "B", "Ba", "Be", "Bi", "Bo", "Bu", "By", "C", "Ca", "Ce", "Ci", "Co", "Cu", "Ch", "Chr", "D", "Da", "De", "Di", "Do", "Du",
               "E", "F", "Fa", "Fe", "Fi", "Fo", "Fu", "G", "Ga", "Ge", "Gi", "Go", "Gu", "Gl", "Gr", "H", "Ha", "He", "Hi", "Ho", "Hu",
               "I", "J", "Ja", "Je", "Ji", "Jo", "Ju", "K", "Ka", "Ke", "Ki", "Ko", "Ku", "M", "Ma", "Me", "Mi", "Mo", "Mu", "N", "Na", "Ne", "Ni" ,"No", "Nu",
               "O", "P", "Pa", "Pe", "Pi", "Po", "Pi", "Ph", "Q", "R", "Ra", "Re", "Ri", "Ro", "Ru", "S", "Sa", "Se", "Si", "So", "Su, "
                "Sh", "Sha", "She", "Shi", "Sho", "Shu", "St", "Sta", "Ste", "Sti", "Sto", "Stu", "T", "Ta", "Te", "Ti", "To", "Tu",
               "Th", "Tha", "The", "Thi", "Tho", "Thu", "U", "V", "W", "Wa", "We", "Wi", "Wo", "Wu", "X", "Y", "Z")

print("GeNamenator, version 1.4")
print("by David Margis, 2020")
print()


def main():
    main_choice = input("GeNamenator Main Menu \n"
                        "                       \n"
                        "What would you like to do? \n"
                        "   (1) Generate a completely random name \n"
                        "   (2) Generate a random alliterative name \n"
                        "   (3) Generate a female or male name \n"
                        "   (4) Generate a female or male alliterative name \n"
                        "   (5) Access the database management menu \n"
                        "   (6) Exit GeNamenator \n"
                        "    ")
    if main_choice == "1":
        random_name()
    elif main_choice == "2":
        random_name_alit()
    elif main_choice == "3":
        mf_name()
    elif main_choice == "4":
        mf_name_alit()
    elif main_choice == "5":
        dbm_menu()
    elif main_choice == "6":
        print("Thank you for using GeNamenator, the name-generating software with a name!")
        raise SystemExit


# NAME GENERATION FUNCTIONS

def random_name():
    random_choice = random.randrange(1, 4)
    if random_choice == 1:
        cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE FEMALE='YES'")
        fn_list_pull = cursor.fetchall()
        cursor.execute(''' SELECT LAST_NAME FROM last_names ''')
        ln_list_pull = cursor.fetchall()
        print(random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
        create_another_in_func(random_name)
    elif random_choice ==2:
        cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE FEMALE='YES'")
        fn_list_pull = cursor.fetchall()
        cursor.execute(''' SELECT LAST_NAME FROM last_names ''')
        ln_list_pull = cursor.fetchall()
        print(random.choice(fn_list_pull) + " " + random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
        create_another_in_func(random_name)
    elif random_choice ==3:
        cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE MALE='YES'")
        fn_list_pull = cursor.fetchall()
        cursor.execute(''' SELECT LAST_NAME FROM last_names ''')
        ln_list_pull = cursor.fetchall()
        print(random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
        create_another_in_func(random_name)
    elif random_choice == 4:
        cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE MALE='YES'")
        fn_list_pull = cursor.fetchall()
        cursor.execute(''' SELECT LAST_NAME FROM last_names ''')
        ln_list_pull = cursor.fetchall()
        print(random.choice(fn_list_pull) + " " + random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
        create_another_in_func(random_name)


def random_name_alit():
    while True:
        random_choice = random.randrange(1, 4)
        alitter = input("What letter or letters do you want your names to start with? Enter * for random. ")
        if alitter == "*":
            end_string =  random.choice(name_starts) + "%"
        else:
            end_string = alitter.upper() + "%"
        if random_choice == 1:
            cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE FEMALE='YES' AND FIRST_NAME LIKE (?)", (end_string,))
            fn_list_pull = cursor.fetchall()
            cursor.execute(" SELECT LAST_NAME FROM last_names WHERE LAST_NAME LIKE (?)", (end_string,))
            ln_list_pull = cursor.fetchall()
            try:
                print(random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
                create_another_in_func(random_name_alit)
            except IndexError:
                print("No first/last name combinations beginning with that sequence exist.")
        elif random_choice ==2:
            cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE FEMALE='YES'AND FIRST_NAME LIKE (?)", (end_string,))
            fn_list_pull = cursor.fetchall()
            cursor.execute(" SELECT LAST_NAME FROM last_names WHERE LAST_NAME LIKE (?)", (end_string,))
            ln_list_pull = cursor.fetchall()
            try:
                print(random.choice(fn_list_pull) + " " + random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
                create_another_in_func(random_name_alit)
            except IndexError:
                print("No first/last name combinations beginning with that sequence exist.")
        elif random_choice ==3:
            cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE MALE='YES' AND FIRST_NAME LIKE (?)", (end_string,))
            fn_list_pull = cursor.fetchall()
            cursor.execute(" SELECT LAST_NAME FROM last_names WHERE LAST_NAME LIKE (?)", (end_string,))
            ln_list_pull = cursor.fetchall()
            try:
                print(random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
                create_another_in_func(random_name_alit)
            except IndexError:
                print("No first/last name combinations beginning with that sequence exist.")
        elif random_choice == 4:
            cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE MALE='YES' AND FIRST_NAME LIKE (?)", (end_string,))
            fn_list_pull = cursor.fetchall()
            cursor.execute(" SELECT LAST_NAME FROM last_names WHERE LAST_NAME LIKE (?)", (end_string,))
            ln_list_pull = cursor.fetchall()
            try:
                print(random.choice(fn_list_pull) + " " + random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
                create_another_in_func(random_name_alit)
            except IndexError:
                print("No first/last name combinations beginning with that sequence exist.")


def mf_name():
    while True:
        mf_choice = input("Would you like a female or male name? (F)emale / (M)ale ")
        if mf_choice.lower() == "f":
            cursor.execute(''' SELECT FIRST_NAME FROM first_names WHERE FEMALE="YES" ''')
            fn_list_pull = cursor.fetchall()
            break
        elif mf_choice.lower() == "m":
            cursor.execute(''' SELECT FIRST_NAME FROM first_names WHERE MALE="YES" ''')
            fn_list_pull = cursor.fetchall()
            break
        else:
            print("Please enter 'F' or 'M'!")
    while True:
        mn_choice = input("Would you like a middle name? Y / N ")
        if mn_choice.lower() == "y":
            cursor.execute(''' SELECT LAST_NAME FROM last_names ''')
            ln_list_pull = cursor.fetchall()
            print(random.choice(fn_list_pull) + " " + random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
            create_another_in_func(mf_name)
        elif mn_choice.lower() == "n":
            cursor.execute(''' SELECT LAST_NAME FROM last_names ''')
            ln_list_pull = cursor.fetchall()
            print(random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
            create_another_in_func(mf_name)
        else:
            print("Please enter 'Y' or 'N'!")


def mf_name_alit():
    random_choice = random.randrange(1, 2)
    while True:
        mf_choice = input("Would you like a random female or male alliterative name? F / M ")
        if mf_choice.lower() == "f" or mf_choice.lower() == "m":
            break
        else:
            print("Please enter 'F' or 'M'!")
    while True:
        alitter = input("What letter or letters do you want your names to start with? Enter * for random. ")
        if alitter == "*":
            end_string = random.choice(name_starts) + "%"
        else:
            end_string = alitter.upper() + "%"
        if random_choice == 1 and mf_choice.lower() == "f":
            cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE FEMALE='YES' AND FIRST_NAME LIKE (?)", (end_string,))
            fn_list_pull = cursor.fetchall()
            cursor.execute(" SELECT LAST_NAME FROM last_names WHERE LAST_NAME LIKE (?) ", (end_string,))
            ln_list_pull = cursor.fetchall()
            try:
                print(random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
                create_another_in_func(mf_name_alit)
            except IndexError:
                print("No first/last name combinations beginning with that sequence exist.")
        elif random_choice == 2 and mf_choice.lower() == "f":
            cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE FEMALE='YES' AND FIRST_NAME LIKE (?)", (end_string,))
            fn_list_pull = cursor.fetchall()
            cursor.execute(" SELECT LAST_NAME FROM last_names WHERE LAST_NAME LIKE (?) ", (end_string,))
            ln_list_pull = cursor.fetchall()
            try:
                print(random.choice(fn_list_pull) + " " + random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
                create_another_in_func(mf_name_alit)
            except IndexError:
                print("No first/last name combinations beginning with that sequence exist.")
        elif random_choice == 1 and mf_choice.lower() == "m":
            cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE MALE='YES' AND FIRST_NAME LIKE (?)", (end_string,))
            fn_list_pull = cursor.fetchall()
            cursor.execute(" SELECT LAST_NAME FROM last_names WHERE LAST_NAME LIKE (?) ", (end_string,))
            ln_list_pull = cursor.fetchall()
            try:
                print(random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
                create_another_in_func(mf_name_alit)
            except IndexError:
                print("No first/last name combinations beginning with that sequence exist.")
        elif random_choice == 2 and mf_choice.lower() == "m":
            cursor.execute(" SELECT FIRST_NAME FROM first_names WHERE MALE='YES' AND FIRST_NAME LIKE (?)", (end_string,))
            fn_list_pull = cursor.fetchall()
            cursor.execute(" SELECT LAST_NAME FROM last_names WHERE LAST_NAME LIKE (?) ", (end_string,))
            ln_list_pull = cursor.fetchall()
            try:
                print(
                    random.choice(fn_list_pull) + " " + random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
                create_another_in_func(mf_name_alit)
            except IndexError:
                print("No first/last name combinations beginning with that sequence exist.")


# ADDITIONAL FUNCTIONS

def create_another_in_func(func):
    while True:
        again = input("   \n"
                      "Would you like to create another or return to the main menu? (C)reate Another / (M)ain Menu ")
        if again.lower() == "c":
            func()
            break
        elif again.lower() == "m":
            main()
            break
        else:
            print("Please enter 'C' to create another or 'M' to return to the main menu!")


# DATABASE FUNCTION

def dbm_menu():
    while True:
        choose = input("What would you like to acces? \n"
                       "   (F)irst Names \n"
                       "   (L)ast Names \n"
                       "   (A)djectives \n"
                       "   (N)ouns \n"
                       "   (M)ain Menu \n"
                       "    ")
        if choose.lower() == "f":
            fn_gename_funcs()
        elif choose.lower() == "l":
            ln_gename_funcs()
        elif choose.lower() == "a":
            adj_funcs()
        elif choose.lower() == "n":
            nouns_funcs()
        elif choose.lower() == "m":
            main()
        else:
            print("Please enter one of the above options.")

def fn_insert_row():
    fn = input("What is the first name you want to enter? ")
    f_yn = input("Is this a female name? YES/NO ")
    m_yn = input("Is this a male name? YES/NO ")
    dup = cursor.execute('''  SELECT FIRST_NAME FROM first_names WHERE FIRST_NAME=(?)''', (fn,))
    x = dup.fetchall()
    if x == []: # checks if number of matching names blank, or, an empty list
        cursor.execute('''  INSERT INTO first_names (FIRST_NAME, FEMALE, MALE) 
            VALUES((?), (?), (?))''', (fn, f_yn, m_yn))
        genamenator_db.commit()
        print(fn + " has been added!")
    else:
        print("That name already exists.")


def ln_insert_row():
    ln = input("What is the surname you would like to enter? ")
    com = input("How common is this surname? COMMON / LESS COMMON / RARE ")
    dup = cursor.execute(''' SELECT LAST_NAME FROM last_names WHERE LAST_NAME=(?)''', (ln,))
    x = dup.fetchall()
    if x == []:
        cursor.execute(''' INSERT INTO last_names (LAST_NAME, COMMONALITY) VALUES((?), (?))''', (ln, com))
        genamenator_db.commit()
        print(ln + " has been added.")
    else:
        print("That name already exists.")


def adj_insert_row():
    adj = input("What adjective would you like to enter? ")
    dup = cursor.execute(''' SELECT ADJECTIVE FROM adjectives WHERE ADJECTIVE=(?)''', (adj,))
    x = dup.fetchall()
    if x== []:
        cursor.execute(''' INSERT INTO adjectives (ADJECTIVE) VALUES(?) ''', (adj,))
        genamenator_db.commit()
        print(adj + " has been added.")
    else:
        print("That name already exists.")


def noun_insert_row():
    noun = input("What noun would you like to enter? ")
    type = input("Is this classified as an occupation, or does it describe their personality? OCCUPATION / PERSONALITY ")
    dup = cursor.execute(''' SELECT NOUN FROM nouns WHERE NOUN=(?)''', (noun,))
    x = dup.fetchall()
    if x == []:
        cursor.execute(''' INSERT INTO nouns (NOUN, TYPE) VALUES(?, ?)''', (noun, type))
        genamenator_db.commit()
        print(noun + " has been added.")
    else:
        print("That name already exists.")


def fn_check_for_name():
    x = input("What name are you checking for? ")
    data = cursor.execute(''' SELECT FIRST_NAME FROM first_names WHERE FIRST_NAME=(?) ''', (x,))
    y = data.fetchall()
    if y == []:
        print("There is no %s!" % (x,))
    else:
        print("%s does exist!" % (x,))


def ln_check_for_name():
    x = input("What name are you checking for? ")
    data = cursor.execute(''' SELECT LAST_NAME FROM last_names WHERE LAST_NAME=(?) ''', (x,))
    y = data.fetchall()
    if y == []:
        print("There is no %s!" % (x,))
    else:
        print("%s does exist!" % (x,))


def check_for_adj():
    x = input("What adjective are you searching for? ")
    data = cursor.execute(''' SELECT ADJECTIVE FROM adjectives WHERE ADJECTIVE=(?) ''', (x,))
    y = data.fetchall()
    if y == []:
        print("There is no %s!" % (x,))
    else:
        print("%s does exist!" % (x,))


def check_for_noun():
    x = input("What noun are you searching for? ")
    data = cursor.execute(''' SELECT NOUN FROM nouns WHERE NOUN=(?)''', (x,))
    y = data.fetchall()
    if y == []:
        print("There is no %s!" % (x,))
    else:
        print("%s does exist!" % (x,))


def update_mf(): # changes the male/female columns from yes to no and vice versa
    while True:
        x = input("Which name do you want to update? ")
        y = input("Do you want to update FEMALE or MALE? ")
        if y == "FEMALE":
            y_yn = input("Do you want FEMALE to be YES or NO? " )
            cursor.execute(''' UPDATE first_names SET FEMALE=(?) WHERE FIRST_NAME=(?) ''', (y_yn, x))
            genamenator_db.commit()
            break
        elif y == "MALE":
            m_yn = input("Do you want MALE to be YES or NO?" )
            cursor.execute(''' UPDATE first_names SET MALE=(?) WHERE FIRST_NAME=(?)''', (m_yn, x))
            genamenator_db.commit()
            break
        else:
            print("Please enter your option as YES or NO.")


def update_commonality():
    while True:
        x = input("Which surname would you like to update the commonality of? ")
        find = cursor.execute(''' SELECT LAST_NAME FROM last_names WHERE LAST_NAME=(?) ''', (x,))
        y = find.fetchall()
        if y == []:
            print("That name does not exist. Please try another name.")
        else:
            while True:
                z = input("How common is this surname? COMMON / LESS COMMON / RARE ")
                if z == "COMMON" or "LESS COMMON" or "RARE":
                    cursor.execute(''' UPDATE last_names SET COMMONALITY=(?) WHERE LAST_NAME=(?)''', (z, x,))
                    genamenator_db.commit()
                    print(x + "has been updated.")
                    break
                else:
                    print("Please enter your option in the form of COMMON, LESS COMMON, or RARE")


def update_type():
    while True:
        x = input("Which noun would you like to update the type of? ")
        find = cursor.execute(''' SELECT NOUN FROM nouns WHERE NOUN=(?)''', (x,))
        y = find.fetchall()
        if y == []:
            print("That noun does not exist. Please try another noun.")
            break
        else:
            while True:
                z = input("What type of noun is it? OCCUPTION / PERSONALITY ")
                if z == "OCCUPATION" or "PERSONALITY":
                    cursor.execute(''' UPDATE nouns TYPE SET TYPE=(?) WHERE NOUN=(?)''', (z, x,))
                    break
                else:
                    print("Please enter your option in the form of OCCUPATION or PERSONALITY.")


def fn_delete_name():
    x = input("What name would you like to delete? ")
    find = cursor.execute(''' SELECT FIRST_NAME FROM first_names WHERE FIRST_NAME=(?)''', (x,))
    y = find.fetchall()
    if y == []:
        print("That name does not exist.")
    else:
        cursor.execute(''' DELETE from first_names WHERE FIRST_NAME=(?) ''', (x,))
        genamenator_db.commit()
        print("%s has been deleted." % x)


def ln_delete_name():
    x = input("What surname would you like to delete? ")
    find = cursor.execute(''' SELECT LAST_NAME FROM last_names WHERE LAST_NAME=(?)''', (x,))
    y = find.fetchall()
    if y == []:
        print("That name does not exist.")
    else:
        cursor.execute(''' DELETE FROM last_names WHERE LAST_NAME=(?) ''', (x,))
        genamenator_db.commit()
        print("%s has been deleted." % x)


def delete_adj():
    x = input("What adjective would you like to delete? ")
    cursor.execute(''' DELETE FROM adjectives WHERE ADJECTIVE=(?)''', (x,))
    genamenator_db.commit()


def delete_noun():
    x = input("What noun would you like to delete? ")
    cursor.execute(''' DELETE FROM nouns WHERE NOUN=(?)''', (x,))
    genamenator_db.commit()


def fn_gename_funcs():
    while True:
        func_cho = input("\n"
                         "What would you like to do? \n"
                         "   (1) Check if a name exists \n"
                         "   (2) Add a new name \n"
                         "   (3) Delete a name \n"
                         "   (4) Update the associated genders of a name \n"
                         "    ")
        if func_cho == '1':
            fn_check_for_name()
        elif func_cho == '2':
            fn_insert_row()
        elif func_cho == '3':
            fn_delete_name()
        elif func_cho == '4':
            update_mf()
        else:
            print("Please choose an option.")


def ln_gename_funcs():
    while True:
        func_cho = input("\n"
                         "What would you like to do? \n"
                         "   (1) Check if a surname exists \n"
                         "   (2) Add a new surname \n"
                         "   (3) Delete a surname \n"
                         "   (4) Updated the commonality of a surname \n")
        if func_cho == "1":
            ln_check_for_name()
        elif func_cho == "2":
            ln_insert_row()
        elif func_cho == "3":
            ln_delete_name()
        elif func_cho == "4":
            update_commonality()
        else:
            print("Please choose an option.")


def adj_funcs():
    while True:
        func_cho = input("What would you like to do? \n"
                       "   (1) Check if an adjective exists \n"
                       "   (2) Insert a new adjective \n"
                       "   (3) Delete an adjective ")
        if func_cho == "1":
            check_for_adj()
        elif func_cho == "2":
            adj_insert_row()
        elif func_cho == "3":
            delete_adj()
        else:
            print("Please choose an option.")


def nouns_funcs():
    while True:
        func_cho = input("What would you like to do? \n"
                       "   (1) Check if an noun exists \n"
                       "   (2) Insert a new noun \n"
                       "   (3) Delete an adjective \n"
                       "   (4) Change the type of noun ")
        if func_cho == "1":
            check_for_noun()
        if func_cho == "2":
            noun_insert_row()
        if func_cho == "3":
            delete_noun()
        if func_cho == "4":
            update_type()

main()