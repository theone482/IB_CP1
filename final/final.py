# IB 2nd final

import random

# --- Player Stats (buffed for balance) ---
player_health = 1500   # Increased health
player_strength = random.randint(150, 250)  # Stronger attacks
player_memory = 10
player_agility = 25
player_speed = 35

# --- Enemy Stats (toned down) ---
phantom_health = 200
phantom_attack = 150   # Lowered attack

soldier3_health = 50
soldier3_attack = random.randint(75, 125)

soldier5_health = 50
soldier5_attack = random.randint(75, 125)

soldier6_health = 700
soldier6_attack = random.randint(100, 175)

mainboss_health = 15000   # Lowered boss health
mainboss_attack = random.randint(300, 450)

# --- Chest Rewards ---
chests = {
    "room3": {"health": 1000},
    "room5": {"attack": 100},
    "room6": {"health": 200},
    "room7": {"random": [{"attack": 100}, {"health": 1000}]}
}

def intro_instructions():
    print("\n--- Welcome to Rosie’s Journey ---")
    print("Instructions:")
    print("1. Attack: Damage is RANDOM between 75 and your Strength.")
    print("2. Heal: Restores +25 HP each time.")
    print("3. Flee: 50% chance to escape.")
    print("4. Chest Rewards: Boost Health or Strength depending on the chest.")
    print("5. If you die, the game ends. Restart to try again.")
    print("6. You can revisit earlier rooms at any time.")
    print("7. Room directions will be explained (e.g., Room 3 is right of Room 4).")
    print("----------------------------------\n")

def player_stats():
    print(f"\n--- Player Stats ---")
    print(f"Health: {player_health}")
    print(f"Strength: {player_strength}")
    print(f"Agility: {player_agility}")
    print(f"Speed: {player_speed}")
    print(f"Memory: {player_memory}")
    print("--------------------\n")

def reset_stats(reward=None):
    global player_memory, player_health, player_strength
    player_memory += 5
    if reward:
        if "health" in reward:
            player_health += reward["health"]
            print(f"You gained +{reward['health']} health!")
        if "attack" in reward:
            player_strength += reward["attack"]
            print(f"You gained +{reward['attack']} strength!")

def fight_enemy(enemy_name, enemy_health, enemy_attack, reward=None):
    global player_health, player_strength
    print(f"\nYou encounter a {enemy_name}!")
    while player_health > 0 and enemy_health > 0:
        choice = input("Choose action: (1) Attack (2) Heal (+25 HP) (3) Flee: ").strip()
        if choice == "1":
            damage = random.randint(75, player_strength)
            enemy_health -= damage
            print(f"You hit the {enemy_name} for {damage} damage! Enemy health: {enemy_health}")
        elif choice == "2":
            player_health += 25
            print(f"You healed! Health: {player_health}")
        elif choice == "3":
            if random.randint(1, 100) <= 50:
                print("You fled successfully!")
                return
            else:
                print("Failed to flee! The fight continues.")
        
        if enemy_health > 0:
            dmg = random.randint(50, enemy_attack)
            player_health -= dmg
            print(f"{enemy_name} hits you for {dmg}! Your health: {player_health}")
    
    if player_health <= 0:
        print("You died. Game Over. Restart to play again.")
        exit()  # End game immediately
    else:
        print(f"{enemy_name} defeated!")
        if reward:
            reset_stats(reward)
            print("You gained a chest reward!")
        player_stats()

# --- Enemy fight wrappers (same names preserved) ---
def fight_phantoms():
    fight_enemy("Phantom", phantom_health, phantom_attack)

def fight_soldier_room3():
    fight_enemy("Soldier (Room 3)", soldier3_health, soldier3_attack, chests["room3"])

def fight_soldier_room5():
    fight_enemy("Soldier (Room 5)", soldier5_health, soldier5_attack, chests["room5"])

def fight_soldier_room6():
    fight_enemy("Soldier (Room 6)", soldier6_health, soldier6_attack, chests["room6"])

