from collections import defaultdict
import re
import sys
import os

# Lists to compare
test_1 = ['hello', 'test', 's', 'python', 'programming', 'is', 'fun']
test_2 = ['this', 'is', 'a', 'test', 'hello', 'world', 's', 'another', 'test', 'python', 'programming']
WORD_RE = re.compile(f"\w+")

# Check occurrences in file if provided path
def build_index_for_file(input_file):
    index = defaultdict(list)
    with open(input_file, encoding="utf-8") as file:
        for line_no , line in enumerate(file, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index.setdefault(word, []).append(location)
    return index 

# Check occurrences in provided 2 example lists 
def build_index_for_list(word_list):
    index = defaultdict(list)
    for line_no, word in enumerate(word_list, 1):
        for match in WORD_RE.finditer(word):
            if match:
                column_no = match.start() + 1
                location = (line_no, column_no)
                index.setdefault(word, []).append(location)
    return index
    
# runs the file check if provided if not runs the occurrences on lists
if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
    input_file = sys.argv[1]
    result = build_index_for_file(input_file)
else:
   result = build_index_for_list(test_1)
   for line_no, word in enumerate(test_2, 1):
       if word in result:
           column_no = line_no
           location = (line_no, column_no)
           result[word].append(location)

for word in sorted(result, key=str.upper):
    print(word, result[word])