import json;
import time;

with open("package.json", 'r', encoding='utf-8') as f:
    jspack = json.load(f)

new_version = '1.1.' + str(int(time.time()))[1:11:1]
hort_version = new_version[:5]  # 截取前 5 个字符
jspack['version'] = hort_version
with open("package.json", 'w', encoding='utf-8') as f:
    json.dump(jspack, f, ensure_ascii=False)
