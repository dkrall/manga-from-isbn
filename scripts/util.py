#!/usr/bin/env python3
# Utility file containing functions to be used by multiple other scripts
import sys

# Based on the input provided in the first (and only) argument and the isbn for which data has been gathered,
# return the file path to the output file to be written.
# For example, an input file of manga.txt and an isbn of 123456 would yield an output path of ../output/manga_123456.json
def get_filepath_to_output_file(isbn):
    output_base_name = sys.argv[1].split('.')[0]
    return "../output/{0}_{1}.json".format(output_base_name, isbn)
