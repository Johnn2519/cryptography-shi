# Set the alphabet used for shifts here (hardcoded):
# Change this value to use a different alphabet or custom character set.
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ! "


def CeasarBruteforceSimple(ciphertext: str, alphabet: str = ALPHABET) -> None:
	"""Print all Caesar shifts of ciphertext using the provided alphabet.

	Preserves case for letters in the alphabet and leaves other characters unchanged.
	The number of shifts equals the length of the alphabet (e.g., 26 for English A-Z).
	"""
	n = len(alphabet)
	for shift in range(n):
		chars = []
		for ch in ciphertext:
			# Find character in alphabet ignoring case
			idx = alphabet.find(ch.upper())
			if idx != -1:
				shifted = alphabet[(idx - shift) % n]
				chars.append(shifted.lower() if ch.islower() else shifted)
			else:
				chars.append(ch)
		print(f"Shift {shift:2d}: {''.join(chars)}")


if __name__ == "__main__":
	# Example usage. To use a different alphabet, change the ALPHABET variable above.
	sample = "! almv !h!pwatlhjmh! aleqvohpizlmz"
	CeasarBruteforceSimple(sample)
