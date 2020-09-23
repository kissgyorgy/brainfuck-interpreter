from collections import deque


def brain_luck(code, input):
    code = clean_code(code)
    input = deque(ord(c) for c in input)
    data = [0] * 100
    data_pointer = 0
    code_pointer = 0
    opening_bracket_indexes = []
    output = []

    # interpret code
    while code_pointer < len(code):
        c = code[code_pointer]

        if c == '>':
            data_pointer += 1

        elif c == '<':
            data_pointer -= 1

        elif c == '+':
            data[data_pointer] += 1

            if data[data_pointer] > 255:
                data[data_pointer] = 0

        elif c == '-':
            if data[data_pointer] == 0:
                data[data_pointer] = 255
            else:
                data[data_pointer] -= 1

        elif c == '.':
            output.append(data[data_pointer])

        elif c == ',':
            data[data_pointer] = input.popleft()

        elif c == '[':
            if data[data_pointer] == 0:
                code_pointer = find_closing_bracket(code, code_pointer)
            else:
                opening_bracket_indexes.append(code_pointer)

        elif c == ']':
            if data[data_pointer] != 0:
                code_pointer = opening_bracket_indexes[-1]
            else:
                opening_bracket_indexes.pop()

        code_pointer += 1

    return ''.join(chr(b) for b in output)


def clean_code(code):
    return ''.join(c for c in code if c in '<>+-.,[]')


def find_closing_bracket(code, code_pointer):
    opening_bracket_count = 0
    closing_bracket_count = 0

    while code_pointer < len(code):
        c = code[code_pointer]
        if c == '[':
            opening_bracket_count += 1
        elif c == ']':
            closing_bracket_count += 1

        if opening_bracket_count == closing_bracket_count:
            break

        code_pointer += 1

    return code_pointer
