# course: INST126
# date: 12/13/2017
# Group name: The Allstars
# Project description: Our program is a platform Fantasy Football users can use to compare the stats of there top 2 defensive teams
# against the teams they will play for the week. 
##Tem roles and contributions
##Nick – Program Architect. Controlled the concept and aim of the project. Provided API Key and managed to hard code the data from nested
##list into if statements for each team, and provided comments.
##CJ – Added interactive print statements, on copying the code and editing the variables in order for the user to only need to run the
##program once, and compare both of their matchups.
##Mahdre – Worked on developing a for loop to stop user from entering same team name twice, input validations, and assisted on coding
##style and corrections. 
##Lindsay – Focused mainly on coding style, making sure that spaces, indentation, spelling were correct on all if statements, 
##and provided comments.
########################################################################
# Imports functions used for extracting json data

import urllib.request, urllib.parse, urllib.error
import json
import urllib

# Here we are accessing the URL with our trial code, which has 1000 calls.

service_url = 'http://api.sportradar.us/nfl-ot2/seasontd/2017/standings.json?api_key=3238yxzhzy955v3pauctmbng'
data = json.loads(urllib.request.urlopen(service_url).read())

print("season:", data["season"]["year"])  # here we are declaring the year of this season
print("week:", data["week"]["title"])  # here we are declaring the week of the season

# First, Select the first defense that you are considering playing.

my_Defense = input("What defense are you going to play?(Enter their mascot name)\n")

if my_Defense == "Patriots":
    def_Allowed = data["conferences"][0]["divisions"][0]["teams"][0]["points_against"]
if my_Defense == "Bills":
    def_Allowed = data["conferences"][0]["divisions"][0]["teams"][1]["points_against"]
if my_Defense == "Jets":
    def_Allowed = data["conferences"][0]["divisions"][0]["teams"][2]["points_against"]
if my_Defense == "Dolphins":
    def_Allowed = data["conferences"][0]["divisions"][0]["teams"][3]["points_against"]
if my_Defense == "Steelers":
    def_Allowed = data["conferences"][0]["divisions"][1]["teams"][0]["points_against"]
if my_Defense == "Ravens":
    def_Allowed = data["conferences"][0]["divisions"][1]["teams"][1]["points_against"]
if my_Defense == "Bengals":
    def_Allowed = data["conferences"][0]["divisions"][1]["teams"][2]["points_against"]
if my_Defense == "Browns":
    def_Allowed = data["conferences"][0]["divisions"][1]["teams"][3]["points_against"]
if my_Defense == "Titans":
    def_Allowed = data["conferences"][0]["divisions"][2]["teams"][0]["points_against"]
if my_Defense == "Jaguars":
    def_Allowed = data["conferences"][0]["divisions"][2]["teams"][1]["points_against"]
if my_Defense == "Texans":
    def_Allowed = data["conferences"][0]["divisions"][2]["teams"][2]["points_against"]
if my_Defense == "Colts":
    def_Allowed = data["conferences"][0]["divisions"][2]["teams"][3]["points_against"]
if my_Defense == "Chiefs":
    def_Allowed = data["conferences"][0]["divisions"][3]["teams"][0]["points_against"]
if my_Defense == "Raiders":
    def_Allowed = data["conferences"][0]["divisions"][3]["teams"][1]["points_against"]
if my_Defense == "Chargers":
    def_Allowed = data["conferences"][0]["divisions"][3]["teams"][2]["points_against"]
if my_Defense == "Broncos":
    def_Allowed = data["conferences"][0]["divisions"][3]["teams"][3]["points_against"]
if my_Defense == "Eagles":
    def_Allowed = data["conferences"][1]["divisions"][0]["teams"][0]["points_against"]
if my_Defense == "Cowboys":
    def_Allowed = data["conferences"][1]["divisions"][0]["teams"][1]["points_against"]
if my_Defense == "Redskins":
    def_Allowed = data["conferences"][1]["divisions"][0]["teams"][2]["points_against"]
if my_Defense == "Giants":
    def_Allowed = data["conferences"][1]["divisions"][0]["teams"][3]["points_against"]
