import csv
import mysql.connector
from mysql.connector import errorcode
from csv import reader

#Connection to the MYSQL Database.
db = mysql.connector.connect(
    host = 'localhost',
    user = 'joseph',
    passwd = 'Herowz22Leeg!',
    database = 'nbadb'
)
print('Connection Successfully made')

#Set up cursor for database manipulation.
mycursor = db.cursor()

#Insert all the data from the nba playoff stats csv file into the player table in MYSQL.

with open (r'C:\Users\josep\Documents\School Work Spring 2022\Learning Python\module2\nba_stats_playoffs.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    
    stmt = ('INSERT INTO player '
    '(player_name,team,age,games_played,position,minutes_played_per_game,'
    'team_minutes_usage,usage_percentage,turnover_percentage,'
    'free_throw_attempts,free_throw_percentage,2_pointer_attempts,2_pointer_percentage,3_pointers_attempted,3_pointer_percentage,effective_shooting_percentage,'
    'true_shooting_percentage,points_per_game,rebounds_per_game,total_rebound_percentage,assists_per_game,'
    'assists_percentage_per_game,steals_per_game,blocks_per_game,turnovers_per_game,versatility_index)'
    "VALUES"
    "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")


    for row in csv_reader:
        mycursor.execute(stmt, row)

    db.commit()

    mycursor.close()

    db.close()

# Prints out the entire player table.
mycursor.execute("SELECT * FROM player")

myresult = mycursor.fetchall()

for x in myresult:
  #print(x)

# Question number one. Who averaged the most points during the NBA playoffs this past year?
# Looks like Luke Doncic of the Dallas Mavericks averaged the most points.

mycursor.execute("SELECT player_name,team,points_per_game FROM player ORDER BY points_per_game desc LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Who was used the most while on the floor?
# According to the data, it was Willy Hernangomez. 4th was Luka Doncic.
mycursor.execute("SELECT player_name,team,points_per_game FROM player ORDER BY points_per_game desc LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

