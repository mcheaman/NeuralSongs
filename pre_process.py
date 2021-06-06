#Preprocesses a given file to facilitate bigram generation

import sys
def process_line(text):
    newline = "<s> "
    firstWord = text.split()[0]
    newline += firstWord.lower() 
    newline += " "
    newline += " ".join(text.split()[1:-1])
    newline += " </s>"
    return newline

def main():
    filename = sys.argv[1];
    newfilename = sys.argv[2];
    with open(filename, encoding='utf-8') as corpus:
        with open(newfilename, 'w', encoding='utf-8') as destination:
            for line in corpus:
                if(len(line) <=1):
                    continue
                print(process_line(line), file=destination)

if __name__ == "__main__":
    main()