if my_Defense == "Vikings":
    def_Allowed = data["conferences"][1]["divisions"][1]["teams"][0]["points_against"]
if my_Defense == "Lions":
    def_Allowed = data["conferences"][1]["divisions"][1]["teams"][1]["points_against"]
if my_Defense == "Packers":
    def_Allowed = data["conferences"][1]["divisions"][1]["teams"][2]["points_against"]
if my_Defense == "Bears":
    def_Allowed = data["conferences"][1]["divisions"][1]["teams"][3]["points_against"]
if my_Defense == "Saints":
    def_Allowed = data["conferences"][1]["divisions"][2]["teams"][0]["points_against"]
if my_Defense == "Panthers":
    def_Allowed = data["conferences"][1]["divisions"][2]["teams"][1]["points_against"]
if my_Defense == "Falcons":
    def_Allowed = data["conferences"][1]["divisions"][2]["teams"][2]["points_against"]
if my_Defense == "Buccaneers":
    def_Allowed = data["conferences"][1]["divisions"][2]["teams"][3]["points_against"]
if my_Defense == "Rams":
    def_Allowed = data["conferences"][1]["divisions"][3]["teams"][0]["points_against"]
if my_Defense == "Seahawks":
    def_Allowed = data["conferences"][1]["divisions"][3]["teams"][1]["points_against"]
if my_Defense == "Cardinals":
    def_Allowed = data["conferences"][1]["divisions"][3]["teams"][2]["points_against"]
if my_Defense == "49ers":
    def_Allowed = data["conferences"][1]["divisions"][3]["teams"][3]["points_against"]
print("Your first choice for defense is:" + " " + my_Defense)

# Below is the team your first option defense is up against. Section determines how well their offense has played this season.

team_Playing = input("What team are they playing?\n")

if team_Playing == "Patriots":
    offense_Scored = data["conferences"][0]["divisions"][0]["teams"][0]["points_for"]
if team_Playing == "Bills":
    offense_Scored = data["conferences"][0]["divisions"][0]["teams"][1]["points_for"]
if team_Playing == "Jets":
    offense_Scored = data["conferences"][0]["divisions"][0]["teams"][2]["points_for"]
if team_Playing == "Dolphins":
    offense_Scored = data["conferences"][0]["divisions"][0]["teams"][3]["points_for"]
if team_Playing == "Steelers":
    offense_Scored = data["conferences"][0]["divisions"][1]["teams"][0]["points_for"]
if team_Playing == "Ravens":
    offense_Scored = data["conferences"][0]["divisions"][1]["teams"][1]["points_for"]
if team_Playing == "Bengals":
    offense_Scored = data["conferences"][0]["divisions"][1]["teams"][2]["points_for"]
if team_Playing == "Browns":
    offense_Scored = data["conferences"][0]["divisions"][1]["teams"][3]["points_for"]
if team_Playing == "Titans":
    offense_Scored = data["conferences"][0]["divisions"][2]["teams"][0]["points_for"]
if team_Playing == "Jaguars":
    offense_Scored = data["conferences"][0]["divisions"][2]["teams"][1]["points_for"]
if team_Playing == "Texans":
    offense_Scored = data["conferences"][0]["divisions"][2]["teams"][2]["points_for"]
if team_Playing == "Colts":
    offense_Scored = data["conferences"][0]["divisions"][2]["teams"][3]["points_for"]
if team_Playing == "Chiefs":
    offense_Scored = data["conferences"][0]["divisions"][3]["teams"][0]["points_for"]
if team_Playing == "Raiders":
    offense_Scored = data["conferences"][0]["divisions"][3]["teams"][1]["points_for"]
if team_Playing == "Chargers":
    offense_Scored = data["conferences"][0]["divisions"][3]["teams"][2]["points_for"]
if team_Playing == "Broncos":
    offense_Scored = data["conferences"][0]["divisions"][3]["teams"][3]["points_for"]
if team_Playing == "Eagles":
    offense_Scored = data["conferences"][1]["divisions"][0]["teams"][0]["points_for"]
