"""
File: sort.py
Editor: Tiffany Nguyen
Date: December 7, 2019
Section: 01
Email: tn4@umbc.edu
Description: This file contains the function getPlayers()  which reads in
the player database into a list data structure and returns it
Program Assumptions:
- Data including first name, last name, special, number, position, shoots,
height, and weight are stored in a database for the roster for all of
the 2019 players.
"""
DEFENSE_POSITION = "D"
GOALIE_POSITION = "G"

from app.model import Player

def getPlayers():
    '''
    goes through the soup and stores individual players' data in a dictionary;
    the dictionaries are all stored in a list
    : param: None
    : return: playerDictionary; dictionary formatted as follows:
        { “offense”: [ [player-1-info] , . . . , [player-n-info] ],
        “defense”: [ [player-1-info] , . . . , [player-n-info] ],
        goalies”: [ [player-1-info] , . . . , [player-n-info] ] }
    Preconditions: database with player information has already been created
    Postconditions: a dictionary of containing players grouped by position
            is returned
    '''
    # query database for all players
    players = Player.query.all()
    # initalize player dictionary
    playerDictionary = {"offense": [], "defense": [], "goalies": []}

    for player in players:
        # store player's data into a list
        playerData = [player.firstName, player.lastName, player.special,\
            player.number,player.position, player.shoots, \
            player.height, player.weight]

        # add the player's data to the appropriate list based on their position
        if player.position == DEFENSE_POSITION:
            playerDictionary["defense"].append(playerData)
        elif player.position == GOALIE_POSITION:
            playerDictionary["goalies"].append(playerData)
        else:
            playerDictionary["offense"].append(playerData)

    return playerDictionary
