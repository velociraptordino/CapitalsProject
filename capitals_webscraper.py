"""
File: capitals_webscraper.py
Editor: Tiffany Nguyen
Date: December 5, 2019
Section: 01
Email: tn4@umbc.edu
Description: This program web-scrapes the Washington Capitals team roster.
Data including first name, last name, special, number, position, shoots,
height, and weight are stored in a database for the roster for all of
the 2019 players.
Program Assumptions:
- roster exists at https://www.nhl.com/capitals/roster
- The site is formatted as it was on Nov 26, 2019; in particular, class names
(ex. name-col__list) are present. If not, program will have to be
modified
- bs4 and requests exist and are properly imported
- app model contains the database and Player class
"""
import requests
from bs4 import BeautifulSoup
from app.model import db, Player

FIRST_NAME = 0
LAST_NAME = 1
SPECIAL = 2
NUMBER = 3
POSITION = 4
SHOOTS = 5
HEIGHT = 6
WEIGHT = 7
##############################################################################
def getPlayersData(soup):
    '''
    goes through the soup and stores individual players' data in a dictionary;
    the dictionaries are all stored in a list
    : param: soup; html soup from the roster site
    : return dataList; list of dictionaries containing the data about
                each of the players
    Preconditions: soup is of the roster site of the Washington Capitals
                   class names such as name-col__firstName, name-col__lastName
                   exist in the soup
    Postconditions: a list of dictionaries with all of the appropriate data
                    is returned
    '''
    # get lists of all relevant data
    firstNamesList = soup.select("span.name-col__firstName")
    lastNamesList = soup.select("span.name-col__lastName")
    specialsList = soup.select("span.name-col__special")
    numbersList = soup.select("td.number-col")
    positionsList =  soup.select("td.position-col")
    shootsList = soup.select("td.shoots-col")
    heightsList = soup.select("td.height-col span.xs-sm-md-only")
    weightsList = soup.select("td.weight-col")

    # intialize table
    dataList = []
    for i in range(len(firstNamesList)):
        # get individual's information
        firstName = firstNamesList[i].text.strip()
        lastName = lastNamesList[i].text.strip()
        special = specialsList[i].text.strip()
        number = numbersList[i].text.strip()
        position = positionsList[i].text.strip()
        shoots = shootsList[i].text.strip()
        height = heightsList[i].text
        weight = weightsList[i].text.strip()

        # store player's info in list
        player = [firstName, lastName, special, number, position,\
            shoots, height, weight]

        # store individual's data into a row
        dataList.append(player)

    return(dataList)
##############################################################################
def writeDatabase(data):
    '''
    goes through 2D list, where each row has the player data and stores
    the data into a database
    : param: data; data stored in a 2D list
    : return: None
    Preconditions: data has been accurately scraped and stored in a 2D list;
        for each row, data is stored as follows: firstName, lastName, special,
        number, position,shoots, height, weight
    Postconditions: database of players has been created
    '''
    # go through list of data and store each row, representing player data
    for i in range(len(data)):
        db.session.add(Player(
            firstName = data[i][FIRST_NAME],
            lastName = data[i][LAST_NAME],
            special = data[i][SPECIAL],
            number = data[i][NUMBER],
            position = data[i][POSITION],
            shoots = data[i][SHOOTS],
            height = data[i][HEIGHT],
            weight = data[i][WEIGHT],
        ))
    # create and commit changes
    db.create_all()
    db.session.commit()
##############################################################################
if __name__ == '__main__':
    # get string of the roster web page
    html = requests.get("https://www.nhl.com/capitals/roster").text
    # get soup of the page
    soup = BeautifulSoup(html, 'html.parser')

    # go through the soup and store data in a list of dictionaries
    dataList = getPlayersData(soup)

    # write the list of players into a database
    writeDatabase(dataList)
