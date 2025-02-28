from bpe_tokenizer import BPETokenizer
from bpe_tokenizer.utils import load_corpus

# Load corpus using the function
corpus = load_corpus("../Data/data.txt")

# Train the tokenizer
tokenizer = BPETokenizer()
tokenizer.train(corpus)

# Example tokenization
sample_text = "ᱥᱟᱱᱛᱟᱞᱤ ᱵᱚᱨᱚ"
utf8_tokens = tokenizer.tokenize(sample_text)

print("UTF-8 Tokens:", utf8_tokens)

