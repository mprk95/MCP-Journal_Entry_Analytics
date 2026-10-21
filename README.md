This project sets up a python MCP server for Journal Entry Analytics.
The python decorators are used to create 4 functions to test - weekend entries, Duplicates, Journal Entries with amounts greater than thresholds, Round Amounts.

The scripts were written on VS code.

If a person/auditor uses claude to ask for weekend entries - the Claude runs the MCP Server - Claude Identifies the suitable python function to run - The output is provided as prompt in Claude.

The importance of using MCP lies in reliability of results. This decreases the LLM blackbox model responses, thus better documentation of procedures applied.


R1,R2,R3-2 signifies - Response 1, Response 2, Second continuation of Response 3 etc. 
