import requests

# url = "https://bbc.co.uk"
# url = "https://undergraduate.degrees.ed.ac.uk/"
#
# response = requests.get(url)
# print(response)
#
# if response.status_code == 200:
#     print("Page fetched successfully.")
#     print(response.content[:500])
# else:
#     print(f"Failed to fetch page")
#
api_url = "https://swapi.dev/api/people"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    # print(data["results"][0]["name"])
    for person in data["results"]:
        print(person["name"])