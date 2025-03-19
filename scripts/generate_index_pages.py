# Read the notes pages and create indexes for top level items

import os
from string import ascii_lowercase

# Assumes this is run from the scripts directory
NOTES_PATH = os.path.join('..', 'notes_pages')
INDEXES_PATH = os.path.join('..', 'index_pages')


def isLinkChar(c):
    if (c in ascii_lowercase) or (c == ' '):
        return True
    return False


def create_anchor_link(heading_text):
    link_chars = filter(isLinkChar, list(heading_text.lower()))
    link = ''.join(link_chars)
    link = link.strip()
    link = link.replace(' ', '-')
    link = "#" + link

    return link


def write_index_page(headings_list, current_letter, output_target):
    o = output_target
    target_page = f'../notes_pages/notes_{current_letter}.md'
    o.write(f'# Index for [{current_letter.upper()}](target_page)')
    o.write('\n')
    for heading in headings_list:
        anchor_link = create_anchor_link(heading[0])

        if heading[1] == 2:
            start_line = '- '
        elif  heading[1] == 3:
            start_line = '  - '
        elif  heading[1] == 4:
            start_line = '    - '
        else:
            print(f"ERROR: Unhandled heading: {heading[0]} Letter: {current_letter}")

        link_line = f"{start_line} [{heading[0]}]({target_page}/{anchor_link})"
        o.write(link_line)
        o.write('\n')
        # # Uncomment to debug
        # print(heading)
    o.write("<br><br>")
    o.write('\n')
    o.write(f'<p align="center">[Home](../README.md#tech-notes)</p>')


def get_headings_list(file_path):
    headings = []

    # Build a filename like: notes_a.md
    notes_files = ['notes_' + letter + '.md' for letter in ascii_lowercase ]
    for notes_file in notes_files:
        input_file = os.path.join(NOTES_PATH, notes_file)
        try:
            with open(input_file, encoding='utf8') as f:
                for line in f.readlines():
                    line = line.strip()
                    heading_count = 0
                    if line.startswith('#'):
                        heading_count = line.count('#', 0, 7)
                        if heading_count > 1:        # Ignore code comment lines
                            tmp, body = line.split(' ', maxsplit=1)
                            headings.append((body, heading_count))
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
