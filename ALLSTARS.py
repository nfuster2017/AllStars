#below we are importing the functions that are being called
import urllib.request, urllib.parse, urllib.error
import json
import urllib


# Here we are accessing the URL with our trial code, which has 1000 calls.
service_url='http://api.sportradar.us/nfl-ot2/seasontd/2017/standings.json?api_key=3238yxzhzy955v3pauctmbng'
data= json.loads(urllib.request.urlopen(service_url).read())

print("season:", data["season"]["year"])#here we are declaring the year of this season
print("week:", data["week"]["title"])#here we are declaring the week of the season

#week = data["week"]["title"]
#print(week)

#print("week:", data["week"])#here we are declaring the week of the season

#example
#afc = data["conferences"][0]["divisions"][0]['teams']
#print(afc[0])
#print(afc[2])
#for x in afc:
    #print(x['strength_of_victory']['sov'])

#First Select the defense you are considering playing.
#def player_stats(my_Defense):
my_Defense = input('What defense are you going to play?(Enter their mascot name)\n')
if my_Defense == "Patriots":
    def_Allowed = data["conferences"][0]["divisions"][0]['teams'][0]['points_against']
if my_defense == "Bills":
    def_Allowed = data["conferences"][0]["divisions"][0]['teams'][1]['points_against']
if my_Defense == "Jets":
    def_Allowed = data["conferences"][0]["divisions"][0]['teams'][2]['points_against']
if my_Defense == "Dolphins":
    def_Allowed = data["conferences"][0]["divisions"][0]['teams'][3]['points_against']
if my_Defense == "Steelers":
    def_Allowed = data["conferences"][0]["divisions"][1]['teams'][0]['points_against']
if my_Defense == "Ravens":
    def_Allowed = data["conferences"][0]["divisions"][1]['teams'][1]['points_against']
if my_Defense == "Bengals":
    def_Allowed = data["conferences"][0]["divisions"][1]['teams'][2]['points_against']
if my_Defense == "Browns":
    def_Allowed = data["conferences"][0]["divisions"][1]['teams'][3]['points_against']
if my_Defense == "Titans":
   def_Allowed = data["conferences"][0]["divisions"][2]['teams'][0]['points_against']
if my_Defense == "Jaguars":
    def_Allowed = data["conferences"][0]["divisions"][2]['teams'][1]['points_against']
if my_Defense == "Texans":
    def_Allowed = data["conferences"][0]["divisions"][2]['teams'][2]['points_against']
if my_Defense == "Colts":
    def_Allowed = data["conferences"][0]["divisions"][2]['teams'][3]['points_against']
if my_Defense == "Chiefs":
    def_Allowed = data["conferences"][0]["divisions"][3]['teams'][0]['points_against']
if my_Defense == "Raiders":
    def_Allowed = data["conferences"][0]["divisions"][3]['teams'][1]['points_against']
if my_Defense == "Chargers":
    def_Allowed = data["conferences"][0]["divisions"][3]['teams'][2]['points_against']
if my_Defense == "Broncos":
    def_Allowed = data["conferences"][0]["divisions"][3]['teams'][3]['points_against']
if my_Defense == "Eagles":
    def_Allowed = data["conferences"][1]["divisions"][0]['teams'][0]['points_against']
if my_Defense == "Cowboys":
    def_Allowed = data["conferences"][1]["divisions"][0]['teams'][1]['points_against']
if my_Defense == "Redskins":
    def_Allowed = data["conferences"][1]["divisions"][0]['teams'][2]['points_against']
if my_Defense == "Giants":
    def_Allowed = data["conferences"][1]["divisions"][0]['teams'][3]['points_against']
if my_Defense == "Vikings":
    def_Allowed = data["conferences"][1]["divisions"][1]['teams'][0]['points_against']
if my_Defense == "Lions":
    def_Allowed = data["conferences"][1]["divisions"][1]['teams'][1]['points_against']
if my_Defense == "Packers":
    def_Allowed = data["conferences"][1]["divisions"][1]['teams'][2]['points_against']
if my_Defense == "Bears":
    def_Allowed = data["conferences"][1]["divisions"][1]['teams'][3]['points_against']
if my_Defense == "Saints":
    def_Allowed = data["conferences"][1]["divisions"][2]['teams'][0]['points_against']
if my_Defense == "Panthers":
    def_Allowed = data["conferences"][1]["divisions"][2]['teams'][1]['points_against']
if my_Defense == "Falcons":
    def_Allowed = data["conferences"][1]["divisions"][2]['teams'][2]['points_against']
if my_Defense == "Buccaneers":
    def_Allowed = data["conferences"][1]["divisions"][2]['teams'][3]['points_against']
if my_Defense == "Rams":
    def_Allowed = data["conferences"][1]["divisions"][3]['teams'][0]['points_against']
if my_Defense == "Seahawks":
    def_Allowed = data["conferences"][1]["divisions"][3]['teams'][1]['points_against']
if my_Defense == "Cardinals":
    def_Allowed = data["conferences"][1]["divisions"][3]['teams'][2]['points_against']