if team_Playing == "Cowboys":
    offense_Scored = data["conferences"][1]["divisions"][0]["teams"][1]["points_for"]
if team_Playing == "Redskins":
    offense_Scored = data["conferences"][1]["divisions"][0]["teams"][2]["points_for"]
if team_Playing == "Giants":
    offense_Scored = data["conferences"][1]["divisions"][0]["teams"][3]["points_for"]
if team_Playing == "Vikings":
    offense_Scored = data["conferences"][1]["divisions"][1]["teams"][0]["points_for"]
if team_Playing == "Lions":
    offense_Scored = data["conferences"][1]["divisions"][1]["teams"][1]["points_for"]
if team_Playing == "Packers":
    offense_Scored = data["conferences"][1]["divisions"][1]["teams"][2]["points_for"]
if team_Playing == "Bears":
    offense_Scored = data["conferences"][1]["divisions"][1]["teams"][3]["points_for"]
if team_Playing == "Saints":
    offense_Scored = data["conferences"][1]["divisions"][2]["teams"][0]["points_for"]
if team_Playing == "Panthers":
    offense_Scored = data["conferences"][1]["divisions"][2]["teams"][1]["points_for"]
if team_Playing == "Falcons":
    offense_Scored = data["conferences"][1]["divisions"][2]["teams"][2]["points_for"]
if team_Playing == "Buccaneers":
    offense_Scored = data["conferences"][1]["divisions"][2]["teams"][3]["points_for"]
if team_Playing == "Rams":
    offense_Scored = data["conferences"][1]["divisions"][3]["teams"][0]["points_for"]
if team_Playing == "Seahawks":
    offense_Scored = data["conferences"][1]["divisions"][3]["teams"][1]["points_for"]
if team_Playing == "Cardinals":
    offense_Scored = data["conferences"][1]["divisions"][3]["teamss"][2]["points_for"]
if team_Playing == "49ers":
    offense_Scored = data["conferences"][1]["divisions"][3]["teams"][3]["points_for"]

print("The" + " " + my_Defense + " are going up against:" + " " + team_Playing)

if my_Defense == "Patriots":
    sos = data["conferences"][0]["divisions"][0]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense == "Bills":
    sos = data["conferences"][0]["divisions"][0]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense == "Jets":
    sos = data["conferences"][0]["divisions"][0]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense == "Dolphins":
    sos = data["conferences"][0]["divisions"][0]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense == "Steelers":
    sos = data["conferences"][0]["divisions"][1]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense == "Ravens":
    sos = data["conferences"][0]["divisions"][1]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense == "Bengals":
    sos = data["conferences"][0]["divisions"][1]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense == "Browns":
    sos = data["conferences"][0]["divisions"][1]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense == "Titans":
    sos = data["conferences"][0]["divisions"][2]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense == "Jaguars":
    sos = data["conferences"][0]["divisions"][2]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense == "Texans":
    sos = data["conferences"][0]["divisions"][2]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense == "Colts":
    sos = data["conferences"][0]["divisions"][2]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense == "Chiefs":
    sos = data["conferences"][0]["divisions"][3]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense == "Raiders":
    sos = data["conferences"][0]["divisions"][3]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense == "Chargers":
    sos = data["conferences"][0]["divisions"][3]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense == "Broncos":
    sos = data["conferences"][0]["divisions"][3]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense == "Eagles":
    sos = data["conferences"][1]["divisions"][0]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense == "Cowboys":
    sos = data["conferences"][1]["divisions"][0]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense == "Redskins":
    sos = data["conferences"][1]["divisions"][0]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense == "Giants":
    sos = data["conferences"][1]["divisions"][0]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense == "Vikings":
    sos = data["conferences"][1]["divisions"][1]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense == "Lions":
    sos = data["conferences"][1]["divisions"][1]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense == "Packers":
    sos = data["conferences"][1]["divisions"][1]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense == "Bears":
    sos = data["conferences"][1]["divisions"][1]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense == "Saints":
    sos = data["conferences"][1]["divisions"][2]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense == "Panthers":
    sos = data["conferences"][1]["divisions"][2]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense == "Falcons":
    sos = data["conferences"][1]["divisions"][2]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense == "Buccaneers":
    sos = data["conferences"][1]["divisions"][2]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense == "Rams":
    sos = data["conferences"][1]["divisions"][3]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense == "Seahawks":
    sos = data["conferences"][1]["divisions"][3]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense == "Cardinals":
    sos = data["conferences"][1]["divisions"][3]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense == "49ers":
    sos = data["conferences"][1]["divisions"][3]["teams"][3]["strength_of_schedule"]["sos"]

