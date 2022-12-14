# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Ask the user for a word
word = input("Enter a word: ")

# Use requests to send a GET request to the Merriam-Webster website
response = requests.get("https://www.merriam-webster.com/dictionary/" >

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the definition of the word in the page using the soup object
definition = soup.find("span", class_="dtText").text

# Print the definition of the word
print(definition)
