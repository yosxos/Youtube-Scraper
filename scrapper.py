import os
import argparse
import json
import scrapper_youtube

parser = argparse.ArgumentParser()
parser.add_argument('--input')
parser.add_argument('--output')
args = vars(parser.parse_args())
i=0
#Opening the inputfile 
f = open(args['input'])
data = json.load(f)
#Opening the output file to parse the scraped data in Json format
fw= open(args['output'], 'w')
fw.write('{')
while i < len(data["videos_id"]):
    fw.write(f'"Channel,{i+1}":'+json.dumps(scrapper_youtube.scrape_data(data["videos_id"][i]),indent=4))
    i += 1
    if i < len(data["videos_id"]):
        fw.write(',')
fw.write('}') 


        
    



