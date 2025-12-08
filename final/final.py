# IB 2nd final

#Player Variables:
player = {
    #health = 1000 (can increase to 2200 or 3200 with upgrades)
    "health": {
        1000
    },
    #strength = 75–150 (can increase to 350 with upgrades)
    "strength": {
        75-150
    },
    #memory = 10 (starts low, grows after each fight)
    "memory": {
        10
    },
    #agility = 10 (out of 100)
    "agility": {
        25
    },
    #speed = 15 (out of 100)
    "speed": {
        35
    }
}

#Phantom Variables:
phantom = {
    #health = 200
    "health": {
        200
    },
    #attack = 250
    "attack": {
        250
    }
}

#Soldier Variables (Room 3 and 5):
soldier3and5 = {
    #health = 500
    "health": {
        500
    },
    #attack = 100–200
    "attack": {
        100-200
    },
    #chest_rewards:
    #Room 3 → +1000 health potion
    "chest 3": {
        1000
    },
    #Room 5 → Sword (+100 damage)
    "chest 5": {
        100
    }
}

#Soldier Variables (Room 6 and 7):
soldier6and7 = {
    #health = 700
    "health": {
        700
    },
    #attack = 150–250
    "attack": {
        150-250
    },
    #chest_rewards:
    #Room 6 → Armor (+200 health)
    "chest 6": {
        200
    },
    #Room 7 → Random reward (50% chance):
    "chest 7": {
        #Option 1 → +100 attack
        "op 1": {
            100
        },
        #Option 2 → +1000 health
        "op 2": {
            1000
        }
    }
}








#Main Boss Variables:
#health = 27,500
#attack = 400–600
#abilities:
#- Shadow claws / energy waves
#- Manipulates environment (falling rocks, surging water)
#- Targets player wound (extra damage)
#- Summons illusions (distraction)
#- Unlocks memory fragments on each successful strike

#RoomStatus:
#Each room has a status flag:
#visited = FALSE (default)
#soldier_defeated = FALSE (default)
#chest_claimed = FALSE (default)

#enter_room(room_number) → checks if the room has been visited before
#If visited == TRUE → no fight, no chest reward
#If visited == FALSE → trigger fight and chest logic, then mark room as

#Function: show_player_stats
#Purpose: Display current player health, strength, agility, speed, and memory.

#Function: fight_phantoms
#Purpose: Handle combat against phantom foes in Room 2.
#Options:
#- Attack (damage based on player strength)
#- Jump over attack (10% success chance)
#- Run away safely (50% success chance)
#- Run away but chased (failure, must fight again)
#Outcome:
#- If player health ≤ 0 → print "Player died. Restart to play again."
#- If phantom health ≤ 0 → print "Phantom defeated. Continue deeper."

#Function: fight_soldier_room3_5
#Purpose: Handle combat against soldiers in Room 3 and 5.
#Options same as phantom fight.
#Outcome:
#- If soldier defeated → chest reward:
#Room 3 → +1000 health
#Room 5 → Sword (+100 damage)

#Function: fight_soldier_room6_7
#Purpose: Handle combat against soldiers in Room 6 and 7.
#Options same as phantom fight.
#Outcome:
#- If soldier defeated → chest reward:
#Room 6 → +200 health
#Room 7 → Random reward (50% chance):
#Option 1 → +100 attack
#Option 2 → +1000 health

#Function: fight_main_boss
#Purpose: Handle combat against the final boss in Room 9.
#Options are the same as soldier fights.
#Boss abilities:
#- Stronger attacks (400–600 damage)
#- Manipulates environment
#- Targets wound for extra damage
#- Summons illusions
#Outcome:
#- If player dies → print "Player died. Restart to play again."
#- If the boss is defeated → unlock full memory, reveal Rosie’s past.

#Function: reset_stats
#Purpose: Update player stats after each fight.
#Actions:
#- Increase memory by +5
#- Apply chest rewards (health, attack, armor)
#- Keep agility/speed progression optional

#Function: enter_room(room_number)
#Purpose: Check if the room has been visited before.
#If visited == TRUE:
#Print "You have already been here. No fight, no chest."
#If visited == FALSE:
#Trigger fight function for that room.
#If soldier defeated:
#Mark soldier_defeated = TRUE
#If chest reward given:
#Mark chest_claimed = TRUE
#Mark visited = TRUE

#Room 1:
#Print story introduction.
#Ask the player: "Do you want to enter the cave?"
#If yes → go to Room 2.
#If no → loop until yes.

#Room 2:
#Print cave description.
#Fight phantoms using fight_phantoms function.
#Ask if player want to go to Room 3, 4, or 5

#Room 3:
#Fight soldier using fight_soldier_room3_5 function.
#Ask player if they want to go to Room 4 or 6

#Room 4:
#Print narrative only (no combat).
#Ask if player want to go to Room 5, 3, or 7

#Room 5:
#Fight soldier using fight_soldier_room3_5 function.
#Ask if player want to go to Room 4, 3, 7, or 8

#Room 6:
#Fight soldier using fight_soldier_room6_7 function.
#Ask if player want to go to Room 3 or 7

#Room 7:
#Fight soldier using fight_soldier_room6_7 function.
#Ask if player want to go to Room 5, 3, 6, or 4

#Room 8:
#Reflection room (narrative choice: face reflection or move deeper).
#Ask if player want to go to Room 5, 7, or 9

#Room 9:
#Fight main boss using fight_main_boss function.
#Unlock Rosie’s full memory and reveal family backstory.
