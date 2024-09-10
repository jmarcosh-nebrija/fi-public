name = input('Enter file: ')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

most_popular_word = None
most_popular_word_count = 0
for word, count in list(counts.items()):
    if count > most_popular_word_count:
        most_popular_word = word
        most_popular_word_count = count

print("Most popular word: " + most_popular_word + ", appears "
      + str(most_popular_word_count) + " times.")
