import items

def Play_Zork():
	loop = 4
	print("---------------------------------------------------------")
	print("Welcome to Zork - The Unofficial Python Version.")
	return loop

def exit_function(exit_inp):
        if exit_inp.lower() == "dead":
                exit()



def room4(second, item_list1):


        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
                alive_dead = 'Alive'
                loop = 4
                
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
                alive_dead = 'Alive'
                loop = 4
                
        elif second.lower() == ("go north"):
                loop = 1
                alive_dead = 'Alive'
                
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
                alive_dead = 'Alive'
                loop = 4
                
        elif second.lower() == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
                alive_dead = 'Alive'
                loop = 4
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
                alive_dead = 'Alive'
                loop = 4
        elif second.lower() == ("go southwest"):
                loop = 8
                alive_dead = 'Alive'
                
        elif second.lower() == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
                alive_dead = 'Alive'
                loop = 8
                
        elif second.lower() == ('go east'):
                loop = 12
                alive_dead = 'Alive'
                
        elif second.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)

        else:
                print("---------------------------------------------------------")
                loop = 4
                alive_dead = 'Alive'
        return[loop, alive_dead]



def room1(north_house_inp, item_list):


        if north_house_inp.lower() == ("go south"):
                loop = 4
                alive_dead = 'Alive'
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
                loop = 1
                alive_dead = 'Alive'
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
                alive_dead = 'Alive'
                loop = 1
        elif north_house_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                loop = 1
                alive_dead = 'Alive'
        return [loop, alive_dead]




def room8(forest_inp, item_list):


        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
                loop = 8
                alive_dead = 'Alive'
                
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
                alive_dead = 'Alive'
                loop = 8
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
                alive_dead = 'Alive'
                loop = 8
        elif forest_inp.lower() == ("go east"):
                loop = 9
                alive_dead = 'Alive'
        elif forest_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                loop = 8
                alive_dead = 'Alive'
        return [loop, alive_dead]




def room9(grating_inp, item_list):

        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
                loop = 9
                alive_dead = 'Alive'
                
        elif grating_inp.lower() == ("descend grating"):
                loop = 10
                alive_dead = 'Alive'
        elif grating_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                loop = 9
                alive_dead = "Alive"
        return [loop, alive_dead]	


def room10(cave_inp, item_list):

        if cave_inp.lower() == ("descend staircase"):
                loop = 11
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
                alive_dead = 'Alive'
                loop = 10
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
                alive_dead = 'Alive'
                loop = 10
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
                alive_dead = 'Alive'
                loop = 10
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
                alive_dead = 'Alive'
                loop = 10
        elif cave_inp.lower() == ("go down staircase"):
                loop = 11
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("scale staircase"):
                loop = 11
                alive_dead = 'Alive'
        elif cave_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        elif cave_inp.lower() == ("scale staircase"):
                loop = 11
                alive_dead = 'Alive'
        else:
                print("---------------------------------------------------------")
                loop = 10
                alive_dead = 'Alive'
        return [loop, alive_dead]

def room11(last_inp, item_list):


        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
                alive_dead = 'Alive'
                print('You WIN!')
                exit()
        elif last_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                loop = 11
                alive_dead = 'Alive'
        return [loop, alive_dead]


def room12(new12_inp, item_list):

        
        if new12_inp.lower() == ('going south'):
                loop = 4
                alive_dead = 'Alive'
        elif new12_inp.lower() == ('going west'):
                print('Opening a rickety window you climb into the house')
                alive_dead = 'Alive'
                loop = 12
        elif new12_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                loop = 12
                alive_dead = 'Alive'
        return [loop, alive_dead]




def room13(new13_inp, item_list):
        if new13_inp.lower() == ('going up'):
                loop = 14
                alive_dead = 'Alive'
        elif new13_inp.lower() == ('going east'):
                loop = 12
                alive_dead = 'Alive'
        elif new13_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                loop = 13
                alive_dead = 'Alive'
        return [loop, alive_dead]


def room14(new14_inp, item_list):
        if new14_inp.lower() == ('going down'):
                loop = 13
                alive_dead = "Alive"
        elif new14_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                loop = 14
                alive_dead = "Alive"
        return [loop, alive_dead]



def room15(new15_inp, item_list):
        if new15_inp.lower() == ('going north'):
                loop = 10
                alive_dead = 'Alive'
        elif new15_inp.lower() == ('going south'):
                loop = 16
                alive_dead = 'Alive'
        elif new15_inp.lower() == ('going east'):
                loop = 17
                alive_dead = 'Alive'
        elif new15_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                loop = 15
                alive_dead = 'Alive'
        return [loop, alive_dead]



def room16(new16_inp, item_list):
        if new16_inp.lower() == ('going north'):
                loop = 15
                alive_dead = 'Alive'
        else:
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        return [loop, alive_dead]

def room17(new17_inp, item_list):
        if new17_inp.lower() == ('going east'):
                print('Looks like all path circle around to one destination')
                loop = 15
                alive_dead = 'Alive'
        elif new17_inp.lower() == ('going west'):
                loop = 15
                print('Looks like all path circle around to one destination')
                alive_dead = 'Alive'
        elif new17_inp.lower() == ('going south'):
                loop = 15
                print('Looks like all path circle around to one destination')
                alive_dead = 'Alive'
        elif new15_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        else:
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                alive_dead = 'Dead'
                dead_inp = alive_dead
                exit_function(dead_inp)
        return [loop, alive_dead]
        
                



















        