if team_Playing == "Patriots":
    sos2 = data["conferences"][0]["divisions"][0]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing == "Bills":
    sos2 = data["conferences"][0]["divisions"][0]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing == "Jets":
    sos2 = data["conferences"][0]["divisions"][0]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing == "Dolphins":
    sos2 = data["conferences"][0]["divisions"][0]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing == "Steelers":
    sos2 = data["conferences"][0]["divisions"][1]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing == "Ravens":
    sos2 = data["conferences"][0]["divisions"][1]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing == "Bengals":
    sos2 = data["conferences"][0]["divisions"][1]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing == "Browns":
    sos2 = data["conferences"][0]["divisions"][1]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing == "Titans":
    sos2 = data["conferences"][0]["divisions"][2]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing == "Jaguars":
    sos2 = data["conferences"][0]["divisions"][2]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing == "Texans":
    sos2 = data["conferences"][0]["divisions"][2]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing == "Colts":
    sos2 = data["conferences"][0]["divisions"][2]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing == "Chiefs":
    sos2 = data["conferences"][0]["divisions"][3]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing == "Raiders":
    sos2 = data["conferences"][0]["divisions"][3]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing == "Chargers":
    sos2 = data["conferences"][0]["divisions"][3]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing == "Broncos":
    sos2 = data["conferences"][0]["divisions"][3]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing == "Eagles":
    sos2 = data["conferences"][1]["divisions"][0]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing == "Cowboys":
    sos2 = data["conferences"][1]["divisions"][0]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing == "Redskins":
    sos2 = data["conferences"][1]["divisions"][0]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing == "Giants":
    sos2 = data["conferences"][1]["divisions"][0]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing == "Vikings":
    sos2 = data["conferences"][1]["divisions"][1]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing == "Lions":
    sos2 = data["conferences"][1]["divisions"][1]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing == "Packers":
    sos2 = data["conferences"][1]["divisions"][1]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing == "Bears":
    sos2 = data["conferences"][1]["divisions"][1]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing == "Saints":
    sos2 = data["conferences"][1]["divisions"][2]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing == "Panthers":
    sos2 = data["conferences"][1]["divisions"][2]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing == "Falcons":
    sos2 = data["conferences"][1]["divisions"][2]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing == "Buccaneers":
    sos2 = data["conferences"][1]["divisions"][2]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing == "Rams":
    sos2 = data["conferences"][1]["divisions"][3]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing == "Seahawks":
    sos2 = data["conferences"][1]["divisions"][3]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing == "Cardinals":
    sos2 = data["conferences"][1]["divisions"][3]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing == "49ers":
    sos2 = data["conferences"][1]["divisions"][3]["teams"][3]["strength_of_schedule"]["sos"]

print("The strength of schedules have been recorded!\n ")

# This is for the second Defense that the user is considering choosing

my_Defense2 = input("What other defense are you going to play?(Enter their mascot name)\n")

if my_Defense2 == "Patriots":
    def_Allowed2 = data["conferences"][0]["divisions"][0]["teams"][0]["points_against"]
if my_Defense2 == "Bills":
    def_Allowed2 = data["conferences"][0]["divisions"][0]["teams"][1]["points_against"]
