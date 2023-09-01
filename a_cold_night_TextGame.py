##I begin by creating a function that returns an input so the user has to press enter in order to print the next line.
#This allows it so python does not print out all the dialogue at one time until the next input 
def pressEnter():
    return input("Press enter to continue: ")
#I do use the basic print to print out my story lines in the terminal 
print("A Cold Night\n")  
pressEnter()
print('''RULES: 
1. After reading a line you must press enter to print out the next line
2. When it comes to make a decision you will only have two options.
Please type one of the two options given to move ahead in the story.
      For example:
            Should he/she run? yes or no:
            You can only type "yes" or "no" as an answer either wise you get an error to retype answer
3. I hope you enjoy the story :)\n''')
pressEnter()
###I now use a while loop to prevent the user from typing any output for the given inputs.
##If a user puts in a wrong output it raises an error and prints out a message and the user has to put in a new output 
#untill it meets the input requirements
while True:
    try: 
        character_name = input("Enter your character name (max 8 characters long): ")
        #Check if the input is a number (int or float)
        if character_name.isdigit() or (character_name.replace('.', '', 1).isdigit()):
            raise ValueError("Name cannot be a number")
        #Check if the input is longer than 8 characters
        if len(character_name) > 8:
            raise ValueError("Name cannot be longer than 8 characters")
        if character_name == "":
            raise ValueError("Name can not be empty")
        character_name = character_name.capitalize()        
    except ValueError as exception1:
        print("\nInvalid name:", exception1)
        continue
    else:
        break
#I use another while loop for another input
while True:
    try:
        character_gender = input("\nIs your character a male or female: ")
        #The only options the user can put for this input is "male" or "female"
        if character_gender != "male" and character_gender != 'female': 
            raise ValueError
    except ValueError:
        print("\nGender entered is not male or female: For the sake of the project, the game only excepts male or female")
        continue
    else:
        break
###I created a dictionary for the user character name and pronouns. This allows me to easily call up the user character name
##and assign the character its pronouns based on the user character gender.
#I leave the pronoun keys empty to give them a value based on the user character gender
character_traits = {"name":character_name, "pro_noun1": "", "pro_noun2": "", "pro_noun3": ""}
#I asaign the keys its values of the pronouns based on the character gender
if character_gender == 'male':
    character_traits["pro_noun1"] = 'him'
    character_traits["pro_noun2"] = "his"
    character_traits["pro_noun3"] = "he"
else:
    character_traits["pro_noun1"] = 'her'
    character_traits["pro_noun2"] = "her"
    character_traits["pro_noun3"] = "she"

print("""\nDate: Thursday, October 26, 1995
Weather: 57°F
Time: 11:43 PM\n""")
pressEnter()
#I used an f-string to call up the character traits in the dictionary for the lines of the story
line1 = f'''Narrator: Enclosed in {character_traits["pro_noun2"]} bedroom, {character_traits["name"]} is laying in {character_traits["pro_noun2"]} bed 
playing {character_traits["pro_noun2"]} gameboy.'''
print(line1, '\n')
pressEnter()
line2 = f'''Narrator: {character_traits["pro_noun2"].capitalize()} window is slightly open letting in a small breeze.'''
print(line2, '\n')
pressEnter()
line3 = f'''Narrator: Playing {character_traits["pro_noun2"]} gameboy, {character_traits["name"]} starts to hear footsteps approaching {character_traits["pro_noun2"]} room.'''
print(line3,'\n')
pressEnter()
print("*tip, tap, tip, tap, tip, tap*\n")
pressEnter()
print("Narrator: The footsteps get louder at every step.\n")
pressEnter()
print('*TIP, TAP, TIP, TAP, TIP, TAP*\n')
pressEnter()
print('Narrator: Suddenly the footsteps stop.\n')
pressEnter()
print('...\n')
pressEnter()
print('*knock, knock, knock*\n')
pressEnter()
#Another while loop for the 1st user game decision 
while True:
    try:
        game_decision1 = input('Do you let the person in? yes or no: \n')
        if game_decision1 != 'yes' and game_decision1 != 'no':
            raise ValueError
    except ValueError:
        print('\nYour answer was neither yes or no. Please type yes or no')
        continue
    else:
        break
##I created line 5 outside the "if" statement because this line will be used again outside the "if" statement.
#If I was to create it inside the "if" statement, I wont be able to use it outside the "if" stament 
line5 = f'''Narrator: It's {character_traits["name"]} mom.''' ##line114 and line 134

