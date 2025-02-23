'''
Problem:
Knights, Warriors, Barbarian, Samurai and Rangers have Strength as their Primary Stat
Sages, Sorcerers, Bards and Jesters have Intelligence as their primary stat
Thieves, Assassins and Monks have Dexterity as their primary stat
Pirests have Wisdom as their primary stat

Determine how many NPC's have chosen the wrong class based on their statistics:
example:
NPC 9906 has:
str 5
int 7
wis 10
dex 8
con 6
cha 5
They have picked the correct class because their wisdom stat was the highest
'''

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

primary = {
    "Knight": "strength", "Warrior": "strength", "Barbarian": "strength", "Samurai": "strength", "Ranger": "strength",
    "Sage": "intelligence", "Sorcerer": "intelligence", "Bard": "intelligence", "Jester": "intelligence",
    "Thief": "dexterity", "Assassin": "dexterity", "Monk": "dexterity",
    "Priest": "wisdom"
}

cursor.execute("SELECT id, strength, intelligence, wisdom, dexterity, constitution, charisma, class FROM npc;")

wrong = 0

for npc in cursor.fetchall():
    #str 5
    #int 7
    #wis 10
    #dex 8
    #con 6
    #cha 5
    id, str, int, wis, dex, con, cha, npc_class = npc

    #puttin into dict cuz u can use max to find what key (stat) is the highest
    stats = {"strength": str, "intelligence": int, "wisdom": wis, "dexterity": dex, "constituion": con, "charisma": cha}
    highest_stat = max(stats, key=stats.get)
    
    if primary[npc_class] != highest_stat:
        wrong += 1

print(f"There is in total: {wrong} NPCs that chose the wrong class")