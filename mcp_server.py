#!/usr/bin/env python3
import json
import sys
from client import AgenticColdOutreachDeliverabilityGuard

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('genpark-agentic-cold-email-outreach-spam-score-guard-skill')

@mcp.tool()
def evaluate_email_deliverability(subject: str = "", body: str = "", sender_domain: str = "acme.io") -> str:
    """Score the supplied email content for deliverability risks."""
    return json.dumps(AgenticColdOutreachDeliverabilityGuard().evaluate_email_deliverability(subject, body, sender_domain))

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        guard = AgenticColdOutreachDeliverabilityGuard()
        subj = "Brief idea on AI customer routing for Acme"
        body = "Hi Alex, noticed your team scaling the support fleet. We built an open MCP server that automates triage. Would love your feedback. Reply stop to unsubscribe."
        res = guard.evaluate_email_deliverability(subj, body)
        assert res["composite_spam_score"] < 2.5
        assert res["deliverability_tier"] == "PRIMARY_INBOX_OPTIMAL"
        print(f"[TEST PASS] Deliverability Score: {res['composite_spam_score']}/10")
        sys.exit(0)

    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
