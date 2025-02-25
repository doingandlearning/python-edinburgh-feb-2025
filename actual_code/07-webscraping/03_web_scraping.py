import requests
from bs4 import BeautifulSoup
import csv
url = "https://undergraduate.degrees.ed.ac.uk/"
file_path = "undergrad_degrees.html"

def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def fetch_and_save_html(url, file_path):
    html_content = get_html_content(url)
    if html_content:
        with open(file_path, "wb") as file:
            file.write(html_content)
        print("Page fetched and saved successfully.")
    else:
        print("Failed to fetch page")

def parse_html(file_path):
    with open(file_path, "rb") as file:
        soup = BeautifulSoup(file, "html.parser")
        subjects_data = []
        for a_tag in soup.find_all("a", class_="list-group-item"):
            subject_name = a_tag.contents[1].strip()
            no_of_courses = a_tag.find("span").text.strip()
            href = f'{url}{a_tag["href"]}'
            subjects_data.append({
                "subject_name": subject_name,
                "no_of_courses": no_of_courses,
                "href": href
            })

        return subjects_data

if __name__ == "__main__":
    # fetch_and_save_html(url, file_path)
    data = parse_html(file_path)
    with open("courses.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["subject_name", "no_of_courses", "href"])
        writer.writeheader()
        for course in data:
            writer.writerow(course)