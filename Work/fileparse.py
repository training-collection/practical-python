# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, has_headers=False, select=None, types=None):
    '''
    Parse a csv file into a list of records
    with optional coloumn selection
    and type conversion
    with option to parse files without headers    

    args:
        has_headers:   True/False
                       Must pass in a value

        select: A list of desired coloumns based on headder
                Used only when a header exists
                Use function csv_headers_firstline to find headders
    
        types:  A list of types (str, int, float) in the order
                they appear in the csv file

    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        # Headers if it has any
        headers = next(rows) if has_headers else []

        # If optional coloumn selection is used
        if select:
            # Find indicies of the specified coloumns
            indices = [headers.index(colname) for colname in select]
            # Narrow the set of headders for the dictionary output
            headers = select
        
        records = []
        for rowno, row in enumerate(rows, start=1):
            # Skip rows with no data
            if not row:
                continue
           
            # Filter by selected coloums if selection was used
            if select:
                row = [row[index] for index in indices]

            # If optional type selection is used
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError:
                    print(f'Row {rowno}: Type does not match type definition, if Row = 1 check has_header is defined correctly')

            # Make a dictionary or tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
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
