# %%
'''
详见readme.md中说明。
卷面成绩各题型最高分、最低分、平均分统计。
将试卷分析工作簿中的考试卷面成绩表复制选择性粘贴到新建的excel文件，并另存为csv类型。该csv为后续分析的源文件。

1. 仅需要运行时输入待分析的文件名；
2. 该文件中的数据为从试卷分析工作簿的第二个工作表“考试成绩表”中复制，并选择性粘贴“仅数值”得来；
3. 如果是考查课，则将工作表组成列（模板见test.xlsx)为，前两列为姓名学号，第三列开始放成绩(没有可以空着或者删除），但保持考核成绩列名为“总分”，最终考核成绩列为“学期总成绩”即可。
'''
import pandas as pd


filename = input('请输入待分析的文件名称：')
df = pd.read_csv(filename,header=3,encoding='gbk') #该文件的第0，1，2行都是无效数据，因此待处理数据的真正列标题从第3行开始，故在代码中读取excel文件时，需要给header设置为3。
print(df.columns)

# %%
# 计算卷面每种题型、总分、学期总成绩的最高分、最低分和平均分
for questiontype in df.columns[2:]:
    if questiontype[:2] != 'Un':              
        print(f'{questiontype}最高分为：{df[questiontype].max()}，最低分为：{df[questiontype].min()}，平均分为：{df[questiontype].mean().round(1)}')
        
           
        
        
# %%
# 计算卷面总分和学期总成绩列的分数段
# columns='90-100	80-89	70-79	60-69	50-59	40-49	30-39	20-29	10-19	0-9'.split('\t')
# results = pd.DataFrame(index=columns)
for i in df.columns:
    if i in ['总分', '学期总成绩']:
        # 90-100	80-89	70-79	60-69	50-59	40-49	30-39	20-29	10-19	0-9	
        grades = [0 for i in range(10)]  #各分数段人数初始化
        for grade in df[i]:
            if grade >= 90:
                grades[0] += 1
            elif grade >= 80:
                grades[1] += 1
            elif grade >=70:
                grades[2] += 1
            elif grade >= 60:
                grades[3] += 1
            elif grade >=50:
                grades[4] += 1    
            elif grade >= 40:
                grades[5] += 1
            elif grade >= 30:
                grades[6] += 1
            elif grade >= 20:
                grades[7] += 1
            elif grade >=10:
                grades[8] += 1
            else:
                grades[9] += 1
        print(f'{i}各分数段统计如下：')
        print('90-100	80-89	70-79	60-69	50-59	40-49	30-39	20-29	10-19	0-9')
        for i in grades:
            print(i,end='\t')    
        print('')   
    # results =  results.append(pd.Series(grades),ignore_index=True)
   
