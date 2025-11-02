import streamlit as st

st.title("🎯 我的第一个 Streamlit 应用")

file = st.file_uploader("上传你的文件（例如 FASTQ 或 CSV）")

if file:
    st.write("✅ 文件已上传：", file.name)
    st.write("🔍 正在分析中...")
    st.success("分析完成！")
