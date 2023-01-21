# manga-from-isbn
A python-based program to fetch manga information based on a list of ISBN numbers. The manga isbns will be provided one-per-line in an input file, and jsons for each item will be output to be consumed by a database program.

Requirements:
Install pip, then run the following:
  - pip install requests

Create separate file /scripts/get_api_key.py with a simple function that returns the api key for https://www.barcodelookup.com/
  - A subscription to https://www.barcodelookup.com/ will be needed.
