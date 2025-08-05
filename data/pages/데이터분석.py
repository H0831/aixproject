import streamlit as st
import plotly.express as px
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Student Grades Dashboard", layout="wide")

# Data
data = {
    'name': ['lee', 'park', 'kim'],
    'grade': [2, 2, 2],
    'number': [1, 2, 3],
    'kor': [90, 88, 99],
    'eng': [91, 89, 99],
    'math': [81, 77, 99],
    'info': [100, 100, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# App title
st.title("Student Grades Dashboard")

# Sidebar for chart selection
st.sidebar.header("Chart Options")
chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Radar Chart", "Box Plot"])

# Main content
st.header("Student Performance Analysis")

# Display raw data
st.subheader("Raw Data")
st.dataframe(df)

# Chart 1: Bar Chart
if chart_type == "Bar Chart":
    fig = px.bar(
        df,
        x='name',
        y=['kor', 'eng', 'math', 'info'],
        barmode='group',
        title="Student Grades by Subject",
        labels={'value': 'Score', 'name': 'Student Name', 'variable': 'Subject'}
    )
    st.plotly_chart(fig, use_container_width=True)

# Chart 2: Line Chart
elif chart_type == "Line Chart":
    fig = px.line(
        df,
        x='name',
        y=['kor', 'eng', 'math', 'info'],
        title="Student Grades Trend",
        labels={'value': 'Score', 'name': 'Student Name', 'variable': 'Subject'},
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

# Chart 3: Radar Chart
elif chart_type == "Radar Chart":
    # Transform data for radar chart
    df_melted = df.melt(id_vars=['name'], value_vars=['kor', 'eng', 'math', 'info'], 
                        var_name='subject', value_name='score')
    fig = px.line_polar(
        df_melted,
        r='score',
        theta='subject',
        color='name',
        line_close=True,
        title="Student Performance Radar Chart"
    )
    st.plotly_chart(fig, use_container_width=True)

# Chart 4: Box Plot
elif chart_type == "Box Plot":
    fig = px.box(
        df.melt(id_vars=['name'], value_vars=['kor', 'eng', 'math', 'info'], 
                var_name='subject', value_name='score'),
        x='subject',
        y='score',
        color='name',
        title="Distribution of Scores by Subject",
        labels={'score': 'Score', 'subject': 'Subject'}
    )
    st.plotly_chart(fig, use_container_width=True)

# Statistics
st.subheader("Basic Statistics")
st.write(df[['kor', 'eng', 'math', 'info']].describe())

# Individual student selection
st.subheader("Individual Student Analysis")
selected_student = st.selectbox("Select Student", df['name'])
student_data = df[df['name'] == selected_student][['kor', 'eng', 'math', 'info']]
st.bar_chart(student_data)