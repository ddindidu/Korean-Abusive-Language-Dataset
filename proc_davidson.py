import pandas as pd
import os

file_path_in = "./../processed_data/Davidson"
file_name_in = "Davidson.csv"

tr_file_path = './../translated_data/Davidson'
tr_file_name = 'Davidson_en2ko.csv'

save_path = './Davidson'
save_name = 'Davidson'


def file_checker(path):
    if not os.path.exists(path):
        raise(FileNotFoundError("File doesn't exist: {}".format(path)))


def set_target(df):
    if df['Target'] == 0:
        return '0'
    else:
        return '1'


if __name__=='__main__':
    origin_path = os.path.join(file_path_in, file_name_in)
    file_checker(origin_path)
    translation_path = os.path.join(tr_file_path, tr_file_name)
    file_checker(translation_path)

    origin_df = pd.read_csv(origin_path)  # [Id, Context=Nan, Comment, Target 0 1 2]
    trans_df = pd.read_csv(translation_path)  # [      same          ]

    print(origin_df.columns)
    print(trans_df.columns)

    merged_df = pd.merge(origin_df[['Dataset', 'Id', 'hate_speech', 'offensive_language', 'neither', 'class']],
                         trans_df[['Id', 'Context', 'Comment', 'Target']],
                         on='Id', how='inner')
    merged_df['Target'] = merged_df.apply(set_target, axis=1)
    merged_df['Context'] = ""

    #print(merged_df.loc[0])

    merged_df = merged_df[['Dataset', 'Id', 'Context', 'Comment', 'Target',  'hate_speech', 'offensive_language', 'neither', 'class']]

    save_file_name = os.path.join(save_path, 'origin_{}.csv'.format(save_name))
    merged_df.to_csv(save_file_name, index=False)

    new_df = merged_df[['Dataset', 'Id', 'Context', 'Comment', 'Target']]
    save_file_name = os.path.join(save_path, 'model_{}.csv'.format(save_name))
    new_df.to_csv(save_file_name, index=False)