if my_Defense2 == "Jets":
    def_Allowed2 = data["conferences"][0]["divisions"][0]["teams"][2]["points_against"]
if my_Defense2 == "Dolphins":
    def_Allowed2 = data["conferences"][0]["divisions"][0]["teams"][3]["points_against"]
if my_Defense2 == "Steelers":
    def_Allowed2 = data["conferences"][0]["divisions"][1]["teams"][0]["points_against"]
if my_Defense2 == "Ravens":
    def_Allowed2 = data["conferences"][0]["divisions"][1]["teams"][1]["points_against"]
if my_Defense2 == "Bengals":
    def_Allowed2 = data["conferences"][0]["divisions"][1]["teams"][2]["points_against"]
if my_Defense2 == "Browns":
    def_Allowed2 = data["conferences"][0]["divisions"][1]["teams"][3]["points_against"]
if my_Defense2 == "Titans":
    def_Allowed2 = data["conferences"][0]["divisions"][2]["teams"][0]["points_against"]
if my_Defense2 == "Jaguars":
    def_Allowed2 = data["conferences"][0]["divisions"][2]["teams"][1]["points_against"]
if my_Defense2 == "Texans":
    def_Allowed2 = data["conferences"][0]["divisions"][2]["teams"][2]["points_against"]
if my_Defense2 == "Colts":
    def_Allowed2 = data["conferences"][0]["divisions"][2]["teams"][3]["points_against"]
if my_Defense2 == "Chiefs":
    def_Allowed2 = data["conferences"][0]["divisions"][3]["teams"][0]["points_against"]
if my_Defense2 == "Raiders":
    def_Allowed2 = data["conferences"][0]["divisions"][3]["teams"][1]["points_against"]
if my_Defense2 == "Chargers":
    def_Allowed2 = data["conferences"][0]["divisions"][3]["teams"][2]["points_against"]
if my_Defense2 == "Broncos":
    def_Allowed2 = data["conferences"][0]["divisions"][3]["teams"][3]["points_against"]
if my_Defense2 == "Eagles":
    def_Allowed2 = data["conferences"][1]["divisions"][0]["teams"][0]["points_against"]
if my_Defense2 == "Cowboys":
    def_Allowed2 = data["conferences"][1]["divisions"][0]["teams"][1]["points_against"]
if my_Defense2 == "Redskins":
    def_Allowed2 = data["conferences"][1]["divisions"][0]["teams"][2]["points_against"]
if my_Defense2 == "Giants":
    def_Allowed2 = data["conferences"][1]["divisions"][0]["teams"][3]["points_against"]
if my_Defense2 == "Vikings":
    def_Allowed2 = data["conferences"][1]["divisions"][1]["teams"][0]["points_against"]
if my_Defense2 == "Lions":
    def_Allowed2 = data["conferences"][1]["divisions"][1]["teams"][1]["points_against"]
if my_Defense2 == "Packers":
    def_Allowed2 = data["conferences"][1]["divisions"][1]["teams"][2]["points_against"]
if my_Defense2 == "Bears":
    def_Allowed2 = data["conferences"][1]["divisions"][1]["teams"][3]["points_against"]
if my_Defense2 == "Saints":
    def_Allowed2 = data["conferences"][1]["divisions"][2]["teams"][0]["points_against"]
if my_Defense2 == "Panthers":
    def_Allowed2 = data["conferences"][1]["divisions"][2]["teams"][1]["points_against"]
if my_Defense2 == "Falcons":
    def_Allowed2 = data["conferences"][1]["divisions"][2]["teams"][2]["points_against"]
if my_Defense2 == "Buccaneers":
    def_Allowed2 = data["conferences"][1]["divisions"][2]["teams"][3]["points_against"]
if my_Defense2 == "Rams":
    def_Allowed2 = data["conferences"][1]["divisions"][3]["teams"][0]["points_against"]
if my_Defense2 == "Seahawks":
    def_Allowed2 = data["conferences"][1]["divisions"][3]["teams"][1]["points_against"]
if my_Defense2 == "Cardinals":
    def_Allowed2 = data["conferences"][1]["divisions"][3]["teams"][2]["points_against"]
