import streamlit as st
import snowflake.connector
import pandas as pd
import requests as rq
from openai import OpenAI
from prompts import get_system_prompt


SCHEMA_PATH="snowflake_sample_data.tpch_sf1"
QUALIFIED_TABLE_NAME = f"{SCHEMA_PATH}.lineitem"
vcontext= "Act as Data Engineer and convert to sql query"



# Logic to convert Natural Language into SQL
def func_return_query(vStr):
    client = OpenAI(api_key="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") # Add API Key
    #client = OpenAI(api_key=st.secrets.OPENAI_API_KEY)
    
    return vStr

st.title("Hello - Please ask question to Snowflake Database")
st.text("Sample - select * from snowflake_sample_data.tpch_sf1.lineitem limit 5")
question = st.text_input("Ask your question")


if st.button("Ask"):    
    # API to convert Natural language to SQL
    st.text(question)
    #st.session_state.messages = [{"role": "system", "content": get_system_prompt()}]
    
    st.session_state.messages = [{"role": "system", "content": vcontext}]
    st.session_state.messages.append({"role": "user", "content": question})
    
    for msg in st.session_state.messages:
       st.text(msg)

    # for message in st.session_state.messages:
    #     if message["role"] == "system":
    #         continue
    #     with st.chat_message(message["role"]):
    #         st.write(message["content"])
    #         if "results" in message:
    #             st.dataframe(message["results"])
    
    
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
    
