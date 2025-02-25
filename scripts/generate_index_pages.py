# Read the notes pages and create indexes for top level items

import os
from string import ascii_lowercase

# Assumes this is run from the scripts directory
NOTES_PATH = os.path.join('..', 'notes_pages')
INDEXES_PATH = os.path.join('..', 'index_pages')

def write_index_page(headings_list, current_letter, output_target):
    o = output_target
    o.write(f'Index for {current_letter.upper()}')
    o.write('\n\n')
    for heading in headings_list:
        o.write(heading)
        o.write('\n')
        # # Uncomment to debug
        # print(heading)


def get_headings_list(file_path):
    headings = []

    # Build a filename like: notes_a.md
    notes_files = ['notes_' + letter + '.md' for letter in ascii_lowercase ]
    for notes_file in notes_files:
        input_file = os.path.join(NOTES_PATH, notes_file)
        try:
            with open(input_file, encoding='utf8') as f:
                for line in f.readlines():

                    # Get the subheadings
                    if line.startswith('###'):
                        line = line.strip()
                        tmp, body = line.split(' ', maxsplit=1)
                        heading = '  - ' + body
                        headings.append(heading)

                    # Get the main headings
                    elif line.startswith('##'):
                        line = line.strip()
                        tmp, body = line.split(' ', maxsplit=1)
                        heading = '- ' + body
                        headings.append(heading)
                    else:
                        pass
        except Exception as e:
            print(f'INPUT ERROR: {e}')

        # Build a filename like: index_a.md
        current_letter = notes_file[6]
        index_file = 'index_' + current_letter + '.md'
        output_file = os.path.join(INDEXES_PATH, index_file)
        try:
            with open(output_file, 'w', encoding='utf8') as output_index:
                write_index_page(headings, current_letter, output_index)
        except Exception as e:
            print(f'OUTPUT ERROR: {e}')

        # Reset for the next notes file
        headings = []


############
### MAIN ###
############

get_headings_list(NOTES_PATH)
