from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))

with open("C:\\Users\\Spencer\\Documents\\DAPT\\Text Mining\\AA_full.txt", 'r') as text_file:
    text = text_file.read()
    token1 = word_tokenize(str(text))
    token1 = [w for w in token1 if not w in stopset]
    print token1

# Find unique words in the set
uniques = []
for word in token1:
  if word not in uniques:
    uniques.append(word)

# Make a list of (count, unique) tuples.
counts = []
for unique in uniques:
  count = 0              # Initialize the count to zero.
  for word in token1:     # Iterate over the words.
    if word == unique:   # Is this word equal to the current unique?
      count += 1         # If so, increment the count
  counts.append((count, unique))

counts.sort()            # Sorting the list puts the lowest counts first.
counts.reverse()         # Reverse it, putting the highest counts first.
# Print the ten words with the highest counts.
for i in range(min(10, len(counts))):
  count, word = counts[i]
  print('%s %d' % (word, count))

