import requests

"""
must accept user input representing a 'name'
must make HTTP GET call to server in the form of: http://localhost:500/hello/{name}
"""

print("Please eneter your name ")
name = input()
url = f"http://localhost:5000/hello/{name}"
response = requests.get(url)
print(response.text)