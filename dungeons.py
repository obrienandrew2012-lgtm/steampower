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
answer = input("Are you ready  to go into the dungeon?? Y/N ").upper()
creature2 = random.randint(15, 25)
if answer == "QSG22":
    print("ADMIN CONTROLS ACTIVATED")
    player_hp += 9999
    gold += 9999
    print(answer)

elif answer == "N":
    input("ok bye, hit enter to leave")
    sys.exit()

elif answer == "Y":
    print("*hear that?*")
    print("*eyes glow in the dark*")

    creatures = ["Goblin", "Slime", "Skeleton", "Bat", "Tiny Demon"]
    creature = random.choice(creatures)
    creature_hp = random.randint(8, 15)

    print(f"\nA {creature} appears!")

    choice = input("FIGHT, CHECK THEIR STATS, OR RUN? F/C/R ").upper()

    if choice == "C":
        print(f"{creature} HP: {creature_hp}")
        print("Damage per hit: 3–8")
        choice = input("Now what? FIGHT OR RUN? F/R ").upper()

    if choice == "R":
        print("You run away safely...")

    elif choice == "F":
        print(f"\nYou engage the {creature}!")

        while player_hp > 0 and creature_hp > 0:
            player_damage = random.randint(6, 12)
            creature_hp -= player_damage
            print(f"You hit the {creature} for {player_damage} damage!")

            if creature_hp <= 0:
                gold += 10
                print(f"The {creature} is defeated!")
                print("You gained 10 GOLD")
                break

            creature_damage = random.randint(3, 8)
            player_hp -= creature_damage
            print(f"The {creature} hits you for {creature_damage} damage!")
            print(f"Your HP: {player_hp}")

            if player_hp <= 0:
                print("You collapse... GAME OVER")
                break

    elif choice not in ["F", "C", "R"]:
        print("Invalid choice. The creature disappears.")

    # --- Dungeon Continues ---
    if player_hp > 0:
        print("\nYou move deeper into the dungeon...")
        action = input("What to do now? S(hop), W(ait), E(xplore): ").upper()

        if action == "S":
            buy1 = input(
                "\nWelcome to the shop!\n"
                "(H)ealing Item (restores 10 HP, 5 GOLD)\n"
                "(B)etter Sword (does nothing, 10 GOLD)\n"
                "(K)ermit relic (ITS FREE I DONT WANT IT)\n"
                "Choose: "
            ).upper()

            if buy1 == "H":
                if gold >= 5:
                    player_hp += 10
                    gold -= 5
                    print(f"Your HP is now {player_hp}")
                    print(f"Gold remaining: {gold}")
                else:
                    print("Not enough gold!")

            elif buy1 == "B":
                if gold >= 10:
                    gold -= 10
                    print("You've pretty much wasted 10 GOLD")
                    print(f"Gold remaining: {gold}")
                else:
                    print("Not enough gold!")

            elif buy1 == "K":
                relic = 1
                print("You obtained the KERMIT RELIC...")

            else:
                print("Invalid shop choice.")

        elif action == "W":
            print("You wait... nothing happens.")
            time.sleep(3)
            print("GAAH? A CREATURE APPEARED!")
            print("A Rock Elemental appears! C(???????)")

            choice2 = input("").upper()

            if choice2 == "C":
                print("You... tried to use CHARISMA")
                print("FAILED MISERABLY!!!!!!")

                choice3 = input("F, R ").upper()

                if choice3 == "F":
                    print("YOU FOUGHT THE ROCK ELEMENTAL! HIT IT FOR 12 DAMAGE!!!!")
                    rocke -= 12
                elif choice3 == "R":
                    print("YOU RAN AWAY, GOT NOTHING")

            print("THE ROCK ELEMENTAL HITS YOU FOR 5 DAMAGE!")
            player_hp -= 5
            print(f"YOUR HEALTH IS NOW {player_hp}")
            print("THE ROCK ELEMENTAL HATES YOU BY THE WAY")
            rockhatesyou = True

        elif action == "E":
            print("You explore...")

            if random.randint(1, 3) == 1:
                print("A BIG SLIME APPEARS!")
                print("WHAT DO YOU DO? F/R/D")
                g = input("").upper()

                if g == "F":
                    print("THE ENEMY IS HIT FOR 3 HP!")
                    print("ENEMY HP IS NOW 5")
                    print("THE BIG SLIME HITS YOU FOR 12 HP")
                    player_hp -= 12
                    print(f"YOUR HP IS NOW {player_hp}")

        else:
            print("Invalid choice.")

        # --- Second Action ---
        action = input("\nWhat now? E/S/W ").upper()

        if action == "E" and relic == 1:
            print("\nKermit appears...")
            kermit_hp = 999999999
            first_hit = True

            while player_hp > 0 and kermit_hp > 0:
                kermit_hp -= 1
                print("You hit Kermit for 1 damage!")
                print(f"Kermit HP: {kermit_hp}")

                if kermit_hp <= 0:
                    print("Kermit has been defeated!")
                    break

                if first_hit:
                    player_hp -= 1
                    print("Kermit spares you... He hits you for 1 damage.")
                    first_hit = False
                else:
                    player_hp -= 9999
                    print("Kermit unleashes true power...")

                print(f"Your HP: {player_hp}")

                if player_hp <= 0:
                    print("You have been obliterated... GAME OVER")
                    break

        elif action == "E":
            print("you explore but nothing really happens")

        elif action == "S":
            print("The shop is closed.")

        elif action == "W":
            print("You wait... the creature doesnt come back.")

        else:
            print("Invalid choice.")
playertook = random.randint(5, 10)
playerhit = random.randint(10, 19)
print("YOU MADE IT TO THE ICE CAVE ZONE THING")
print("A creature appears!")
if input("F/R/T") == "F":
    print("You hit the SNOWDOG for 6 health")
    creature2 -= 6
    print(creature_hp)
    print("THE SNOWDOG HITS YOU FOR {playertook} HEALTH")
    player_hp -= playertook
    print("YOU HIT THE SNOWDOG FOR {playerhit} HEALTH")
    creature_hp -= {playerhit}
    if creature2 == 0:
        print("YOU WIN")
    break
elif input("F/R/T") == "T":
    print("you showed the SNOWDOG the TORCH")
    print("well its gone now")
    print(f"YOU SURVIVE WITH {player_hp} AND {gold} GOLD")
where2 = input("What now? S/E/W")
if where2 == "W":
    print("you wait...")
    print("AN ICE ELEMENTAL APPEARS!")
    if rockhatesyou == True:
        print("IT HITS YOU FOR 20 DAMAGE AND LEAVES FOR SOME REASON")
        print("i wonder why")
    else:
        print("THE ICE ELEMENTAL TAKES THE FIRST TURN AND HITS YOU FOR 2 DAMAGE")
        player_hp -= 2
        print("SPARE OR FIGHT?")
        if input(" ") == "S":
            print("YOU SPARE THE ICE ELEMENTAL, IT APPRECIATES YOUR KINDNESS AND IS TELLING ITS FRIENDS ABOUT YOU")
        else:
            print("YOU HIT THE ICE ELEMENTAL FOR 4 DAMAGE")
            print("THE ICE ELEMENTAL HAS 16 HP LEFT!")
            print("THE ICE ELEMENTAL MAKES AND ICE WALL!")
            print("IT SHOOTS ICE ABOVE THE WALL!")
            print("YOU ARE HIT FOR 5 DAMAGE")
print(f"\nYou survive with {player_hp} HP and {gold} GOLD!")
input("")
