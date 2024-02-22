# Build Your Own `wc` Tool

This challenge invites you to create your version of the Unix command line tool `wc`, exploring the Unix philosophies:

1. **Simple Parts, Clean Interfaces:**
   - Each tool does one thing, offering a straightforward CLI that handles text input from files or streams.

2. **Connectable Programs:**
   - Tools should effortlessly connect with others, fostering the creation of powerful compositions.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Examples](#examples)
- [Implementation Details](#implementation-details)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python script, `ccwc.py`, is your personal implementation of the `wc` tool, focusing on simplicity and extensibility. It provides functionalities to count bytes, lines, words, and characters in a specified text file.

## Features

- **Count Bytes (`-c` or `--count-bytes`):**
  - Simply counts the bytes in a file without affecting the file content.

- **Count Lines (`-l` or `--count-lines`):**
  - Determines the number of lines in the specified file.

- **Count Words (`-w` or `--count-words`):**
  - Calculates the total word count in the specified file.

- **Count Characters (`-m` or `--count-characters`):**
  - Considers character count, accounting for potential multibyte characters.

## Usage

```bash
python ccwc.py [-c/-l/-w/-m] [file_path]
```

- `-c` or `--count-bytes`: Count bytes in the file.
- `-l` or `--count-lines`: Count lines in the file.
- `-w` or `--count-words`: Count words in the file.
- `-m` or `--count-characters`: Count characters in the file, considering multibyte characters based on the locale.

## Examples

1. **Count Bytes:**
   ```bash
   python ccwc.py -c test.txt
   ```

2. **Count Lines:**
   ```bash
   python ccwc.py -l test.txt
   ```

3. **Count Words:**
   ```bash
   python ccwc.py -w test.txt
   ```

4. **Count Characters (Multibyte-aware):**
   ```bash
   python ccwc.py -m test.txt
   ```

## Implementation Details

- **Encoding Considerations:**
  - The script uses UTF-8 encoding for reading text files, and it considers the locale-specific encoding for multibyte character count.

- **Error Handling:**
  - Handles common file-related errors such as file not found and general exceptions.

## Contributing

Feel free to contribute by submitting issues, providing feedback, or creating pull requests. Your input is valuable!

## License

This project is licensed under the [MIT License](LICENSE).