def fight_soldier_room7():
    reward = random.choice(chests["room7"]["random"])
    fight_enemy("Soldier (Room 7)", soldier6_health, soldier6_attack, reward)

def fight_main_boss():
    fight_enemy("Main Boss", mainboss_health, mainboss_attack)
    if player_health > 0:
        flashback()

# --- Rooms (same names preserved, cave choice fixed) ---
def room_1():
    print("You wake up by the river... You notice a cave nearby.")
    choice = ""
    while choice.lower() != "yes":
        choice = input("Do you want to enter the cave? (yes/no): ")
        if choice.lower() == "no":
            print("You feel drawn to the cave... you must enter to continue.")
    room_2()
def room_2():
    print("Each step echoed faintly against the stone, the sound swallowed quickly by the heavy silence inside. " 
        "The walls glistened with moisture, and faint trickles of water ran down into shallow pools that reflected your " 
        "uncertain face. You reached out to steady yourself, your fingers brushing against the cold, rough surface of the rock,"
        " and the sensation sent a shiver through your body.As you moved deeper, the light from the river faded, replaced by " 
        "shadows that seemed to shift and breathe. The cut on your head throbbed with each heartbeat, and you pressed your hand" 
        " against it, leaving a faint smear of dried blood on the stone. The air smelled of earth and something older, " 
        "something forgotten. You paused, listening—was that the drip of water, or the faint whisper of voices carried through " 
        "the cavern? The photograph in your pocket felt heavier now, as if it wanted to be seen again, and you pulled it out, " 
        "staring at the little girl's face that looked so much like yours. The cave seemed to lean closer, as if it too wanted " 
        "to know who you were. All of a sudden a wizard came out.The wizard's staff glowed faintly as he stepped closer, his " 
        "voice calm but commanding. “To know yourself, place your hand over your heart and breathe—the cave will show your " 
        "stats,” he said, and as you obeyed, shimmering symbols rose before you, revealing your health, strength, agility, and " 
        "fractured memory. He explained that health was your endurance, strength, power, agility, your speed, and memory, the " 
        "broken pieces of who you are, waiting to be restored. Then he raised his staff and shadows formed into phantom foes "
        "around you. “To fight, plant your feet wide and keep your balance. Block first, then counter. Strike with purpose, " 
        "not fear, and listen to the rhythm of battle—every enemy has a pattern, and once you find it, you can break it.” " 
        "His words echoed through the cavern, each lesson sinking into your bones, until you felt not only trained but awakened" 
        ", ready to face the dangers waiting deeper in the cave.")
    fight_phantoms()
    next_room = input("Go to Room 3, 4, or 5? ").strip()
    if next_room == "3": room_3()
    elif next_room == "4": room_4()
    elif next_room == "5": room_5()

def room_3():
    print("Each step echoed faintly against the stone, the sound swallowed quickly by the heavy silence inside. " 
     "The walls glistened with moisture, and faint trickles of water ran down into shallow pools that reflected your uncertain " 
     "face. You reached out to steady yourself, your fingers brushing against the cold, rough surface of the rock, and the " 
     "sensation sent a shiver through your body.As you moved deeper, the light from the river faded, replaced by shadows that " 
     "seemed to shift and breathe. The cut on your head throbbed with each heartbeat, and you pressed your hand against it, " 
     "leaving a faint smear of dried blood on the stone. The air smelled of earth and something older, something forgotten. " 
     "You paused, listening—was that the drip of water, or the faint whisper of voices carried through the cavern? The " 
     "photograph in your pocket felt heavier now, as if it wanted to be seen again, and you pulled it out, staring at the " 
     "little girl's face that looked so much like yours. The cave seemed to lean closer, as if it too wanted to know who you " 
     "were.As you lower the photograph, the silence breaks with the sound of armored footsteps echoing from the shadows. A " 
     "figure emerges—a soldier clad in battered steel, his face hidden beneath a dented helm. His sword gleams faintly in the " 
     "dim light, and he raises it with deliberate precision. You realize instantly that he is not just any foe; he moves " 
     "exactly as the wizard taught you to fight. His stance is wide, balanced, his shield raised to block, his strikes measured"
     " and purposeful.The soldier lunges, and you react, recalling the wizard's lessons. You plant your feet, block the first " 
     "blow, and counter with a strike of your own. The clash of steel rings through the cavern, each movement testing your " 
     "strength, agility, and focus. He circles you, forcing you to listen to the rhythm of battle, to anticipate his pattern. " 
     "Every heartbeat, every breath, becomes part of the fight.At last, you find the opening. You dodge his swing, step inside" 
     " his guard, and strike with purpose. The soldier stumbles, his armor clattering against the stone, before dissolving into" 
     " shadow, leaving only silence behind.In the center of the chamber, where he fell, a chest materializes—ancient wood bound" 
     " with iron, glowing faintly as if alive. You kneel and lift the lid. Inside, you find a surge of energy: a vial shimmering" 
     " with light. As you touch it, warmth floods your body, restoring your health and strengthening your stamina. The cavern " 
     "seems to sigh, as though acknowledging your victory, and the photograph in your pocket feels lighter, as if the path " 
     "forward has grown clearer.")
    fight_soldier_room3()
    next_room = input("Go to Room 4 or 6? ").strip()
    if next_room == "4": room_4()
    elif next_room == "6": room_6()

