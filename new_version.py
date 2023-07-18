import json;

# 读取 package.json 文件
with open('package.json', 'r',encoding='utf-8') as f:
    jspack = json.load(f)

# 获取当前版本号
current_version = jspack['version']

# 递增版本号
major, minor, patch = map(int, current_version.split('.'))
patch += 1
new_version = f"{major}.{minor}.{patch}"

# 更新版本号
jspack['version'] = new_version

# 写入更新后的 package.json 文件
with open('package.json', 'w',encoding='utf-8') as f:
    json.dump(jspack, f,ensure_ascii=False)
