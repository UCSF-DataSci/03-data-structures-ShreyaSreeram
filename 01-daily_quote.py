#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date

quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Do not wait to strike till the iron is hot; but make it hot by striking. – William Butler Yeats",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Whether you think you can or you think you can’t, you’re right. – Henry Ford",
    "I have not failed. I’ve just found 10,000 ways that won’t work. – Thomas A. Edison",
    "Act as if what you do makes a difference. It does. – William James",
    "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt"
]

def get_quote_of_the_day(quotes):
    # Use today's date to set the seed for the random number generator
    today = date.today()
    random.seed(today.toordinal())
    
    # Select a random quote from the list
    todays_quote = random.choice(quotes)
    
    return todays_quote

if __name__ == "__main__":
    daily_quote = get_quote_of_the_day(quotes)
    print(daily_quote)

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt