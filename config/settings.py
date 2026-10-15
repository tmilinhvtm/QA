"""Configuration settings for QA Requirement Assistant."""
import os

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "1BG5HNlQBEqyG_hjM9WwklrME2lZbysNFHBSggsSQetk")
GOOGLE_ACCOUNT_EMAIL = os.getenv("GOOGLE_ACCOUNT_EMAIL", "tmi.linhvtm@gmail.com")
SPREADSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit"

# Tab names
TAB_BUG_REPO = "Bug_Repository"
TAB_REQUIREMENTS_ANALYSIS = "Requirements_Analysis"
TAB_TEST_SPECIFICATION = "Test_Cases_Specification"
