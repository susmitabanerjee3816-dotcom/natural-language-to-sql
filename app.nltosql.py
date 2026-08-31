import streamlit as st
from openai import OpenAI
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=True)
print("API KEY LOADED:", bool(os.getenv("NVIDIA_API_KEY")))

# Get Gemini API key
API_KEY = st.secrets("NVIDIA_API_KEY")

# Create Gemini client
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = st.secrets["NVIDIA_API_KEY"]
)


# --------------------------------
# Generate SQL prompt
# --------------------------------

def generate_sql_query(user_question):

    prompt = f"""
You are a SQL query generator.

Database: school_db
Table: Student

Columns:
ID, FullName, DOB, Sex, Class, HCode, DCode, Remission, MTest, PTest

Convert the user's question into a MySQL query.

Important:
- Return ONLY the SQL query.
- Do not explain the query.
- Do not use markdown.
- Do not use ```sql or ```.

User question:
{user_question}
"""

    return prompt


# --------------------------------
# Connect to MySQL
# --------------------------------

def connect_to_sql():
    print("CONNECT FUNCTION RUNNING")
    

    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

    print("MYSQL CONNECTED")
    return conn


# --------------------------------
# Streamlit UI
# --------------------------------

st.title("🤖 Natural Language to SQL Agent")

st.write(
    "Ask a question about the Student database in normal English."
)

user_question = st.text_input(
    "Enter your question:"
)


# --------------------------------
# Generate SQL and execute
# --------------------------------

if st.button("Generate SQL"):

    if user_question:

        # Generate prompt
        prompt = generate_sql_query(user_question)

        # Ask Gemini
        response = client.chat.completions.create(
    model="poolside/laguna-xs-2.1",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

        # Get SQL
        sql_query = response.choices[0].message.content.strip()

        # Remove markdown formatting
        sql_query = (
            sql_query
            .replace("```sql", "")
            .replace("```", "")
            .strip()
        )

        # Display SQL
        st.subheader("Generated SQL")
        st.code(sql_query, language="sql")

        # Connect to MySQL
        conn = connect_to_sql()
        cursor = conn.cursor()

        # Execute SQL
        cursor.execute(sql_query)

        # Get results
        results = cursor.fetchall()

        # Display results
        st.subheader("Results")

        for row in results:
            st.write(row)

        # Close connection
        cursor.close()
        conn.close()

    else:

        st.warning("Please enter a question.")
