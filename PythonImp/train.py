from bpe_tokenizer import BPETokenizer
from bpe_tokenizer.utils import load_corpus

# Load corpus
corpus = load_corpus("../Data/data.txt")

# Train the tokenizer
tokenizer = BPETokenizer()
tokenizer.train(corpus)

# Example tokenization
sample_text = "ᱥᱟᱱᱛᱟᱞᱤ ᱵᱚᱨᱚ"
utf8_tokens, numerical_tokens = tokenizer.tokenize(sample_text)

print("Original Text:", sample_text)
print("UTF-8 Tokens:", utf8_tokens)
print("Numerical Tokens:", numerical_tokens)

# Decode back to original text
decoded_text = tokenizer.decode(numerical_tokens)
print("Decoded Text:", decoded_text)
