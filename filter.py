import pandas as pd
import numpy as np
import pingouin as pg

def flt_data():
    df = pd.read_excel('questionarie0524.xlsx')

    idx_ques_dict = {}
    for idx, ques in enumerate(df.columns):
        idx_ques_dict[idx] = ques

    df.columns = [*range(0, len(df.columns))]

    reverse_dict = {1.0:7.0, 2.0:6.0, 3.0:5.0, 4.0:4.0, 5.0:3.0, 6.0:2.0, 7.0:1.0}

    effective = df.loc[(df[1] == '是') & (df[18] == 3)]

    for i in range(len(effective)):
        effective.iloc[i, 26] = reverse_dict[effective.iloc[i, 26]]


    effective.to_excel('effective.xlsx', index=False)
    pass

def analysis():
    effective_df = pd.read_excel('effective.xlsx')
    factor0 = [6,7,8,10,11,12,13,14,15,19,20]
    factor1 = [22,23,24]

    factor0_df = effective_df.iloc[:, factor0]
    factor1_df = effective_df.iloc[:, factor1]

    factor0_avg_df = factor0_df.mean(axis=1)
    factor1_avg_df = factor1_df.mean(axis=1)

    ys = effective_df.iloc[:, 28:31]
    ys_avg_df = ys.mean(axis=1)

    xy_df = pd.concat([factor0_avg_df, factor1_avg_df, ys_avg_df], axis=1)
    xy_df.columns = ['x0_avg', 'x1_avg', 'y_avg']
    xy_df.to_excel('xy_regression_input.xlsx', index=False)

    pass



if __name__ == '__main__':
    analysis()