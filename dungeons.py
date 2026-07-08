import random
import time
import sys

rocke = 50
gold = 0
player_hp = 30
relic = 0
rockhatesyou = False

print("You are now an explorer/knight")
print("You've heard rumors about this DUNGEON...")
print("You've heard about a great reward...")
print("It's now or never...")

answer = input("Are you ready to go into the dungeon?? Y/N ").upper()

if answer == "QSG22":
    print("ADMIN CONTROLS ACTIVATED")
    player_hp += 9999
    gold += 9999

elif answer == "N":
    input("ok bye, hit enter to leave")
    sys.exit()

elif answer == "Y":

    creatures = ["Goblin", "Slime", "Skeleton", "Bat", "Tiny Demon"]
    creature = random.choice(creatures)
    creature_hp = random.randint(8, 15)

    print("*hear that?*")
    print("*eyes glow in the dark*")
    print(f"A {creature} appears!")

    choice = input("FIGHT, CHECK THEIR STATS, OR RUN? F/C/R ").upper()

    if choice == "C":
        print(f"{creature} HP: {creature_hp}")
        print("Damage per hit: 6-12")
        choice = input("Now what? FIGHT OR RUN? F/R ").upper()

    if choice == "R":
        print("You run away safely.")

    elif choice == "F":

        while player_hp > 0 and creature_hp > 0:
            damage = random.randint(6, 12)
            creature_hp -= damage
            print(f"You hit the {creature} for {damage} damage!")

            if creature_hp <= 0:
                gold += 10
                print(f"The {creature} is defeated!")
                print("You gained 10 GOLD")
                break

            enemy_damage = random.randint(3, 8)
            player_hp -= enemy_damage
            print(f"The {creature} hits you for {enemy_damage} damage!")
            print(f"HP: {player_hp}")

        if player_hp <= 0:
            print("GAME OVER")
            sys.exit()

    else:
        print("The creature disappears.")

    print("\nYou move deeper into the dungeon...")

    action = input("Shop, Wait, or Explore? S/W/E ").upper()

    if action == "S":
        shop = input(
            "(H)ealing item = 5 gold\n"
            "(B)etter sword = 10 gold\n"
            "(K)ermit relic = FREE\n"
            "Choose: "
        ).upper()

        if shop == "H" and gold >= 5:
            player_hp += 10
            gold -= 5
            print("You healed!")

        elif shop == "B" and gold >= 10:
            gold -= 10
            print("The sword does nothing.")

        elif shop == "K":
            relic = 1
            print("You got the Kermit relic!")

        else:
            print("You can't buy that.")

    elif action == "W":

        print("You wait...")
        time.sleep(2)

        print("A ROCK ELEMENTAL APPEARS!")

        while rocke > 0 and player_hp > 0:

            fight = input("Fight or Run? F/R ").upper()

            if fight == "R":
                print("You escaped.")
                break

            damage = random.randint(8, 15)
            rocke -= damage
            print(f"You hit the Rock Elemental for {damage}")

            if rocke <= 0:
                print("Rock Elemental defeated!")
                break

            player_hp -= 5
            print("Rock Elemental hits you for 5")
            print(f"HP: {player_hp}")

        rockhatesyou = True

    elif action == "E":
        print("You explore...")
        if random.randint(1,3) == 1:
            print("A BIG SLIME APPEARS!")
            player_hp -= 12
            print("The slime hits you for 12!")

    if player_hp <= 0:
        print("GAME OVER")
        sys.exit()


    action = input("\nWhat now? E/S/W ").upper()

    if action == "E" and relic == 1:

        print("Kermit appears...")
        kermit_hp = 999999999

        while player_hp > 0:

            kermit_hp -= 1
            print("You hit Kermit for 1 damage.")

            if kermit_hp <= 0:
                print("You defeated Kermit!")
                break

            player_hp -= 9999
            print("Kermit uses true power!")

    elif action == "E":
        print("Nothing happens.")

    elif action == "S":
        print("The shop is closed.")

    elif action == "W":
        print("Nothing appears.")


# ICE CAVE

if player_hp > 0:

    print("\nYOU MADE IT TO THE ICE CAVE ZONE!")

    snowdog_hp = 15

    print("A SNOWDOG APPEARS!")

    choice = input("F/R/T ").upper()

    if choice == "F":

        player_damage = random.randint(10,19)
        enemy_damage = random.randint(5,10)

        snowdog_hp -= player_damage

        print(f"You hit the SNOWDOG for {player_damage} damage!")

        if snowdog_hp <= 0:
            print("YOU WIN!")

        else:
            print(f"The SNOWDOG hits you for {enemy_damage} damage!")
            player_hp -= enemy_damage


    elif choice == "T":

        print("You showed the SNOWDOG the torch.")
        print("It ran away!")

    elif choice == "R":

        print("You escaped the Snowdog.")


    where2 = input("What now? S/E/W ").upper()

    if where2 == "W":

        print("You wait...")
        print("AN ICE ELEMENTAL APPEARS!")

        if rockhatesyou:
            print("The Ice Elemental hits you for 20 damage and leaves.")
            player_hp -= 20

        else:
            print("The Ice Elemental hits you for 2 damage.")
            player_hp -= 2

            choice = input("Spare or Fight? S/F ").upper()

            if choice == "S":
                print("The Ice Elemental appreciates your kindness.")

            else:
                print("You attack the Ice Elemental!")
                player_hp -= 5
                print("The Ice Elemental attacks back!")


print(f"\nYou survive with {player_hp} HP and {gold} GOLD!")
input("Press enter to exit.")
