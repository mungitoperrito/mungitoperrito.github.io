# Count the number of times a word appears in a file
import string
import sys

def get_args():
    if len(sys.argv) != 2:
        print('Needs a filename')
        exit()

    return sys.argv[1]


def get_file_handle(filename):
    try:
        fh = open(filename, encoding="utf8")
    except Exception as e:
        print(f"Can't open file: {filename}")
        print(e)
        exit()

    return fh


def get_stop_words(filename='stop-words.txt'):
    stop_words = list()
    stop_words_file = get_file_handle(filename)
    for ln in stop_words_file.readlines():
        if ((ln.startswith('#')) or (len(ln) == 1)):
           continue
        
        this_line = ln.split()
        for w in this_line:
            stop_words.append(w)

    # # Uncomment to count how many stop words there are
    # print(f"There are {len(stop_words)} stop words.")

    return stop_words


def get_words(file_handle):
    words = dict()
    this_line = []
    stop_words = get_stop_words()

    for line in fh:
        line = line.lower()
        line = line.translate(line.maketrans('', '', string.punctuation))
        this_line = line.split()
        for word in this_line:
            if word in stop_words:
                continue
            words[word] = words.get(word, 0) + 1

    return words


def sort_by_count(count_dict):
    # Doesn't work with python pre-3.6
    sorted_dict = dict()

    # # Uncomment for smallest to largest
    # sorted_dict = dict(sorted(
    #         count_dict.items(),
    #         key=lambda item: item[1]
    #         )
    #     )

    # Uncomment for largest to smallest
    sorted_dict = dict(sorted(
            count_dict.items(),
            key=lambda item: item[1],
            reverse=True
            )
        )

    return sorted_dict


def get_total(word_dict, count=None):
    # Assumes incoming dict is already sorted
    total = 0
    n = 0

    if count == None:
        count = len(word_dict)

    for n in range(count):
        total += list(word_dict.items())[n][1]
   
    print(total)
    return total


############
### MAIN ###
############
DISPLAY_COUNT = 30

filename = get_args()
fh = get_file_handle(filename)
words = get_words(fh)

sorted_words = sort_by_count(words) 

# # Uncomment to display words and counts
# for dc in range(DISPLAY_COUNT):
#     print(f"{list(sorted_words.items())[dc]}")

# # Uncomment to print out potential stop words
# start_point = 0
# most_frequent = list(sorted_words.keys())[:start_point + 20]
# print(most_frequent)
    
total_words = get_total(sorted_words)
total_top_500 = get_total(sorted_words, 5)