if my_Defense2 == "49ers":
    def_Allowed2 = data["conferences"][1]["divisions"][3]["teams"][3]["points_against"]

print("Your second choice for defense is:" + " " + my_Defense2 )

# Now, this is the second team the users second defense is up against.

team_Playing2 = input("What team are they playing?\n")

if team_Playing2 == "Patriots":
    offense_Scored2 = data["conferences"][0]["divisions"][0]["teams"][0]["points_for"]
if team_Playing2 == "Bills":
    offense_Scored2 = data["conferences"][0]["divisions"][0]["teams"][1]["points_for"]
if team_Playing2 == "Jets":
    offense_Scored2 = data["conferences"][0]["divisions"][0]["teams"][2]["points_for"]
if team_Playing2 == "Dolphins":
    offense_Scored2 = data["conferences"][0]["divisions"][0]["teams"][3]["points_for"]
if team_Playing2 == "Steelers":
    offense_Scored2 = data["conferences"][0]["divisions"][1]["teams"][0]["points_for"]
if team_Playing2 == "Ravens":
    offense_Scored2 = data["conferences"][0]["divisions"][1]["teams"][1]["points_for"]
if team_Playing2 == "Bengals":
    offense_Scored2 = data["conferences"][0]["divisions"][1]["teams"][2]["points_for"]
if team_Playing2 == "Browns":
    offense_Scored2 = data["conferences"][0]["divisions"][1]["teams"][3]["points_for"]
if team_Playing2 == "Titans":
    offense_Scored2 = data["conferences"][0]["divisions"][2]["teams"][0]["points_for"]
if team_Playing2 == "Jaguars":
    offense_Scored2 = data["conferences"][0]["divisions"][2]["teams"][1]["points_for"]
if team_Playing2 == "Texans":
    offense_Scored2 = data["conferences"][0]["divisions"][2]["teams"][2]["points_for"]
if team_Playing2 == "Colts":
    offense_Scored2 = data["conferences"][0]["divisions"][2]["teams"][3]["points_for"]
if team_Playing2 == "Chiefs":
    offense_Scored2 = data["conferences"][0]["divisions"][3]["teams"][0]["points_for"]
if team_Playing2 == "Raiders":
    offense_Scored2 = data["conferences"][0]["divisions"][3]["teams"][1]["points_for"]
if team_Playing2 == "Chargers":
    offense_Scored2 = data["conferences"][0]["divisions"][3]["teams"][2]["points_for"]
if team_Playing2 == "Broncos":
    offense_Scored2 = data["conferences"][0]["divisions"][3]["teams"][3]["points_for"]
if team_Playing2 == "Eagles":
    offense_Scored2 = data["conferences"][1]["divisions"][0]["teams"][0]["points_for"]
if team_Playing2 == "Cowboys":
    offense_Scored2 = data["conferences"][1]["divisions"][0]["teams"][1]["points_for"]
if team_Playing2 == "Redskins":
    offense_Scored2 = data["conferences"][1]["divisions"][0]["teams"][2]["points_for"]
if team_Playing2 == "Giants":
    offense_Scored2 = data["conferences"][1]["divisions"][0]["teams"][3]["points_for"]
if team_Playing2 == "Vikings":
    offense_Scored2 = data["conferences"][1]["divisions"][1]["teams"][0]["points_for"]
if team_Playing2 == "Lions":
    offense_Scored2 = data["conferences"][1]["divisions"][1]["teams"][1]["points_for"]
if team_Playing2 == "Packers":
    offense_Scored2 = data["conferences"][1]["divisions"][1]["teams"][2]["points_for"]
if team_Playing2 == "Bears":
    offense_Scored2 = data["conferences"][1]["divisions"][1]["teams"][3]["points_for"]
if team_Playing2 == "Saints":
    offense_Scored2 = data["conferences"][1]["divisions"][2]["teams"][0]["points_for"]
if team_Playing2 == "Panthers":
    offense_Scored2 = data["conferences"][1]["divisions"][2]["teams"][1]["points_for"]
