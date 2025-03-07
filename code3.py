def create_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I"))) 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [char for char in key if char in alphabet] + [char for char in alphabet if char not in key]

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def process_playfair(text, matrix, encrypt=True):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) and text[i] != text[i + 1] else "X"
        pairs.append((a, b))
        i += 2 if text[i] != text[i + 1] else 1

    result = ""
    shift = 1 if encrypt else -1

    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  
            result += matrix[row1][(col1 + shift) % 5] + matrix[row2][(col2 + shift) % 5]
        elif col1 == col2:  
            result += matrix[(row1 + shift) % 5][col1] + matrix[(row2 + shift) % 5][col2]
        else: 
            result += matrix[row1][col2] + matrix[row2][col1]

    return result


key = "LARKSPUR"
matrix = create_playfair_matrix(key)
ciphertext = "ILMILDRKRY"

plaintext = process_playfair(ciphertext, matrix, encrypt=False)
print("Decrypted Text:", plaintext)
