# this is going to be a program that exports data from the music league website (webscraping) and 
# creates a line graph from the data

# downloadMusicLeagueResults



# i think to progress with this i
# need to get a better understanding
# of html and how to use
# beautiful soup

import openpyxl
import pandas as pd
import bs4
import requests
import os
import webbrowser
from selenium import webdriver
import selenium

# step 1: log in

loginURL = 'https://musicleague.app/'

driver = webdriver.Firefox(executable_path=r"C:\Users\MatthewDennis\geckodriver\geckodriver.exe")
type(driver)
selenium.webdriver.firefox.webdriver.WebDriver
driver.get(loginURL)

# very first page where you only really have the option to click "log in"

loginElem = driver.find_element_by_partial_link_text('Log In')
loginElem.click()

# second page where you can enter your email address and password

emailElem = driver.find_element_by_id('login-username')
emailElem.send_keys('mattdennis108@gmail.com')

pwElem = driver.find_element_by_id('login-password')
pwElem.send_keys('what33Remains')

loginElem2 = driver.find_element_by_id('login-button')
loginElem2.click()

# now we've opened the home page of the music league. let's open the league home page

leagueElem = driver.find_element_by_class_name('league-item')
leagueElem.click()


# now we're on the league home page, let's create a list that contains
# all of the different action link elements

# for some reason, I have the run the program in two parts: everything up to this point AND THEN everything
# after this point. If I try to run it all at once then it doesn't work as it can't identify any 'action-link's

actionLinkElems = driver.find_elements_by_class_name('action-link')

# now let's loop through the list to create a new list that only has the 'Round Results' elements

roundResultElems = []
for i in actionLinkElems:
    if i.text == "Round Results":
        roundResultElems.append(i)

# let's define a couple of things that we'll need for the loop we're about to use
# for each season, the loop is going to append the 'scores' list with one dictionary, containing
# a key for each participant and a value for their score that round

scores = []

i = 1

# let's open the first round results page
roundResultElems[0].click()

while i <= len(roundResultElems):

    # the following gives a list of elements, the "text" for each one being all text associated with
    # each element (e.g. song name, submitter name, score and comments)
    songElems = driver.find_elements_by_class_name('song')

    songTexts = []
    for songElem in songElems:
        songTexts.append(songElem.text)
	# now we have a list that contains one item for each submission. this item is all the text associated
	# with each submission, usefully including the submitter name and the score they got

	# this is the dictionary we are going to put the scores for this round in
    roundX = {}
        
    for songText in songTexts:
        submitter = songText[songText.find('Submitted by')+13:songText.find('Voted On This')-10]
        
        scoreStart = songText.find('Voted On This')+14
        subString = songText[scoreStart:songText.find('Voted On This')+23]
        scoreEnd = subString.find('\n')
        scoreStaging = subString[:scoreEnd]
        finalScore = int(scoreStaging[len(scoreStaging)-2:len(scoreStaging)])
        
        roundX[submitter] = finalScore
    
    scores.append(roundX)
    
    driver.back()
    
    if i == len(roundResultElems):
        print("Finished!")
        break
    
    actionLinkElems2 = driver.find_elements_by_class_name('action-link')

    # we need attain the 'Round Results' elements each time we do the loop, as we don't seem to be able to
	# reuse the elements after we have "clicked into" a round's results

    roundResultElems2 = []
    for actionLink2 in actionLinkElems2:
        if actionLink2.text == "Round Results":
            roundResultElems2.append(actionLink2)
            
    roundResultElems2[i].click()
    
    i += 1
    
	
# now we have a list 'scores' that we should be able to loop through to create a dataframe containing all the
# scores for the season

participants = []
for roundDict in scores:
    for lad in roundDict.keys():
        if lad not in participants:
            participants.append(lad)


	
	
# some other stuff that might come in handy

df = pd.DataFrame(
{"Week 1" : list(Round1.values())},
index = list(Round1.keys()))

# to create a dataframe that i can make a line chart out of, i first need to create a dictionary where
# the participants are the keys and a list of their scores are the values

participants = []
for roundDict in scores:
    for lad in roundDict.keys():
        if lad not in participants:
            participants.append(lad)


# let's make a dictionary, where the participants are keys and their positions in the dataframe we
# are yet to make are the values

participantIndex = {}

for lad in participants:
    participantIndex[lad]=participants.index(lad)