if my_Defense == "49ers":
    def_Allowed = data["conferences"][1]["divisions"][3]['teams'][3]['points_against']


#below is the team your defense is up against. What it does it find out how well their offense has played this season.

#for data......

team_Playing = input('what team are these guys playing?\n')

if Team_playing == "Patriots":
    offense_scored=data["conferences"][0]["divisions"][0]['teams'][0]['points_for']
if Team_playing == "Bills":
    offense_scored=data["conferences"][0]["divisions"][0]['teams'][1]['points_for']
if Team_playing == "Jets":
    offense_scored=data["conferences"][0]["divisions"][0]['teams'][2]['points_for']
if Team_playing == "Dolphins":
    offense_scored=data["conferences"][0]["divisions"][0]['teams'][3]['points_for']
if Team_playing== "Steelers":
    offense_scored=data["conferences"][0]["divisions"][1]['teams'][0]['points_for']
if Team_playing == "Ravens":
    offense_scored=data["conferences"][0]["divisions"][1]['teams'][1]['points_for']
if Team_playing == "Bengals":
    offense_scored=data["conferences"][0]["divisions"][1]['teams'][2]['points_for']
if Team_playing == "Browns":
    offense_scored=data["conferences"][0]["divisions"][1]['teams'][3]['points_for']
if Team_playing == "Titans":
    offense_scored=data["conferences"][0]["divisions"][2]['teams'][0]['points_for']
if Team_playing== "Jaguars":
    offense_scored=data["conferences"][0]["divisions"][2]['teams'][1]['points_for']
if Team_playing == "Texans":
    offense_scored=data["conferences"][0]["divisions"][2]['teams'][2]['points_for']
if Team_playing == "Colts":
    offense_scored=data["conferences"][0]["divisions"][2]['teams'][3]['points_for']
if Team_playing == "Chiefs":
    offense_scored=data["conferences"][0]["divisions"][3]['teams'][0]['points_for']
if Team_playing == "Raiders":
    offense_scored=data["conferences"][0]["divisions"][3]['teams'][1]['points_for']
if Team_playing == "Chargers":
    offense_scored=data["conferences"][0]["divisions"][3]['teams'][2]['points_for']
if Team_playing == "Broncos":
    offense_scored=data["conferences"][0]["divisions"][3]['teams'][3]['points_for']
if Team_playing == "Eagles":
    offense_scored=data["conferences"][1]["divisions"][0]['teams'][0]['points_for']

if Team_playing == "Cowboys":
    offense_scored=data["conferences"][1]["divisions"][0]['teams'][1]['points_for']

if Team_playing== "Redskins":
    offense_scored=data["conferences"][1]["divisions"][0]['teams'][2]['points_for']
if Team_playing== "Giants":
    offense_scored=data["conferences"][1]["divisions"][0]['teams'][3]['points_for']
if Team_playing == "Vikings":
    offense_scored=data["conferences"][1]["divisions"][1]['teams'][0]['points_for']
if Team_playing== "Lions":
    offense_scored=data["conferences"][1]["divisions"][1]['teams'][1]['points_for']
if Team_playing== "Packers":
    offense_scored=data["conferences"][1]["divisions"][1]['teams'][2]['points_for']
if Team_playing== "Bears":
    offense_scored=data["conferences"][1]["divisions"][1]['teams'][3]['points_for']
if Team_playing== "Saints":
    offense_scored=data["conferences"][1]["divisions"][2]['teams'][0]['points_for']
if Team_playing== "Panthers":
    offense_scored=data["conferences"][1]["divisions"][2]['teams'][1]['points_for']
if Team_playing== "Falcons":
    offense_scored=data["conferences"][1]["divisions"][2]['teams'][2]['points_for']
if Team_playing== "Buccaneers":
    offense_scored=data["conferences"][1]["divisions"][2]['teams'][3]['points_for']
if Team_playing== "Rams":
    offense_scored=data["conferences"][1]["divisions"][3]['teams'][0]['points_for']
if Team_playing== "Seahawks":
    offense_scored=data["conferences"][1]["divisions"][3]['teams'][1]['points_for']
if Team_playing== "Cardinals":
    offense_scored=data["conferences"][1]["divisions"][3]['teamss'][2]['points_for']
if Team_playing== "49ers":
    offense_scored=data["conferences"][1]["divisions"][3]['teams'][3]['points_for']

str_=data["conferences"][1]["divisions"][3]['teams'][3]['points_for']


print("Defense allowed", Def_allowed," points, The offense they are playing scored ",offense_scored," this season.")
point_differential= offense_scored-Def_allowed
print("Point Differential: ",point_differential)


# the point differential determines the likelihood of the defenses success, the user should track the out put and compare it to the next defenses out put to determine a winner.
#print("it is like golf, the smaller the number the better:",point_differential)
#if point_differential<=
#data["conferences"][0]["divisions"][0]['teams'][0]['points_against']

#user_input = input(bjsakbja)
#playerstat(user_input)
