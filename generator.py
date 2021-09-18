import hashlib


def md5_hash():
    with open('countries.json', encoding='utf8') as read_file:
        for line in read_file:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


for hash in md5_hash():
        print(hash)
