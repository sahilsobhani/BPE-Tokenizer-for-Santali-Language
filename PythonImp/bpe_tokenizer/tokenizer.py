import re
from collections import defaultdict
from .config import NUM_MERGES
from .utils import load_corpus

class BPETokenizer:
    def __init__(self):
        self.vocab = {}
        self.merges = []

    def train(self, text, num_merges=NUM_MERGES):
        text = text.encode("utf-8")  # Convert text to bytes
        words = [tuple(word) for word in text.split()]
        self.vocab = {word: freq for word, freq in self._get_word_frequencies(words).items()}

        for _ in range(num_merges):
            pairs = self._get_pair_frequencies()
            if not pairs:
                break
            best_pair = max(pairs, key=pairs.get)
            self._merge(best_pair)
            self.merges.append(best_pair)

    def tokenize(self, text):
        tokens = list(text.encode("utf-8"))  # Convert input to bytes
        tokens = tuple(tokens)  # Convert list to tuple for processing
        for merge in self.merges:
            tokens = self._apply_merge(tokens, merge)

        # Recursively flatten tuples and convert them to bytes
        def flatten(t):
            if isinstance(t, int):
                return bytes([t])
            else:
                return b''.join(flatten(x) for x in t)

        utf8_tokens = [flatten(t).decode("utf-8", errors="ignore") for t in tokens]
        numerical_tokens = [[byte for byte in flatten(t)] for t in tokens]

        return utf8_tokens, numerical_tokens

    def _get_word_frequencies(self, words):
        freqs = defaultdict(int)
        for word in words:
            freqs[word] += 1
        return freqs

    def _get_pair_frequencies(self):
        pairs = defaultdict(int)
        for word, freq in self.vocab.items():
            for i in range(len(word) - 1):
                pairs[(word[i], word[i + 1])] += freq
        return pairs

    def _merge(self, pair):
        new_vocab = {}
        for word, freq in self.vocab.items():
            new_word = []
            i = 0
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
                    new_word.append(pair)  # Store as tuple
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            new_vocab[tuple(new_word)] = freq
        self.vocab = new_vocab

    def _apply_merge(self, tokens, merge):
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == merge:
                new_tokens.append(merge)  # Store merged pair as tuple
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        return tuple(new_tokens)