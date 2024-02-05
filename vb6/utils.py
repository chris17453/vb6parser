


def file_fragment(file_name, start=1, start_col=1, end=None, end_col=None):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        if start < 1 or start > len(lines) or (end and end > len(lines)):
            return "Invalid start/end line numbers"

        if start_col < 1:
            return "Invalid start column number"

        if end_col and end_col < 1:
            return "Invalid end column number"

        if not end:
            end = len(lines)

        text_lines = []
        for i in range(start - 1, end):
            line = lines[i]
            if i == start - 1:
                line = line[start_col - 1:]
            elif i == end - 1:
                if end_col:
                    line = line[:end_col]
                else:
                    line = line.rstrip()
            text_lines.append(line)

        return ''.join(text_lines)

    except FileNotFoundError:
        return "File not found"
