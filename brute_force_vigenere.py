import string
from collections import Counter

# Standard English letter frequency (A-Z)
ENGLISH_FREQ = [
    0.0817, 0.0150, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 0.0697, 
    0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193, 0.0010, 0.0599, 
    0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007
]

def chi_squared_score(text):
    """Scores how close a text is to English frequency (lower is better)."""
    counts = Counter(text.upper())
    total = sum(counts.values())
    if total == 0: return float('inf')
    
    score = 0
    for i, freq in enumerate(ENGLISH_FREQ):
        observed = counts[string.ascii_uppercase[i]]
        expected = total * freq
        score += ((observed - expected)**2) / expected
    return score

def decrypt_vigenere(ciphertext, key):
    """Standard Vigenere decryption logic."""
    plaintext = ""
    key = key.upper()
    key_idx = 0
    for char in ciphertext:
        if char.isalpha():
            offset = ord(key[key_idx % len(key)]) - ord('A')
            start = ord('A') if char.isupper() else ord('a')
            plaintext += chr(start + (ord(char) - start - offset) % 26)
            key_idx += 1
        else:
            plaintext += char
    return plaintext

def brute_force_vigenere(ciphertext, max_key_length=10):
    # Remove non-alpha for analysis
    filtered_text = "".join(filter(str.isalpha, ciphertext.upper()))
    
    best_overall_key = ""
    best_overall_score = float('inf')

    # 1. Try different possible key lengths
    for length in range(1, max_key_length + 1):
        current_key = ""
        
        # 2. For each position in the key, solve it like a Caesar cipher
        for i in range(length):
            nth_chars = filtered_text[i::length]
            best_char = ''
            best_char_score = float('inf')
            
            for shift in range(26):
                test_decrypt = "".join([chr(((ord(c) - ord('A') - shift) % 26) + ord('A')) for c in nth_chars])
                score = chi_squared_score(test_decrypt)
                if score < best_char_score:
                    best_char_score = score
                    best_char = chr(ord('A') + shift)
            
            current_key += best_char
        
        # 3. Score the full decryption with this key
        full_test = decrypt_vigenere(ciphertext, current_key)
        total_score = chi_squared_score("".join(filter(str.isalpha, full_test)))
        
        print(f"Testing Key Length {length}: Potential Key [{current_key}]")
        
        if total_score < best_overall_score:
            best_overall_score = total_score
            best_overall_key = current_key

    print("\n--- BEST GUESS ---")
    print(f"Key: {best_overall_key}")
    print(f"Message: {decrypt_vigenere(ciphertext, best_overall_key)}")

# Example: "The quick brown fox" encrypted with key "CODE"
msg = "Vvw txlgy duckp iqy"
brute_force_vigenere(msg)