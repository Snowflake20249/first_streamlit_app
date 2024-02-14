import streamlit as st
import snowflake.connector
import pandas as pd
import requests as rq

#from frosty import parse_sentence
#import snowpark
#from snowpark.sql import SparkSession


st.title("Hello - Please ask question to Snowflake Database")
question = st.text_input("Ask your question")



if st.button("Ask"):
    # Parse user question
    st.header(question)
    # API to convert Natural language to SQL
    SQL= question

        
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
    my_data_row = my_cur.fetchall()

    load_df = pd.DataFrame(my_data_row)
      #fruit_load_df.rename(columns = {0: 'Fruit Name'},inplace = True)
      #st.header('Fruit Load Contains')
      #st.dataframe(load_df)
    st.dataframe(load_df)



    #parsed_query = parse_sentence(question)
    
    # Convert parsed query to Snowpark compatible SQL
    #snowpark_query = parsed_query.to_sql()
    
    # Execute query in Snowflake
    #result = spark.sql(snowpark_query)
    
    # Display results
   # st.write(result.toPandas())



my_cnx.close()
