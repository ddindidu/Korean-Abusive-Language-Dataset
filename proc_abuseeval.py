import pandas as pd
import os

file_path_in = "./../processed_data/AbuseEval"
file_name_in = ["train.csv", "valid.csv", 'test.csv']

tr_file_path = './../translated_data/AbuseEval'
tr_file_name = ['train_en2ko.csv', 'valid_en2ko.csv', 'test_en2ko.csv']

save_path = './AbuseEval'
save_name = ['train', 'valid', 'test']


def file_checker(path):
    if not os.path.exists(path):
        raise(FileNotFoundError("File doesn't exist: {}".format(path)))


def set_class(df):
    if df['Target'] == 0:
        return 'NOTABU'
    elif df['Target'] == 1:
        return 'EXP'
    elif df['Target'] == 2:
        return 'IMP'
    else:
        return None


def set_target(df):
    # non 0
    # abu 1
    if df['abuse'] == 'NOTABU':
        return '0'
    else:
        return '1'


if __name__ == "__main__":
    for ind in range(len(file_name_in)):
        origin_path = os.path.join(file_path_in, file_name_in[ind])
        file_checker(origin_path)
        translation_path = os.path.join(tr_file_path, tr_file_name[ind])
        file_checker(translation_path)

        origin_df = pd.read_csv(origin_path)    # [Id, Context=Nan, Comment, Target 0 1 2]
        trans_df = pd.read_csv(translation_path)    # [      same          ]

        #print(origin_df.loc[0])

        origin_df['abuse'] = origin_df.apply(set_class, axis=1)
        origin_df['Target'] = origin_df.apply(set_target, axis=1)   # [Id, Context, Comment, abuse, Target]

        merged_df = pd.merge(origin_df[['Id', 'abuse', 'Target']], trans_df[['Id', 'Context', 'Comment']], on='Id', how='inner')

        merged_df['Dataset'] = "AbuseEval"
        merged_df['Context'] = ""

        merged_df = merged_df[['Dataset', 'Id', 'Context', 'Comment', 'Target', 'abuse']]

        save_file_name = os.path.join(save_path, 'origin_{}.csv'.format(save_name[ind]))
        merged_df.to_csv(save_file_name, index=False)

        new_df = merged_df[['Dataset', 'Id', 'Context', 'Comment', 'Target']]
        save_file_name = os.path.join(save_path, 'model_{}.csv'.format(save_name[ind]))
        new_df.to_csv(save_file_name, index=False)
        