import pandas as pd
import glob


df = pd.DataFrame()
data_paths = glob.glob('./crawling_data/*')

#
# for i in range(1, 44):
#     df_temp = pd.read_csv('./crawling_data/reviews_2019_{}page.csv'.format(i))
#     df_temp.dropna(inplace=True)
#     df_temp.drop_duplicates(inplace=True)
#     df=pd.concat([df,df_temp], ignore_index=True)
# df.drop_duplicates(inplace=True)
for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df=pd.concat([df,df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df.info()
df.to_csv('./crawling_data/naver_comments_1300_501_page.csv', index=False)
# naver_comments_{}_{}_page.csv'.format(end_page, i)