
from mcp.server.fastmcp import FastMCP

from je_tests import (
    weekend_je_test,
    round_amount_test,
    duplicate_je_test,
    high_value_je_test
)

mcp = FastMCP("JE Audit Analytics")


# Tool 1: Weekend JE Test
@mcp.tool()
def run_weekend_je_test() -> dict:
    """Find journal entries posted on Saturday or Sunday."""
    exceptions = weekend_je_test()

    return {
        "exception_count": len(exceptions),
        "exceptions": exceptions.to_json(
            orient="records", date_format="iso"
        )
    }


# Tool 2: Round Amount Test
@mcp.tool()
def run_round_amount_test() -> dict:
    """Find journal entries with amounts divisible by 10000."""
    exceptions = round_amount_test()

    return {
        "exception_count": len(exceptions),
        "exceptions": exceptions.to_json(
            orient="records", date_format="iso"
        )
    }


# Tool 3: Duplicate JE Test
@mcp.tool()
def run_duplicate_je_test() -> dict:
    """Find potential duplicate journal entries."""
    exceptions = duplicate_je_test()

    return {
        "exception_count": len(exceptions),
        "exceptions": exceptions.to_json(
            orient="records", date_format="iso"
        )
    }


# Tool 4: High Value JE Test
@mcp.tool()
def run_high_value_je_test() -> dict:
    """Find journal entries with absolute amounts above 500000."""
    exceptions = high_value_je_test()

    return {
        "exception_count": len(exceptions),
        "exceptions": exceptions.to_json(
            orient="records", date_format="iso"
        )
    }


# Tool 5: Run All Tests
@mcp.tool()
def run_all_je_tests() -> dict:
    """Run all four journal entry audit tests."""

    return {
        "weekend": run_weekend_je_test(),
        "round_amount": run_round_amount_test(),
        "duplicate": run_duplicate_je_test(),
        "high_value": run_high_value_je_test()
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
  