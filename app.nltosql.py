import streamlit as st
from openai import OpenAI

# NVIDIA API client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=st.secrets["NVIDIA_API_KEY"]
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
- Do not show your thinking.
- Do not use <think> or </think>.
- Do not use markdown.
- Do not use ```sql or ```.

User question:
{user_question}
"""

    return prompt


# --------------------------------
# Streamlit UI
# --------------------------------

st.title("🤖 Natural Language to SQL Agent")

st.write(
    "Ask a question about the Student database in normal English."
)

user_question = st.text_input("Enter your question:")


# --------------------------------
# Generate SQL
# --------------------------------

if st.button("Generate SQL"):

    if not user_question:

        st.warning("Please enter a question.")

    else:

        prompt = generate_sql_query(user_question)

        try:

            response = client.chat.completions.create(
                model="poolside/laguna-xs-2.1",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            # Get generated response
            sql_query = response.choices[0].message.content

            # Remove thinking tags and markdown
            sql_query = (
                sql_query
                .replace("<think>", "")
                .replace("</think>", "")
                .replace("```sql", "")
                .replace("```", "")
                .strip()
            )

            # If the model repeats the same SQL twice,
            # keep only the first occurrence
            sql_parts = sql_query.split(";")

            if len(sql_parts) > 2:
                first_query = sql_parts[0].strip()

                if first_query:
                    sql_query = first_query + ";"

            # Display SQL
            st.subheader("Generated SQL")
            st.code(sql_query, language="sql")

        except Exception:

            st.error(
                "The AI service is temporarily unavailable. "
                "Please try again later."
            )