def room_4():
    print("you instinctively turn left, drawn by a faint draft that whispers through the stone corridor. The passage narrows, " 
     "forcing you to brush against the rough walls, and the sound of your footsteps echoes strangely, as if the cave itself is " 
     "listening.After a few careful steps, the tunnel opens into a new chamber. This room feels different—larger, but lower, " 
     "the ceiling heavy with hanging stalactites that drip water in slow, steady rhythms. The floor is uneven, scattered with " 
     "rocks and shallow puddles that reflect the dim light like broken mirrors. You crouch to steady yourself, touching the " 
     "damp stone, and the chill seeps into your skin.The air here smells faintly metallic, like rust or old blood, and your " 
     "wound throbs in response. You press your hand to your head, feeling the sticky residue of dried blood, and glance around." 
     " On the far wall, faint markings catch your eye—scratches, symbols, or perhaps just the scars of time. You move closer, " 
     "tracing them with your fingertips, and the photograph in your pocket feels heavier again, as though urging you to connect" 
     " the pieces.The silence is thicker here, broken only by the drip of water and the faint scurry of something unseen in the" 
     " shadows. You pause, heart racing, wondering if you are truly alone in this chamber.You pause, heart racing, when the " 
     "silence breaks with the scrape of metal against stone. From the shadows, a soldier steps forward, clad in tarnished armor" 
     ", his sword gleaming faintly in the dim light. His stance is wide and balanced, exactly as the wizard had taught you. He " 
     "raises his shield, testing you with a deliberate strike.You react instinctively, planting your feet and blocking the blow." 
     " The clash rings through the chamber, echoing against the stalactites above. He presses forward, each strike measured, " 
     "forcing you to remember the rhythm of battle. You dodge, counter, and strike with purpose, your movements sharper now, " 
     "guided by the wizard's lessons. The soldier circles, relentless, until you find the opening—slipping past his guard and " 
     "landing a decisive blow. His form shudders, then dissolves into shadow, leaving only silence behind.Where he fell, a chest" 
     " materialized, ancient wood bound with iron, glowing faintly in the dim light. You kneel and lift the lid. Inside lies a " 
     "shimmering vial, its glow pulsing like a heartbeat. As you touch it, warmth floods your body, restoring your health and " 
     "strengthening your stamina. The chamber feels lighter, the markings on the wall glowing faintly as if acknowledging your " 
     "victory.")
    fight_soldier_room3()
    next_room = input("Go to Room 5, 3, or 7? ").strip()
    if next_room == "5": room_5()
    elif next_room == "3": room_3()
    elif next_room == "7": room_7()

