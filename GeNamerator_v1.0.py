import random

first_name_M = ('Bob', 'Gus', 'Frank', 'Harvey', 'Tod', 'Archibald', 'Jerry', 'Lenny', 'Guy', 'Guy', 'Jack', 'Jack', 'Jack', 'Johnny', 'Jim', 'Vladimir', 'Guiseppe', 'Wolfgang', 'Dirk', 'William', 'Bill', 'Billy', 'Art', 'Johann', 'Ken', 'Rick', 'Richard', 'Dick', 'Armand', 'Roger', 'Hunter', 'Mark', 'Hans', 'Derrick', 'Sean', 'Seamus', 'Jeremiah', 'Clint', 'Clark')
first_name_F = ('May', 'Sarah', 'Amanda', 'Jessica', 'Megan', 'Meg', 'Sadie', 'Beth', 'Gertrude', 'Ethel', 'Marianne', 'Helen', 'Yoko', 'Peggy', 'Jennifer', 'Jenny', 'Jenny', 'Scarlett', 'Natasha', 'Wilma', 'Holly', 'Juanita', 'Petra', 'Magda', 'Ashley', 'Hortense', 'Amy', 'Elizabeth', 'Jane', 'Madison', 'Lucinda', 'Kelly', 'Cathleen', 'Kat', 'Katherine')
last_name = ('Johnson', 'Jackson', 'McMillan', 'McCool', 'Steak', 'Wellington', 'Horowitz', 'Harvey', 'Franklin', 'Dooley', 'Gunner', 'Deathrage', 'Grant', 'Caravalli', 'Horses', 'Merman', 'Sanchez', 'Fernendez', 'Anderson', 'Williams', 'Grabelski', 'Trotsky', 'Levin', 'Jones', 'Stryker', 'Hunter', 'Gormley', 'Mushashi', 'Florida', 'Beefley', 'Appleseed')
middle_initial = ('A.', 'Q.', 'P.', 'X', 'T.')
adjective = ('Professional', 'Amatuer', 'Master', 'Private', 'Secret', 'Avid', 'Local', 'Renegade')
occupation = ('Detective', 'Private Eye', 'Solder of Fortune', 'Cop', 'Investigative Reporter', 'Carpenter', 'Ninja', 'Accountant', 'Mariner', 'Professional', 'Birdwatcher', 'Scientist', 'Astronaut', 'Cosmonaut', 'Electrician', 'Chef', 'Programmer', 'Ornithologist', 'Customer Service Rep', 'Pilot')



def game():
    m_or_f = input("Do you want a male or female? M/F ")
    mid_init_choice = input("Do you want a middle initial? Y/N ")
    if m_or_f == "M" and mid_init_choice == "Y":
        print(random.choice(first_name_M) + " " + random.choice(middle_initial) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))
    elif m_or_f == "M" and mid_init_choice == "N":
        print(random.choice(first_name_M) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))
    elif m_or_f == "F" and mid_init_choice == "Y":
        print(random.choice(first_name_F) + " " + random.choice(middle_initial) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))
    else:
        print(random.choice(first_name_F) + " " + random.choice(last_name) + ", " + random.choice(adjective) + " " + random.choice(occupation))

def play_again():
    cont_game = True
    while cont_game == True:
        play_again = input("Would you like to play again? Y/N ")
        if play_again == "Y" and cont_game == True:
            game()
        else:
            print("Enjoy your fictional character!")
            cont_game = False

game()
play_again()