#Created an "if", "else" statement so diffrent lines are printed based on the user game decision 
if game_decision1 == "yes":
    line4 = f'''{character_traits["name"]}: Come in.'''
    print(line4,"\n")
    pressEnter()
    print("Narrator: The door slowly opens.\n")
    pressEnter()
    print("...\n")
    pressEnter()
    print(line5,"\n")
    pressEnter()
else:
    #'added lines' are lines I forgot to put after finshing the project and rereading the story 
    added_line1 = f'Narrator: {character_traits["name"]} looks at {character_traits["pro_noun2"]} door in silence.'
    print(added_line1,"\n")
    pressEnter()
    print("*knock, knock, knock*\n")
    pressEnter()
    added_line2 = f'Narrator: {character_traits["name"]} continues to stare at {character_traits["pro_noun2"]} door.'
    print(added_line2,"\n")
    pressEnter()
    print("...\n")
    pressEnter()
    print("Narrator: The knocking stops.\n")
    pressEnter()
    print("Narrator: The door slowly opens.\n")
    pressEnter()
    print("...\n")
    pressEnter()
    print(line5,"\n")
    pressEnter()
    line6 = f'''Mom: It's not a monster it's just me {character_traits["name"]}.'''
    print(line6,"\n")
    pressEnter()
    line7 = f'''Narrator: {character_traits["name"]} takes a sigh of relif.'''
    print(line7,"\n")
    pressEnter()
line8 = f'''Mom: Time to go to sleep {character_traits["name"]}, it's not the weekend yet.'''
print(line8,"\n")
pressEnter()
line9 = f'{character_traits["name"]}: Ok mom.'
print(line9,"\n")
pressEnter()
line10 = f'''Narrator: {character_traits["name"]} turns off {character_traits["pro_noun2"]} gameboy and puts it on {character_traits["pro_noun2"]} nightstand.'''
print(line10,"\n")
pressEnter()
line11 = f'''Narrator: {character_traits["name"]} mom goes to turn off the light.'''
print(line11,"\n")
pressEnter()
line12 = f'{character_traits["name"]}: WAIT!'
print(line12,"\n")
pressEnter()
line13 = f'{character_traits["name"]}: Can you check if there are any monsters.'
print(line13,'\n')
pressEnter()
line14 = f'''Narrator: {character_traits["name"]} mother quickly looks around the room to find no monsters in sight.'''
print(line14,"\n")
pressEnter()
line15 = f'Narrator: {character_traits["name"]} is relieved.'
print(line15,"\n")
pressEnter()
line16 = f'''Narrator: {character_traits["name"]} mother kisses {character_traits["pro_noun1"]} on the head and wishes {character_traits["pro_noun1"]} a goodnight.'''
print(line16,"\n")
pressEnter()
#Another while loop for another game decision
while True:
    try:
        game_decision2 = input("Say goodnight back? yes or no: \n")
        if game_decision2 != "yes" and game_decision2 != "no":
            raise ValueError
    except ValueError:
        print('\nYour answer was neither yes or no. Please type yes or no')
        continue
    else:
        break
#Another "if", "else" statement to print diffrent lines based on user decision
if game_decision2 == "yes":
    line17 = f'{character_traits["name"]}: Goodnight mom.'
    print(line17,"\n")
    pressEnter()
    line18 = f'Narrarator: As {character_traits["name"]} mom goes to leave the room, she looks up at {character_traits["name"]}.'
    print(line18,"\n")
    pressEnter()
    print("Mom: Remember to close your window, you don't want any monsters coming in.\n")
    pressEnter()
    line19 = f'Narrator: {character_traits["name"]} gets up to close {character_traits["pro_noun2"]} window.'
    print(line19,"\n")
    pressEnter()
    print("*shut*\n")
    pressEnter()
    line20 = f'''Narrator: With {character_traits["name"]} window now close, {character_traits["name"]} mom turns off the light and
she exits the room closing the door behind her.'''
    print(line20,"\n")
    pressEnter()
else: 
    line21 = f'''Narrator: {character_traits["name"]} mom slgihtly frowns and turns off the light.
She exits the room closing the door behind her.'''
    print(line21,"\n")
    pressEnter()

