import itertools

def decrypt_monoalphabetic_bruteforce(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    possible_permutations = itertools.permutations(alphabet)

    for perm in possible_permutations:
        decryption_map = dict(zip(perm, alphabet))
        decrypted_text = "".join(decryption_map.get(char, char) for char in ciphertext)
        print(decrypted_text)

ciphertext = "YVCCF NFICU"
decrypt_monoalphabetic_bruteforce(ciphertext)
