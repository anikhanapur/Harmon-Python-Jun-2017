import sys

def extract_lines_from_file(file_name='words-data.txt'):
    return open(file_name, 'r').readlines()


def prep_line(line):
    return line.replace(',', '').replace('"', '').replace('.', '')


def extract_words(lines):
    # all_words = []
    # for line in lines:
    #     prepped_line = prep_line(line)
    #     words = prepped_line.split(' ')
    #     all_words.extend(words)
    # return all_words
    # prepped_lines = [prep_line(line) for line in lines]
    return [word for prepped_line in [prep_line(line) for line in lines] for word in prepped_line.split(' ')]


def get_occurance_count(words):
    # stats = {}
    # for word in words:
    #     if word not in stats:
    #         stats[word] = 0
    #     stats[word] += 1
    # return stats
    return {word: words.count(word) for word in words}


def get_top_10_occurance(stats):
    # result = []
    # for word in stats:
    #    result.append((stats[word], word))
    result = [(stats[word], word) for word in stats]
    result.sort(reverse=True)
    return result[:10]


def run(file_name):
    lines = extract_lines_from_file(file_name)
    words = extract_words(lines)
    stats = get_occurance_count(words)
    result = get_top_10_occurance(stats)
    print result


if (__name__ == '__main__'):
    if (len(sys.argv) <= 1 or sys.argv[1] is None):
        print('Invalid arguments')
    else:
        run(sys.argv[1])
