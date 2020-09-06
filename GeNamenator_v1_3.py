import random
import sqlite3

genamenator_db = sqlite3.connect('GeNamenator_DB.db')
cursor = genamenator_db.cursor()
cursor.row_factory = lambda cursor, row: row[0]
cursor.fetchall()

print("GeNamenator, version 1.3")
print("by David Margis, 2020")
print()


def mf_name():
    while True:
        mf_choice = input("Would you like a female, male, or any name? (F)emale / (M)ale / (A)ny ")
        if mf_choice.lower() == "f":
            cursor.execute(''' SELECT FIRST_NAME FROM first_names WHERE FEMALE="YES" ''')
            fn_list_pull = cursor.fetchall()
            break
        elif mf_choice.lower() == "m":
            cursor.execute(''' SELECT FIRST_NAME FROM first_names WHERE MALE="YES" ''')
            fn_list_pull = cursor.fetchall()
            break
        elif mf_choice.lower() == "a":
            rando_opt = (1, 2)
            if random.choice(rando_opt) == 1:
                cursor.execute(''' SELECT FIRST_NAME FROM first_names WHERE FEMALE="YES" ''')
                fn_list_pull = cursor.fetchall()
                break
            elif random.choice(rando_opt) == 2:
                cursor.execute(''' SELECT FIRST_NAME FROM first_names WHERE MALE="YES"  ''')
                fn_list_pull = cursor.fetchall()
                break
        else:
            print("Please enter 'F', 'M', or 'A'!")
    while True:
        mn_choice = input("Would you like a middle name? Y / N ")
        if mn_choice.lower() == "y":
            cursor.execute(''' SELECT LAST_NAME FROM last_names ''')
            ln_list_pull = cursor.fetchall()
            print(random.choice(fn_list_pull) + " " + random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
            break
        elif mn_choice.lower() == "n":
            cursor.execute(''' SELECT LAST_NAME FROM last_names ''')
            ln_list_pull = cursor.fetchall()
            print(random.choice(fn_list_pull) + " " + random.choice(ln_list_pull))
            break
        else:
            print("Please enter 'Y' or 'N'!")


def create_another():
    while True:
        anoth = input("Would you like to create another? Y / N ")
        if anoth.lower() == "y":
            mf_name()
        elif anoth.lower() == "n":
            print("Thank you fur using GeNamenator!")
            break
        else:
            print("Please enter 'Y' or 'N'!")


mf_name()
create_another()