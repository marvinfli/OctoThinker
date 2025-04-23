import os
import json
import pandas as pd


fl=os.listdir("/Users/bytedance/Desktop/lxf/projects/o1/projects/octo-thinker/OctoThinker/plot/data/octothinker/1b")

for fn in fl:
    df1=pd.read_csv("/Users/bytedance/Desktop/lxf/projects/o1/projects/octo-thinker/OctoThinker/plot/data/octothinker/1b/"+fn)
    df2=pd.read_csv("/Users/bytedance/Desktop/lxf/projects/o1/projects/octo-thinker/OctoThinker/plot/data/backup/"+fn)

    merge_key = df1.columns[0]

    # 设置索引为合并键
    df1.set_index(merge_key, inplace=True)
    df2.set_index(merge_key, inplace=True)

    # 使用 combine_first 填充空值
    df_merged = df1.combine_first(df2)
    df_merged.reset_index(inplace=True)

    # 保存合并后的结果
    df_merged.to_csv('/Users/bytedance/Desktop/lxf/projects/o1/projects/octo-thinker/OctoThinker/plot/data/octothinker/1b/'+fn, index=False)