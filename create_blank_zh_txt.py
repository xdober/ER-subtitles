import os
import numpy as np
from py_linq import Enumerable
from pathlib import Path

# 1. 将你的字幕内容保存到一个文件中，例如 'subtitle.ass'

# 2. 设置输入和输出文件名
season='14'

for ep in np.arange(1,22+1):
    output_file = f'S{season}/S{season}E{ep:02}.zh.txt'  # 希望保存结果的文件名
    Path(output_file).touch()

    # 你也可以直接打印结果而不是保存到文件
    # from pprint import pprint
    # lines = extract_subtitle_text_list(input_file)
    # if lines:
    #    pprint(lines)