import os
import numpy as np
from py_linq import Enumerable

def make_subtitle_text(input_filepath, dialogue_zh_path, output_filepath):
    """
    从 .ass 字幕文件中提取对话文本。

    参数:
    input_filepath (str): 输入的 .ass 文件路径。
    output_filepath (str): 输出的纯文本文件路径。
    """
    lines_to_write = []
    try:
        zh_lines = []
        with open(dialogue_zh_path, 'r', encoding='utf-8') as dialogue_zh_text:
            for line in dialogue_zh_text:
                zh_lines.append(line)
        print(f'read zh done')
        # 使用 utf-8 编码打开文件，以兼容多种语言
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            cnt = 0
            for line in infile:
                head, sep, tail = line.strip().partition('Default,,0,0,0,,')
                if sep:
                    new_line = head + sep + zh_lines[cnt].strip() + '\\N' + tail
                    cnt += 1
                else:
                    new_line = line
                lines_to_write.append(new_line)
        print(f'merge zh done')
        # 将提取的内容写入新文件
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            for line in lines_to_write:
                outfile.write(line+'\n')

        print(f"处理完成！字幕内容已保存到: {output_filepath}")

    except FileNotFoundError:
        print(f"错误: 文件 '{input_filepath}' 未找到。")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")


# --- 如何使用 ---

# 1. 将你的字幕内容保存到一个文件中，例如 'subtitle.ass'

# 2. 设置输入和输出文件名
file_path='/Volumes/desktop-jnjl486/downloads/pt/movie/ER(1994)/ER (1994) S05 1080p WEBRip 10bit EAC3 2 0 x265-iVy/'

all_files = os.listdir(file_path)
# print(len(ass_files))
for ep in [5,6]:
    ass_files = Enumerable([x for x in all_files if x.endswith('[eng].ass')])
    dialogue_zh=f'ER.S05E{ep:02}.Dialogue.zh.txt'
    print(f"extract_subtitle_text: {ep:02}")
    dist_file = ass_files.first(lambda x: f'S05E{ep:02}' in x)
    # print(f"dist_files: {len(dist_files)}")
    # dist_file = dist_files.first()
    print(f"dist_file: {dist_file}")
    # print(f"dist_files: {len(dist_files)}")
    full_path=os.path.join(file_path,dist_file)
    output_file = str.replace(dist_file,'[eng]','')  # 希望保存结果的文件名

    # 3. 运行函数
    make_subtitle_text(full_path, dialogue_zh, output_file)
