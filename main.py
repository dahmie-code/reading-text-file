# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here 
   
   file = open(filename, "r")
   return file.read()



def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count = dict()
    texts = text.split()
    for string in texts:
        if string in count:
            count[string] += 1
        else:
            count[string] = 1
    return(count)
print(count_words())