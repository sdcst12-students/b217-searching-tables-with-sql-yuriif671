'''
1. What is the structure of the table?  What are the columns and what datatypes do they store?
2. How many records are in the table?
3. How many Knights are in the table?
4. Which class has the highest number of members?
5. What is the ID number of the Jester with the most gold?
6. What is the total gold of the 100 wealthiest npc's in the table?
7. What is the total gold of the 100 wealthiest npc's under level 5?
8. What is the stats of the Bard with the highest strength?
9. What is the ID number of the npc with highest total sum of their 6 primary stats?
10. What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?
11. What is the average hitpoints per level of the npc's that are level 10 or higher?

'''

import sqlite3

# Some text in the output is bolded for better readability
# the rich library is imported here,
# because [bold][/bold] is easier to write than \033[1m\033[0m
# and better visibility in table output
#
#   pip install rich
#
from rich import print

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

# 1. What is the structure of the table?  What are the columns and what datatypes do they store?
cursor.execute("pragma table_info(npc)")
print(f"\n[bold]The structure of the table:[/bold]\n{cursor.fetchall()}")

# 2. How many records are in the table?
cursor.execute("SELECT COUNT(*) FROM npc")
print(f"\n[bold]Total number of records:[/bold] {cursor.fetchone()[0]}")

# 3. How many Knights are in the table?
cursor.execute("SELECT COUNT(*) FROM npc WHERE class = 'Knight'")
print(f"\n[bold]Number of knights:[/bold] {cursor.fetchone()[0]}")

# 4. Which class has the highest number of members?
cursor.execute("SELECT class, COUNT(*) as count FROM npc GROUP BY class ORDER BY count DESC LIMIT 1")
print(f"\n[bold]Class with the most members:[/bold] {cursor.fetchone()}")

# 5. What is the ID number of the Jester with the most gold?
cursor.execute("SELECT id FROM npc WHERE class = 'Jester' ORDER BY gold DESC LIMIT 1")
print(f"\n[bold]Richest jester id:[/bold] {cursor.fetchone()[0]}")

# 6. What is the total gold of the 100 wealthiest npc's in the table?
cursor.execute("SELECT SUM(gold) FROM (SELECT gold FROM npc ORDER BY gold DESC LIMIT 100)")
print(f"\n[bold]Total gold of the 100 wealthiest npcs:[/bold] {cursor.fetchone()[0]}")

# 7. What is the total gold of the 100 wealthiest npc's under level 5?
cursor.execute("SELECT SUM(gold) FROM (SELECT gold FROM npc WHERE level < 5 ORDER BY gold DESC LIMIT 100)")
print(f"\n[bold]Total gold of the 100 wealthiest npcs under level 5:[/bold] {cursor.fetchone()[0]}")

# 8. What is the stats of the Bard with the highest strength?
cursor.execute("SELECT * FROM npc WHERE class = 'Bard' ORDER BY strength DESC LIMIT 1")
print(f"\n[bold]Bard with the highest strength:[/bold] {cursor.fetchone()}")

# 9. What is the ID number of the npc with highest total sum of their 6 primary stats?
cursor.execute("SELECT id FROM npc ORDER BY (strength + intelligence + wisdom + dexterity + constitution + charisma) DESC LIMIT 1")
print(f"\n[bold]id of the npc with the highest total sum of primary stats:[/bold] {cursor.fetchone()[0]}")

# 10. What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?
cursor.execute("SELECT COUNT(*) FROM npc WHERE class IN ('Barbarian', 'Warrior', 'Knight', 'Samurai')")
total_fighters = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM npc WHERE class = 'Warrior'")
total_warriors = cursor.fetchone()[0]

print(f'\n[bold]Percentage of Warriors among fighter classes:[/bold] {((total_warriors / total_fighters) * 100):.2f}%')

# 11. What is the average hitpoints per level of the npc's that are level 10 or higher?
cursor.execute("SELECT AVG(hp / level) FROM npc WHERE level >= 10")
print(f'\n[bold]Avg hp per level for npcs level 10 and up:[/bold] {cursor.fetchone()[0]:.2f}')



connection.close()