def room_5():
    print("you step into the cave and instinctively veer to the right, drawn by a faint glow that flickers " 
     "against the stone. The passage is wider here, but the floor slopes downward, forcing you to tread carefully" 
     " as loose pebbles scatter beneath your boots. The air grows colder with each step, carrying the sharp " 
     "scent of minerals and something faintly sweet, almost like decaying flowers.The tunnel opens into a chamber" 
     " that feels alive. Strange fungi cling to the walls, their pale caps glowing faintly in the darkness, " 
     "casting ghostly light across the room. Shadows dance along the jagged surfaces, shifting with your " 
     "movements as though the cave itself is watching. You kneel to examine one of the glowing mushrooms, " 
     "brushing your fingers across its damp surface, and the light pulses faintly, responding to your touch.The " 
     "cut on your head throbs again, and you press your hand against it, leaving a faint smear of blood on the " 
     "stone. You glance around and notice that the chamber isn't empty—bones, small and brittle, lie scattered"
     "near the far wall, half-buried in dust. They look old, but their presence makes your chest tighten. You" 
     "clutch the photograph in your pocket, pulling it out once more. The little girl's face seems to glow in" 
     " the eerie light, her eyes reflecting the same strange luminescence as the fungi.The silence here is " 
     "different—less oppressive, more expectant, as if the cave is holding its breath, waiting for you to " 
     "take the next step deeper into its secrets.")
    fight_soldier_room5()
    next_room = input("Go to Room 4, 3, 7, or 8? ").strip()
    if next_room == "4": room_4()
    elif next_room == "3": room_3()
    elif next_room == "7": room_7()
    elif next_room == "8": room_8()

def room_6():
    print("The path slopes downward, twisting like a serpent through the earth. Each step feels heavier, the " 
     "air growing colder and thicker, until the tunnel finally opens into a vast chamber—the fifth room. Unlike" 
     " the others, this space feels ancient, almost sacred. The ceiling arches high above, lost in shadow, and " 
     "the walls are lined with jagged formations that glitter faintly, as though the stone itself remembers " 
     "forgotten light.The floor is uneven, scattered with broken rocks and shallow pools that reflect the dim "
     "glow of mineral veins running through the walls. At the center of the chamber lies something unexpected:" 
     "a stone pedestal, cracked and worn, its surface etched with markings that seem too deliberate to be " 
     "natural. You approach cautiously, your footsteps echoing in the cavernous silence. The photograph in your" 
     " pocket feels heavier than ever, as if it belongs here, as if the cave itself has been guiding you to this" 
     " place.You reach out, brushing your fingers across the pedestal. The markings are rough beneath your touch" 
     ", but they pulse faintly with warmth, sending a shiver through your body. The cut on your head throbs in " 
     "rhythm, and for a moment you feel dizzy, as though the room itself is spinning. The silence deepens, " 
     "broken only by the steady drip of water and the faint hum that seems to rise from the stone.The chamber " 
     "feels alive, waiting, holding its breath. You realize this room is not just another hollow in the earth—it"
     "is a place of meaning, a place where answers might finally begin to reveal.As the hum from the " 
     "pedestal grows louder, the silence shatters with the heavy clang of armored boots. From the shadows " 
     "at the far wall, a soldier emerges—larger, stronger, and more imposing than the one you faced before." 
     " His armor is darker, scarred from countless battles, and his sword gleams with a sharper edge. His " 
     "stance is firm, his movements deliberate, and you recognize instantly that he fights with the same " 
     "iscipline the wizard taught you—but faster, harder, and with no hesitation.He charges, his strikes " 
     "ringing through the chamber like thunder. You block, but the force rattles your arms, forcing you to " 
     "dig deeper into your strength and agility. Each swing tests your balance, each shield bash pushes you" 
     " back toward the pedestal. You remember the wizard's words—block first, then counter, strike with " 
     "purpose, not fear. You dodge, step inside his guard, and land a blow, but he recovers quickly, " 
     "pressing harder. The fight becomes a rhythm of survival, every heartbeat echoing against the cavern " 
     "walls.At last, you find the opening. With a final surge of stamina, you slip past his guard and " 
     "strike true. The soldier staggers, his armor cracking, before dissolving into shadow that fades into " 
     "the pedestal's glow. The chamber exhales, the hum softening, and where the soldier fell, a chest" 
     " materializes—larger and brighter than before, bound in iron and glowing with golden light.You kneel "
     "and open it. Inside lies not just a vial, but a radiant crystal pulsing with energy. As you touch it," 
     " warmth floods your body, restoring your health completely and expanding your stamina beyond its " 
     "limits. You feel stronger, faster, more alive")
    fight_soldier_room6()
    next_room = input("Go to Room 3 or 7? ").strip()
    if next_room == "3": room_3()
    elif next_room == "7": room_7()

