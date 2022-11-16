# Youtube-Scraper

A youtube data scrapper using beautifulsoup/Requests

Data scrapped :

    "id": 
    
    "title": 
    
    "upload_date": 
    
    "duration": 
    
    "description": 
    
    "genre": ,
    
    "uploader": {
    
        "channel_id": 
        
    },
    "statistics": {
    
        "views": 
        
        "likes": 
        
    },
    
    "thumbnail_url": 
    
    "playerType":
    
To scrape the youtube comments uncomment the line 29 and 96 in the scrapper_youtube.py but take note that this will add more time for the programme to run

# Run the programme : 

**source .venv/bin/activate**

python scrapper.py --input input.json --output output.json

# How to run :

**python -m pytest tests**

**coverage run -m pytest tests**

**coverage report to show the test coverage result **

