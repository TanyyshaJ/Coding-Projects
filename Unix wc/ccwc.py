import argparse
import sys
import locale

def count_bytes(file_path): #byte count, simply counts the bytes in a file without interfering with the file content
    try:
        with open(file_path, 'rb') as f:
                content = f.read()
        return len(content)
    
    except FileNotFoundError:
        print(f"Error Filr: {file_path} not found!!")
    
    except Exception as e:
        print(f"Error{e}")

def line_count(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return len(lines)

    except FileNotFoundError:
        print(f"Error Filr: {file_path} not found!!")
    
    except Exception as e:
        print(f"Error{e}")

def word_count(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            words = [word for line in lines for word in line.split()]
        return len(words)

    except FileNotFoundError:
        print(f"Error Filr: {file_path} not found!!")
    
    except Exception as e:
        print(f"Error{e}")

def character_count(file_path, multibyte=False): #charcter count counts the number of character in the file
    #The difference in character count between the expected answer and your result may be due to the way characters are encoded and the specific encoding used when reading the file.
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if multibyte:   #Use locale-specific encoding to count characters
            encoding = locale.getpreferredencoding()
            content_encoded = content.encode(encoding)
            return len(content_encoded)
        else:           #Count ASCII characters only
            return len(content)

    except FileNotFoundError:
        print(f"Error Filr: {file_path} not found!!")
    
    except Exception as e:
        print(f"Error{e}")

def default(file_path):
    byte = count_bytes(file_path)
    line = line_count(file_path)
    word = word_count(file_path)
    return line, word, byte

def ccwc(file_path, count_bytes_flag, line_count_flag, word_count_flag, character_count_flag, default_flag):
    if not any([count_bytes_flag, line_count_flag, word_count_flag, character_count_flag, default_flag]):
        # No flags are set, use the default function
        answer = default(file_path)
        if answer is not None:
            print(answer)
    else:
        if count_bytes_flag:
            byte_count = count_bytes(file_path)
            if byte_count is not None:
                print(byte_count)
            
        if line_count_flag:
            count_lines = line_count(file_path)
            if count_lines is not None:
                print(count_lines)

        if word_count_flag:
            count_words = word_count(file_path)
            if count_words is not None:
                print(count_words)

        if character_count_flag:
            count_character = character_count(file_path)
            if count_character is not None:
                print(count_character)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                        prog='ccwc',
                        description='Command line tool')
    parser.add_argument('file', type=str, metavar='FILE', nargs='?', help='specify the file')
    parser.add_argument('--count-all', action='store_true', help='perform all activities')
    parser.add_argument('-c', '--count-bytes', action='store_true', help='count the bytes in file')
    parser.add_argument('-l', '--count-lines', action='store_true', help='count the lines in file')
    parser.add_argument('-w', '--count-words', action='store_true', help='count the words in file')
    parser.add_argument('-m', '--count-characters', action='store_true', help='count the characters in file')

    args = parser.parse_args()

    if args.file is None:
        file_path = sys.stdin.read()
    ccwc(args.file, args.count_bytes, args.count_lines, args.count_words, args.count_characters, args.count_all) 