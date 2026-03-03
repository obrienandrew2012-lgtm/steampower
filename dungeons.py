import random

gold = 0
player_hp = 30
relic = 0

print("HELLO DUNGEON CRAWLER!")
answer = input("ARE YOU READY TO GO IN THE DUNGEON??? Y/N ").upper()

if answer != "Y":
    input("ok bye, hit enter to leave")
else:
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
        action = input("What to do now? S(hop), W(all), E(xplore): ").upper()

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

        elif action == "E":
            print("You explore...")

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
                    print("He hits you for massive damage!")

                print(f"Your HP: {player_hp}")

                if player_hp <= 0:
                    print("You have been obliterated... GAME OVER")
                    break

        elif action == "E":
            print("You explore but nothing special happens.")

        elif action == "S":
            print("The shop is closed.")

        elif action == "W":
            print("You wait... ominously.")

        else:
            print("Invalid choice.")

    print(f"\nYou survive with {player_hp} HP and {gold} GOLD!")
    input("")
