import csv
import json
from elasticsearch import Elasticsearch
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("Filename", help="The filename of your CSV file containing your workout data")
parser.add_argument("ES_server", help="The Elasticsearch server you want to send the data to")

csvfile = open('workout.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')