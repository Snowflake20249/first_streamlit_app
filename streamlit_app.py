import streamlit as st
import snowflake.connector
#from frosty import parse_sentence
#import snowpark
#from snowpark.sql import SparkSession


st.title("Hello - Please ask question to Snowflake Database")
question = st.text_input("Ask your question")

if st.button("Ask"):
    # Parse user question
    st.header(question)
    #parsed_query = parse_sentence(question)
    
    # Convert parsed query to Snowpark compatible SQL
    #snowpark_query = parsed_query.to_sql()
    
    # Execute query in Snowflake
    #result = spark.sql(snowpark_query)
    
    # Display results
   # st.write(result.toPandas())
