"""CLI output helpers."""

from __future__ import annotations

import json
from typing import Any

from ..contracts.models import GenerateResponse


def render_text(response: GenerateResponse) -> str:
    """Return a human-readable string for CLI display."""
    header = f"[{response.finish_reason}] latency={response.latency_ms}ms tokens={response.usage.total_tokens}"
    body = response.output_text
    return f"{header}\n{body}"


def render_json(response: GenerateResponse) -> str:
    """Return a JSON string representation of the response."""
    data = response.model_dump(mode="json")
    return json.dumps(data, indent=2)
