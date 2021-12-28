#uncomment lines 8 and 50 if your computer is running too hot or haivng performance issues
#uncomment line 81 if you want a message sent to your channel when the program first runs

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import Notifications
#import time

# webdriver option managing
# sets up webdriver in the least annoying way possible (runs invisibly, doesn't spam the console)
browserOptions = webdriver.ChromeOptions()
browserOptions.add_argument('headless') #to keep selenium from opening browsers
browserOptions.add_argument('log-level=3') #to keep selenium from spamming the console
browser = webdriver.Chrome(options=browserOptions)

classNums = []
urls = []
retries = 0


# This method reads the class numbers written in the classnumbers.txt file
# All class numbers should be written on a single line seperated by spaces
# There should only be one line in the text file
def getClassNums():
    global classNums

    textFile = open('classnumbers.txt')
    lines = textFile.read()
    classNums = lines.split(' ')

    textFile.close()


# This method uses the class numbers to create strings of the urls used to search classes
def getUrls():
    for num in classNums:
        url = 'https://webapp4.asu.edu/catalog/classlist?t=2221&k=' + num + '&hon=F&promod=F&e=all&page=1'
        urls.append(url)

# This method waits for an element to load on the selenium browser so that no errors occur when trying to access it
#
# Parameters-
# element: the XPATH of the desired element
def waitForLoad(element):
    while i:
        try:
            browser.find_element(By.XPATH, element)
        except NoSuchElementException:
            #time.sleep(1)
            continue
        break
    return

# This method endlessly checks for availability of classes whose urls are defined in the urls array
def checkClasses():
    global retries #this is simply to log how many times the program has looped
    
    #loop constantly forever
    while True:
        #for every loop, check every class in the urls list created earlier
        for i, url in enumerate(urls):
            #go to this url
            browser.get(urls[i])
            
            #wait for the open seat number to load, once it has, get the number with the find_element method of webdriver
            waitForLoad('//*[@id="informal"]/td[11]/div/span[1]')
            openSeats = browser.find_element(By.XPATH, '//*[@id="informal"]/td[11]/div/span[1]').text
            
            #this if statement checks if there is an available seat, notifying the discord channel if there is one
            if(openSeats != '0'):
                Notifications.postMessageGeneral(classNums[i])
            
            #log the amount of available seats in the console (not very important just so you can see its working)
            print('Class ' + str(classNums[i]) + ': ' + openSeats + ' seats available.')
        
        #log the amount of times the program has retried to console
        retries += 1
        print('All classes checked, retrying for the ' + str(retries) + ' time.')

#Notifications.BeginTesting()

# This is what is run when the program is executed
getClassNums()
getUrls()
checkClasses()
