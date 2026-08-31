# 🤖 Natural Language to SQL Agent

An AI-powered Natural Language to SQL application that converts plain-English questions into MySQL queries using **NVIDIA's Laguna XS 2.1 model**.

The application provides a simple Streamlit interface where users can ask questions about a Student database in natural language and receive the corresponding SQL query instantly.

## 🚀 Features

* Convert natural-language questions into SQL queries
* Powered by NVIDIA's Laguna XS 2.1 AI model
* OpenAI-compatible API integration
* Interactive Streamlit web interface
* SQL syntax displayed in a readable format
* Secure API key management using Streamlit Secrets
* Removes unwanted AI thinking tags and markdown formatting
* User-friendly error handling

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **OpenAI Python SDK**
* **NVIDIA API**
* **Laguna XS 2.1**
* **MySQL**

## 🔄 How It Works

```text
User Question
      ↓
Streamlit Interface
      ↓
SQL Generation Prompt
      ↓
NVIDIA Laguna XS 2.1
      ↓
Generated MySQL Query
      ↓
SQL Displayed to User
```

## 💡 Example

### User Input

```text
Show all students
```

### Generated SQL

```sql
SELECT * FROM Student;
```

Another example:

### User Input

```text
How many students are there?
```

### Generated SQL

```sql
SELECT COUNT(*) FROM Student;
```

## 📊 Database Schema

The application is designed around the following `Student` table:

| Column    | Description           |
| --------- | --------------------- |
| ID        | Student ID            |
| FullName  | Student's full name   |
| DOB       | Date of birth         |
| Sex       | Gender                |
| Class     | Student's class       |
| HCode     | HCode                 |
| DCode     | DCode                 |
| Remission | Remission information |
| MTest     | MTest score           |
| PTest     | PTest score           |

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd natural-language-to-sql
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the NVIDIA API key

Create your Streamlit secrets configuration and add:

```toml
NVIDIA_API_KEY = "your_nvidia_api_key"
```

**Never commit your actual API key to GitHub.**

### 4. Run the application

```bash
streamlit run app.nltosql.py
```

## 🔐 Security

API credentials are not stored directly in the source code.

The deployed application uses **Streamlit Secrets** to securely store the NVIDIA API key.

The `.env` file, if used for local development, should remain excluded from GitHub.

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

The NVIDIA API key should be added through the application's **Secrets** settings rather than committed to the repository.

## ⚠️ Current Limitation

The public Streamlit version focuses on **Natural Language → SQL generation**.

It does not directly connect to a local MySQL database because a database running on a developer's local machine cannot be accessed by the deployed Streamlit application.

The local development version can be extended to execute the generated SQL against a MySQL database.

## 🔮 Future Improvements

* Connect to a cloud-hosted MySQL database
* Execute generated SQL queries directly
* Display query results in interactive tables
* Add SQL query validation
* Add support for multiple database schemas
* Add query history
* Add data visualization based on query results
* Add authentication for database access

## 👩‍💻 Project Purpose

This project demonstrates practical skills in:

* Generative AI integration
* Natural Language Processing
* SQL
* Python
* Streamlit
* API integration
* Database concepts
* AI-assisted data analytics

---

**Built as a practical AI + Data Analytics project using Python, Streamlit, NVIDIA Laguna XS 2.1, and SQL.**
