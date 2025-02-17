
* __功能一__：统计卷面成绩中各题型分值情况，如最高分、最低分和平均分。

  输入文件格式要求：该文件中的数据为从试卷分析工作簿的第二个工作表“考试成绩表”中复制，并选择性粘贴“仅数值”得来；

  参考模板：examples/算法卷面成绩2021.csv
* __功能二__：统计期末成绩和总评成绩的各分数段分布情况。

  输入文件格式要求：工作表组成列为：前两列为姓名学号，第三列开始放成绩(没有可以空着或者删除），但保持期末考核成绩列名为“**总分**”，最终考核成绩列为“**学期总成绩**”即可。

  参考模板：examples/test.csv

  **环境要求：**

  - Python 3.10+
  - Streamlit
  - Pandas
  
  **使用方法：**

  1. 下载本项目到本地，然后打开命令行工具，进入本项目的根目录；
  2. 准备好待分析的文件（文件格式要求见上述功能说明部分），将其放置到本项目的根目录；
  3. 执行命令：`streamlit run student_grade_analysis-V1.py`
