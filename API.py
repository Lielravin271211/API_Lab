"""
API LAB: Calling Real Data from the Internet

GOAL:
Learn how to use an API to get real data from the internet using Python.

An API is just a URL that returns DATA instead of a webpage.
"""

# STEP 1: Choose an API (USE THIS LIST ONLY) 

# Pick ONE API from this list on schoology https://github.com/teacher-aj/public-apis?tab=readme-ov-file#social


# STEP 2: Make an API Call

# Paste the API URL you chose as a STRING below

# Convert the response into Python data (dictionary or list) below

# ALWAYS print the full data first so you can see its structure
import requests
stories = []
url = "https://hacker-news.firebaseio.com/v0/topstories.json"#library with a lot of 
response = requests.get(url)
data = response.json()
stories1 = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(data[0]) + ".json").json()
stories.append(stories1)
topstory = stories[-1]
print("This program gets the most recent story/resource from Hacker News and prints the title, author, id, and url.")
print("Hacker News is a website for coders and other people to share their code, ideas, and helpful resources.")
print("The most recent resource:")
print("Story id:", topstory["id"])
print("Story title:",topstory["title"])
print("By:", topstory["by"])
print(topstory["url"])
while True:#For a fun game do 46451768
    idrequest = input("To see a different story input your requested id: ").strip()
    try:
        int(idrequest)
        print("This is a number.")
        break
    except ValueError:
        print("This is NOT a number.")
        continue 
stories2 = requests.get("https://hacker-news.firebaseio.com/v0/item/" + idrequest + ".json").json()
print("Your requested resource:")
print("Story id:", stories2["id"])
print("Story title:",stories2["title"])
print("By:", stories2["by"])
print(stories2["url"])
# STEP 3: Extract a Piece of Data

# Look at what printed above.
# Find ONE specific value you want to use.


# Examples (yours will be different):

# cat_fact = data["fact"]
# print(cat_fact)

# latitude = data["iss_position"]["latitude"]
# print(latitude)

# write your code here


# STEP 4: Do Something With the Data


# Do ONE of the following:
# - Print it in a sentence
# - Store it in a variable
# - Add it to a list
# - Combine it with text

# Example:
# print(f"The ISS is currently at latitude {latitude}.")
