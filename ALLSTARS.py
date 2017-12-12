# Imports functions used for extracting json data

import urllib.request, urllib.parse, urllib.error
import json
import urllib


# Here we are accessing the URL with our trial code, which has 1000 calls.

service_url = 'http://api.sportradar.us/nfl-ot2/seasontd/2017/standings.json?api_key=3238yxzhzy955v3pauctmbng'
data = json.loads(urllib.request.urlopen(service_url).read())

print("season:", data["season"]["year"]) # here we are declaring the year of this season
print("week:", data["week"]["title"]) # here we are declaring the week of the season



    

#First, Select the defense you are considering playing.

my_Defense = input("What defense are you going to play?(Enter their mascot name)\n")
if my_Defense == "Patriots":
    def_Allowed = data["conferences"][0]["divisions"][0]["teams"][0]["points_against"]
if my_defense == "Bills":
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
    def_Allowed = data["conferences"][0]["divisions"][3]["teams"][3]['points_against"]
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
    def_Allowed = data["conferences"][1]["divisions"][3]['teams'][0]['points_against']
if my_Defense == "Seahawks":
    def_Allowed = data["conferences"][1]["divisions"][3]['teams'][1]['points_against']
if my_Defense == "Cardinals":
    def_Allowed = data["conferences"][1]["divisions"][3]['teams'][2]['points_against']
if my_Defense == "49ers":
    def_Allowed = data["conferences"][1]["divisions"][3]['teams'][3]['points_against']


#below is the team your defense is up against. Section determines how well their offense has played this season.


team_Playing=input("What team are these guys playing?\n")

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
if Team_Playing == "Bengals":
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
if team_Playin g== "Rams":
    offense_Scored =data["conferences"][1]["divisions"][3]["teams"][0]["points_for"]
if team_playing == "Seahawks":
    offense_Scored = data["conferences"][1]["divisions"][3]["teams"][1]["points_for"]
if team_Playing == "Cardinals":
    offense_Scored = data["conferences"][1]["divisions"][3]["teamss"][2]["points_for"]
if team_Playing == "49ers":
    offense_Scored = data["conferences"][1]["divisions"][3]["teams"][3]["points_for"]


if my_Defense == "Patriots":
    sos = data["conferences"][0]["divisions"][0]['teams'][0]['strength_of_schedule']['sos']
if my_Defense == "Bills":
    sos =data["conferences"][0]["divisions"][0]['teams'][1]['strength_of_schedule']['sos']
if my_Defense == "Jets":
    sos =data["conferences"][0]["divisions"][0]['teams'][2]['strength_of_schedule']['sos']
if my_Defense == "Dolphins":
    sos =data["conferences"][0]["divisions"][0]['teams'][3]['strength_of_schedule']['sos']
if my_Defense == "Steelers":
    sos =data["conferences"][0]["divisions"][1]['teams'][0]['strength_of_schedule']['sos']
if my_Defense == "Ravens":
    sos =data["conferences"][0]["divisions"][1]['teams'][1]['strength_of_schedule']['sos']
if my_Defense == "Bengals":
    sos =data["conferences"][0]["divisions"][1]['teams'][2]['strength_of_schedule']['sos']
if my_Defense == "Browns":
    sos = data["conferences"][0]["divisions"][1]['teams'][3]['strength_of_schedule']['sos']
if my_Defense == "Titans":
   sos = data["conferences"][0]["divisions"][2]['teams'][0]['strength_of_schedule']['sos']
if my_Defense == "Jaguars":
    sos = data["conferences"][0]["divisions"][2]['teams'][1]['strength_of_schedule']['sos']
if my_Defense == "Texans":
    sos = data["conferences"][0]["divisions"][2]['teams'][2]['strength_of_schedule']['sos']
if my_Defense == "Colts":
    sos = data["conferences"][0]["divisions"][2]['teams'][3]['strength_of_schedule']['sos']
if my_Defense == "Chiefs":
    sos = data["conferences"][0]["divisions"][3]['teams'][0]['strength_of_schedule']['sos']
if my_Defense == "Raiders":
    sos = data["conferences"][0]["divisions"][3]['teams'][1]['strength_of_schedule']['sos']
if my_Defense == "Chargers":
    sos = data["conferences"][0]["divisions"][3]['teams'][2]['strength_of_schedule']['sos']
if my_Defense == "Broncos":
    sos = data["conferences"][0]["divisions"][3]['teams'][3]['strength_of_schedule']['sos']
if my_Defense == "Eagles":
    sos = data["conferences"][1]["divisions"][0]['teams'][0]['strength_of_schedule']['sos']
if my_Defense == "Cowboys":
    sos = data["conferences"][1]["divisions"][0]['teams'][1]['strength_of_schedule']['sos']
if my_Defense == "Redskins":
    sos = data["conferences"][1]["divisions"][0]['teams'][2]['strength_of_schedule']['sos']
if my_Defense == "Giants":
    sos = data["conferences"][1]["divisions"][0]['teams'][3]['strength_of_schedule']['sos']
if my_Defense == "Vikings":
    sos = data["conferences"][1]["divisions"][1]['teams'][0]['strength_of_schedule']['sos']
if my_Defense == "Lions":
    sos = data["conferences"][1]["divisions"][1]['teams'][1]['strength_of_schedule']['sos']
if my_Defense == "Packers":
    sos = data["conferences"][1]["divisions"][1]['teams'][2]['strength_of_schedule']['sos']
if my_Defense == "Bears":
    sos = data["conferences"][1]["divisions"][1]['teams'][3]['strength_of_schedule']['sos']
if my_Defense == "Saints":
    sos = data["conferences"][1]["divisions"][2]['teams'][0]['strength_of_schedule']['sos']
if my_Defense == "Panthers":
    sos = data["conferences"][1]["divisions"][2]['teams'][1]['strength_of_schedule']['sos']
if my_Defense == "Falcons":
    sos = data["conferences"][1]["divisions"][2]['teams'][2]['strength_of_schedule']['sos']
if my_Defense == "Buccaneers":
    sos = data["conferences"][1]["divisions"][2]['teams'][3]['strength_of_schedule']['sos']
if my_Defense == "Rams":
    sos = data["conferences"][1]["divisions"][3]['teams'][0]['strength_of_schedule']['sos']
if my_Defense == "Seahawks":
    sos = data["conferences"][1]["divisions"][3]['teams'][1]['strength_of_schedule']['sos']
if my_Defense == "Cardinals":
    sos = data["conferences"][1]["divisions"][3]['teams'][2]['strength_of_schedule']['sos']
if my_Defense == "49ers":
    sos = data["conferences"][1]["divisions"][3]['teams'][3]['strength_of_schedule']['sos']





if Team_playing == "Patriots":
    sos2=data["conferences"][0]["divisions"][0]['teams'][0]['strength_of_schedule']['sos']
if Team_playing == "Bills":
    sos2=data["conferences"][0]["divisions"][0]['teams'][1]['strength_of_schedule']['sos']
if Team_playing == "Jets":
    sos2=data["conferences"][0]["divisions"][0]['teams'][2]['strength_of_schedule']['sos']
if Team_playing == "Dolphins":
    sos2=data["conferences"][0]["divisions"][0]['teams'][3]['strength_of_schedule']['sos']
if Team_playing== "Steelers":
    sos2=data["conferences"][0]["divisions"][1]['teams'][0]['strength_of_schedule']['sos']
if Team_playing == "Ravens":
    sos2=data["conferences"][0]["divisions"][1]['teams'][1]['strength_of_schedule']['sos']
if Team_playing == "Bengals":
    sos2=data["conferences"][0]["divisions"][1]['teams'][2]['strength_of_schedule']['sos']
if Team_playing == "Browns":
    sos2=data["conferences"][0]["divisions"][1]['teams'][3]['strength_of_schedule']['sos']
if Team_playing == "Titans":
    sos2=data["conferences"][0]["divisions"][2]['teams'][0]['strength_of_schedule']['sos']
if Team_playing== "Jaguars":
    sos2=data["conferences"][0]["divisions"][2]['teams'][1]['strength_of_schedule']['sos']
if Team_playing == "Texans":
    sos2=data["conferences"][0]["divisions"][2]['teams'][2]['strength_of_schedule']['sos']
if Team_playing == "Colts":
    sos2=data["conferences"][0]["divisions"][2]['teams'][3]['strength_of_schedule']['sos']
if Team_playing == "Chiefs":
    sos2=data["conferences"][0]["divisions"][3]['teams'][0]['strength_of_schedule']['sos']
if Team_playing == "Raiders":
    sos2=data["conferences"][0]["divisions"][3]['teams'][1]['strength_of_schedule']['sos']
if Team_playing == "Chargers":
    sos2=data["conferences"][0]["divisions"][3]['teams'][2]['strength_of_schedule']['sos']
if Team_playing == "Broncos":
    sos2=data["conferences"][0]["divisions"][3]['teams'][3]['strength_of_schedule']['sos']
if Team_playing == "Eagles":
    sos2=data["conferences"][1]["divisions"][0]['teams'][0]['strength_of_schedule']['sos']
if Team_playing == "Cowboys":
    sos2=data["conferences"][1]["divisions"][0]['teams'][1]['strength_of_schedule']['sos']
if Team_playing== "Redskins":
    sos2=data["conferences"][1]["divisions"][0]['teams'][2]['strength_of_schedule']['sos']
if Team_playing== "Giants":
    sos2=data["conferences"][1]["divisions"][0]['teams'][3]['strength_of_schedule']['sos']
if Team_playing == "Vikings":
    sos2=data["conferences"][1]["divisions"][1]['teams'][0]['strength_of_schedule']['sos']
if Team_playing== "Lions":
    sos2=data["conferences"][1]["divisions"][1]['teams'][1]['strength_of_schedule']['sos']
if Team_playing== "Packers":
    sos2=data["conferences"][1]["divisions"][1]['teams'][2]['strength_of_schedule']['sos']
if Team_playing== "Bears":
    sos2=data["conferences"][1]["divisions"][1]['teams'][3]['strength_of_schedule']['sos']
if Team_playing== "Saints":
    sos2=data["conferences"][1]["divisions"][2]['teams'][0]['strength_of_schedule']['sos']
if Team_playing== "Panthers":
    sos2=data["conferences"][1]["divisions"][2]['teams'][1]['strength_of_schedule']['sos']
if Team_playing== "Falcons":
    sos2=data["conferences"][1]["divisions"][2]['teams'][2]['strength_of_schedule']['sos']
if Team_playing== "Buccaneers":
    sos2=data["conferences"][1]["divisions"][2]['teams'][3]['strength_of_schedule']['sos']
if Team_playing== "Rams":
    sos2=data["conferences"][1]["divisions"][3]['teams'][0]['strength_of_schedule']['sos']
if Team_playing== "Seahawks":
    sos2=data["conferences"][1]["divisions"][3]['teams'][1]['strength_of_schedule']['sos']
if Team_playing== "Cardinals":
    sos2=data["conferences"][1]["divisions"][3]['teamss'][2]['strength_of_schedule']['sos']
if Team_playing== "49ers":
    sos2=data["conferences"][1]["divisions"][3]['teams'][3]['strength_of_schedule']['sos']










print("The Strength of your defenses schedule is ",sos,", the team you are playing schedule strength is",sos2,",")

    
    

print("Defense allowed", Def_allowed," points, The offense they are playing scored ",offense_scored," this season.")
point_differential= offense_scored-Def_allowed
print("Point Differential: ",point_differential)


# the point differential determines the likelihood of the defenses success, the user should track the out put and compare it to the next defenses out put to determine a winner.
#print("it is like golf, the smaller the number the better:",point_differential)
#if point_differential<=
#data["conferences"][0]["divisions"][0]['teams'][0]['points_against']



#For loop example



#afc = data["conferences"][0]["divisions"][0]['teams']
#print(afc[0])
#print(afc[2])
#for x in afc:
    #print(x['strength_of_victory']['sov'])
