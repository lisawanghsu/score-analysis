import streamlit as st
import pandas as pd

st.title("期末成绩统计工具箱")
st.markdown(
   '''

* __功能一__：统计卷面成绩中各题型分值情况，如最高分、最低分和平均分。支持上传成绩文件或手动输入成绩数据。  
  输入文件格式要求：该文件中的数据为从试卷分析工作簿的第二个工作表“考试成绩表”中复制，并选择性粘贴“仅数值”得来；  
  参考模板：examples/算法卷面成绩2021.csv 
  |选择题|	填空题|	简答题|	算法设计与分析题|					总分|
  |:--:|:--:|:--:|:--:|:--:|
  |27	|20	|8	|6	|61|
  |24	|30	|5	|9	|68|
  |24	|24	|5	|4	|57|
  |24	|24	|5	|4	|54|
 
* __功能二__：统计期末成绩和总评成绩的各分数段分布情况。  
  输入文件格式要求：工作表组成列为：前两列为姓名学号，第三列开始放成绩(没有可以空着或者删除），但保持期末考核成绩列名为“**总分**”，最终考核成绩列为“**学期总成绩**”即可。  
  参考模板：examples/test.csv
  |总分|	学期总成绩|
  |:--:|:--:|
  |61	|61|
  |68	|68|
  |57	|57|
  |57	|57|
  |54	|47|
**Note**：上述功能均支持通过手动复制成绩表格中的数据到输入框。成绩数据格式要求：每行代表一条记录，首行为所需列标题，列之间用tab键分隔。   
  ''' 
)

def calculate_grade_distribution(df, column_name):
    '''
    计算指定列的各分数段分布情况
    :param df: 包含成绩数据的DataFrame
    :param column_name: 要计算的列名
    :return: 各分数段的计数器列表
    '''
    
    # 初始化各分数段的计数器
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


def manual_input(key=1):
    '''
    # 新增代码：接受用户输入的多行文本数据并解析成二维表格数据
    '''
    st.subheader("手动输入成绩数据")
    text_input = st.text_area("请输入成绩数据（每行代表一条记录，首行为所需列标题，列之间用tab键分隔）",key=key)
    if text_input:
        # 将输入的文本数据按行分割
        lines = text_input.split("\n")
        # st.write(lines)
        # 提取第一行作为列标题
        headers = [x for x in lines[0].split("\t") if x]
        # st.write(headers)
        # 解析剩余行作为数据
        data = [[float(xx) for xx in line.split("\t") if xx] for line in lines[1:]]
        # 创建DataFrame
        df = pd.DataFrame(data, columns=headers)
        st.write("手动输入的成绩数据核对：",'待确认人数：',len(data))
        st.write(df)
        return df

    
st.header("功能一：卷面成绩分析")

# 上传卷面成绩文件·
st.subheader("请上传卷面成绩文件")
uploaded_file = st.file_uploader("选择卷面成绩文件（CSV格式）", type="csv")
if uploaded_file is not None:
    header = st.selectbox('选择第几行为表格标题行（一般为第0行）', list(range(5)),key=1)
    
    df = pd.read_csv(uploaded_file, header=header, encoding='gbk')
    st.write("文件预览：")
    st.write(df.head())

    st.write("### 卷面成绩各题型最高分、最低分、平均分统计")
    for questiontype in df.columns[0:]:
        if questiontype[:2] != 'Un':
            st.write(f"{questiontype}最高分为：{df[questiontype].max()}，最低分为：{df[questiontype].min()}，平均分为：{df[questiontype].mean().round(1)}")

# 手动输入卷面成绩
df = manual_input()
st.write("### 各题型最高分、最低分、平均分统计")
for questiontype in df.columns[0:]:
    st.write(f"{questiontype}最高分为：{df[questiontype].max()}，最低分为：{df[questiontype].min()}，平均分为：{df[questiontype].mean().round(1)}")

st.markdown('---')

st.header("功能二：期末和总评成绩分析")

# 上传期末成绩和总评成绩文件
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

# 手动输入期末成绩和总评成绩
df = manual_input(key=2)
for i in df.columns:
    grades = calculate_grade_distribution(df, i)
    st.write(f"{i}各分数段统计如下：")
    levels = '90-100\t80-89\t70-79\t60-69\t50-59\t40-49\t30-39\t20-29\t10-19\t0-9'.split('\t')
    # st.write(pd.DataFrame([levels, grades], index=['分数段', '人数']).T.set_index('分数段'))
    st.write(pd.DataFrame([grades], columns=levels, index=['人数']))        

