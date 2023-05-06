import os

def generate_summary(path):
    summary = "# 目录\n\n"
    for root, dirs, files in os.walk(path):
        # 忽略隐藏的目录
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        level = root.replace(path, '').count(os.sep)
        indent = '  ' * level
        summary += f"{indent}* [{os.path.basename(root)}]({root}/README.md)\n"
        for file in files:
            if file.endswith(".md"):
                summary += f"{indent}  * [{os.path.splitext(file)[0]}]({os.path.join(root, file)})\n"
    with open("SUMMARY.md", "w", encoding="utf-8") as file:
        file.write(summary)

generate_summary(".")

