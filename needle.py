import requests

"""
Step 3 of the Code2040 Challenge
"""

token = "d0bb9c55a63d412ccf361fb695c9e5af"
endpoint = "http://challenge.code2040.org/api/haystack"
validation_endpoint = "http://challenge.code2040.org/api/haystack/validate"


def getData():
    payload = {"token": token}
    response = requests.post(endpoint, json=payload)

    # Dictionary with needle and haystack
    data_dict = response.json()
    return data_dict

"""
Needle - a string to find
Haystack - array of strings

Returns the index of the needle in the haystack
"""


def findNeedle(data_dict):
    needle = data_dict.get("needle")
    haystack = data_dict.get("haystack")

    index = None
    if(needle in haystack):
        index = haystack.index(needle)

    return index


def main():
    # Get the needle and haystack from the endpoint
    data_dict = getData()

    # Find the index of the needle in the haystack
    position = findNeedle(data_dict)

    # Send the index of the needle to the validation endpoint
    payload = {"token": token,
               "needle": position}
    response = requests.post(validation_endpoint, data=payload)

if __name__ == '__main__':
    main()
