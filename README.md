# LangChain Assignment

## Overview

This project demonstrates how to use the LangChain framework to interact with an OpenAI chat model and trace executions using LangSmith.

## Features

* Uses LangChain to communicate with an OpenAI chat model
* Reads API keys securely from environment variables
* Enables LangSmith tracing
* Prints model responses in the terminal
* Keeps all application logic in a single `main.py` file

## Project Structure

```text
langchain-app/
├── main.py
├── .env
├── .gitignore
├── README.md
└── venv/
```

## Setup Instructions

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install langchain langchain-openai langsmith python-dotenv
```

### Configure Environment Variables

Create a `.env` file and add:

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=langchain-assignment
```

### Run the Application

```bash
python main.py
```

## Sample Output

```text
Input: Tell me a fun fact about Tamil Nadu.
Output: Tamil Nadu is home to one of the world's oldest continuously practiced classical languages, Tamil.
```

## Technologies Used

* Python
* LangChain
* OpenAI API
* LangSmith
* Git & GitHub
