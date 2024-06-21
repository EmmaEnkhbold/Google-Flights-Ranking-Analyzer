from selenium import webdriver
from bs4 import BeautifulSoup
import time

#initialize WebDriver
driver = webdriver.Chrome()

#Google Flights, NYC to LA, One Adult, Economy, January 1, 2025
URL="https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI1LTAxLTAxag0IAhIJL20vMDJfMjg2cg4IAxIKL20vMDMwcWIzdEABSAFwAYIBCwj___________8BmAEC&tfu=EgYIABABGAA&hl=en-US&gl=US"

#retrieve the HTML content
driver.get(URL)
time.sleep(5)

#source code
source = driver.page_source

#parse with BeautifulSoup object
soup = BeautifulSoup(source, 'html.parser')

#“Best flights” as determined by Google
bestFlightResults = soup.find_all('div',class_="YMlIz FpEdX jLMuyc")
firstTwo = bestFlightResults[0:6:3]

#next three Google Flight results
flightResults = soup.find_all('div',class_="YMlIz FpEdX")
nextThree = flightResults[0:9:3]

#prints prices for top five Google Flight results
topFiveResults = firstTwo + nextThree
for result in topFiveResults:
    spanElement = result.find('span', {'aria-label': True})
    ariaLabel = spanElement['aria-label']
    print(ariaLabel)
