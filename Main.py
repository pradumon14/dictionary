
# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
Word=str(input("Enter the word :"))

# Set the URL of the word to be searched
url = "https://www.dictionary.com/browse/" + word

# Make a request to the URL and store the response
response = requests.get(url)

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the definition of the word from the soup
definition = soup.find('div', class_='css-1o58fj8 e1hk9ate4').text

# Print the definition of the word
print(definition)
