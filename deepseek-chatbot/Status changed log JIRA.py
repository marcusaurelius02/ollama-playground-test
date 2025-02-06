from jira import JIRA
import csv
from datetime import datetime, timedelta
import pandas as pd 

# Set the credentials for the JIRA REST API
USERNAME = "sinjav"
# Read the password from the file
with open(r"C:\\Users\\sinjav\\Password.txt", "r") as password_file:
    PASSWORD = password_file.read()

# Initialize JIRA connection
jira = JIRA(server='https://rndjira.sas.com', basic_auth=("sinjav", PASSWORD))

# Get the project object
project = jira.project('PMRRM')

# Create an empty DataFrame to store changelog
changelog = pd.DataFrame(columns=['key', 'summary','author', 'date', 'field', 'fieldtype', 'from', 'fromString', 'to', 'toString'])

# Specify the minimum date filter
min_date = datetime(2024, 11, 5)

# JQL Query to fetch issues
JQL_QUERY = "project in (PMRRM, PMEBA) and issuetype = Requirement and fixVersion = v02.2025 ORDER BY updated ASC"
issues = jira.search_issues(JQL_QUERY, maxResults=0)

for issue in issues:
    issue = jira.issue(issue.key, expand='changelog')
    
    achangelog = issue.changelog
    for history in achangelog.histories:
        # Convert history date to datetime
        history_date = datetime.strptime(history.created[:10], '%Y-%m-%d')
        
        # Only process if history date is after the minimum date
        if history_date >= min_date:
            for item in history.items:
                changelog = pd.concat([changelog, pd.DataFrame([{
                    'key': issue.key,
                    'summary': issue.fields.summary,
                    'author': history.author,
                    'date': history.created[:10],  # Extract only the date part (YYYY-MM-DD)
                    'field': item.field,
                    'fieldtype': item.fieldtype,
                    'from': getattr(item, 'from'),  # because using item.from doesn't work
                    'fromString': item.fromString,
                    'to': item.to,
                    'toString': item.toString
                }])], ignore_index=True)

# Save to CSV
changelog.to_csv(r"C:\Users\sinjav\OneDrive - SAS\Python Coding\PMRRM_EBA_Jan2024_data.csv", index=False, encoding='utf-8', doublequote=True, header=True)
print("changelog file created")

