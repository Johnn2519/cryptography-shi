def decode_rail_fence(ciphertext, rails):
    fence = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    rail, direction = 0, 1

    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*' and index < len(ciphertext):
                fence[r][c] = ciphertext[index]
                index += 1

    result = []
    rail, direction = 0, 1
    for i in range(len(ciphertext)):
        result.append(fence[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return "".join(result)

# The target string
encoded_str = "waymiwx dxjiylaivbpndrrig!ayxx"

print(f"{'Rails':<6} | {'Decoded Message'}")
print("-" * 40)

# Brute force from 2 to 15 rails
for r in range(2, 16):
    decoded = decode_rail_fence(encoded_str, r)
    print(f"{r:<6} | {decoded}")