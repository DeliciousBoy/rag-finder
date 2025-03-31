import streamlit as st
import json
from pathlib import Path
import pandas as pd

FILE = Path("src/knowledgbase/Fantastic_Beasts_and_Where_to_Find_Them.json")

# โหลด JSON จากไฟล์
with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)
# แสดงข้อมูล JSON ใน Streamlit
st.dataframe(data=data, width=900, height=500)
