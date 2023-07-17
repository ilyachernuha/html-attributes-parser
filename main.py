from requests import get
from bs4 import BeautifulSoup
from json import dumps

from settings import settings

def get_tags(url, headers, tag):
    res = get(url=url, headers=headers)
    content = res.content
    soup = BeautifulSoup(content, "html.parser")
    soup.prettify()
    return soup.find_all(tag)

def get_elements(tags, attributes):
    elements = []
    for tag in tags:
        element = {}
        for attribute in attributes:
            element[attribute] = tag.get(attribute)
        elements.append(element)
    return elements

def main():
    url = settings["url"]
    headers = settings["headers"]
    tag = settings["tag"]
    attributes = settings["attributes"]
    tags = get_tags(url, headers, tag)
    print(tags)
    elements = get_elements(tags, attributes)
    json_elements = dumps(elements, indent=4)
    with open("elements.json", "w") as outfile:
        outfile.write(json_elements)

if __name__ == '__main__':
    main()