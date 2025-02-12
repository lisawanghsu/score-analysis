import streamlit as st
import pandas as pd

st.title("期末成绩统计工具箱")
st.markdown(
   '''

* __功能一__：统计卷面成绩中各题型分值情况，如最高分、最低分和平均分。  
  输入文件格式要求：该文件中的数据为从试卷分析工作簿的第二个工作表“考试成绩表”中复制，并选择性粘贴“仅数值”得来；  
  参考模板：examples/算法卷面成绩2021.csv  
* __功能二__：统计期末成绩和总评成绩的各分数段分布情况。  
  输入文件格式要求：工作表组成列为：前两列为姓名学号，第三列开始放成绩(没有可以空着或者删除），但保持期末考核成绩列名为“**总分**”，最终考核成绩列为“**学期总成绩**”即可。  
  参考模板：examples/test.csv
  ''' 
)

def calculate_grade_distribution(df, column_name):
    grades = [0 for i in range(10)]
    for grade in df[column_name]:
        if grade >= 90:
            grades[0] += 1
        elif grade >= 80:
            grades[1] += 1
        elif grade >= 70:
            grades[2] += 1
        elif grade >= 60:
            grades[3] += 1
        elif grade >= 50:
            grades[4] += 1
        elif grade >= 40:
            grades[5] += 1
        elif grade >= 30:
            grades[6] += 1
        elif grade >= 20:
            grades[7] += 1
        elif grade >= 10:
            grades[8] += 1
        else:
            grades[9] += 1
    return grades


    
st.header("功能一：卷面成绩分析")

uploaded_file = st.file_uploader("选择卷面成绩文件（CSV格式）", type="csv")
if uploaded_file is not None:
    header = st.selectbox('选择第几行为表格标题行（一般为第0行）', list(range(5)),key=1)
    
    df = pd.read_csv(uploaded_file, header=header, encoding='gbk')
    st.write("文件预览：")
    st.write(df.head())

    st.write("### 卷面成绩各题型最高分、最低分、平均分统计")
    for questiontype in df.columns[2:]:
        if questiontype[:2] != 'Un':
            st.write(f"{questiontype}最高分为：{df[questiontype].max()}，最低分为：{df[questiontype].min()}，平均分为：{df[questiontype].mean().round(1)}")

st.markdown('---')
st.header("功能二：期末和总评成绩分析")
uploaded_file = st.file_uploader("选择期末和总评成绩文件（CSV格式）", type="csv")
if uploaded_file is not None:
    header2 = st.selectbox('选择第几行为表格标题行（一般为第0行）', list(range(5)),key=2)
    df = pd.read_csv(uploaded_file, header=header2, encoding='utf-8')
    st.write("文件预览：")
    st.write(df.head())
    st.write("### 卷面总分和学期总评成绩列的分数段")
    for i in ['总分', '学期总成绩']:
        grades = calculate_grade_distribution(df, i)
        st.write(f"{i}各分数段统计如下：")
        levels = '90-100\t80-89\t70-79\t60-69\t50-59\t40-49\t30-39\t20-29\t10-19\t0-9'.split('\t')
        # st.write(pd.DataFrame([levels, grades], index=['分数段', '人数']).T.set_index('分数段'))
        st.write(pd.DataFrame([grades], columns=levels, index=['人数']))
        
        

