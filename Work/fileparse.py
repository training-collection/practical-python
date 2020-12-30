# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None):
    '''
    Parse a csv file inot a list of records
    with optional coloumn selection
    and type conversion    

    args:
        select: A list of desired coloumns based on headder
                Use function csv_headers to find headders
    
        types:  A list of types (str, int, float) in the order
                they appear in the csv file
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        # Read the file headers        
        headers = next(rows)
        
        # If optional coloumn selection is used
        if select:
            # Find indicies of the specified coloumns
            indices = [headers.index(colname) for colname in select]
            # Narrow the set of headders for the dictionary output
            headers = select
        else:
            indices = []
        
        records = []
        for row in rows:
            # Skip rows with no data
            if not row:
                continue
           
            # Filter by selected coloums if selection was used
            if indices:
                row = [row[index] for index in indices]

            # If optional type selection is used
            if types:
                row = [func(val) for func, val in zip(types, row)]
        
            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)
    
    return records


def csv_header_firstrow(filename):
    '''
    Call header and first row of data in csv as tuple
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        first_row = next(rows)    

    return headers, first_row
