import requests
from lxml import html

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

headers = {
    'User-Agent': user_agent
}

url = "https://www.linkedin.com/jobs/search?keywords=Desarrollo%20De%20Software&location=Spain"

response = requests.get(url, headers=headers)

parser: html.HtmlElement = html.fromstring(response.text)
# using xpath to get the elements
elements = parser.xpath("//h3[@class='base-search-card__title']")
print("length of tags: ", len(elements))
for element in elements:
    if "Clases" in element.text_content():
        elements.remove(element)

print("Without 'Clases': ", len(elements))

for i, element in enumerate(elements):
    # get the text of the tag in a single line
    print("-",i, element.text_content().strip())