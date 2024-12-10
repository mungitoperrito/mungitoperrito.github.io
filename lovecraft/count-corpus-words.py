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

def get_words(file_handle):
    words = dict()
    this_line = []

    # Stopwords - see below to help generate the list
    # These are from a lightly updated corpus of HP Lovecraft stories:
    # https://arkhamarchivist.com/wordcount-lovecraft-favorite-words/
    stop_words = [
        'the', 'and', 'of', 'to', 'a', 'in', 'was', 'i', 'that', 'had',
        'he', 'it', 'with', 'as', 'his', 'for', 'at', 'from', 'on',
        'which', 'not', 'but', 'were', 'my', 'by', 'they', 'all', 'be',
        'or', 'this', 'there', 'have', 'could', 'me', 'one', 'when',
        'him', 'we', 'no', 'an', 'been', 'their', 'some', 'so', 'would',
        'what', 'is', 'its', 'more', 'old', 'them', 'out', 'only',
        'about', 'now', 'up', 'did', 'very', 'into', 'before', 'seemed',
        'then', 'than', 'great', 'those', 'who', 'after', 'through',
        'where', 'any', 'time', 'even', 'our', 'saw', 'things',
        'though', 'over', 'must', 'other', 'down', 'you', 'if', 'came',
        'like', 'man', 'these', 'found', 'such', 'might', 'are',
        'night', 'whose', 'strange', 'upon', 'never', 'made', 'once',
        'thing', 'men', 'place', 'certain', 'much', 'many', 'still', 
        'long', 'most', 'beyond', 'come', 'first', 'heard', 'house',
        'see', 'two', 'last', 'seen', 'too', 'city', 'knew', 'black',
        'thought', 'again', 'told', 'back', 'said', 'far', 'dark',
        'almost', 'know', 'something', 'little', 'yet', 'since', 'new',
        'ever', 'will', 'stone', 'left', 'how', 'do', 'ancient', 'way',
        'world', 'years', 'light', 'away', 'room', 'felt', 'toward',
        'door', 'day', 'nothing', 'us', 'around', 'can', 'well',
        'without', 'while', 'above', 'off', 'life', 'known', 'began',
        'unknown', 'an‘', 'terrible', 'just', 'horror', 'street', 'her',
        'eyes', 'because', 'own', 'indeed', 'human', 'every', 'later',
        'under', 'here', 'near', 'may', 'another', 'say', 'three',
        'fear', 'ward', 'small', 'tell', 'less', 'curious', 'face',
        'dreams', 'people', 'soon', 'himself', 'looked', 'both',
        'earth', 'mind', 'think', 'feet', 'floor', 'behind', 'few',
        'sound', 'high', 'being', 'always', 'hideous', 'course',
        'walls', 'till', 'has', 'among', 'open', 'outside', 'she',
        'space', 'went', 'young', 'end', 'kind', 'find', 'against',
        'dr', 'brought', 'hill', 'past', 'enough', 'perhaps', 'sea',
        'am', 'same', 'make', 'however', 'vast', 'sometimes', 'town',
        'land', 'moon', 'became', 'myself', 'took', 'sight', 'set',
        'west', 'whole', 'gods', 'moment', 'turned', 'gave', 'dead',
        'nor', 'get', 'body', 'head', 'half', 'wholly', 'others',
        'part', 'side', 'ones', 'look', 'ye', 'along', 'willett', 'air',
        'windows', 'close', 'lay', 'window', 'below', 'queer', 'each',
        'alone', 'morning', 'across', 'voice', 'right', 'held', 'go',
        'sky', 'death', 'white', 'having', 'north', 'matter', 'grew',
        'quite', 'days', 'next', 'grey', 'within', 'odd', 'hand',
        'gone', 'second','home', 'during', 'take', 'low', 'work',
        'reached', 'full', 'case', 'possible', 'none', 'least', 'good',
        'nature', 'beneath', 'hills', 'often', 'several', 'tried',
        'wind', 'why', 'itself', 'ahead', 'point', 'ground', 'despite',
        'sort', 'large',  'kept', 'rather', 'appeared', 'vague',
        'family', 'cold', 'keep', 'wall', 'steps',  'save', 'anything',
        'shall', 'between', 'hours', 'deep','name', 'read', 'distant',
        'whilst', 'let', 'taken', 'finally', 'houses', 'places',
        'faint',  'use', 'age', 'your', 'times', 'used', 'youth',
        'suddenly', 'spoke', 'mr',  'wild', 'water', 'o‘', 'tales',
        'better', 'amidst', 'dream', 'memory', 'stars', 'general',
        'called', 'sleep', 'friend', 'noticed', 'stood', 'books',
        'evening', 'sounds', 'river', 'beings', 'race', 'whom', 'done',
        'also',  'hands', 'led', 'green', 'mountain', 'terror', 'lost',
        'greater', 'road', 'give', 'rest', 'got', 'living', 'trees',
        'sense', 'clear', 'probably', 'early', 'should', 'rock',
        'words', 'state', 'doubt', 'put', 'whether', 'present',
        'father', 'followed', 'wonder', 'mountains', 'talk', 'son',
        'cannot', 'narrow', 'call', 'passed', 'fresh', 'visible',
        'learned', 'nearly', 'south', 'wish', 'able', 'lake', 'dogs',
        'late', 'change', 'streets', 'ruins', 'help', 'library',
        'hidden', 'object', 'hear', 'really',  'common', 'region',
        'heavy', 'formed', 'either', 'five', 'merely', 'sent', 'cats',
        'length','opened', 'church', 'become', 'somewhat', 'wondered',
        'singular', 'knowledge', 'year', 'silent', 'village', 'reason',
        'ago', 'line', 'parts', 'distance', 'real', 'twilight', 'four',
        'given', 'study', 'return', 'party', 'doctor', 'red', 'speak',
        'final', 'ship', 'darkness', 'peaks', 'need', 'view', 'valley',
        'order', 'various', 'earth‘s', 'wide','hour', 'wished', 'don‘t',
        'believe', 'afterward', 'themselves', 'camp', 'legends',
        'cases', 'stones', 'leave', 'died', 'different', 'familiar',
        'scene', 'poor', 'best', 'nightmare', 'sought', 'odour', 'sure',
        'entered', 'surface', 'evidently', 'secrets', 'building', 'boy',
        'moved', 'talked', 'cities', 'everything']
    
    # Uncomment to count how many stop words there are
    print(f"There are {len(stop_words)} stop words.")

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

############
### MAIN ###
############
DISPLAY_COUNT = 30

filename = get_args()
fh = get_file_handle(filename)
words = get_words(fh)

sorted_words = sort_by_count(words) 
print(f"First {DISPLAY_COUNT} of {len(words)}")
for dc in range(DISPLAY_COUNT):
    print(f"{list(sorted_words.items())[dc]}")

# # Uncomment to print out potential stop words
# start_point = 0
# most_frequent = list(sorted_words.keys())[:start_point + 20]
# print(most_frequent)
    
