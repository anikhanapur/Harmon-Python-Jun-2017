def extract_lines_from_file():
    file = open('words-data.txt', 'r')
    file_contents = file.readlines()
    return file_contents


def prep_line(line):
    return line.replace(',', '').replace('"', '').replace('.', '')


def extract_words(lines):
    all_words = []
    for line in lines:
        prepped_line = prep_line(line)
        words = prepped_line.split(' ')
        all_words.extend(words)
    return all_words


def get_occurance_count(words):
    stats = {}
    for word in words:
        if word not in stats:
            stats[word] = 0
        stats[word] += 1
    return stats


def get_top_10_occurance(stats):
    result = []
    for word in stats:
        result.append((stats[word], word))

    result.sort(reverse=True)
    return result[:10]


def run():
    lines = extract_lines_from_file()
    words = extract_words(lines)
    stats = get_occurance_count(words)
    result = get_top_10_occurance(stats)
    print result


run()
