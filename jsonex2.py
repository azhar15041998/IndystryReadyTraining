import json
with open("large_file.json",encoding='utf-8') as f:
    s = f.read()
    d = json.loads(s)
print(d)