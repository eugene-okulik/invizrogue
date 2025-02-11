import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("search", help="Text for search")
parser.add_argument("--path", help="Path to directory (current directory by default)", default='.')
parser.add_argument("--before", help="Number of words before found one (5 by default)", default=5)
parser.add_argument("--after", help="Number of words after found one (5 by default)", default=5)
parser.add_argument("--one", help="Find one", action='store_true')
args = parser.parse_args()

dir_items = map(lambda item: os.path.join(args.path, item), os.listdir(args.path))
files = filter(os.path.isfile, dir_items)

for file in list(files):
    with open(file, 'r') as log_file:
        for row_number, row in enumerate(log_file, start=1):
            if args.search in row:
                words = row.split()
                for i, word in enumerate(words):
                    if word == args.search:
                        index_start = max(i - int(args.before), 0)
                        index_end = min(i + int(args.after) + 1, len(words))
                        result = ' '.join(words[index_start:index_end])
                        print(f'File: {file}, row: {row_number}:\nFounded: {result}')
            if args.one:
                break
        if args.one:
            break
