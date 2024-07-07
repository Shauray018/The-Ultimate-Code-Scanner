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

    def find_word_line_number(contents, target_word):
        line_number = 0
        for line in contents.split('\n'):
            line_number += 1
            if target_word in line:
                return line_number
        # If the word is not found in the file, return None
        return None
 
    # If the word is not found in the file, return None
        return None
    
    error = False
    for c in file_contents:
        if c == "(":
            print("LEFT_PAREN ( null")
        elif c == ")":
            print("RIGHT_PAREN ) null")
        elif c == "{":
            print("LEFT_BRACE { null")
        elif c == "}":
            print("RIGHT_BRACE } null")
        elif c == "*":
            print("STAR * null")
        elif c == ".":
            print("DOT . null")
        elif c == ",":
            print("COMMA , null")
        elif c == "+":
            print("PLUS + null")
        elif c == "-":
            print("MINUS - null")
        elif c == ";":
            print("SEMICOLON ; null")
        else : 
            error = True 
            ln = find_word_line_number(file_contents, c)
            print(f"[line {ln}] Error: Unexpected character: {c}")
            
    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)


if __name__ == "__main__":
    main()
