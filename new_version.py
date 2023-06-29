import json;

with open("package.json", 'r', encoding='utf-8') as f:
    jspack = json.load(f)

current_version = jspack['version']


major, minor, patch = map(int, current_version.split('.'))
patch += 1
new_version = f"{major}.{minor}.{patch}"

jspack['version'] = new_version

with open("package.json", 'w', encoding='utf-8') as f:
    json.dump(jspack, f, ensure_ascii=False)