print('''Date: Thursday, October 26, 1995
Weather: 55°F
Time: 11:49 PM\n''')
pressEnter()   
line22 = f'Narrator: {character_traits["name"]} closes {character_traits["pro_noun2"]} eyes and tries to go to sleep.'
print(line22,"\n")
pressEnter()
print("Narrator: The wind outside has picked up.\n")
pressEnter()
#defining lines outside the "if" statement so I can use those lines outside the "if" statement
line35 = f'Narrator: {character_traits["name"]} calls {character_traits["pro_noun2"]} mom but to no response, {character_traits["pro_noun2"]} mom is probably in the shower.'
line37 = f'Narrator: {character_traits["name"]} gets up and slowly walks towards {character_traits["pro_noun2"]} window.'
#Another "if", "else" statement to print diffrent lines based on the user previous decision
if game_decision2 == "yes":
    line33 = f'''Narrator: The strength of the wind outside has caused the trees to rustle.'''
    print(line33,"\n")
    pressEnter()
    line34 = f'''Narrator: {character_traits["name"]} is frightned by the noise outside and can't decide if {character_traits["pro_noun3"]} should 
call {character_traits["pro_noun2"]} mom into {character_traits["pro_noun2"]} room or look out the window {character_traits["pro_noun1"]}self.'''
    print(line34,"\n")
    pressEnter()
    ##I created a while loop inside the "if" statement because based on the user pervious decision they will recieve a 
    #diffrent input 
    while True:
        try:
            game_decision3A = input(f'''Call {character_traits["name"]} mom into {character_traits["pro_noun2"]} room or let {character_traits["name"]} check the window {character_traits["pro_noun1"]}self? 
call mom or check window: \n''')
            if game_decision3A != "call mom" and game_decision3A != "check window":
                raise ValueError
        except ValueError:
            print("\nYour answer was neither call mom or check window. Please type call mom or check window")
            continue
        else: 
            break
    if game_decision3A == "call mom":
        print(line35,"\n")
        pressEnter()
        line36 = f'Narrator: {character_traits["name"]} has no other option but to check the window.'
        print(line36,"\n")
        pressEnter()
    print(line37,"\n")
    pressEnter()
    line38 = f'''Narrator: As {character_traits["name"]} looks out the window to see where the noise is coming from,
{character_traits["pro_noun3"]} sees a monstrous figure out {character_traits["pro_noun2"]} window looking up at {character_traits["pro_noun1"]}.'''
    print(line38,"\n")
    pressEnter()
if game_decision2 == "no":
    line39 = f'''Narrator: The cold air from the outside enters {character_traits["pro_noun2"]} room through the open window'''
    print(line39,"\n")
    pressEnter()
    line40 = f'Narrator: {character_traits["name"]} forgot to close the window before {character_traits["pro_noun2"]} mom left {character_traits["pro_noun2"]} room.'
    print(line40,"\n")
    pressEnter()
    line41 = f'''Narrator: The cold air from the outside begins to fill up in {character_traits["name"]}'s room.'''
    print(line41,"\n")
    pressEnter()
    line42 = f'Narrator: {character_traits["name"]} begins to feel cold and is frighten to close the window by {character_traits["pro_noun1"]}self.'
    print(line42,"\n")
    pressEnter()
    line43 = f'''Narrator: {character_traits["name"]} cant decide if {character_traits["pro_noun3"]} should call {character_traits["pro_noun2"]} mom into {character_traits["pro_noun2"]} room to help {character_traits["pro_noun1"]} close the window or 
close the window by {character_traits["pro_noun1"]}self.'''
    print(line43,"\n")
    pressEnter()
    #Another while loop inside the "if" statement because the user pervious decision they will decide what input they will recieve 
    while True:
        try:
            game_decision3B = input(f'''Should {character_traits["name"]} call {character_traits["pro_noun2"]} mom into {character_traits["pro_noun2"]} room or close the window {character_traits["pro_noun1"]}self?
call mom or close window: \n''')
            if game_decision3B != "call mom" and game_decision3B != "close window":
                raise ValueError
        except ValueError:
            print("\nYour answer was neither call mom or close window. Please type call mom or close window")
            continue
        else:
            break
    if game_decision3B == "call mom":
        print(line35,"\n")
        pressEnter()
        line44 = f'Narrator: {character_traits["name"]} has no other option but to close the window.'
        print(line44,"\n")
        pressEnter()
    print(line37,"\n")
    pressEnter()
    line45 = f'Narrator: {character_traits["name"]} closes the window.'
    print(line45,"\n")
    pressEnter()
    print("*shut*\n")
    pressEnter()
    line46 = f'''Narrator: With the window now shut, {character_traits["name"]} takes a quick look out the window 
and sees a monstrous figure out {character_traits["pro_noun2"]} window looking up at {character_traits["pro_noun1"]}.'''
    print(line46,"\n")
    pressEnter()
print('''Date: Thursday, October 26, 1995
Weather: 56°F
Time: 11:53 PM\n''')
pressEnter()

