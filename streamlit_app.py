import streamlit as st
import snowflake.connector
import pandas as pd
import requests as rq
from openai import OpenAI

# Logic to convert Natural Language into SQL
def func_return_query(vStr):
    return vStr

st.title("Hello - Please ask question to Snowflake Database")
st.text("Sample - select * from snowflake_sample_data.tpch_sf1.lineitem limit 5")
question = st.text_input("Ask your question")


if st.button("Ask"):    
    st.spinner("Thinking")
    # API to convert Natural language to SQL
    st.text(question)
    st.text("Convert to")
    vSQL= func_return_query(question)
    st.text(vSQL)    
    
    # Execute SQL
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute(vSQL)   # "SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST"
    my_data_row = my_cur.fetchall()

    load_df = pd.DataFrame(my_data_row)
    st.dataframe(load_df)

    my_cnx.close()
    
