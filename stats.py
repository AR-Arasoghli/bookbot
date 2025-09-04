
def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file = f.read()
        num_words = len(file.split())
        return num_words

def count_chars(path_to_file):
    counter = {}
    with open(path_to_file) as f:
        file = f.read().lower().split()
        for word in file:
            for letter in word:
                if letter in counter:
                    counter[letter] +=1
                else:
                    counter[letter] = 1
    return counter


def sorted_list(counter):
    #need to first create list of dictionaries
    new_counts = []
    for k,v in counter.items():
        new_counts.append({"char":k,"num":v})
    new_counts.sort(reverse=True,key=sort_on)
    return new_counts
    #sort list of dictionaries

def sort_on(list):
    return list["num"]
#    return new_counts