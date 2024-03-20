import csv
import logging
import os
from exceptions import csvexceptions


def read_row_from_csv_file(row_number):
    # get the current  working directory
    current_working_directory = os.getcwd()
    organizations_path = '../resources/organizations.txt'

    try:
        with open(os.path.join(current_working_directory, organizations_path), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                if line_count == row_number:
                    return row
                else:
                    line_count += 1

            # raise RowNotFoundInCsv if row_number wasn't found
            raise csvexceptions.RowNotFoundInCsv(
                "The row number {} wasn't found in the file".format(row_number))
    except FileNotFoundError as e:
        print('The file wasn\'t found: ', e)


def read_one_value_from_row(row, index):
    try:
        value = row[index]
        return value
    except Exception as error:
        raise csvexceptions.IndexNotFoundInRow("The index {} wasn't found in the row".format(index))


