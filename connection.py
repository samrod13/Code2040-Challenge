import requests

"""
Step 1 of Code2040 Api Code2040 Challenge
"""

token = "d0bb9c55a63d412ccf361fb695c9e5af"
repo = "https://github.com/samrod13/Code2040-Challenge"
endpoint = "http://challenge.code2040.org/api/register"


def connect():

    # Send JSON data with token and repo
    payload = {"token": token,
               "github": repo}
    response = requests.post(endpoint, json=payload)

    # Output the response
    print("Response: " + response.text)


def main():
    connect()

if __name__ == '__main__':
    main()
