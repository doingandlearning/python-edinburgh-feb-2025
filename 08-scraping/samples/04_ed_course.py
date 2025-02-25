import os
import requests
from bs4 import BeautifulSoup

url = "https://undergraduate.degrees.ed.ac.uk/"
html_file_path = "undergrad_degrees.html"


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
        print(soup.title.string)
        subjects_data = []

        # Find all anchor tags within the specified divs
        for a_tag in soup.find_all("a", class_="list-group-item"):
            # Extract the subject name, which is the text after the span
            subject_name = a_tag.contents[1].strip()

            # Extract the number of courses from the span
            no_of_courses = a_tag.find("span", class_="badge pull-right").text.strip()

            # Append the extracted data to the list as a dictionary
            subjects_data.append(
                {
                    "subject": subject_name,
                    "no_of_courses": no_of_courses,
                    "href": a_tag["href"],
                }
            )

        return subjects_data


if __name__ == "__main__":
    if not os.path.exists(html_file_path):
        fetch_and_save_html(url, html_file_path)

    subjects_data = parse_html(html_file_path)

    # Output the extracted data
    for item in subjects_data:
        print(item)
