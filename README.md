# Byte Pair Encoding (BPE) Tokenizer for Santali Language

## Overview
This repository contains an implementation of a Byte Pair Encoding (BPE) tokenizer specifically designed for the Santali language. The tokenizer is implemented in both Python and C++.

## Project Structure
```
├── Data/
│   ├── data.txt  # Corpus used for training
├── PythonImp/
│   ├── bpe_tokenizer/
│   │   ├── __init__.py
│   │   ├── tokenizer.py
│   │   ├── utils.py
│   │   ├── config.py
│   ├── train.py  # Script to train and test the tokenizer
├── CppImp/
│   ├── src/
│   │   ├── tokenizer.cpp
│   │   ├── utils.cpp
│   ├── include/
│   │   ├── tokenizer.h
│   │   ├── utils.h
│   ├── CMakeLists.txt  # Build configuration for C++ implementation
├── README.md  # Project documentation
```

## Installation
### Python Implementation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-folder>/PythonImp
   ```

### C++ Implementation
1. Navigate to the C++ directory:
   ```sh
   cd <repo-folder>/CppImp
   ```
2. Compile the project:
   ```sh
   mkdir build && cd build
   cmake .. && make
   ```

## Usage
### Python
Train and test the tokenizer using:
```sh
python train.py
```

### C++
Run the compiled tokenizer:
```sh
./bpe_tokenizer
```

## Features
- Supports UTF-8 encoding
- Handles Santali script (Ol Chiki)
- Byte Pair Encoding (BPE) training and tokenization
- Implemented in both Python and C++ for performance optimization

## License
This project is licensed under the MIT License.

