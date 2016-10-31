import requests
import datetime

"""
Part 5 of the Code2040 Challenge
"""

token = "d0bb9c55a63d412ccf361fb695c9e5af"
endpoint = "http://challenge.code2040.org/api/dating"
validation_endpoint = "http://challenge.code2040.org/api/dating/validate"


def getData():
    payload = {"token": token}
    response = requests.post(endpoint, json=payload)
    data_dict = response.json()
    return data_dict


def addTime(datestamp, seconds):
    # Convert the datestamp string to a datetime object
    dtime = datetime.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
    # Add the interval(seconds) to the datetime object
    updatedTime = dtime + datetime.timedelta(0, seconds)
    # convert the datetime object to iso format %Y-%m-%dT%H:%M:%S:%fZ
    updatedTime = updatedTime.isoformat()
    # parse the datetime object to a string
    finalTime = str(updatedTime)
    # remove the :%f from the iso format
    finalTime = finalTime[:len(finalTime)] + "Z"
    return finalTime


def sendData(datestamp):
    payload = {"token": token,
               "datestamp": datestamp}
    response = requests.post(validation_endpoint, json=payload)


def main():
    # Get the data from the endpoint as a json dict
    data_dict = getData()
    dstamp = data_dict["datestamp"]
    secs = data_dict["interval"]

    # Add the interval to the datestamp
    newTime = addTime(dstamp, secs)

    # Send the new datestamp
    sendData(newTime)


if __name__ == '__main__':
    main()
