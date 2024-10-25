import requests


# Set up the API URL
url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/lirr%2Fgtfs-lirr"

# Make the GET request to the MTA API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Process the binary protobuf data
    data = response.content
    print(data)  # Print or decode as needed
else:
    # Handle errors
    print("Request failed:", response.status_code, response.text)
