# GeNamerator v1.1, by David Margis
# generates a random name and occupation for fictional comedic purposes

import random

first_name_M = ('Rutiger', 'Bob', 'Gus', 'Frank', 'Harvey', 'Tod', 'Archibald', 'Jerry', 'Lenny', 'Guy', 'Guy', 'Jack', 'Jack', 'Jack', 'Johnny', 'Jim', 'Kevin', 'Vladimir', 'Guiseppe', 'Wolfgang', 'Dirk', 'William', 'Bill', 'Billy', 'Art', 'Johann', 'Ken', 'Rick', 'Richard', 'Dick', 'Armand', 'Roger', 'Hunter', 'Mark', 'Hans', 'Derrick', 'Sean', 'Seamus', 'Stewart', 'Stu', 'Jeremiah', 'Clint', 'Clark')
first_name_F = ('May', 'Sarah', 'Amanda', 'Jessica', 'Megan', 'Meg', 'Sadie', 'Beth', 'Gertrude', 'Ethel', 'Marianne', 'Helen', 'Yoko', 'Peggy', 'Jennifer', 'Jenny', 'Jenny', 'Scarlett', 'Natasha', 'Wilma', 'Holly', 'Juanita', 'Petra', 'Magda', 'Ashley', 'Hortense', 'Amy', 'Elizabeth', 'Jane', 'Madison', 'Lucinda', 'Kelly', 'Cathleen', 'Kat', 'Katherine', 'Gwen', 'Flora', 'Carolina')
last_name = ('Johnson', 'Jackson', 'McMillan', 'McCool', 'Steak', 'Wellington', 'Horowitz', 'Harvey', 'Franklin', 'Dooley', 'Gunner', 'Deathrage', 'Grant', 'Caravalli', 'Horses', 'Merman', 'Sanchez', 'Fernendez', 'Anderson', 'Williams', 'Grabelski', 'Trotsky', 'Levin', 'Jones', 'Stryker', 'Hunter', 'Gormley', 'Mushashi', 'Florida', 'Beefley', 'Appleseed', 'Studebaker', 'Scooter', 'Zimmer', 'Delbacher', 'Delbrook', 'Frankenheimer', 'Lavezzo', 'Hunter')
middle_initial = ('A.', 'J.', 'Q.', 'P.', 'X.', 'T.')
no_middle_initial = ("", "", "", "", "", "", "", "", "", "", "")
adjective = ('Professional', 'Amateur', 'Master', 'Private', 'Secret', 'Avid', 'Local', 'Renegade')
occupation = ('Detective', 'Private Eye', 'Solder of Fortune', 'Cop', 'Investigative Reporter', 'Carpenter', 'Ninja', 'Accountant', 'Auditor', 'Bookkeeper', 'Mariner', 'Immunologist', 'Photographer', 'Professional', 'Birdwatcher', 'Scientist', 'Astronaut', 'Cosmonaut', 'Electrician', 'Chef', 'Programmer', 'Ornithologist', 'Customer Service Rep', 'Pilot')

random_first_name = (first_name_M + first_name_F)
random_middle = (middle_initial + no_middle_initial)

def generator():
    while True:
        comp_rando = input("Do you want to generate a completely random character? Choose 'N' to see more options! Y/N ")
        if comp_rando.lower() == "y":
            print(random.choice(random_first_name) + " " + random.choice(random_middle) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))
            break
        elif comp_rando.lower() == "n":
            m_or_f = input("Do you want a male or female? M/F ")
            mid_init_choice = input("Do you want a middle initial? Y/N ")
            if m_or_f.lower() == "m" and mid_init_choice.lower() == "y":
                print(random.choice(first_name_M) + " " + random.choice(middle_initial) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))
                break
            elif m_or_f.lower() == "m" and mid_init_choice.lower() == "n":
                print(random.choice(first_name_M) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))
                break
            elif m_or_f.lower() == "f" and mid_init_choice.lower() == "y":
                print(random.choice(first_name_F) + " " + random.choice(middle_initial) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))
                break
            elif m_or_f.lower() == "f" and mid_init_choice.lower() == "n":
                print(random.choice(first_name_F) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))
                break
            else:
                print("Please enter Y or N!")
        else:
            print("Please enter Y or N!")

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

print("GeNamenator, version 1.1")
print("by David Margis, 2020")
print()

generator()
run_again()