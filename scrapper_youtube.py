from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

VERSION = '0.1.0'

RESPONSE = {
    'id': str,
    'title': str,
    'upload_date': str,
    'duration': str,
    'description': str,
    'genre': str,

    'uploader': {
        'channel_id': str,
    },
    'statistics': {
        'views': str,
        'likes': int,
    },
    #'comments': str
}



def make_soup(url):
    '''
    Reads the contents at the given URL and returns a Python object based on
    the structure of the contents (HTML).
    '''
    html = urlopen(url).read()
    return BeautifulSoup(html, 'lxml')


def scrape_data(id):
    '''
    Scrapes data from the YouTube video's page whose ID is passed in the URL,
    and returns a JSON object as a response.
    '''
    youtube_video_url = 'https://www.youtube.com/watch?v=' + id
    soup = make_soup(youtube_video_url)
    soup_itemprop = soup.find(id='watch7-content')
    if len(soup_itemprop.contents) > 1:
        video = RESPONSE
        uploader = video['uploader']
        statistics = video['statistics']
        video['id'] = id
        # get data from tags having `itemprop` attribute
        for tag in soup_itemprop.find_all(itemprop=True, recursive=False):
            key = tag['itemprop']
            if key == 'name':
                # get video's title
                video['title'] = tag['content']
            elif key == 'duration':
                # get video's duration
                video['duration'] = tag['content']
            elif key == 'datePublished':
                # get video's upload date
                video['upload_date'] = tag['content']
            elif key == 'genre':
                # get video's genre (category)
                video['genre'] = tag['content']
            elif key == 'thumbnailUrl':
                # get video thumbnail URL
                video['thumbnail_url'] = tag['href']
            elif key == 'interactionCount':
                # get video's views
                statistics['views'] = int(tag['content'])
            elif key == 'channelId':
                # get uploader's channel ID
                uploader['channel_id'] = tag['content']
            elif key == 'description':
                video['description'] = tag['content']
            elif key == 'playerType':
                video['playerType'] = tag['content']

        data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
        data_json = json.loads(data)
        videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
        likes=videoPrimaryInfoRenderer["videoActions"]['menuRenderer']["topLevelButtons"][0]["segmentedLikeDislikeButtonRenderer"]["likeButton"]["toggleButtonRenderer"]['defaultText']["simpleText"]
        video['statistics']['likes'] = likes
        #video['comments']=ScrapComment(youtube_video_url)
        return RESPONSE

    return ({
        'error': 'Video with the ID {} does not exist'.format(id)
    })

def ScrapComment(url):
    """  Scrapes comments from the YouTube video's page whose ID is passed in the URL,
    and returns a List  as a response.
    """
    option = webdriver.FirefoxOptions()
    option.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
    driver.get(url)
    prev_h = 0
    while True:
        height = driver.execute_script("""
                function getActualHeight() {
                    return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                    );
                }
                return getActualHeight();
            """)
        driver.execute_script(f"window.scrollTo({prev_h},{prev_h + 200})")
        # fix the time sleep value according to your network connection
        time.sleep(1)
        prev_h +=200  
        if prev_h >= height:
            break
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    comment_div = soup.select("#content #content-text")
    comment_list = [x.text for x in comment_div]
    return(comment_list)
