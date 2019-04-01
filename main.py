from room import Room
from character import Enemy, Character
from character_test import dave

from item import Item

dave.set_conversation("i will beat you")
dave.talk()

kitchen = Room('Kitchen')
kitchen.set_description('A dank and dirty room buzzing with flies.')

dining_hall = Room('Dining Hall')
dining_hall.set_description("A big room with a table and chairs in the center")

ballroom = Room('Ballroom')
ballroom.set_description("where Talented swimmers.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

cheese = Item("cheese")
cheese.set_description("A larg and smelly block of cheese.")
ballroom.set_item(cheese)
current_room = kitchen
backpack = []
dead = False

while dead is False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            print("There is no one here to fight with.")
            fight_with = input()
            if fight_with in backpack:
                if inhabitant.fight(fight_with) is True:
                    print("Hooooray, you won the fight")
                    current_room.character = None
                if inhabitant.get_defeated() == 2:
                    print("Congratulations, you have vanquished the enemy horde!")
                    dead = True
                else:
                    print("Oh dear, you lost the fight")
                    print("That is the end of the game.")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with!")
    elif command == "hug":
        if inhabitant is None:
            print("There is no one here to hug :(")
        else:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that is I were you ...")
            else:
                inhabitant.hug()
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is noting here to take!")
    else:
        print("I don't know how to " + command)