if team_Playing2 == "Falcons":
    offense_Scored2 = data["conferences"][1]["divisions"][2]["teams"][2]["points_for"]
if team_Playing2 == "Buccaneers":
    offense_Scored2 = data["conferences"][1]["divisions"][2]["teams"][3]["points_for"]
if team_Playing2 == "Rams":
    offense_Scored2 = data["conferences"][1]["divisions"][3]["teams"][0]["points_for"]
if team_Playing2 == "Seahawks":
    offense_Scored2 = data["conferences"][1]["divisions"][3]["teams"][1]["points_for"]
if team_Playing2 == "Cardinals":
    offense_Scored2 = data["conferences"][1]["divisions"][3]["teamss"][2]["points_for"]
if team_Playing2 == "49ers":
    offense_Scored2 = data["conferences"][1]["divisions"][3]["teams"][3]["points_for"]

print("The" + " " + my_Defense2 + " are going up against:" + " " + team_Playing2)

if my_Defense2 == "Patriots":
    sos3 = data["conferences"][0]["divisions"][0]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense2 == "Bills":
    sos3 = data["conferences"][0]["divisions"][0]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense2 == "Jets":
    sos3 = data["conferences"][0]["divisions"][0]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense2 == "Dolphins":
    sos3 = data["conferences"][0]["divisions"][0]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense2 == "Steelers":
    sos3 = data["conferences"][0]["divisions"][1]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense2 == "Ravens":
    sos3 = data["conferences"][0]["divisions"][1]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense2 == "Bengals":
    sos3 = data["conferences"][0]["divisions"][1]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense2 == "Browns":
    sos3 = data["conferences"][0]["divisions"][1]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense2 == "Titans":
    sos3 = data["conferences"][0]["divisions"][2]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense2 == "Jaguars":
    sos3 = data["conferences"][0]["divisions"][2]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense2 == "Texans":
    sos3 = data["conferences"][0]["divisions"][2]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense2 == "Colts":
    sos3 = data["conferences"][0]["divisions"][2]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense2 == "Chiefs":
    sos3 = data["conferences"][0]["divisions"][3]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense2 == "Raiders":
    sos3 = data["conferences"][0]["divisions"][3]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense2 == "Chargers":
    sos3 = data["conferences"][0]["divisions"][3]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense2 == "Broncos":
    sos3 = data["conferences"][0]["divisions"][3]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense2 == "Eagles":
    sos3 = data["conferences"][1]["divisions"][0]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense2 == "Cowboys":
    sos3 = data["conferences"][1]["divisions"][0]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense2 == "Redskins":
    sos3 = data["conferences"][1]["divisions"][0]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense2 == "Giants":
    sos3 = data["conferences"][1]["divisions"][0]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense2 == "Vikings":
    sos3 = data["conferences"][1]["divisions"][1]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense2 == "Lions":
    sos3 = data["conferences"][1]["divisions"][1]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense2 == "Packers":
    sos3 = data["conferences"][1]["divisions"][1]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense2 == "Bears":
    sos3 = data["conferences"][1]["divisions"][1]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense2 == "Saints":
    sos3 = data["conferences"][1]["divisions"][2]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense2 == "Panthers":
    sos3 = data["conferences"][1]["divisions"][2]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense2 == "Falcons":
    sos3 = data["conferences"][1]["divisions"][2]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense2 == "Buccaneers":
    sos3 = data["conferences"][1]["divisions"][2]["teams"][3]["strength_of_schedule"]["sos"]
if my_Defense2 == "Rams":
    sos3 = data["conferences"][1]["divisions"][3]["teams"][0]["strength_of_schedule"]["sos"]
if my_Defense2 == "Seahawks":
    sos3 = data["conferences"][1]["divisions"][3]["teams"][1]["strength_of_schedule"]["sos"]
if my_Defense2 == "Cardinals":
    sos3 = data["conferences"][1]["divisions"][3]["teams"][2]["strength_of_schedule"]["sos"]
