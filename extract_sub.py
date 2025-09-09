import os
import numpy as np
from py_linq import Enumerable

def extract_subtitle_text(input_filepath, output_filepath):
    """
    从 .ass 字幕文件中提取对话文本。

    参数:
    input_filepath (str): 输入的 .ass 文件路径。
    output_filepath (str): 输出的纯文本文件路径。
    """
    extracted_lines = []
    try:
        # 使用 utf-8 编码打开文件，以兼容多种语言
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            for line in infile:
                # 检查该行是否是对话行
                if line.strip().startswith('Dialogue:'):
                    # 对话内容是第9个逗号之后的所有部分
                    # 使用 split(',', 9) 可以保证只分割前9次，避免对话中的逗号影响
                    dialogue_text = line.split(',', 9)[-1].strip()
                    # 2. (新功能) 替换掉 "\N" 字符，这里替换为空格以保持可读性
                    cleaned_text = dialogue_text.replace('\\N', ' ')
                    extracted_lines.append(cleaned_text)

        # 将提取的内容写入新文件
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            for line in extracted_lines:
                outfile.write(line + '\n')

        print(f"处理完成！字幕内容已保存到: {output_filepath}")

    except FileNotFoundError:
        print(f"错误: 文件 '{input_filepath}' 未找到。")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")


# --- 如何使用 ---

# 1. 将你的字幕内容保存到一个文件中，例如 'subtitle.ass'

# 2. 设置输入和输出文件名
season='15'
file_path=f'/Volumes/desktop-jnjl486/downloads/pt/movie/ER(1994)/ER (1994) S{season} 1080p WEBRip 10bit EAC3 2 0 x265-iVy/'
if season == '15':
    file_path = f'/Volumes/desktop-jnjl486/downloads/pt/movie/ER(1994)/ER (1994) S{season} 1080p WEBRip 10bit EAC3 5 1 x265-iVy/'
if not os.path.exists(f'S{season}'):
    os.makedirs(f'S{season}')

all_files = os.listdir(file_path)
ass_files = Enumerable([x for x in all_files if x.endswith('[eng].ass')])
print(len(ass_files))
for ep in np.arange(1,22+1):
    print(f"extract_subtitle_text: {ep:02}")
    dist_files = ass_files.where(lambda x: f'S{season}E{ep:02}' in x)
    # print(f"dist_files: {len(dist_files)}")
    dist_file = ass_files.first(lambda x: f'S{season}E{ep:02}' in x)
    print(f"dist_file: {dist_file}")
    # print(f"dist_files: {len(dist_files)}")
    full_path=os.path.join(file_path,dist_files.first())
    output_file = f'S{season}/ER.S{season}E{ep:02}.Dialogue.txt'  # 希望保存结果的文件名

    # 3. 运行函数
    extract_subtitle_text(full_path, output_file)

    # 你也可以直接打印结果而不是保存到文件
    # from pprint import pprint
    # lines = extract_subtitle_text_list(input_file)
    # if lines:
    #    pprint(lines)