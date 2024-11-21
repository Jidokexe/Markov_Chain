import random
from collections import defaultdict

def build_markov_chain(text, order=1):
    markov_chain = defaultdict(list)
    for i in range(len(text) - order):
        state = text[i:i+order]
        next_char = text[i+order]
        markov_chain[state].append(next_char)
    return markov_chain

def generate_text(markov_chain, length, order=1):
    start_state = random.choice(list(markov_chain.keys()))
    generated = start_state
    
    for _ in range(length - len(start_state)):
        current_state = generated[-order:]
        if current_state in markov_chain:
            next_char = random.choice(markov_chain[current_state])
            generated += next_char
        else:
            break  
    return generated

def main(input_file, n, m, order=1):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', ' ')
    
    markov_chain = build_markov_chain(text, order=order)
    
    generated_lines = [generate_text(markov_chain, m, order=order) for _ in range(n)]
    return generated_lines

input_file = r"C:\Users\Jidok_exe\Documents\input.txt"  
n = 5  
m = 50  
order = 2  

if __name__ == "__main__":
    generated_lines = main(input_file, n, m, order)
    for line in generated_lines:
        print(line)
