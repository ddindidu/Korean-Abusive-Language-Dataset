import pandas as pd
import os


file_path_in = "./../raw_data/CADD_dataset/CADD"
file_name_in = ["CADD_train.csv", "CADD_dev.csv", "CADD_test.csv"]

tr_file_path = './../translated_data/CADD'
tr_file_name = ['train_en2ko.csv', 'valid_en2ko.csv', 'test_en2ko.csv']

save_path = './CADD'
save_name = ['train', 'valid', 'test']


def file_checker(path):
    if not os.path.exists(path):
        raise(FileNotFoundError("File doesn't exist: {}".format(path)))


def set_target(df):
    # non 0
    # abu 1
    if df['L.Abusive'] == 0:
        return '0'
    else:
        return '1'


if __name__ == "__main__":
    for ind in range(len(file_name_in)):
        origin_path = os.path.join(file_path_in, file_name_in[ind])
        file_checker(origin_path)
        translation_path = os.path.join(tr_file_path, tr_file_name[ind])
        file_checker(translation_path)

        origin_df = pd.read_csv(origin_path, sep=',', encoding='latin_1')
        trans_df = pd.read_csv(translation_path)

        #print(origin_df.columns); print(trans_df.columns)

        # print(len(origin_df), len(trans_df))

        merged_df = pd.merge(origin_df, trans_df, on='Id', how='inner')

        merged_df['Dataset'] = "CADD"
        merged_df['Target'] = merged_df.apply(set_target, axis=1)

        merged_df = merged_df[['Dataset', 'Id', 'Context', 'Comment_y', 'Target',
                               'L.Type', 'L.Abusive', 'lAttack', 'L.Dem', 'L.Implicit', 'L.Profanity', 'lenComment', 'lenContext']]
        merged_df.columns = ['Dataset', 'Id', 'Context', 'Comment', 'Target',
                              'L.Type', 'L.Abusive', 'lAttack', 'L.Dem', 'L.Implicit', 'L.Profanity', 'lenComment', 'lenContext']

        save_file_name = os.path.join(save_path, 'origin_{}.csv'.format(save_name[ind]))
        merged_df.to_csv(save_file_name, index=False)

        new_df = merged_df[['Dataset', 'Id', 'Context', 'Comment', 'Target']]
        save_file_name = os.path.join(save_path, 'model_{}.csv'.format(save_name[ind]))
        new_df.to_csv(save_file_name, index=False)
        
        #print(merged_df.columns, len(merged_df))
        #print(merged_df.loc[0])

        #break
        '''
        df['Context'] = df['Title'] + " " + df['Body']
        df['Target'] = df.apply(set_target, axis=1)
        #print(df.columns)

        # drop if target==nan because of dataset error
        df = df.dropna()

        newdf = df[['Id', 'Context', 'Comment', 'Target']]

        write_path = ""
        if os.path.exists(file_path_out):
            write_path = os.path.join(file_path_out, file_n_out)
            print("out file path: %s" % write_path)
        else:
            print("invalid out file path")
            exit()

        newdf.to_csv(write_path, index=False)
        print("Write the file successfully: %s\n"%file_n_out)
        '''
