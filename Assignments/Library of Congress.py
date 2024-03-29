import sys

def book_conversion(file_name):
    lines = {}
    longest_line = ""
    longest_line_number = 0
    total_length = 0
    line_count = 0

    with open(file_name, 'r') as file:
        for line in file:
            text, line_number = line.strip().split('|')
            line_number = int(line_number)
            lines[line_number] = text

            if len(text) > len(longest_line) or (len(text) == len(longest_line) and line_number > longest_line_number):
                longest_line = text
                longest_line_number = line_number

            total_length += len(text)
            line_count += 1

    average_length = round(total_length / line_count)

    book_lines = [lines[line_number] for line_number in sorted(lines.keys())]

    output_file_name = file_name.split('.')[0] + '_book.txt'

    with open(output_file_name, 'w') as output_file:

        output_file.write(file_name.split('.')[0].upper() + '\n')
        output_file.write(f'Longest line ({longest_line_number}): {longest_line}\n')
        output_file.write(f'Average length: {average_length}\n')

        for line in book_lines:
            output_file.write(line + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 library.py <filename>")
        sys.exit(1)

    file_name = sys.argv[1]
    book_conversion(file_name)
    