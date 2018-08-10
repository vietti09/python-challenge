
#Dependencies
from bs4 import BeautifulSoup
import pymongo
from splinter import Browser
import time
import pandas as pd

#Create "Scrape" function
def scrape():

    ## NASA Mars News ##

    #Set up splinter browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Set variable for NASA Mars News site
    url = 'https://mars.nasa.gov/news/'


    browser.visit(url)
    response = browser.html

    #Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response, 'html.parser')

    #Retrieve latest news title & description
    news_title = soup.find('div', 'content_title', 'a').text
    news_p = soup.find('div', 'article_teaser_body').text


    ## JPL Mars Space Images - Featured Image ###

    #Set up splinter browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Set variable for JPL Featured Space Image site
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    #Visit url
    browser.visit(url)

    #Code for moving through pages on site
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    #Pull html text
    response = browser.html

    #Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response, 'html.parser')

    #Retrieve featured image
    image_href = soup.find('figure', 'lede').a['href']
    link = 'https://www.jpl.nasa.gov'
    featured_image_url = link + image_href


    ## Mars Weather ##

    #Set up splinter browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Set variable for Mars Weather Twitter Account
    url = 'https://twitter.com/marswxreport?lang=en'

    #Visit url
    browser.visit(url)

    #Pull html text
    response = browser.html

    #Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response, 'html.parser')

    #Retrieve latest tweet
    mars_weather = soup.find('p', 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text


    ## Mars Facts ##

    #Set up splinter browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Set variable for Mars Facts Webpage
    url = 'https://space-facts.com/mars/'


    browser.visit(url)
    response = browser.html

    #Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response, 'html.parser')

    #Retrieve entire table
    table= soup.find('table', 'tablepress tablepress-id-mars')

    #Retrieve all the rows in the table
    rows = table.find_all('tr')

    #Create empty lists to hold td elements from each row (alternates between label & value)
    labels = []
    values = []

    #Loop through rows & add first td element to labels & second td element to values
    for row in rows:
        td_elements = row.find_all('td')
        labels.append(td_elements[0].text)
        values.append(td_elements[1].text)

    #Create Dataframe
    mars_facts = pd.DataFrame({" ": labels,
                            "Values": values})

    #Set new index
    mars_facts.set_index(" ", inplace=True)

    #Display Dataframe
    mars_facts

    #Covert Dataframe to html table string
    html_table = mars_facts.to_html(header=False)


     ## Mars Hemispheres ##

    #Set up splinter browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Set variable for Mars Facts Webpage
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    #Visit url
    browser.visit(url)

    #Pull html text
    response = browser.html

    #Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response, 'html.parser')

    #Retrieve class for each hemisphere available
    returns = soup.find('div', 'collapsible results')

    #Retrieve all anchors in each class pulled above
    hemispheres = returns.find_all('div', {"class": 'description'})

    #Create empty list to hold dictionaries
    hemisphere_image_urls = []

    #Loop through all anchors for each hemisphere class
    for description in hemispheres:
        a = description.find('a')

        #Retrieve title and link to specific hemisphere page
        title = a.h3.text
        link = 'https://astrogeology.usgs.gov' + a['href']

        #Visit above link
        browser.visit(link)
        time.sleep(5)

        #Retrieve link to image
        page = browser.html
        results = BeautifulSoup(page, 'html.parser')
        image_link = results.find('div', 'downloads').find('li').a['href']

        #Create empty dictionary for title & image
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = image_link

        #Add image_dict to empty list from above
        hemisphere_image_urls.append(image_dict)

    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "fact_table": html_table,
        "hemispheres_images": hemisphere_image_urls}


    return mars_dict
