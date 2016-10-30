import requests

"""
Stage 4 of the Code2040 Challenge
"""
token = "d0bb9c55a63d412ccf361fb695c9e5af"
endpoint = "http://challenge.code2040.org/api/prefix"
validation_endpoint = "http://challenge.code2040.org/api/prefix/validate"


def getData():
    payload = {"token": token}
    response = requests.post(endpoint, json=payload)
    data_dict = response.json()
    return data_dict

"""
prefix - a string
arr - array of strings

Remove all of the items in arr that begin with the prefix
"""


def removePrefix(data_dict):
    prefix = data_dict.get("prefix")
    arr = data_dict.get("array")
    answers = []

    for item in arr:
        if item[:len(prefix)] != prefix:
            answers.append(item)

    return answers


def sendData(arr):
    payload = {"token": token,
               "array": arr}
    response = requests.post(validation_endpoint, json=payload)


def main():
    data_dict = getData()
    arr = removePrefix(data_dict)
    sendData(arr)

if __name__ == '__main__':
    main()
