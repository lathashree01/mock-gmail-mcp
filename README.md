# Mock Gmail MCP Server

A small MCP server that provides a sample Gmail-like inbox. 

This is a trial project for my article on [Understanding MCP: From Architecture to Building My First MCP Server](https://lathashreeh.medium.com/understanding-mcp-from-architecture-to-building-my-first-mcp-server-755c3b1c42c6).

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)

## Run the server

From this directory, install the project dependencies and start the server:

```bash
uv sync
uv run python server.py
```

The server uses MCP's stdio transport by default. Run it from an MCP-compatible
client configured to launch `server.py` with `uv run python` as its command and
this project directory as its working directory. 

## Available MCP features

### Tools

- `search_emails(sender="", max_results=5)` searches the sample inbox. The
  optional sender filter is a case-insensitive substring match. Results are
  sorted newest first and include the email ID, sender, subject, and date.
- `get_email(email_id)` returns the full matching email, including its body.
  An unknown ID returns an error.

### Prompt

- `summarise_action_items(sender)` provides a prompt to find the latest email
  from a sender and list its action items.

## Sample inbox

The server starts with three in-memory sample emails (IDs `1`, `2`, and `3`).
They are defined in `server.py` and reset to those defaults whenever the
process restarts. There is no email sending, deletion, persistence, Gmail
authentication, or live inbox access.
