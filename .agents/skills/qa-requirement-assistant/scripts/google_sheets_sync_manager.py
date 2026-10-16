"""
google_sheets_sync_manager.py
Helper module for Bidirectional Synchronization, Cache Validation,
Accumulative Record Updates (Append-only / Upsert, Never Reset/Clear),
and Professional Google Sheets Styling for QA Requirements & Test Specifications.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
ENV_FILE = os.path.join(ROOT_DIR, ".env")

if os.path.exists(ENV_FILE):
    try:
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    if key and key not in os.environ:
                        os.environ[key] = val
    except Exception:
        pass

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../data"))
METADATA_FILE = os.path.join(DATA_DIR, ".sync_metadata.json")
BUGS_FILE = os.path.join(DATA_DIR, "bug_repository.json")
REQUIREMENTS_FILE = os.path.join(DATA_DIR, "requirements_analysis.json")
TEST_CASES_FILE = os.path.join(DATA_DIR, "test_cases_specification.json")

DEFAULT_SPREADSHEET_ID = os.getenv("DEFAULT_SPREADSHEET_ID", "1BG5HNlQBEqyG_hjM9WwklrME2lZbysNFHBSggsSQetk")
DEFAULT_USER_EMAIL = os.getenv("DEFAULT_USER_EMAIL", "tmi.linhvtm@gmail.com")
CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH", os.path.expanduser(f"~/.google_workspace_mcp/credentials/{DEFAULT_USER_EMAIL}.json"))


def load_metadata():
    if not os.path.exists(METADATA_FILE):
        return {}
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_metadata(metadata):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)


def is_cache_valid(drive_modified_time: str) -> bool:
    if not os.path.exists(BUGS_FILE) or not os.path.exists(REQUIREMENTS_FILE):
        return False
    metadata = load_metadata()
    last_mod = metadata.get("last_modified_time_drive")
    if not last_mod or not drive_modified_time:
        return False
    return last_mod == drive_modified_time


def load_bugs():
    if not os.path.exists(BUGS_FILE):
        return []
    with open(BUGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_bugs(bugs_list, drive_modified_time=None):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(BUGS_FILE, "w", encoding="utf-8") as f:
        json.dump(bugs_list, f, indent=2, ensure_ascii=False)
    if drive_modified_time:
        meta = load_metadata()
        meta["last_modified_time_drive"] = drive_modified_time
        meta["last_synced_at"] = datetime.utcnow().isoformat() + "Z"
        save_metadata(meta)


def load_requirements():
    if not os.path.exists(REQUIREMENTS_FILE):
        return []
    with open(REQUIREMENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def append_requirement(req_dict):
    """
    Appends a new requirement or updates an existing requirement in local JSON cache.
    Never wipes or resets previously saved requirements.
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    reqs = load_requirements()
    req_id = req_dict.get("requirement_id")
    updated = False
    for i, r in enumerate(reqs):
        if r.get("requirement_id") == req_id:
            reqs[i] = req_dict
            updated = True
            break
    if not updated:
        reqs.append(req_dict)
    with open(REQUIREMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(reqs, f, indent=2, ensure_ascii=False)
    return reqs


def load_test_cases():
    if not os.path.exists(TEST_CASES_FILE):
        return []
    with open(TEST_CASES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def append_test_cases(tc_list):
    """
    Appends new test cases or updates existing ones in local JSON cache.
    Never wipes or resets previously saved test cases.
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    existing = load_test_cases()
    existing_ids = {t.get("test_case_id") for t in existing}
    for tc in tc_list:
        tc_id = tc.get("test_case_id")
        if tc_id in existing_ids:
            for idx, item in enumerate(existing):
                if item.get("test_case_id") == tc_id:
                    existing[idx] = tc
        else:
            existing.append(tc)
    with open(TEST_CASES_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    return existing


def record_successful_sync(drive_modified_time=None):
    meta = load_metadata()
    if drive_modified_time:
        meta["last_modified_time_drive"] = drive_modified_time
    meta["last_synced_at"] = datetime.utcnow().isoformat() + "Z"
    save_metadata(meta)


def get_sheets_service():
    if not os.path.exists(CREDENTIALS_PATH):
        raise FileNotFoundError(f"Credential file not found at {CREDENTIALS_PATH}")
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    with open(CREDENTIALS_PATH, "r", encoding="utf-8") as f:
        creds_data = json.load(f)
    creds = Credentials.from_authorized_user_info(creds_data)
    return build("sheets", "v4", credentials=creds)


def format_google_sheets(spreadsheet_id=None):
    """
    Applies Enterprise QA Styling to Google Spreadsheet tabs:
    - Test_Cases_Specification (10 columns, custom widths, Ant Design Blue header, wrap text, dropdown Pass/Fail)
    - Requirements_Analysis (8 columns, custom widths, Ant Design Blue header, wrap text)
    - Bug_Repository (5 columns, custom widths, Ant Design Blue header, wrap text)
    Cleans up duplicate conditional formatting rules before re-applying.
    """
    if not spreadsheet_id:
        meta = load_metadata()
        spreadsheet_id = meta.get("spreadsheet_id", DEFAULT_SPREADSHEET_ID)

    sheets_service = get_sheets_service()
    sheet_meta = sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheet_map = {s["properties"]["title"]: s for s in sheet_meta.get("sheets", [])}

    requests = []

    # 1. Format Test_Cases_Specification
    if "Test_Cases_Specification" in sheet_map:
        tc_sheet_info = sheet_map["Test_Cases_Specification"]
        tc_sheet_id = tc_sheet_info["properties"]["sheetId"]
        tc_cols = 10
        total_rows = max(tc_sheet_info["properties"].get("gridProperties", {}).get("rowCount", 100), 500)

        # Clear existing conditional formats to prevent accumulation
        existing_cf = tc_sheet_info.get("conditionalFormats", [])
        for cf_idx in range(len(existing_cf) - 1, -1, -1):
            requests.append({
                "deleteConditionalFormatRule": {
                    "sheetId": tc_sheet_id,
                    "index": cf_idx
                }
            })

        # Freeze row 1
        requests.append({
            "updateSheetProperties": {
                "properties": {
                    "sheetId": tc_sheet_id,
                    "gridProperties": {"frozenRowCount": 1}
                },
                "fields": "gridProperties.frozenRowCount"
            }
        })

        # Header style (Row 0): Ant Design Blue #1677FF, white text, bold, 11pt, center/middle
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": tc_sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": tc_cols
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 22/255, "green": 119/255, "blue": 255/255},
                        "textFormat": {
                            "bold": True,
                            "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                            "fontSize": 11
                        },
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "wrapStrategy": "WRAP"
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)"
            }
        })

        # Header height: 45px
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": tc_sheet_id,
                    "dimension": "ROWS",
                    "startIndex": 0,
                    "endIndex": 1
                },
                "properties": {"pixelSize": 45},
                "fields": "pixelSize"
            }
        })

        # Data rows formatting: 10pt, verticalAlignment TOP, wrapStrategy WRAP
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": tc_sheet_id,
                    "startRowIndex": 1,
                    "endRowIndex": total_rows,
                    "startColumnIndex": 0,
                    "endColumnIndex": tc_cols
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {"fontSize": 10},
                        "verticalAlignment": "TOP",
                        "wrapStrategy": "WRAP"
                    }
                },
                "fields": "userEnteredFormat(textFormat,verticalAlignment,wrapStrategy)"
            }
        })

        # Align center & bold for Requirement ID (Col 0), Test Case ID (Col 1), Test Type (Col 3), Priority (Col 4), Status (Col 5)
        for col_idx in [0, 1, 3, 4, 5]:
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": tc_sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": total_rows,
                        "startColumnIndex": col_idx,
                        "endColumnIndex": col_idx + 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "CENTER",
                            "textFormat": {"bold": (col_idx in [1, 4, 5])}
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat.bold)"
                }
            })

        # Column widths for Test_Cases_Specification (10 columns)
        tc_col_widths = [
            160,  # 0: Requirement ID
            130,  # 1: Test Case ID
            260,  # 2: Scenario Name
            160,  # 3: Test Type
            120,  # 4: Priority
            130,  # 5: Status (Pass/Fail)
            240,  # 6: Pre-conditions
            360,  # 7: Bước thực hiện (Steps)
            420,  # 8: Kết quả mong đợi (UI / API / DB)
            160   # 9: Notes / Defect ID
        ]
        for idx, width in enumerate(tc_col_widths):
            requests.append({
                "updateDimensionProperties": {
                    "range": {
                        "sheetId": tc_sheet_id,
                        "dimension": "COLUMNS",
                        "startIndex": idx,
                        "endIndex": idx + 1
                    },
                    "properties": {"pixelSize": width},
                    "fields": "pixelSize"
                }
            })

        # Data Validation (Dropdown) for Col 5 (Status)
        requests.append({
            "setDataValidation": {
                "range": {
                    "sheetId": tc_sheet_id,
                    "startRowIndex": 1,
                    "endRowIndex": total_rows,
                    "startColumnIndex": 5,
                    "endColumnIndex": 6
                },
                "rule": {
                    "condition": {
                        "type": "ONE_OF_LIST",
                        "values": [
                            {"userEnteredValue": "NOT_RUN"},
                            {"userEnteredValue": "PASS"},
                            {"userEnteredValue": "FAIL"},
                            {"userEnteredValue": "BLOCKED"}
                        ]
                    },
                    "inputMessage": "Vui lòng chọn trạng thái kiểm thử: NOT_RUN, PASS, FAIL, hoặc BLOCKED.",
                    "strict": True,
                    "showCustomUi": True
                }
            }
        })

        # Conditional Formatting for Col 5 (Status colors)
        status_colors = [
            ("PASS", {"red": 209/255, "green": 250/255, "blue": 223/255}, {"red": 2/255, "green": 122/255, "blue": 72/255}),     # Green
            ("FAIL", {"red": 254/255, "green": 228/255, "blue": 226/255}, {"red": 180/255, "green": 35/255, "blue": 24/255}),     # Red
            ("BLOCKED", {"red": 254/255, "green": 240/255, "blue": 199/255}, {"red": 181/255, "green": 71/255, "blue": 8/255}),   # Orange
            ("NOT_RUN", {"red": 242/255, "green": 244/255, "blue": 247/255}, {"red": 71/255, "green": 84/255, "blue": 103/255})   # Gray
        ]
        for val, bg, fg in status_colors:
            requests.append({
                "addConditionalFormatRule": {
                    "rule": {
                        "ranges": [{
                            "sheetId": tc_sheet_id,
                            "startRowIndex": 1,
                            "endRowIndex": total_rows,
                            "startColumnIndex": 5,
                            "endColumnIndex": 6
                        }],
                        "booleanRule": {
                            "condition": {
                                "type": "TEXT_EQ",
                                "values": [{"userEnteredValue": val}]
                            },
                            "format": {
                                "backgroundColor": bg,
                                "textFormat": {"foregroundColor": fg, "bold": True}
                            }
                        }
                    },
                    "index": 0
                }
            })

        # Grid borders for Test_Cases_Specification
        requests.append({
            "updateBorders": {
                "range": {
                    "sheetId": tc_sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": total_rows,
                    "startColumnIndex": 0,
                    "endColumnIndex": tc_cols
                },
                "top": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "bottom": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "left": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "right": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "innerHorizontal": {"style": "SOLID", "color": {"red": 0.88, "green": 0.9, "blue": 0.94}},
                "innerVertical": {"style": "SOLID", "color": {"red": 0.88, "green": 0.9, "blue": 0.94}}
            }
        })

    # 2. Format Requirements_Analysis
    if "Requirements_Analysis" in sheet_map:
        req_sheet_info = sheet_map["Requirements_Analysis"]
        req_sheet_id = req_sheet_info["properties"]["sheetId"]
        req_cols = 8
        req_total_rows = max(req_sheet_info["properties"].get("gridProperties", {}).get("rowCount", 100), 500)

        # Freeze row 1
        requests.append({
            "updateSheetProperties": {
                "properties": {
                    "sheetId": req_sheet_id,
                    "gridProperties": {"frozenRowCount": 1}
                },
                "fields": "gridProperties.frozenRowCount"
            }
        })
        # Header style: Ant Design Blue
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": req_sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": req_cols
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 22/255, "green": 119/255, "blue": 255/255},
                        "textFormat": {
                            "bold": True,
                            "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                            "fontSize": 11
                        },
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "wrapStrategy": "WRAP"
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)"
            }
        })
        # Header height: 45px
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": req_sheet_id,
                    "dimension": "ROWS",
                    "startIndex": 0,
                    "endIndex": 1
                },
                "properties": {"pixelSize": 45},
                "fields": "pixelSize"
            }
        })
        # Data rows formatting
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": req_sheet_id,
                    "startRowIndex": 1,
                    "endRowIndex": req_total_rows,
                    "startColumnIndex": 0,
                    "endColumnIndex": req_cols
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {"fontSize": 10},
                        "verticalAlignment": "TOP",
                        "wrapStrategy": "WRAP"
                    }
                },
                "fields": "userEnteredFormat(textFormat,verticalAlignment,wrapStrategy)"
            }
        })
        # Requirement ID & Analyzed At center alignment
        for col_idx in [0, 1]:
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": req_sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": req_total_rows,
                        "startColumnIndex": col_idx,
                        "endColumnIndex": col_idx + 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "CENTER",
                            "textFormat": {"bold": (col_idx == 0)}
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat.bold)"
                }
            })

        # Column widths for Requirements_Analysis (8 columns)
        req_col_widths = [
            160,  # 0: Requirement ID
            160,  # 1: Analyzed At
            280,  # 2: Requirement Text
            360,  # 3: Business Rules
            340,  # 4: Questions for BA
            340,  # 5: Possible Risks
            260,  # 6: Related Historical Bugs
            200   # 7: Key Decisions Log
        ]
        for idx, width in enumerate(req_col_widths):
            requests.append({
                "updateDimensionProperties": {
                    "range": {
                        "sheetId": req_sheet_id,
                        "dimension": "COLUMNS",
                        "startIndex": idx,
                        "endIndex": idx + 1
                    },
                    "properties": {"pixelSize": width},
                    "fields": "pixelSize"
                }
            })

        # Grid borders for Requirements_Analysis
        requests.append({
            "updateBorders": {
                "range": {
                    "sheetId": req_sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": req_total_rows,
                    "startColumnIndex": 0,
                    "endColumnIndex": req_cols
                },
                "top": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "bottom": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "left": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "right": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "innerHorizontal": {"style": "SOLID", "color": {"red": 0.88, "green": 0.9, "blue": 0.94}},
                "innerVertical": {"style": "SOLID", "color": {"red": 0.88, "green": 0.9, "blue": 0.94}}
            }
        })

    # 3. Format Bug_Repository
    if "Bug_Repository" in sheet_map:
        bug_sheet_info = sheet_map["Bug_Repository"]
        bug_sheet_id = bug_sheet_info["properties"]["sheetId"]
        bug_cols = 5
        bug_total_rows = max(bug_sheet_info["properties"].get("gridProperties", {}).get("rowCount", 100), 500)

        # Clear existing conditional formats
        existing_cf = bug_sheet_info.get("conditionalFormats", [])
        for cf_idx in range(len(existing_cf) - 1, -1, -1):
            requests.append({
                "deleteConditionalFormatRule": {
                    "sheetId": bug_sheet_id,
                    "index": cf_idx
                }
            })

        # Freeze row 1
        requests.append({
            "updateSheetProperties": {
                "properties": {
                    "sheetId": bug_sheet_id,
                    "gridProperties": {"frozenRowCount": 1}
                },
                "fields": "gridProperties.frozenRowCount"
            }
        })
        # Header style: Ant Design Blue
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": bug_sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": bug_cols
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 22/255, "green": 119/255, "blue": 255/255},
                        "textFormat": {
                            "bold": True,
                            "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                            "fontSize": 11
                        },
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "wrapStrategy": "WRAP"
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)"
            }
        })
        # Header height: 45px
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": bug_sheet_id,
                    "dimension": "ROWS",
                    "startIndex": 0,
                    "endIndex": 1
                },
                "properties": {"pixelSize": 45},
                "fields": "pixelSize"
            }
        })
        # Data rows formatting
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": bug_sheet_id,
                    "startRowIndex": 1,
                    "endRowIndex": bug_total_rows,
                    "startColumnIndex": 0,
                    "endColumnIndex": bug_cols
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {"fontSize": 10},
                        "verticalAlignment": "TOP",
                        "wrapStrategy": "WRAP"
                    }
                },
                "fields": "userEnteredFormat(textFormat,verticalAlignment,wrapStrategy)"
            }
        })
        # Bug ID (Col 0) and Severity (Col 4) center alignment & bold
        for col_idx in [0, 4]:
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": bug_sheet_id,
                        "startRowIndex": 1,
                        "endRowIndex": bug_total_rows,
                        "startColumnIndex": col_idx,
                        "endColumnIndex": col_idx + 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "horizontalAlignment": "CENTER",
                            "textFormat": {"bold": True}
                        }
                    },
                    "fields": "userEnteredFormat(horizontalAlignment,textFormat.bold)"
                }
            })

        # Column widths for Bug_Repository (5 columns)
        bug_col_widths = [
            130,  # 0: Bug ID
            500,  # 1: Description
            280,  # 2: Root Cause Domain
            280,  # 3: Impacted Flow
            130   # 4: Severity
        ]
        for idx, width in enumerate(bug_col_widths):
            requests.append({
                "updateDimensionProperties": {
                    "range": {
                        "sheetId": bug_sheet_id,
                        "dimension": "COLUMNS",
                        "startIndex": idx,
                        "endIndex": idx + 1
                    },
                    "properties": {"pixelSize": width},
                    "fields": "pixelSize"
                }
            })

        # Conditional formatting for Severity (Col 4)
        sev_colors = [
            ("P1 (Critical)", {"red": 254/255, "green": 228/255, "blue": 226/255}, {"red": 180/255, "green": 35/255, "blue": 24/255}),   # Light red
            ("P2 (High)", {"red": 254/255, "green": 240/255, "blue": 199/255}, {"red": 181/255, "green": 71/255, "blue": 8/255}),       # Light orange
        ]
        for val, bg, fg in sev_colors:
            requests.append({
                "addConditionalFormatRule": {
                    "rule": {
                        "ranges": [{
                            "sheetId": bug_sheet_id,
                            "startRowIndex": 1,
                            "endRowIndex": bug_total_rows,
                            "startColumnIndex": 4,
                            "endColumnIndex": 5
                        }],
                        "booleanRule": {
                            "condition": {
                                "type": "TEXT_EQ",
                                "values": [{"userEnteredValue": val}]
                            },
                            "format": {
                                "backgroundColor": bg,
                                "textFormat": {"foregroundColor": fg, "bold": True}
                            }
                        }
                    },
                    "index": 0
                }
            })

        # Grid borders for Bug_Repository
        requests.append({
            "updateBorders": {
                "range": {
                    "sheetId": bug_sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": bug_total_rows,
                    "startColumnIndex": 0,
                    "endColumnIndex": bug_cols
                },
                "top": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "bottom": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "left": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "right": {"style": "SOLID", "color": {"red": 0.8, "green": 0.85, "blue": 0.9}},
                "innerHorizontal": {"style": "SOLID", "color": {"red": 0.88, "green": 0.9, "blue": 0.94}},
                "innerVertical": {"style": "SOLID", "color": {"red": 0.88, "green": 0.9, "blue": 0.94}}
            }
        })

    # Execute batchUpdate
    if requests:
        sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={"requests": requests}
        ).execute()
        print(f"✅ Successfully applied Enterprise QA Styling to Google Spreadsheet ({spreadsheet_id}).")


def sync_local_requirements_to_drive(spreadsheet_id=None):
    """
    Pushes requirements from local requirements_analysis.json to Google Sheet Requirements_Analysis tab
    using an ACCUMULATIVE APPEND / UPSERT mechanism.
    NEVER clears the sheet or removes prior records.
    """
    if not spreadsheet_id:
        meta = load_metadata()
        spreadsheet_id = meta.get("spreadsheet_id", DEFAULT_SPREADSHEET_ID)

    sheets_service = get_sheets_service()

    headers = [
        "Requirement ID",
        "Analyzed At",
        "Requirement Text",
        "Business Rules",
        "Questions for BA",
        "Possible Risks",
        "Related Bugs",
        "Key Decisions Log"
    ]

    # 1. Read existing rows from Sheet to prevent overwriting / resetting
    res = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range="Requirements_Analysis!A1:H1000"
    ).execute()
    existing_rows = res.get("values", [])

    if not existing_rows:
        # If completely empty sheet, initialize header
        sheets_service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range="Requirements_Analysis!A1",
            valueInputOption="USER_ENTERED",
            body={"values": [headers]}
        ).execute()
        existing_rows = [headers]

    # Map existing Requirement IDs (Column A) to 1-based row index in Sheet
    sheet_req_map = {}
    for idx, row in enumerate(existing_rows[1:], start=2):
        if row and len(row) > 0 and row[0].strip():
            sheet_req_map[row[0].strip()] = idx

    local_reqs = load_requirements()
    new_rows_to_append = []
    updated_count = 0

    for r in local_reqs:
        req_id = r.get("requirement_id", "").strip()
        analyzed_at = r.get("analyzed_at", "")
        req_text = r.get("requirement_text", "")

        br = r.get("business_rules", {})
        if isinstance(br, dict):
            br_str = (
                f"• Pre-condition: {br.get('pre_condition', '')}\n"
                f"• Trigger: {br.get('trigger', '')}\n"
                f"• Constraints: {br.get('constraints', '')}\n"
                f"• Post-condition: {br.get('post_condition', '')}"
            )
        else:
            br_str = str(br)

        q_ba = r.get("questions_for_ba", "")
        if isinstance(q_ba, list):
            q_ba_str = "\n".join(q_ba)
        else:
            q_ba_str = str(q_ba)

        risks = r.get("possible_risks", "")
        if isinstance(risks, list):
            risks_str = "\n".join(risks)
        else:
            risks_str = str(risks)

        bugs = r.get("related_historical_bugs", "")
        if isinstance(bugs, list):
            bugs_str = "\n".join(bugs)
        else:
            bugs_str = str(bugs)

        decisions = r.get("key_decisions_log", "")

        row_data = [
            req_id,
            analyzed_at,
            req_text,
            br_str,
            q_ba_str,
            risks_str,
            bugs_str,
            decisions
        ]

        if req_id in sheet_req_map:
            # Update existing row
            row_num = sheet_req_map[req_id]
            sheets_service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=f"Requirements_Analysis!A{row_num}:H{row_num}",
                valueInputOption="USER_ENTERED",
                body={"values": [row_data]}
            ).execute()
            updated_count += 1
        else:
            # New requirement -> accumulate into append queue
            new_rows_to_append.append(row_data)

    if new_rows_to_append:
        sheets_service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range="Requirements_Analysis!A1",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body={"values": new_rows_to_append}
        ).execute()
        print(f"✅ Appended {len(new_rows_to_append)} new requirement(s) to 'Requirements_Analysis'.")

    if updated_count > 0:
        print(f"✅ Updated {updated_count} existing requirement(s) in 'Requirements_Analysis'.")

    format_google_sheets(spreadsheet_id)


def sync_local_test_cases_to_drive(spreadsheet_id=None):
    """
    Pushes local test cases from test_cases_specification.json to Google Sheet Test_Cases_Specification tab
    using an ACCUMULATIVE APPEND / UPSERT mechanism.
    NEVER clears the sheet or removes prior test cases.
    """
    if not spreadsheet_id:
        meta = load_metadata()
        spreadsheet_id = meta.get("spreadsheet_id", DEFAULT_SPREADSHEET_ID)

    sheets_service = get_sheets_service()

    headers = [
        "Requirement ID",
        "Test Case ID",
        "Scenario Name",
        "Test Type",
        "Priority",
        "Status (Pass/Fail)",
        "Pre-conditions",
        "Bước thực hiện (Steps)",
        "Kết quả mong đợi (UI / API / DB)",
        "Notes / Defect ID"
    ]

    # 1. Read existing rows from Sheet to prevent overwriting / resetting
    res = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range="Test_Cases_Specification!A1:J2000"
    ).execute()
    existing_rows = res.get("values", [])

    if not existing_rows:
        sheets_service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range="Test_Cases_Specification!A1",
            valueInputOption="USER_ENTERED",
            body={"values": [headers]}
        ).execute()
        existing_rows = [headers]

    # Map existing Test Case IDs (Column B) to 1-based row index in Sheet
    sheet_tc_map = {}
    for idx, row in enumerate(existing_rows[1:], start=2):
        if row and len(row) > 1 and row[1].strip():
            sheet_tc_map[row[1].strip()] = idx

    test_cases = load_test_cases()
    new_rows_to_append = []
    updated_count = 0

    for tc in test_cases:
        req_id = tc.get("requirement_id", "")
        tc_id = tc.get("test_case_id", "").strip()
        name = tc.get("scenario_name", "")
        t_type = tc.get("test_type", "")
        priority = tc.get("priority", "")
        status = tc.get("status", "NOT_RUN")
        precond = tc.get("pre_conditions", "")

        # Format steps
        steps_list = tc.get("test_steps", [])
        if isinstance(steps_list, list) and steps_list:
            step_texts = []
            expected_texts = []
            for s in steps_list:
                s_num = s.get("step_no", "")
                action = s.get("action_step", "")
                exp_ui = s.get("expected_ui", "")
                exp_api = s.get("expected_api", "")
                exp_db = s.get("expected_db", "")
                exp_event = s.get("expected_event", "")

                step_texts.append(f"Bước {s_num}: {action}")

                exp_parts = []
                if exp_ui:
                    exp_parts.append(f"[UI] {exp_ui}")
                if exp_api:
                    exp_parts.append(f"[API] {exp_api}")
                if exp_db:
                    exp_parts.append(f"[Database] {exp_db}")
                if exp_event:
                    exp_parts.append(f"[Event] {exp_event}")

                expected_texts.append(f"Bước {s_num}:\n" + "\n".join(exp_parts))

            steps_str = "\n\n".join(step_texts)
            expected_str = "\n\n".join(expected_texts)
        else:
            sim_steps = tc.get("simulated_steps", {})
            if isinstance(sim_steps, dict):
                steps_str = f"Hành động: {sim_steps.get('user_action', '')}\nEndpoint: {sim_steps.get('endpoint', '')}"
            else:
                steps_str = str(sim_steps)
            exp_results = tc.get("expected_results", {})
            if isinstance(exp_results, dict):
                expected_str = f"[UI/API] {exp_results.get('tier1_ui_api', '')}\n[DB] {exp_results.get('tier2_database', '')}\n[Event] {exp_results.get('tier3_event_bus', '')}"
            else:
                expected_str = str(exp_results)

        notes = tc.get("notes", "")

        row_data = [
            req_id,
            tc_id,
            name,
            t_type,
            priority,
            status,
            precond,
            steps_str,
            expected_str,
            notes
        ]

        if tc_id in sheet_tc_map:
            row_num = sheet_tc_map[tc_id]
            sheets_service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=f"Test_Cases_Specification!A{row_num}:J{row_num}",
                valueInputOption="USER_ENTERED",
                body={"values": [row_data]}
            ).execute()
            updated_count += 1
        else:
            new_rows_to_append.append(row_data)

    if new_rows_to_append:
        sheets_service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range="Test_Cases_Specification!A1",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body={"values": new_rows_to_append}
        ).execute()
        print(f"✅ Appended {len(new_rows_to_append)} new test case(s) to 'Test_Cases_Specification'.")

    if updated_count > 0:
        print(f"✅ Updated {updated_count} existing test case(s) in 'Test_Cases_Specification'.")

    format_google_sheets(spreadsheet_id)


def sync_bugs_to_drive(spreadsheet_id=None):
    """
    Pushes bugs from local bug_repository.json to Google Sheet Bug_Repository tab
    in APPEND / UPSERT mode (preserves existing bugs, never resets/clears sheet).
    """
    if not spreadsheet_id:
        meta = load_metadata()
        spreadsheet_id = meta.get("spreadsheet_id", DEFAULT_SPREADSHEET_ID)

    sheets_service = get_sheets_service()

    headers = [
        "Bug ID",
        "Description",
        "Root Cause Domain",
        "Impacted Flow",
        "Severity"
    ]

    res = sheets_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range="Bug_Repository!A1:E1000"
    ).execute()
    existing_rows = res.get("values", [])

    if not existing_rows:
        sheets_service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range="Bug_Repository!A1",
            valueInputOption="USER_ENTERED",
            body={"values": [headers]}
        ).execute()
        existing_rows = [headers]

    sheet_bug_map = {}
    for idx, row in enumerate(existing_rows[1:], start=2):
        if row and len(row) > 0 and row[0].strip():
            sheet_bug_map[row[0].strip()] = idx

    bugs = load_bugs()
    new_rows_to_append = []
    updated_count = 0

    for b in bugs:
        bug_id = b.get("bug_id", "").strip()
        row_data = [
            bug_id,
            b.get("description", ""),
            b.get("root_cause_domain", ""),
            b.get("impacted_flow", ""),
            b.get("severity", "P2 (High)")
        ]
        if bug_id in sheet_bug_map:
            row_num = sheet_bug_map[bug_id]
            sheets_service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=f"Bug_Repository!A{row_num}:E{row_num}",
                valueInputOption="USER_ENTERED",
                body={"values": [row_data]}
            ).execute()
            updated_count += 1
        else:
            new_rows_to_append.append(row_data)

    if new_rows_to_append:
        sheets_service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range="Bug_Repository!A1",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body={"values": new_rows_to_append}
        ).execute()
        print(f"✅ Appended {len(new_rows_to_append)} new bug(s) to 'Bug_Repository'.")

    if updated_count > 0:
        print(f"✅ Updated {updated_count} existing bug(s) in 'Bug_Repository'.")

    format_google_sheets(spreadsheet_id)


def sync_all_to_drive(spreadsheet_id=None):
    """
    Syncs Bug_Repository, Requirements_Analysis, and Test_Cases_Specification to Drive
    in accumulative append mode, then applies full styling.
    """
    sync_bugs_to_drive(spreadsheet_id)
    sync_local_requirements_to_drive(spreadsheet_id)
    sync_local_test_cases_to_drive(spreadsheet_id)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "format":
        format_google_sheets()
    elif len(sys.argv) > 1 and sys.argv[1] == "sync_bugs":
        sync_bugs_to_drive()
    elif len(sys.argv) > 1 and sys.argv[1] == "sync_requirements":
        sync_local_requirements_to_drive()
    elif len(sys.argv) > 1 and sys.argv[1] == "sync_tests":
        sync_local_test_cases_to_drive()
    elif len(sys.argv) > 1 and sys.argv[1] == "sync_all":
        sync_all_to_drive()
    else:
        meta = load_metadata()
        print("Metadata:", json.dumps(meta, indent=2))
        print(f"Total bugs in local cache: {len(load_bugs())}")
        print(f"Total requirements in local cache: {len(load_requirements())}")
        print(f"Total test cases in local cache: {len(load_test_cases())}")
