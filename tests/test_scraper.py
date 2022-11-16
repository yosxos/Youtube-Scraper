import scrapper_youtube
import pytest
from bs4 import BeautifulSoup
import requests
url="OdMgsdMzdbc"

def test_id() :
    fonc=scrapper_youtube.scrape_data(url)
    assert fonc['id']=='OdMgsdMzdbc'

def test_title() :
    fonc=scrapper_youtube.scrape_data(url)
    assert fonc ['title']=="ALWAYS get Recombobulator with Dragon Soul"

def test_upload_date() :
    fonc=scrapper_youtube.scrape_data(url)
    assert fonc ['upload_date']=="2022-11-15"

def test_duration() :
    fonc=scrapper_youtube.scrape_data(url)
    assert fonc ['duration']=="PT26M22S"
def test_genre() :
    fonc=scrapper_youtube.scrape_data(url)
    assert fonc ['genre']=="Gaming"
def test_description() :
    fonc=scrapper_youtube.scrape_data(url)
    assert fonc ['description']=="ALWAYS get Recombobulator with Dragon Soul00:00 - Patch 12.2101:52 - Pandora's Items 08:26 - Dragon Soul 13:41 - RecombobulatorYouTube Business Contact: BoxB..."
