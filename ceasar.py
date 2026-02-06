import substitution, english

def generate_key(shift):
    end   = english.LANGUAGE["alphabet"][-shift:]
    start = english.LANGUAGE["alphabet"][:-shift]
    return end + start

def encode(message, shift):
    message = message.lower()
    key = generate_key(shift)
    return substitution.encode(message, key, english.LANGUAGE["alphabet"])

def decode(message, shift):
    return encode(message, -shift)

def crack(message, all_matches=False):
    """
        Breaks a Ceasar Cypher
        top_matches: how many of the top matches to return (-1 = all)
        Returns: list of cypher decodings, ordered by ammount of common english words 
    """
    messages = []
    for shift in range(len(english.LANGUAGE["alphabet"])):
        messages.append(decode(message, shift))

    matches = sorted(messages, key=english.score, reverse=True)

    if all_matches: return matches
    return matches[0]

if __name__ == "__main__":
    # print(crack("wklv lv d vhfuhw phvvdjh"))
    cypher = input("cypher to break: ")
    print("")
    print(crack(cypher))
    input()