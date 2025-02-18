'''
What is the structure of the table?  What are the columns and what datatypes do they store?
How many records are in the table?
How many Knights are in the table?
Which class has the highest number of members?
What is the ID number of the Jester with the most gold?
What is the total gold of the 100 wealthiest npc's in the table?
What is the total gold of the 100 wealthiest npc's under level 5?
What is the stats of the Bard with the highest strength?
What is the ID number of the npc with highest total sum of their 6 primary stats?
What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?
What is the average hitpoints per level of the npc's that are level 10 or higher?

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

# How many records are in the table?
query = "select count(*) from npc"

cursor.execute(query)
count = cursor.fetchone()[0]
print(f'How many records are in the table?: {count}')

# How many Knights are in the table?
query = "select count(*) from npc where class='Knight'"

cursor.execute(query)
count = cursor.fetchone()[0]
print(f'How many Knights are in the table?: {count}')

# Which class has the highest number of members?
query = "select count(*) from npc where class='Knight'"

cursor.execute(query)
count = cursor.fetchone()[0]
print(f'How many Knights are in the table?: {count}')