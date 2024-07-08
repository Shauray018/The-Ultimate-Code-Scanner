import sys

def main():
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    error = False
    skip_next = False
    tokens = []
    error_messages = []
    line_number = 1

    i = 0
    while i < len(file_contents):
        if skip_next:
            skip_next = False
            i += 1
            continue

        c = file_contents[i]
        next_c = file_contents[i + 1] if i + 1 < len(file_contents) else None  # Peek at the next character

        if c == "\n":
            line_number += 1
            i += 1
            continue

        if c == "(":
            tokens.append("LEFT_PAREN ( null")
        elif c == ")":
            tokens.append("RIGHT_PAREN ) null")
        elif c == "{":
            tokens.append("LEFT_BRACE { null")
        elif c == "}":
            tokens.append("RIGHT_BRACE } null")
        elif c == "*":
            tokens.append("STAR * null")
        # elif c == ".":
        #     if next_c and next_c.isdigit():
        #         num_str = c
        #         i += 1
        #         while i < len(file_contents) and file_contents[i].isdigit():
        #             num_str += file_contents[i]
        #             i += 1
        #         tokens.append(f'NUMBER {num_str} {float(num_str)}')
        #         i -= 1  # Adjust since the outer loop will also increment `i`
        #     else:
        #         tokens.append("DOT . null")
        elif c == ",":
            tokens.append("COMMA , null")
        elif c == "+":
            tokens.append("PLUS + null")
        elif c == "-":
            tokens.append("MINUS - null")
        elif c == ";":
            tokens.append("SEMICOLON ; null")
        elif c == "=":
            if next_c == "=":
                tokens.append("EQUAL_EQUAL == null")
                skip_next = True
            else:
                tokens.append("EQUAL = null")
        elif c == "!":
            if next_c == "=":
                tokens.append("BANG_EQUAL != null")
                skip_next = True
            else:
                tokens.append("BANG ! null")
        elif c == "<":
            if next_c == "=":
                tokens.append("LESS_EQUAL <= null")
                skip_next = True
            else:
                tokens.append("LESS < null")
        elif c == ">":
            if next_c == "=":
                tokens.append("GREATER_EQUAL >= null")
                skip_next = True
            else:
                tokens.append("GREATER > null")
        elif c == "/":
            if next_c == "/":
                while i < len(file_contents) and file_contents[i] != "\n":
                    i += 1
                continue
            else:
                tokens.append("SLASH / null")
        elif c == " " or c == "\t":
            pass  # Ignore whitespace characters
        elif c == '"':
            string_token = ''
            i += 1
            start_line = line_number
            while i < len(file_contents) and file_contents[i] != '"':
                if file_contents[i] == "\n":
                    line_number += 1
                string_token += file_contents[i]
                i += 1

            if i >= len(file_contents) or file_contents[i] != '"':
                error = True
                error_messages.append("[line %d] Error: Unterminated string." % start_line)
                break
            else:
                tokens.append(f'STRING \"{string_token}\" {string_token}')
        elif c.isdigit() or c == '.':
                num_str = c
                i += 1
                dot_count = 1 if c == '.' else 0
                while i < len(file_contents) and (file_contents[i].isdigit() or (file_contents[i] == '.' and dot_count == 0)):
                    if file_contents[i] == '.':
                        dot_count += 1
                    num_str += file_contents[i]
                    i += 1
                
                # Check if we actually parsed a number
                if num_str == '.':
                    tokens.append("DOT . null")
                else:
                    # Check if the number ends with a dot
                    if num_str.endswith('.'):
                        num_str = num_str[:-1]  # Remove the trailing dot
                        tokens.append(f'NUMBER {num_str} {float(num_str)}')
                        tokens.append("DOT . null")
                    else:
                        tokens.append(f'NUMBER {num_str} {float(num_str)}')
                
                # Handle any additional decimal points
                while i < len(file_contents) and file_contents[i] == '.':
                    tokens.append("DOT . null")
                    i += 1
                
                i -= 1  # Adjust since the outer loop will also increment `i`
        elif c == '.':
                tokens.append("DOT . null")
        else:
            error = True
            error_messages.append("[line %d] Error: Unexpected character: %s" % (line_number, c))

        i += 1

    tokens.append("EOF  null")

    for error_message in error_messages:
        print(error_message, file=sys.stderr)
    for token in tokens:
        print(token)

    if error:
        exit(65)
    else:
        exit(0)

if __name__ == "__main__":
    main()
