'''
In this lab, we will use the NBA API to determine how well the Golden State Warriors performed against the Toronto Raptors.
We will use the API to determine the number of points the Golden State Warriors won or lost by for each game.
So if the value is three, the Golden State Warriors won by three points. 
Similarly it the Golden State Warriors lost by two points the result will be negative two. 
The API will handle a lot of the details, such a Endpoints and Authentication.
'''

#use pip install nba_api for installation

from nba_api.stats.static import teams
import matplotlib.pyplot as plt
import pandas as pd

from nba_api.stats.endpoints import leaguegamefinder

import requests
'''
The one_dict function takes a list of dictionaries (each representing one team's details)
and combines them into a sngle dictionary where each key contains a list of all
corresponding values.
'''
def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key,value in dict_.items():
            out_dict[key].append(value)
    return out_dict  

# The method get_teams() returns a list of dictionaries.

nba_teams=teams.get_teams()      
#The dictionary key id has a unique identifier for each team as a value, Let's look at the first three elements of the list

print(nba_teams[0:3])

'''
To make things easier, we an convert the dictionary to a table .First we use the function 
one dict  to create  a dictionary . We use the common keys for each team as the keys , the value 
is a list; each elements of the lsit corresponds to the values for each team.
We then convert the dictionary to a dataframe, each row contains the information for a 
different team.
'''

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
#print(df_teams.head())
#We will use the team's nickname to find the unique id, we can see the row that contains 
#the warriors by using the column nickname as follows:

df_warriors=df_teams[df_teams['nickname']=='Warriors']
#print(df_warriors)
#df_warriors.to_csv("DataOfWarriors.csv")

id_warriors=df_warriors[['id']].values[0][0]
#print(id_warriors)

'''
The funciton "League Game Finder  will make an API call, it's in the module stats.endpoints

The parameter team_id_nullable is the unique ID for the warriors . Under the hood,
the NBA API is making a HTTP request
The information requested is provided and is transmitted via an HTTP response this
is assigned to the object game finder.
'''

# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is commented out, you can run it on jupyter labs on your own computer.
# gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

gamefinder=leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
# gamefinder.get_json
#print(gamefinder.get_json)
#We can see the json file by running the following line of code

'''
The game finder object has a method get_data_frames(),that returns a dataframe.
If we view the dataframe , we can see it contains information about all the games
teh Warriors played . The PLUS_MINUS column contains information on the score, if
the value is negative , the Warriors lost by that many points , if the value is positive,
the warriors won by that amout of points. The column MATCHUP has the team the Warriors were playing,
GSW stands for Golden State Warriors and TOR means Toranto Raptors. vs signifies it was home game
and the @ symbol means an away game.
'''

#games=gamefinder.get_data_frames()[0]
#print(games.head())


filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")

file_name="Golden_State.pkl"
games=pd.read_pickle(file_name)
#print(games.head())
'''
We can create two dataframes, one for the games that the Warriors faced the raptors
at home, and the second for away games.
'''
games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']

games_home['PLUS_MINUS'].mean()
games_away['PLUS_MINUS'].mean()

'''
We can plot out the PLUS MINUS column for the dataframes games_home and games _away.
We see the warriors played batter at home.
'''
fig, ax=plt.subplots()
games_away.plot(x="GAME_DATE",y="PLUS_MINUS",ax=ax)
games_home.plot(x="GAME_DATE",y="PLUS_MINUS",ax=ax)
ax.legend("away","home")
print(plt.show())