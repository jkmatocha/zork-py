# Main game file

import zork
def PrintOutput(s):
    print("OUTPUT", s)

loop = zork.Play_Zork()
while True:
    while loop == 4:
        if loop == 4:
            print("---------------------------------------------------------")
            print("You are standing in an open field west of a white house, with a boarded front door.")
            print("You can see a small lake to the north.")
            print("(A secret path leads southwest into the forest.)")
            print("There is a Small Mailbox.")
            second = input("What do you do? ")
            room = zork.room4(second, [])
            loop = room[0]
    while loop == 1:
            if loop == 1:
                print("---------------------------------------------------------")
                print("You find yourself at the edge of a beautiful lake aside rolling hills.")
                print("A small pier juts out into the lake.")
                print("A fishing rod rests on the pier.")
                print("(You can see a white house in the distance to the south.)")
                north_house_inp = input("What do you do? ")
                room = zork.room1(north_house_inp, [])
                loop = room[0]



    while loop == 8:
            if loop == 8:
                print("---------------------------------------------------------")
                print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
                forest_inp = input("What do you do? ")
                room = zork.room8(forest_inp, [])
                loop = room[0]

    # East Loop and Grating Input
    while loop == 9:
            if loop == 9:
                print("---------------------------------------------------------")
                print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
                print("There is an open grating, descending into darkness.")
                grating_inp = input("What do you do? ")
                room = zork.room9(grating_inp, [])
                loop = room[0]

    # Grating Loop and Cave Input
    while loop == 10:
            if loop == 10:
                print("---------------------------------------------------------")
                print("You are in a tiny cave with a dark, forbidding staircase leading down.")
                print("There is a skeleton of a human male in one corner.")
                cave_inp = input("What do you do? ")
                room = zork.room10(cave_inp, [])
                loop = room[0]

    # End of game
    while loop == 11:
            if loop == 11:
                print("---------------------------------------------------------")
                print("You have entered a mud-floored room.")
                print("Lying half buried in the mud is an old trunk, bulging with jewels.")
                last_inp = input("What do you do? ")
                room = zork.room11(last_inp, [])
                loop = room[0]
                    


    while loop == 12:
            if loop == 12:
                print("---------------------------------------------------------")
                print("You have found yourself behind the house. The only paths are south or west")
                room = zork.room12(new12_inp, [])
                loop = room[0]
                new12_inp = input("What do you do? ")
                room = zork.room12(new12_inp, [])
                loop = room[0]

    while loop == 13:
            if loop == 13:
                print("---------------------------------------------------------")
                print("You have found yourself in a kitchen with poor lighting and dust on the floor")
                print('You spot a lantern on the kitchen table')
                print('There is a set of stairs in front of you')
                new13_inp = input("What do you do? ")
                room = zork.room13(new13_inp, [])
                loop = room[0]
                    


    while loop == 14:
            if loop == 14:
                print("---------------------------------------------------------")
                print("You are in the attic, all you can do is go back down")
                new14_inp = input("What do you do? ")
                room = zork.room14(new14_inp, [])
                loop = room[0]



    while loop == 15:
            if loop == 15:
                print("---------------------------------------------------------")
                print("You see a sign that reads MAZE")
                print('There is a cave North, the MAZE is South, and Nothing in sight East')
                new15_inp = input("What do you do? ")
                room = zork.room15(new15_inp, [])
                loop = room[0]


    while loop == 16:
            if loop == 16:
                print("---------------------------------------------------------")
                print("You are in the MAZE")
                print('North takes you back to the start, but you can go any direction')
                new16_inp = input("What do you do? ")
                room = zork.room16(new16_inp, [])
                loop = room[0]

    while loop == 17:
            if loop == 17:
                print("---------------------------------------------------------")
                print("There is a beautiful garden, but it seems you are trapped?!")
                print("All paths lead to the same place")
                new17_inp = input("What do you do? ")
                room = zork.room17(new17_inp, [])
                loop = room[0]

		


















				
