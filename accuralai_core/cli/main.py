"""CLI entry point for accuralai-core."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

import click

from .commands.generate import register_generate_command


@click.group()
@click.option(
    "--config",
    "config_paths",
    multiple=True,
    type=click.Path(exists=True, path_type=Path),
    help="Path to configuration file (TOML). Can be supplied multiple times.",
)
@click.pass_context
def app(ctx: click.Context, config_paths: tuple[Path, ...]) -> None:
    """AccuralAI core orchestrator CLI."""
    ctx.ensure_object(dict)
    ctx.obj["config_paths"] = [str(path) for path in config_paths]
    ctx.obj["config_overrides"] = None


register_generate_command(app)


def main() -> None:
    """Console entry point."""
    app(obj={})
