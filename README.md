# genpark-agentic-cold-email-outreach-spam-score-guard-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![MCP Dependency](https://img.shields.io/badge/MCP-mcp%20SDK-blue?style=for-the-badge)](requirements.txt)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

AI B2B Cold Email Outreach Spam Score & Deliverability Guard. Analyzes email copy against SpamAssassin keyword heuristics, exclamation/caps ratios, unsubscribe compliance, and reading ease grade levels to maximize primary inbox placement.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

---

## 🌟 Key Features

- **Core Client**: Uses Python's standard library. The MCP server additionally requires the official MCP SDK.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Source Repository**: [Alpha-Park/genpark-agentic-cold-email-outreach-spam-score-guard-skill](https://github.com/Alpha-Park/genpark-agentic-cold-email-outreach-spam-score-guard-skill).

---

## MCP Runtime Requirements

Use Python 3.10+ for the MCP server. The core `client.py` has no external dependencies; MCP transport requires `mcp>=1.0.0,<2`. From this checkout, install it into the Python environment used by your MCP client:

```bash
python -m pip install -r requirements.txt
```

Use the same Python interpreter to launch `mcp_server.py`. In desktop client configuration, set `command` to that interpreter's absolute path.

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
from client import AgenticColdOutreachDeliverabilityGuard

def main():
    guard = AgenticColdOutreachDeliverabilityGuard()
    s = "ACT NOW! 100% FREE GROWTH TOOL!!!"
    b = "Click here to make money guaranteed! Limited time special promotion!"
    res = guard.evaluate_email_deliverability(s, b)
    print("--- Email Deliverability Audit ---")
    print(f"Spam Score: {res['composite_spam_score']}/10 | Tier: {res['deliverability_tier']}")
    print(f"Flags: {res['triggered_spam_keywords']}")
    print(f"Recommendation: {res['recommendation']}")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Verify connectivity with an MCP client by sending `initialize`, then `tools/list`.

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)
