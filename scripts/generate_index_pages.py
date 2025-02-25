# Read the notes pages and create indexes for top level items

import os
from string import ascii_lowercase

# Assumes this is run from the scripts directory
NOTES_PATH = os.path.join('..', 'notes_pages')
INDEXES_PATH = os.path.join('..', 'index_pages')

def write_index_page(headings_list):
    print(headings_list)


def get_headings_list(file_path):
    headings = []

    notes_files = ['notes_' + letter + '.md' for letter in ascii_lowercase ]
    for notes_file in notes_files:
        input_file = os.path.join(NOTES_PATH, notes_file)
        try:
            with open(input_file, encoding='utf8') as f:
                for line in f.readlines():
                    if line.startswith('###'):
                        line = line.strip()
                        tmp, body = line.split(' ', maxsplit=1)
                        heading = '  - ' + body
                        headings.append(heading)
                    elif line.startswith('##'):
                        line = line.strip()
                        tmp, body = line.split(' ', maxsplit=1)
                        heading = '- ' + body
                        headings.append(heading)
                    else:
                        pass
        except Exception as e:
            print(f'INPUT ERROR: {e}')

        index_file = 'index_' + notes_file[6] + '.md'
        output_file = os.path.join(INDEXES_PATH, index_file)
        try:
            with open(output_file, encoding='utf8') as f:
                write_index_page(headings)
        except Exception as e:
            print(f'OUTPUT ERROR: {e}')


############
### MAIN ###
############

get_headings_list(NOTES_PATH)
