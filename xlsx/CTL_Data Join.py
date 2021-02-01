import pandas as pd

# 판다스 크기 키우기
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

PATH = './data/'

Full = PATH + 'Full_Join.xlsx'
grade = PATH + 'grade.xlsx'

# print(Full)
# print(grade)

Full_data_pd = pd.read_excel(Full, index_col=None, names=None)

print(Full_data_pd)

# 시작은 1번부터
print(Full_data_pd.iloc[1])
print(Full_data_pd.iloc[1, 9])

grade_data_pd = pd.read_excel(grade, index_col=None, names=None)

print(grade_data_pd)

# 데이터 프레임
print(type(grade_data_pd.iloc[[0]]))
# 시리즈
print(type(grade_data_pd.iloc[0]))
print("\n")

# 타입 확인
print(Full_data_pd.dtypes)
print(grade_data_pd.dtypes)
print("\n")
# print(Full_data_pd.astype({'stu_num':'int'}).dtypes)
# print(pd.to_numeric(Full_data_pd.stu_num, errors='coerce'))

# print(Full_data_pd['stu_num'].astype(str))
# Full_data_pd[['stu_num']] = Full_data_pd[['stu_num']].apply(pd.to_numeric)
# Full_data_pd['stu_num_2'] = pd.to_numeric(Full_data_pd['stu_num']).fillna(0)
# print(pd.to_numeric(Full_data_pd['stu_num'], errors='coerce').fillna(0))
# print(Full_data_pd['stu_num'].astype(int).fillna(0))
# Full_data_pd['stu_num'].fillna(0, inplace=True)
# print(Full_data_pd.dtypes)
# print(Full_data_pd)
# print("\n")
# Full_data_pd['stu_num'].astype(int)
# print(Full_data_pd.dtypes)
# print(Full_data_pd)
# print("\n")


grade_std_num_pd = grade_data_pd['hakbun']
Full_std_num_pd = Full_data_pd['stu_num']

count = 0
for i, grade_std_num in enumerate(grade_std_num_pd):
    for j, Full_std_num in enumerate(Full_std_num_pd):
        if (grade_std_num == Full_std_num):
            test = grade_data_pd.iloc[i, 3:]
            # print(test)
            count = count + 1
            # print(Full_data_pd.iloc[j, 10])
            # 데이터 집어넣기
            Full_data_pd.iloc[j, 11] = grade_data_pd.iloc[i, 3]
            Full_data_pd.iloc[j, 12] = grade_data_pd.iloc[i, 4]
            Full_data_pd.iloc[j, 13] = grade_data_pd.iloc[i, 5]
            Full_data_pd.iloc[j, 14] = grade_data_pd.iloc[i, 6]
            Full_data_pd.iloc[j, 15] = grade_data_pd.iloc[i, 7]
            Full_data_pd.iloc[j, 16] = grade_data_pd.iloc[i, 8]

            print(Full_data_pd.iloc[j,])
            print('\n')

            # print(grade_data_pd.iloc[1, ['avg_2018_1',
            #                           'avg_2018_2',
            #                           'avg_2019_1',
            #                           'avg_2019_2',
            #                           'avg_2020_1',
            #                           'avg_2020_2']])

print(count)

Full_data_pd.to_excel('test_Full_join.xlsx')