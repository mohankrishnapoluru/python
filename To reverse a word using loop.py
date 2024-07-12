print("puneeth")
def reverse_word(word):
    reversed_word = ""
    # Iterate through the word from the last character to the first
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

# Get input from the user
word = input("Enter a word to reverse: ")

# Call the function to reverse the word
reversed_word = reverse_word(word)

# Print the reversed word
print(f"The reversed word is: {reversed_word}")
