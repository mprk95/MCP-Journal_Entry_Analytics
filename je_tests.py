
import pandas as pd
from pathlib import Path

file_path = Path(
    r"C:\A-Other\JE_MCP_Project\data\JE_Sample.xlsx"
)

# Read the Excel file
je = pd.read_excel(file_path)

# Convert posting date to datetime
je["Posting_Date"] = pd.to_datetime(je["Posting_Date"])


# TEST 1: Weekend Journal Entries
def weekend_je_test():
    return je[je["Posting_Date"].dt.dayofweek >= 5].copy()


# TEST 2: Round Dollar Amounts
def round_amount_test():
    return je[
        (je["Amount"] != 0) &
        (je["Amount"] % 10000 == 0)
    ].copy()


# TEST 3: Potential Duplicate Journal Entries
def duplicate_je_test():
    return je[
        je.duplicated(
            subset=[
                "Posting_Date",
                "Amount",
                "Account",
                "Description"
            ],
            keep=False
        )
    ].copy()


# TEST 4: High Value Journal Entries
def high_value_je_test():
    return je[je["Amount"].abs() > 500000].copy()


# Run all four tests
if __name__ == "__main__":

    tests = {
        "Weekend JE": weekend_je_test(),
        "Round Amount JE": round_amount_test(),
        "Duplicate JE": duplicate_je_test(),
        "High Value JE": high_value_je_test()
    }

    for test_name, exceptions in tests.items():
        print(f"{test_name}: {len(exceptions)} exceptions")
  