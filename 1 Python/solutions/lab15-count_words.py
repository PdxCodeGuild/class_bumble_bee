
import requests
import string
import re

book_url = 'http://www.gutenberg.org/cache/epub/1065/pg1065.txt'
response = requests.get(book_url)
response.encoding = 'utf-8'

text = response.text

beginning_junk_index = text.find('*** START OF THIS PROJECT GUTENBERG')
beginning_junk_index = text.find('\n', beginning_junk_index)
text = text[beginning_junk_index:]

end_junk_index = text.find('End of the Project Gutenberg EBook')
text = text[:end_junk_index]

text = text.lower()


# text = text.replace('.', ' ')
# text = text.replace('-', ' ')

# for punctuation in string.punctuation:
#     text = text.replace(punctuation, ' ')

# print(text.split())


print(re.findall('[\\w\']+', text))


