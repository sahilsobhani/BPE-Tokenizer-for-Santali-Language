# BPE Tokenizer for Santali Language

This repository contains an implementation of a Byte Pair Encoding (BPE) tokenizer for the Santali language in both Python and C++. The tokenizer learns subword merges from a training corpus and applies them to segment new text efficiently.

## Features

- Tokenizes Santali text using BPE.
- Learns subword merges from a training corpus.
- Implemented in **Python** for prototyping and **C++** for efficiency.
- Supports saving and loading trained vocabulary.

## Installation

### Python Version

Ensure you have Python 3 installed, then clone the repository and install dependencies:

```bash
pip install -r requirements.txt  # If dependencies are required
```

### C++ Version

Ensure you have a C++ compiler (GCC or Clang). Compile with:

```bash
g++ -o bpe_tokenizer bpe_tokenizer.cpp
```

## Usage

### Python

```python
from bpe_tokenizer import BPETokenizer

corpus = "ᱥᱟᱱᱛᱟᱞᱤ ᱡᱷᱤᱡᱤ ᱵᱚᱨᱚ ᱯᱷᱚᱦᱚ"
tokenizer = BPETokenizer(num_merges=10)
tokenizer.train(corpus)
print("Tokenized text:", tokenizer.tokenize("ᱥᱟᱱᱛᱟᱞᱤ ᱵᱚᱨᱚ"))
```

### C++

Compile and run:

```bash
./bpe_tokenizer input.txt
```

## Future Improvements

- Optimize C++ version for large-scale processing.
- Implement GPU acceleration using CUDA.
- Extend to other low-resource languages.

## License

This project is open-source under the MIT License.
