#!/usr/bin/env python3
"""
push_to_sheets.py
Pushes 20 structured interview questions, technical problems, and strategic answers
into the Google Spreadsheet 'Interview QA - Tester Data & Automation' (ID: 1lTZIfQ_6V_bLWI6J5f066C-pGx1zIED_D9t7cj1MxOs),
tab 'AI QA - Accuracy & Effort (3M)', and formats it with Ant Design Blue enterprise styling.
"""

import json
import os
import sys
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from populate_excel_questions import ROWS

SPREADSHEET_ID = "1lTZIfQ_6V_bLWI6J5f066C-pGx1zIED_D9t7cj1MxOs"
SHEET_TITLE = "AI QA - Accuracy & Effort (3M)"
CREDENTIALS_PATH = os.path.expanduser("~/.google_workspace_mcp/credentials/tmi.linhvtm@gmail.com.json")

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip("#")
    return {
        "red": int(hex_str[0:2], 16) / 255.0,
        "green": int(hex_str[2:4], 16) / 255.0,
        "blue": int(hex_str[4:6], 16) / 255.0,
    }

def main():
    if not os.path.exists(CREDENTIALS_PATH):
        print(f"Credentials not found at {CREDENTIALS_PATH}")
        sys.exit(1)

    with open(CREDENTIALS_PATH, "r", encoding="utf-8") as f:
        creds_data = json.load(f)

    creds = Credentials.from_authorized_user_info(creds_data)
    service = build("sheets", "v4", credentials=creds)

    # 1. Get Sheet ID
    meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    sheet_id = None
    for s in meta["sheets"]:
        if s["properties"]["title"] == SHEET_TITLE:
            sheet_id = s["properties"]["sheetId"]
            break

    if sheet_id is None:
        print(f"Sheet {SHEET_TITLE} not found. Creating it...")
        req = {
            "addSheet": {
                "properties": {
                    "title": SHEET_TITLE
                }
            }
        }
        res = service.spreadsheets().batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body={"requests": [req]}
        ).execute()
        sheet_id = res["replies"][0]["addSheet"]["properties"]["sheetId"]

    print(f"Target Sheet ID: {sheet_id}")

    # 2. Write Data Rows (A2:F21)
    range_data = f"'{SHEET_TITLE}'!A2:F{len(ROWS)+1}"
    body = {
        "values": ROWS
    }
    update_res = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_data,
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()
    print(f"Updated {update_res.get('updatedCells')} cells in {range_data}")

    # 3. Apply Professional Enterprise Styling via batchUpdate
    requests = []

    # Freeze Row 1
    requests.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": sheet_id,
                "gridProperties": {
                    "frozenRowCount": 1
                }
            },
            "fields": "gridProperties.frozenRowCount"
        }
    })

    # Header Row Height (Row 0 -> 48px)
    requests.append({
        "updateDimensionProperties": {
            "range": {
                "sheetId": sheet_id,
                "dimension": "ROWS",
                "startIndex": 0,
                "endIndex": 1
            },
            "properties": {
                "pixelSize": 48
            },
            "fields": "pixelSize"
        }
    })

    # Column Widths
    col_widths = [90, 160, 280, 440, 360, 600]
    for col_idx, width in enumerate(col_widths):
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": col_idx,
                    "endIndex": col_idx + 1
                },
                "properties": {
                    "pixelSize": width
                },
                "fields": "pixelSize"
            }
        })

    # Header Row Styling (Ant Design Blue, White Bold Text, Centered)
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": hex_to_rgb("#1677FF"),
                    "textFormat": {
                        "foregroundColor": hex_to_rgb("#FFFFFF"),
                        "fontSize": 11,
                        "bold": True,
                        "fontFamily": "Roboto"
                    },
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "wrapStrategy": "WRAP"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)"
        }
    })

    # Data Rows Styling (All Cells: WRAP, TOP vertical alignment, font size 10)
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": len(ROWS) + 1,
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "cell": {
                "userEnteredFormat": {
                    "textFormat": {
                        "foregroundColor": hex_to_rgb("#1E293B"),
                        "fontSize": 10,
                        "fontFamily": "Roboto"
                    },
                    "verticalAlignment": "TOP",
                    "wrapStrategy": "WRAP"
                }
            },
            "fields": "userEnteredFormat(textFormat,verticalAlignment,wrapStrategy)"
        }
    })

    # Format Column A & B (Centered, Bold)
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": len(ROWS) + 1,
                "startColumnIndex": 0,
                "endColumnIndex": 2
            },
            "cell": {
                "userEnteredFormat": {
                    "horizontalAlignment": "CENTER",
                    "textFormat": {
                        "bold": True
                    }
                }
            },
            "fields": "userEnteredFormat(horizontalAlignment,textFormat.bold)"
        }
    })

    # Color highlight by category:
    # Rows 1-10: Câu hỏi phỏng vấn (Light blue tint #F0F7FF on Col A-B)
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 1,
                "endRowIndex": 11,
                "startColumnIndex": 0,
                "endColumnIndex": 2
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": hex_to_rgb("#F0F7FF"),
                    "textFormat": {
                        "foregroundColor": hex_to_rgb("#0958D9")
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat.foregroundColor)"
        }
    })

    # Rows 11-16: Vấn đề kỹ thuật (Light amber tint #FFFBEB on Col A-B)
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 11,
                "endRowIndex": 17,
                "startColumnIndex": 0,
                "endColumnIndex": 2
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": hex_to_rgb("#FFFBEB"),
                    "textFormat": {
                        "foregroundColor": hex_to_rgb("#B45309")
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat.foregroundColor)"
        }
    })

    # Rows 17-20: Bài test tình huống (Light green tint #F0FDF4 on Col A-B)
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 17,
                "endRowIndex": 21,
                "startColumnIndex": 0,
                "endColumnIndex": 2
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": hex_to_rgb("#F0FDF4"),
                    "textFormat": {
                        "foregroundColor": hex_to_rgb("#15803D")
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat.foregroundColor)"
        }
    })

    # Add soft borders (#E2E8F0) to entire table
    requests.append({
        "updateBorders": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": 0,
                "endRowIndex": len(ROWS) + 1,
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "top": {"style": "SOLID", "color": hex_to_rgb("#CBD5E1")},
            "bottom": {"style": "SOLID", "color": hex_to_rgb("#CBD5E1")},
            "left": {"style": "SOLID", "color": hex_to_rgb("#CBD5E1")},
            "right": {"style": "SOLID", "color": hex_to_rgb("#CBD5E1")},
            "innerHorizontal": {"style": "SOLID", "color": hex_to_rgb("#E2E8F0")},
            "innerVertical": {"style": "SOLID", "color": hex_to_rgb("#E2E8F0")}
        }
    })

    # Execute batchUpdate
    batch_res = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={"requests": requests}
    ).execute()
    print(f"Successfully applied {len(requests)} formatting rules to {SHEET_TITLE}!")

if __name__ == "__main__":
    main()
