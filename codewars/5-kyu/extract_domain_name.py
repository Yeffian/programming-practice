import re

def domain_name(url):
    part = ''

    if re.search(r'//', url):
        parts = url.split(r'//')
        part = parts[1]
    else:
        part = url

    if re.search("www.", part):
        part = part.replace('www.', '')

    return part.split('.')[0]

print(domain_name("www.xakep.ru"))