if my_Defense2 == "49ers":
    sos3 = data["conferences"][1]["divisions"][3]["teams"][3]["strength_of_schedule"]["sos"]

if team_Playing2 == "Patriots":
    sos4 = data["conferences"][0]["divisions"][0]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing2 == "Bills":
    sos4 = data["conferences"][0]["divisions"][0]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing2 == "Jets":
    sos4 = data["conferences"][0]["divisions"][0]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing2 == "Dolphins":
    sos4 = data["conferences"][0]["divisions"][0]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing2 == "Steelers":
    sos4 = data["conferences"][0]["divisions"][1]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing2 == "Ravens":
    sos4 = data["conferences"][0]["divisions"][1]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing2 == "Bengals":
    sos4 = data["conferences"][0]["divisions"][1]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing2 == "Browns":
    sos4 = data["conferences"][0]["divisions"][1]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing2 == "Titans":
    sos4 = data["conferences"][0]["divisions"][2]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing2 == "Jaguars":
    sos4 = data["conferences"][0]["divisions"][2]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing2 == "Texans":
    sos4 = data["conferences"][0]["divisions"][2]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing2 == "Colts":
    sos4 = data["conferences"][0]["divisions"][2]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing2 == "Chiefs":
    sos4 = data["conferences"][0]["divisions"][3]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing2 == "Raiders":
    sos4 = data["conferences"][0]["divisions"][3]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing2 == "Chargers":
    sos4 = data["conferences"][0]["divisions"][3]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing2 == "Broncos":
    sos4 = data["conferences"][0]["divisions"][3]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing2 == "Eagles":
    sos4 = data["conferences"][1]["divisions"][0]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing2 == "Cowboys":
    sos4 = data["conferences"][1]["divisions"][0]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing2 == "Redskins":
    sos4 = data["conferences"][1]["divisions"][0]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing2 == "Giants":
    sos4 = data["conferences"][1]["divisions"][0]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing2 == "Vikings":
    sos4 = data["conferences"][1]["divisions"][1]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing2 == "Lions":
    sos4 = data["conferences"][1]["divisions"][1]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing2 == "Packers":
    sos4 = data["conferences"][1]["divisions"][1]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing2 == "Bears":
    sos4 = data["conferences"][1]["divisions"][1]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing2 == "Saints":
    sos4 = data["conferences"][1]["divisions"][2]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing2 == "Panthers":
    sos4 = data["conferences"][1]["divisions"][2]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing2 == "Falcons":
    sos4 = data["conferences"][1]["divisions"][2]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing2 == "Buccaneers":
    sos4 = data["conferences"][1]["divisions"][2]["teams"][3]["strength_of_schedule"]["sos"]
if team_Playing2 == "Rams":
    sos4 = data["conferences"][1]["divisions"][3]["teams"][0]["strength_of_schedule"]["sos"]
if team_Playing2 == "Seahawks":
    sos4 = data["conferences"][1]["divisions"][3]["teams"][1]["strength_of_schedule"]["sos"]
if team_Playing2 == "Cardinals":
    sos4 = data["conferences"][1]["divisions"][3]["teams"][2]["strength_of_schedule"]["sos"]
if team_Playing2 == "49ers":
    sos4 = data["conferences"][1]["divisions"][3]["teams"][3]["strength_of_schedule"]["sos"]

print("The strength of schedules have been recorded!\n ")

print("The Strength of your Defenses schedule is ", sos, ", the team you are playing against strength of schedule is", sos3, ",")

print("Defense allowed", def_Allowed, " points, The offense they are playing scored ", offense_Scored, " this season.")
point_Differential = offense_Scored - def_Allowed
print("Point Differential: ", point_Differential)


# the point differential determines the likelihood of the defenses success, the user should track the out put and compare it to the next defenses out put to determine a winner.
# print("it is like golf, the smaller the number the better:",point_Differential)
# if point_Differential<=
# data["conferences"][0]["divisions"][0]["teams"][0]["points_against"]



