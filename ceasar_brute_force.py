from collections import Counter

def auto_decrypt_caesar(ciphertext):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ciphertext.lower()
    
    # We ignore 'z' if it's being used as a space to avoid skewing frequency
    clean_text = ciphertext.replace('z', '')
    
    best_shift = 0
    max_score = 0
    
    # Common English letters to look for
    common_letters = "etaoin" 

    for shift in range(26):
        score = 0
        decrypted = ""
        
        for char in ciphertext:
            if char in alphabet:
                index = alphabet.find(char)
                new_char = alphabet[(index - shift) % 26]
                decrypted += new_char
                if new_char in common_letters:
                    score += 1
            else:
                decrypted += char
        
        # Track the shift that produces the most "English-looking" result
        if score > max_score:
            max_score = score
            best_shift = shift
            best_text = decrypted

    return best_shift, best_text

# Your input
cipher_text = "benjaminzhranklinzhadzonezofz hezgrea es zscien ificzmindszofzhisz ime."

shift, result = auto_decrypt_caesar(cipher_text)

print(f"Detected Shift: {shift}")
print(f"Decoded Message: {result.replace('z', ' ')}")