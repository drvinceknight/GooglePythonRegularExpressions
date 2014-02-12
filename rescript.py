import re

# Uncomment particular expression

#match = re.search(r'iii', 'piiig')  # Match 3 'i's exactly
#match = re.search(r'igs', 'piiig')  # Match 'igs' exactly
#match = re.search(r'..g', 'piiig')  # Match 2 characters followed by 'g'
#match = re.search(r'.g', 'piiig')  # Match 1 character by 'g'
#match = re.search(r'\d\d\d', 'p123g')  # Match 3 digits
#match = re.search(r'\d\d\d', 'p1k234g')  # Match 3 digits
#match = re.search(r'\d\d\d', 'p1k234g')  # Match 3 digits
#match = re.search(r'\w\w\w', '@@abcd!!')  # Match 3 words
#match = re.search(r'pi+', 'piiig')  # Match 'p' followed by any number of 'i's
#match = re.search(r'i+', 'piigiiii')  # Match any number of 'i's
#match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')  # Match 3 digits seperated by any number of white spaces
#match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')  # Match 3 digits seperated by any number of white spaces
#match = re.search(r'\d\s*\d\s*\d', 'xx123xx')  # Match 3 digits seperated by any number of white spaces
#match = re.search(r'^b\w+', 'foobar')  # Match 'b' followed by any number of words at beginning of line
match = re.search(r'b\w+', 'foobar')  # Match 'b' followed by any number of words

# If-statement after search() tests if it succeeded
if match:
    print 'found', match.group() ## 'found word:cat'
else:
    print 'did not find'
