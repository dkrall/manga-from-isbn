#!/usr/bin/env python3
import sys
import subprocess
import requests
import time
from get_api_key import get_api_key
from util import get_filepath_to_output_file

# Main function of get_manga_from_isbn. This function will read the list of isbns
# provided as inputs (one per line) and fetch information about those isbns,
# writing each isbn's data to an output file. That is to say that an input file
# with 20 isbns would output 20 json files.

# Sample usage:
#   ./get_manga_from_isbn.py manga.txt
# The sample command above will read from ../input/manga.txt
# The sample command above will output to ../output/manga_<isbn>.json

# The main function, which iterates through the lines of the input file. Each
# line corresponds to one ISBN
def get_manga_from_isbn():
    input_filepath = get_filepath_to_input_file()
    input_file = open(input_filepath, 'r')
    readline = input_file.readline()
    counter = 0

    while readline:
        # API accepts maximum of 100 calls per minute. Wait 1 minute of cooldown to be safe after each 100 calls.
        if counter > 99:
            counter = 0
            # Sleep for 70 seconds, as the API is a bit finicky about how it calculates usage
            time.sleep(70)

        isbn = readline.replace('\n', '')
        populate_output_json(isbn)
        readline = input_file.readline()
        counter+=1

    input_file.close()


# Calls the api to get data related to the product and prints that data to an output JSON file.
# Prints to the console in case of an error.
def populate_output_json(isbn):
    api_url = "https://api.barcodelookup.com/v3/products?barcode={0}&key={1}".format(isbn, get_api_key())

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        write_details_to_file(isbn, response.text)
    except Exception as error:
        print("Failed to create file for %s" % isbn)
        print(error)


# Call API and return the output. Does not evaluate output in any way.
def call_api(url):
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output


# Create a new file with the isbn as the fil
# Takes an argument with a list of headers which is iterated through, with details pulled based on these headers.
def write_details_to_file(isbn, details):
    output_filepath = get_filepath_to_output_file(isbn)
    output_file = open(output_filepath, 'w')
    output_file.write(details)
    output_file.close()


# Based on the input provided in the first (and only) argument, return the file path to the input file including the filename.
def get_filepath_to_input_file():
    return "../input/%s" % sys.argv[1]


if __name__ == "__main__":
    get_manga_from_isbn()
