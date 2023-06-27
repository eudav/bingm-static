import json

# 读取 package.json 文件
with open('package.json', 'r') as file:
    data = json.load(file)

# 获取当前版本号
current_version = data['version']

# 递增版本号
major, minor, patch = map(int, current_version.split('.'))
patch += 1
new_version = f"{major}.{minor}.{patch}"

# 更新版本号
data['version'] = new_version

# 写入更新后的 package.json 文件
with open('package.json', 'w') as file:
    json.dump(data, file, indent=4)
