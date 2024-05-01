import re
text = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentil's on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."

"""
1. Convert all text to lower case
2. filter to get rid of special characters except the apostrophe
3. separate each text
4. Count the number of each element
5. sort the order and return the top 3 elements
"""
#  convert to lowercase
text_lower = text.lower()

# filter all punctuation marks
text_filter = re.sub(r"[^\w\s']", '', text_lower)

# separate each word into a list
text_sep = text_filter.split()
text_distinct = list(set(text_sep))
frequency = {key: 0 for key in text_distinct}
print(len(text_sep), len(text_distinct))