# wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
with open('1984.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# here are all the unique characters that occur in this text
chars = list(text)
chars = sorted(list(set(text)))

vocab_size = len(chars)
print(vocab_size)

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# here are all the unique characters that occur in this text
chars = list(text)
vocab_size = len(chars)
print(vocab_size)