# IB 2nd cobat program
import random

# Character creation
def create_character():
    name = input("What is your name: ").strip().title()
    fighter = input("Choose your class:\n1. Fighter\n2. Mage\n3. Rogue\nEnter number: ").strip()
    stat_one = sum(random.randint(1, 20) for _ in range(3))
    stat_two = sum(random.randint(1, 8) for _ in range(3))
    atack_bounds = 3
    damage_bounds = 4

    if fighter == "1":
        return name, "Fighter", 30, 14, stat_one + atack_bounds, stat_two + damage_bounds
    elif fighter == "2":
        return name, "Mage", 20, 16, stat_one + atack_bounds, stat_two + damage_bounds
    elif fighter == "3":
        return name, "Rogue", 25, 15, stat_one + atack_bounds, stat_two + damage_bounds
    else:
        print("Invalid class. Try again.")
        return create_character()

# User turn
def user_turn(name, hp, attack, damage, monster_hp):
    wild_attack = random.randint(1, 10)
    choice = input(f"\n{name}, choose your action:\n1. Normal Attack\n2. Wild Attack\n3. Heal (+9 HP)\n4. Flee\n5. Defend\nEnter number: ").strip()
    
    if choice == "1":
        monster_hp -= attack
        print(f"You hit the monster! Monster HP is now {monster_hp}")
    elif choice == "2":
        monster_hp -= attack * 2
        hp -= wild_attack
        print(f"Wild attack! Monster HP: {monster_hp}, Your HP: {hp}")
    elif choice == "3":
        hp += 9
        print(f"You healed. Your HP is now {hp}")
    elif choice == "4":
        if random.choice([True, False]):
            print("You successfully fled the battle!")
            return hp, monster_hp, True
        else:
            print("Flee failed! You must fight.")
    elif choice == "5":
        print("You brace for impact. Incoming damage will be halved next turn.")
        return hp, monster_hp, False, True
    else:
        print("Invalid choice.")
    
    return hp, monster_hp, False, False

# Monster turn
def monster_turn(hp, defense, defended=False):
    monster_attack = random.randint(5, 15)
    if defended:
        monster_attack //= 2
        print("Your defense reduced the damage!")
    hp -= max(0, monster_attack - defense)
    print(f"Monster attacks! Your HP is now {hp}")
    return hp

# Main game loop
def combat():
    name, char_class, hp, defense, attack, damage = create_character()
    monster_hp = 35
    turn = random.choice(["player", "monster"])
    print(f"\n{name} the {char_class} enters battle! First turn: {turn.capitalize()}")

    defended = False
    while hp > 0 and monster_hp > 0:
        if turn == "player":
            hp, monster_hp, fled, defended = user_turn(name, hp, attack, damage, monster_hp)
            if fled:
                break
            turn = "monster"
        else:
            hp = monster_turn(hp, defense, defended)
            defended = False
            turn = "player"

    # Outcome
    if monster_hp <= 0 and hp > 0:
        print("You defeated the monster!")
    elif hp <= 0 and monster_hp > 0:
        print("You were slain by the monster.")
    elif hp <= 0 and monster_hp <= 0:
        print("Both you and the monster fell in battle.")
    else:
        print("Combat ended.")

combat()
