import re


def find_wiki_links(content: str):
    regex = r"\[\[(.*?)\]\]"
    matches = re.findall(regex, content, re.MULTILINE | re.IGNORECASE)
    return matches
