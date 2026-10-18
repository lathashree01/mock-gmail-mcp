from mcp.server.mcpserver import MCPServer

mcp = MCPServer("mock-gmail-mcp", description="A mock Gmail inbox for testing MCP clients.")

EMAILS = [
    {
        "id": "1",
        "sender": "manager@company.com",
        "subject": "Q4 planning follow-up",
        "date": "2026-10-14",
        "body": (
            "Thanks for the update. Action items: 1) send the revised "
            "budget by Friday, 2) book the review meeting with design, "
            "3) share the draft roadmap with the team."
        ),
    },
    {
        "id": "2",
        "sender": "newsletter@ai-weekly.com",
        "subject": "This week in AI",
        "date": "2026-10-16",
        "body": "Ten stories you might have missed...",
    },
    {
        "id": "3",
        "sender": "manager@company.com",
        "subject": "Quick one-to-one notes",
        "date": "2026-10-09",
        "body": "Action items: update the onboarding doc.",
    },
]


@mcp.tool()
def search_emails(sender: str = "", max_results: int = 5) -> list[dict]:
    """Search the inbox, newest first. Optionally filter by sender."""
    matches = [e for e in EMAILS if sender.lower() in e["sender"].lower()]
    matches.sort(key=lambda e: e["date"], reverse=True)
    return [
        {"id": e["id"], "sender": e["sender"], "subject": e["subject"], "date": e["date"]}
        for e in matches[:max_results]
    ]


@mcp.tool()
def get_email(email_id: str) -> dict:
    """Return the full content of one email by its id."""
    for e in EMAILS:
        if e["id"] == email_id:
            return e
    raise ValueError(f"No email with id {email_id}")


@mcp.resource("inbox://stats")
def inbox_stats() -> str:
    """A quick summary of the inbox."""
    return f"{len(EMAILS)} emails in the inbox."


@mcp.prompt()
def summarise_action_items(sender: str) -> str:
    """Template: find the latest email from a sender and list action items."""
    return (
        f"Find the latest email from {sender}, read it, and list the "
        "action items as a short numbered list."
    )


if __name__ == "__main__":
    mcp.run()  # stdio transport by default