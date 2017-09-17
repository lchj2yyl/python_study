import os


def consume_file_data(file_path, consumer):
    for line in file(file_path):
        consumer.send(line)

@consumer
def consume_words(consumer):
    while True:
        line = yield
        line = str(line)
        for word in (w for w in line.split()if w.strip()):
            consumer.send(word)

@consumer
def count_words():
    while True:
        word = yield
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

words_dict = {}

consumer = count_words()
consumer.next()

consumer = consume_words(consumer)
consumer.next()

consume_file_data('GenerateorTest3.py', consumer)

for key, value in words_dict.items():
    print key, value


