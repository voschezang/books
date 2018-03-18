""" Read/write from/to disk
"""
import pandas, os, config

import tfidf, config


def read_book(dirname, filename):
    if not dirname[-1] == '/':
        dirname += '/'
    text = open(dirname + filename, 'r', errors='replace').read()
    tokenized = tfidf.tokenize(text)
    return tokenized


def read_unique_genres():
    genres_file = open(config.dataset_dir + 'unique_genres.txt', 'r')
    return [genre.strip('\n') for genre in genres_file.readlines()]


def print_dict(dirname="", d={}, name="text"):
    if not dirname == "":
        dirname += "/"
    name += ".txt"
    with open(dirname + "0_" + name, "w") as text_file:
        print(name + "\n", file=text_file)
        for k, v in d.items():
            # print(f"{k}:{v}", file=text_file) # pythonw, python3
            print('{:s}, {:s}'.format(str(k), str(v)), file=text_file)


def save_dict_to_csv(dirname, name, data):
    # panda df requires data to be NOT of type {key: scalar}
    if not dirname[-1] == '/':
        dirname += '/'
    filename = dirname + name + ".csv"
    df = pandas.DataFrame(data=data)
    df.to_csv(filename, sep=',', index=False)
    # mkdir filename
    # for k in d.keys(): gen png
    return filename
