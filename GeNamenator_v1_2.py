# GeNamerator v1.2, by David Margis
# generates a random name and occupation for fictional comedic purposes

import random

first_name_m = ('Rutiger', 'Bob', 'Gus', 'Dean', 'Frank', 'Harvey', 'Tod', 'Archibald', 'Jerry', 'Lenny', 'Charles', 'Charlie', 'Chuck', 'Guy', 'Guy', 'Jack', 'Jack', 'Jack', 'Johnny', 'James', 'Jim', 'Kevin', 'Vladimir', 'Guiseppe', 'Wolfgang', 'Dirk', 'William', 'Bill', 'Billy', 'Art', 'Johann', 'Ken', 'Rick', 'Richard', 'Dick', 'Armand', 'Roger', 'Hunter', 'Mark', 'Hans', 'Derrick', 'Sean', 'Seamus', 'Stewart', 'Stu', 'Jeremiah', 'Clint', 'Clark', 'Sam', 'Samuel', 'Max', 'Maximillian', 'Maxwell')
first_name_f = ('Dana', 'Diana', 'May', 'Sarah', 'Amanda', 'Jessica', 'Megan', 'Meg', 'Hillary', 'Sadie', 'Beth', 'Haley', 'Hayley', 'Gertrude', 'Ethel', 'Marianne', 'Helen', 'Yoko', 'Peggy', 'Jennifer', 'Jenny', 'Jenny', 'Scarlett', 'Natasha', 'Wilma', 'Holly', 'Juanita', 'Petra', 'Magda', 'Ashley', 'Hortense', 'Amy', 'Elizabeth', 'Jane', 'Madison', 'Lucinda', 'Kelly', 'Cathleen', 'Kat', 'Katherine', 'Gwen', 'Flora', 'Carolina', 'Samantha', 'Sam', 'Maxine', 'Nicole')
first_name_any = ('Avery', 'Bailey', 'Blake', 'Cameron', 'Cary', 'Chris', 'Drew', 'Morgan', 'Shannon', 'Kay', 'Lane', 'Lindsay', 'Lindsey', 'Leslie', 'Lesley', 'Riley', 'Shelby', 'Tracy', 'Terry', 'Parker', 'Marian')
last_name = ('Johnson', 'Jackson', 'McMillan', 'McCool', 'Steak', 'Wellington', 'Horowitz', 'Harvey', 'Franklin', 'Dooley', 'Gunner', 'Deathrage', 'Grant', 'Caravalli', 'Horses', 'Merman', 'Sanchez', 'Fernendez', 'Anderson', 'Williams', 'Grabelski', 'Trotsky', 'Levin', 'Jones', 'Stryker', 'Hunter', 'Gormley', 'Mushashi', 'Florida', 'Beefley', 'Appleseed', 'Studebaker', 'Scooter', 'Zimmer', 'Delbacher', 'Delbrook', 'Frankenheimer', 'Lavezzo', 'Hunter', 'Roosevelt', 'Washington')
middle_init = ('A.', 'J.', 'Q.', 'P.', 'X.', 'T.', 'A.', 'J.', 'Q.', 'P.', 'X.', 'T.')
middle_blank = ("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
adjective = ('Professional', 'Amateur', 'Master', 'Private', 'Secret', 'Avid', 'Local', 'Renegade')
occupation = ('Detective', 'Detective', 'Detective', 'Private Eye', 'Solder of Fortune', 'Cop', 'Cop', 'Cop', 'Bounty Hunter', 'Bounty Hunter', 'Bounty Hunter', 'Investigative Reporter', 'Carpenter', 'Ninja', 'Accountant', 'Auditor', 'Bookkeeper', 'Mariner', 'Immunologist', 'Photographer', 'Professional', 'Birdwatcher', 'Scientist', 'Astronaut', 'Cosmonaut', 'Electrician', 'Chef', 'Programmer', 'Ornithologist', 'Customer Service Rep', 'Pilot', 'Blacksmith')

first_names = (first_name_m + first_name_f + first_name_any)
middle_all = (middle_init + middle_blank)

def generator():
    while True:
        m_or_f = input("Pick a gender, or choose 'A' for any. F/M/A ")
        if m_or_f.lower() == "f":
            input_first = first_name_f + first_name_any
            break
        elif m_or_f.lower() == "m":
            input_first = first_name_m + first_name_any
            break
        elif m_or_f.lower() == "a":
            input_first = first_names
            break
        else:
            print("Please enter 'F', 'M', or 'A'!")
    while True:
        m_n = input("Do you want a middle name? Choose 'A' for random. Y/N/A ")
        if m_n.lower() == "y":
            input_middle = str(random.choice(middle_init + input_first) + " ")
            break
        elif m_n.lower() == "n":
            input_middle = ""
            break
        elif m_n.lower() == "a" and m_or_f.lower() == "a":
            input_middle = str(random.choice(input_first + middle_all) + " ")
            break
        else:
            print("Please enter 'F', 'M', or 'A'!")
    while True:
        occu = input("Do you want an occupation? Y/N ")
        if occu.lower() == "y":
            add_occu = str(", " + random.choice(adjective) + " " + random.choice(occupation))
            break
        elif occu.lower() == 'n':
            add_occu = ""
            break
        else:
            print("Please enter 'Y' or 'N'!")
    print(random.choice(input_first) + " " + input_middle + random.choice(last_name) + add_occu)

def run_again():
    while True:
        play_again = input("Would you like to create another? Y/N ")
        if play_again.lower() == "y":
            generator()
        elif play_again.lower() == 'n':
            print("Enjoy your fictional character!")
            break
        else:
            print("Please enter Y or N!")

print("GeNamenator, version 1.2")
print("by David Margis, 2020")
print()

generator()
run_again()