def room_7():
    print("The tunnel bends sharply to the left, narrowing until you have to press your shoulder against the " 
     "damp wall to squeeze through. The air grows colder, and a faint draft brushes past your face, carrying " 
     "with it the smell of wet stone and something faintly metallic. As you push forward, the passage widens " 
     "suddenly into a chamber that feels older than the others, as though it has been untouched for centuries." 
     "The ceiling here is low, heavy with stalactites that drip water in slow, rhythmic beats, echoing like a " 
     "heartbeat through the chamber. The walls are streaked with dark mineral veins, glistening faintly in the " 
     "dim light. At the far end of the room, half-buried in rubble, lies what looks like a carved stone archway"
     ". Its surface is etched with markings—symbols you don't recognize, but they seem deliberate, purposeful, " 
     "as if they were meant to guard or conceal something.You step closer, your hand brushing against the cold " 
     "stone, and the cut on your head throbs in response, sharp and insistent. The photograph in your pocket feels " 
     "heavier again, and when you pull it out, the little girl's eyes seem to glow faintly in the dim light" 
     ", reflecting the shimmer of the mineral veins. The silence in this chamber is different—thicker, almost " 
     "suffocating—broken only by the drip of water and the faint sound of your own breathing.You kneel near the" 
     " archway, brushing away loose stones, and notice that beneath the rubble lies a narrow gap, just wide " 
     "enough for someone to slip through. The chamber feels like it's holding its breath, waiting for you to " 
     "decide whether to push deeper into the unknown.")
    fight_soldier_room7()
    next_room = input("Go to Room 5, 3, 6, or 4? ").strip()
    if next_room == "5": room_5()
    elif next_room == "3": room_3()
    elif next_room == "6": room_6()
    elif next_room == "4": room_4()

def room_8():
    print("The tunnel stretches on, straight and unyielding, as though it wants to test your resolve. The air" 
     " grows colder with each step, and the silence presses heavier against your ears. Your footsteps echo " 
     "faintly, swallowed by the darkness, until at last the passage opens into a seventh chamber.This room is " 
     "vast, larger than any you've seen before. The ceiling arches high overhead, lost in shadow, and the walls" 
     " are lined with jagged stone that glitters faintly, as if tiny shards of crystal are embedded within. The" 
     " floor dips into a wide basin, filled with still water that reflects the faint shimmer of the walls like " 
     "a mirror. You approach cautiously, kneeling at the edge of the basin, and the reflection staring back at " 
     "you seems distorted—your face ripples into something unfamiliar, older, or perhaps not you at all.The air" 
     " here hums faintly, a low vibration that seems to rise from the water itself. You press your hand to your" 
     " wound, feeling the throb of pain match the rhythm of the hum. The photograph in your pocket feels heavier" 
     " than ever, and when you pull it out, the little girl's face seems to glow faintly in the reflection, her " 
     "eyes shimmering with the same strange light as the crystalsYou step deeper into the chamber, and notice " 
     "that the far wall is not solid. A narrow crack runs from floor to ceiling, wide enough to slip through, and"
     " from within it comes a faint breeze carrying the scent of earth and something unfamiliar—something alive." 
     " The seventh room feels like a threshold, a place where the cave is offering you a choice: stay and face " 
     "the reflection of yourself, or push through the crack into whatever lies beyond.")
    next_room = input("Go to Room 5, 7, or 9? ").strip()
    if next_room == "5": room_5()
    elif next_room == "7": room_7()
    elif next_room == "9": room_9()

