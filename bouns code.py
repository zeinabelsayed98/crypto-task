from collections import Counter

def frequency_analysis(ciphertext):
    ciphertext = ciphertext.replace(" ", "").upper() 
    letter_counts = Counter(ciphertext)  
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)  
    print("Letter Frequency Analysis:")
    for letter, freq in sorted_letters:
        print(f"{letter}: {freq}")

ciphertext = "YVCCF NFICU"  
frequency_analysis(ciphertext)
