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
    frequencies = {}  #dictionary to store word frequencies
    
    #converting the entire text to lowercase to ignore case sensitivity
    text = text.lower()
    
    #removing punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    words = text.split()
    
    #counting freq of each word 
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
            
    #sort alphabetically
    sorted_frequencies = dict(sorted(frequencies.items())[:20])
    
    return sorted_frequencies

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read() 
        
        frequencies = word_frequency(text)
        
        print(f"Word frequencies for '{filename}':")
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)