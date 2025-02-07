# DeepSeek Chatbot Documentation

This document provides a brief overview of each file within the `deepseek-chatbot` project.

## app.py

`app.py` is a Streamlit application that serves as an AI coding assistant. It uses the DeepSeek language model, facilitated by Ollama and LangChain. The application provides a chat interface where users can ask coding-related questions and receive assistance. Key features include model selection (between `deepseek-r1:1.5b` and `deepseek-r1:7b`), a sidebar for configuration, and a chat interface for interaction. It's designed to help with Python code, debugging, documentation generation, and solution design. The application uses custom CSS for styling. The core logic involves setting up a LangChain pipeline with a system prompt, managing session state for chat history, and handling user input to generate AI responses.

## Status _changed_log_JIRA.py

`Status _changed_log_JIRA.py` is a Python script that interacts with the JIRA REST API to retrieve and process issue changelogs from the 'PMRRM' and 'PMEBA' projects. It authenticates using a username and a password read from a separate file. The script fetches issues based on a JQL query, focusing on 'Requirement' issue types with a specific fixVersion. It extracts changelog data, including the author, date, field modified, and the old/new values. The extracted data is stored in a Pandas DataFrame and then saved to a CSV file. The script filters changelogs based on a minimum date.

### Detailed Documentation for `Status _changed_log_JIRA.py`

#### Overview

The `Status _changed_log_JIRA.py` script is designed to extract changelog information from JIRA issues and save it to a CSV file. It connects to a JIRA instance, retrieves issues based on a JQL query, and iterates through the changelog of each issue to gather relevant data.

#### Functionality

1.  **JIRA Connection**:
    *   Establishes a connection to the JIRA REST API using a username and password. The password is read from a file for security.
    *   The JIRA server URL is hardcoded as `https://rndjira.sas.com`.
2.  **Issue Retrieval**:
    *   Uses a JQL query to fetch issues from the 'PMRRM' and 'PMEBA' projects.
    *   The query filters issues of type 'Requirement' with a specific `fixVersion`.
3.  **Changelog Extraction**:
    *   Iterates through each issue's changelog histories.
    *   Extracts the author, date, field modified, and the old/new values for each change.
    *   Filters changelogs based on a minimum date (`2024-11-05`).
4.  **Data Storage**:
    *   Stores the extracted data in a Pandas DataFrame.
    *   Saves the DataFrame to a CSV file named `PMRRM_EBA_Jan2024_data.csv`.

#### Variables

*   `USERNAME`: JIRA username (`sinjav`).
*   `PASSWORD`: JIRA password read from `C:\\Users\\sinjav\\Password.txt`.
*   `JQL_QUERY`: JQL query used to fetch issues.
*   `min_date`: Minimum date filter for changelogs (`2024-11-05`).
*   `changelog`: Pandas DataFrame to store changelog data.

#### Dependencies

The script uses the following Python libraries:

*   `jira`: For interacting with the JIRA REST API.
*   `csv`: For writing data to a CSV file.
*   `datetime`: For handling dates and times.
*   `pandas`: For creating and manipulating DataFrames.

#### Instructions to install packages

To install the required packages, run the following command:

```bash
pip install jira pandas
```

## readme.md

`readme.md` is the main README file for the project, providing an overview, instructions for setup and usage, and other relevant information about the DeepSeek Code Companion application.
