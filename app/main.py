import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
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

    def find_word_line_number(filename, target_word):
        line_number = 0
    
        with open(filename, 'r') as file:
            for line in file:
                line_number += 1
                if target_word in line:
                    return line_number
 
    # If the word is not found in the file, return None
        return None
    
    error = False
    for c in file_contents:
        if c == "(":
            print("LEFT_PAREN ( null")
        if c == ")":
            print("RIGHT_PAREN ) null")
        if c == "{":
            print("LEFT_BRACE { null")
        if c == "}":
            print("RIGHT_BRACE } null")
        if c == "*":
            print("STAR * null")
        if c == ".":
            print("DOT . null")
        if c == ",":
            print("COMMA , null")
        if c == "+":
            print("PLUS + null")
        if c == "-":
            print("MINUS - null")
        if c == ";":
            print("SEMICOLON ; null")
        else : 
            error = True 
            ln = find_word_line_number(filename, c)
            print(f"\n[line {ln}] Error: Unexpected character: {c}")
            
    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)


if __name__ == "__main__":
    main()


# [line 1] Error: Unexpected character: $