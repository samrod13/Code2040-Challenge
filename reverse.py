import requests

"""
Step 2 of the Code2040 Challenge
"""

token = "d0bb9c55a63d412ccf361fb695c9e5af"
endpoint = "http://challenge.code2040.org/api/reverse"

"""
Connects to the endpoint and receives a string to reverse
"""


def getString():

    # Sends JSON data to endpoint and gets the string
    payload = {"token": token}
    response = requests.post(endpoint, json=payload)
    string = response.text

    return string

"""
Reverse the string and send to endpoint
"""


def sendString(string):
    endpoint = "http://challenge.code2040.org/api/reverse/validate"

    payload = {"token": token,
               "string": string}

    response = requests.post(endpoint, json=payload)
    print("Response: " + response.text)


def main():
    # Get the string
    stringToReverse = getString()

    # Reverse the string
    stringToReverse = stringToReverse[::-1]

    # Send the string back to the endpoint
    sendString(stringToReverse)

if __name__ == '__main__':
    main()
