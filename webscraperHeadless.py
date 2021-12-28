from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import Notifications

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
    i = True
    while i:
        try:
            browser.find_element(By.XPATH, element)
        except NoSuchElementException:
            continue
        i = False
    return

# This method endlessly checks for availability of classes whose urls are defined in the urls array
# It prints info to the console about these classes if their number is in the classNums array
def checkClasses():
    global retries
    while True:
        for i, url in enumerate(urls):
            browser.get(urls[i])

            waitForLoad('//*[@id="informal"]/td[11]/div/span[1]')
            openSeats = browser.find_element(By.XPATH, '//*[@id="informal"]/td[11]/div/span[1]').text
            if(openSeats != '0'):
                Notifications.postMessageGeneral(classNums[i])
            print('Class ' + str(classNums[i]) + ': ' + openSeats + ' seats available.')

        retries += 1
        print('All classes checked, retrying for the ' + str(retries) + ' time.')

Notifications.BeginTesting()

getClassNums()
getUrls()
checkClasses()

#unreachable, but here in case somehow it is reached to prevent memory leak
browser.quit()