line47 = f'Narrator: In shock, {character_traits["name"]} stares at the monstrous figure in the dark and the monstrous figure stares right back at {character_traits["pro_noun1"]}.'
print(line47,"\n")
pressEnter()
print("...\n")
pressEnter()
print("Narrator: The only sound that can be heard is the clock on the wall.\n")
pressEnter()
print("*tick, tick, tick*\n")
pressEnter()
line48 = f'Narrator: A chill goes down {character_traits["name"]} spine.'
print(line48,"\n")
pressEnter()
print('''Date: Thursday, October 26, 1995
Weather: 53°F
Time: 11:55 PM\n''')
pressEnter()
line49 = f'''Narrator: Looking at the monstrous figure in the dark, {character_traits["name"]} cant decide if {character_traits["pro_noun3"]} should 
turn on the light in {character_traits["pro_noun2"]} room or stand still staring at the monstrous figure until morning.'''
print(line49,"\n")
pressEnter()
#Another while loop for another game decision
while True:
    try:
        game_decision4 = input(f'''Should {character_traits["name"]} turn on the light in {character_traits["pro_noun2"]} room, or stand still till morning? 
turn on light or stand still: \n''')
        if game_decision4 != "turn on light" and game_decision4 != "stand still":
            raise ValueError
    except ValueError:
        print("\nYour answer was neither turn on light or stand still. Please type turn on light or stand still")
        continue
    else: 
        break
#defining lines outside the "if" statement so i can reuse them outside the "if" statement
line54 = "Narrator: All that is seen outside is a garbage can with a jack-o-lattern on top of it.\n"
line55 = "Narrator: There was no monster, it was just a garbage can.\n"
line57 = "THE END."
if game_decision4 == "turn on light":
    line50 = f'Narrator: {character_traits["name"]} takes in a deep breath.'
    print(line50,"\n")
    pressEnter()
    line51 = f'Narrator: {character_traits["name"]} quickly runs towards the other side of {character_traits["pro_noun2"]} room and turns on the light.'
    print(line51,"\n")
    pressEnter()
    print("*flick*\n")
    pressEnter()
    line52 = f'Narrator: {character_traits["name"]} quickly runs back to the window.'
    print(line52,"\n")
    pressEnter()
    line53 = f'Narrator: Looking out the window with the light now on, {character_traits["name"]} no longer sees the monstrous figure.'
    print(line53,"\n")
    pressEnter()
    print(line54)
    pressEnter()
    print(line55)
    pressEnter()
    line56 = f'Narrator: {character_traits["name"]} is relieved that there was no actually monster outside and goes back to bed.'
    print(line56,"\n")
    pressEnter()
    print(line57)
if game_decision4 == "stand still":
    line58 = f'Narrator: {character_traits["name"]} stands still looking out the window at the monstrous figure.'
    print(line58,"\n")
    pressEnter()
    print('''Date: Thursday, October 26, 1995
Weather: 51°F
Time: 12:38 AM\n''')
    pressEnter()
    print('Narrator: The monstrous figure has not moved an inch.\n')
    pressEnter()
    line59 = f'Narrator: {character_traits["name"]} contiunes to stand still looking at the monstrous figure outside.'
    print(line59,"\n")
    pressEnter()
    print('''Date: Thursday, October 26, 1995
Weather: 49°F
Time: 2:56 AM\n''')
    pressEnter()
    line60 = f'Narrator: {character_traits["name"]} nor the monstrous figure has moved.'
    print(line60,"\n")
    pressEnter()
    line61 = f'Narrator: {character_traits["name"]} beigns to feel tired.'
    print(line61,"\n")
    pressEnter()
    print('''Date: Thursday, October 26, 1995
Weather: 52°F
Time: 4:23 AM\n''')
    pressEnter()
    line62 = f'Narrator: {character_traits["name"]} continues to stand still and so does the monstrous figure outside.'
    print(line62,"\n")
    pressEnter()
    line63 = f'Narrator: {character_traits["name"]} is struggling to keep {character_traits["pro_noun2"]} eyes open.'
    print(line63,"\n")
    pressEnter()
    print('''Date: Thursday, October 26, 1995
Weather: 54°F
Time: 6:17 AM\n''')
    pressEnter()
    print("Narrator: The sun begins to rise and shine light outside.\n")
    pressEnter()
    print("Narrator: The monstrous figure is gone.\n")
    pressEnter()
    print(line54)
    pressEnter()
    print(line55)
    pressEnter()
    line64 = f'Mom: {character_traits["name"]} get ready for school, the bus is almost here.'
    print(line64,"\n")
    pressEnter()
    line65 = f'Narrator: With {character_traits["name"]} eyes struggling to stay open, {character_traits["pro_noun3"]} falls down to the ground and goes to sleep.'
    print(line65,"\n")
    pressEnter()
    print(line57)
    