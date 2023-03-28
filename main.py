import time
import os
import re
import pytz
from datetime import datetime

def main():

    # replace content between `---start` and `---end`
    # pytz.timezone('Asia/Shanghai')).strftime('%Y年%m月%d日%H时M分')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    insert_info = "---start---\nDaily update via Github Actions(" + datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S') + ")" + "\n---end---"
    
    # update README.md
    with open (os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()

    # print(readme_md_content)
    # print(insert_info)

    new_readme_md_content = re.sub(r'---start(.|\n)*---end', insert_info, readme_md_content)

    print(new_readme_md_content)

    with open (os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)

main()
