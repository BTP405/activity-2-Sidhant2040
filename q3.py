def wordCount(file_path):
    word_line_mapping = {}

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()
            for word in words:
                word_line_mapping.setdefault(word, []).append(line_number)

    return word_line_mapping

file_path = 'snow_data.txt'  
result = wordCount(file_path)

for word, line_numbers in result.items():
    print(f'{word}: {line_numbers}')