def room_9():
    print("The tunnel plunges deeper than any before, the air growing colder and heavier with each step. Your " 
     "breath comes in shallow bursts as the walls close in, then suddenly open into a cavern so vast it feels " 
     "like the heart of the earth itself. The ceiling disappears into shadow, and the ground trembles faintly " 
     "beneath your feet. At the center of the chamber, a figure waits—towering, twisted, its form shifting like" 
     " smoke and stone. Its eyes burn with a light that pierces straight into your wound, making your head " 
     "throb violently.You stagger forward, clutching the photograph, and the creature lets out a sound that is " 
     "neither roar nor whisper but something in between—an echo of your own fear. The battle begins. (after the" 
     " main boss dies)You dodge its strikes, each one shaking the cavern walls, and fight back with everything " 
     "you can muster. The cave itself seems to join the struggle: stones fall, water surges from cracks, and " 
     "the glowing veins in the walls pulse with each clashThe fight is brutal, but as you press on, flashes of " 
     "memory begin to break through the pain (flash back).Finally, with one last desperate blow, the creature " 
     "collapses, dissolving into mist that vanishes into the cavern walls. Silence falls, heavy and absolute. " 
     "You drop to your knees, exhausted, clutching the photograph. But now you understand—the little girl in " 
     "the picture is you. The family is yours. The cave, the blood, the confusion… All of it was a trial, a " 
     "barrier between you and the truth of who you are.Tears sting your eyes as the memories flood back in full." 
     " You are not lost. You are not alone. This is your family, your life, and you have found your way back to " 
     "it.")
    fight_main_boss()
    flashback()

def flashback():
    print("There was once a happy family living on this mountain called Lugh. And in that family there was a " 
     " special little girl named Rosie Jane and her two brothers named James and Giorgio . One day she is " 
     "walking when she sees a soldier running towards her and her family with weapons and torches. Her family, " 
     "who is a kind and happy person, looked nervous and serious as he told Rosie to take her James who at the " 
     "time was 3 and Giorgio who was 4 down to cross  the river and to their aunt. As Rosie took her giorgio " 
     "hand and carried James and she ran as fast as she could. Once she was almost at the river she had her " 
     "house burn down and her parents getting taken away. Rosie was shocked but remembered what her dad told " 
     "her as she crossed the river with her brother and made it to her aunt.When she made it her aunt hugged " 
     "them and asked rosie where are your parents. Are they coming? That is then Rosie replies with a sad voice" 
     " no they took them. Their aunt looked devastated but tried to take it together for Rosie and her brothers." 
     " Rosie touched her pocket only to realize she left her family's last picture that was not burned with the " 
     "house on the other side of the river. Her aunt tried to stop her from going but Rosie said that is the " 
     "only picture i have of them let me go get it. As Rosie crossed the river she put her family picture in " 
     "her pocket. She could hear the soldier come back and it was coming near the river. Rosie was so shocked " 
     "she didn't move. One of the soldiers looked at her and threw a rock at her scalp.After the rock hit her " 
     "head she could feel the blood drip down her forehead as she fell on the river bank, her finger in the " 
     "river. As she heard horse running and her aunt and her brothers  running and the soldiers yelling where " 
     "did they go. As her eyes closed and everything went black.")

def training_room():
    print("\n--- Training Room ---")
    print("Here you learn how combat works and chest rewards:")
    print("- Attack is random between 75 and your Strength.")
    print("- Healing restores +25 HP.")
    print("- Chest rewards can boost Health or Strength.")
    print("You feel prepared to continue your journey.\n")


def game():
    intro_instructions()
    player_stats()
    training_room()
    room_1()
    room_2()
    fight_phantoms()
    room_3()
    fight_soldier_room3()   # ✅ fixed
    room_4()
    fight_soldier_room3()   # or fight_soldier_room5() depending on story
    room_5()
    fight_soldier_room5()   # ✅ fixed
    room_6()
    fight_soldier_room6()   # ✅ fixed
    room_7()
    fight_soldier_room7()   # ✅ fixed
    room_8()
    room_9()
    fight_main_boss()
    print("Game complete! Thanks for playing.")

game()
