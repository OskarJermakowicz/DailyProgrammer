import time
import urllib.request
import bs4
import re

def find_philosophy(subject):
    path = []
    while subject != "Philosophy":
        path.append(subject)

        req = urllib.request.Request("http://en.wikipedia.org/wiki/" + subject)
        content = urllib.request.urlopen(req).read()
        soup = bs4.BeautifulSoup(strip_brackets(content.decode()).encode(), "html.parser")

        subject = find_next_subject(soup.findAll("div", {"class": "mw-parser-output"})[0].findAll('p'))

        if subject == '__n/a__':
            path.append("No more links found at subject: " + path[len(path)-1])
            return path

        if subject in path:
            path.append("Loop found at subject: " + subject + " in " + path[len(path)-1])
            return path

    return path

def find_next_subject(s):
    for paragraph in s:
        for link in paragraph.findAll("a"):
            if not link.get("href").startswith('#') and not link.get("href").startswith('//') and ":" not in link.get("href"):
                return link.get("href")[6:]
    return '__n/a__'


# Strips all brackets, including nested brackets in a String. Brackets that are preceded directly by an underscore are not stripped.
def strip_brackets(text):
    while True:
        text_new = re.sub(r'(?<!_)\([^\(]*?\)', r'', text)
        if text_new == text:
            break
        text = text_new
    return text

start_time = time.time()
print("Enter a starting article:")
for subject in find_philosophy(input()): print(subject)
print("\nExecution time: %s seconds" % (time.time() - start_time))