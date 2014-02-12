import re

str = 'an example word:cat!!'
#match = re.search(r'word:\w\w\w', str)
#match = re.search(r'iii', 'piiig')
#match = re.search(r'igs', 'piiig')
#match = re.search(r'..g', 'piiig')
#match = re.search(r'.g', 'piiig')
match = re.search(r'\d\d\d', 'p1k234g')

# If-statement after search() tests if it succeeded
if match:
    print 'found', match.group() ## 'found word:cat'
else:
    print 'did not find'
