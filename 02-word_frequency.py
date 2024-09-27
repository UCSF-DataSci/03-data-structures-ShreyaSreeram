#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys
import string

def word_frequency(text):
    frequencies = {}  # Dictionary to store word frequencies
    
    # Convert the entire text to lowercase to ignore case sensitivity
    text = text.lower()
    
    # Remove punctuation using str.translate and string.punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
            
    # Sort the dictionary alphabetically and limit to the first 20 items
    sorted_frequencies = dict(sorted(frequencies.items())[:20])
    
    return sorted_frequencies

# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()  # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        print(f"Word frequencies for '{filename}':")
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)