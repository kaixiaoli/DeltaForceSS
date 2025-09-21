"""Standalone CLI that uses pyautogui to type a username/password sequence.

This script is designed to be easily invoked from external tools such as
Easy Language (易语言).  It can optionally launch a target executable before
performing the keyboard automation.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

try:
    import pyautogui
except ImportError as exc:  # pragma: no cover - import error path depends on environment
    raise SystemExit(
        "pyautogui is required. Install dependencies with 'pip install -r requirements.txt'."
    ) from exc


def wait_for(seconds: float) -> None:
    """Sleep for the requested amount of time while displaying feedback."""
    if seconds <= 0:
        return

    end_time = time.perf_counter() + seconds
    while True:
        remaining = end_time - time.perf_counter()
        if remaining <= 0:
            break
        # Provide minimal feedback so callers know the script is still running.
        print(f"Waiting... {remaining:0.1f}s remaining", end="\r", flush=True)
        time.sleep(min(0.5, remaining))
    print(" " * 40, end="\r", flush=True)


def launch_target(executable: Optional[str], launch_wait: float) -> None:
    """Launch an optional executable before performing the keyboard automation."""
    if not executable:
        if launch_wait > 0:
            wait_for(launch_wait)
        return

    exe_path = Path(executable).expanduser()
    if not exe_path.exists():
        raise SystemExit(f"Target executable not found: {exe_path}")

    try:
        subprocess.Popen([str(exe_path)])
    except OSError as exc:  # pragma: no cover - depends on local OS state
        raise SystemExit(f"Failed to launch {exe_path}: {exc}") from exc

    wait_for(launch_wait)


def perform_login(
    username: str,
    password: str,
    *,
    typing_interval: float,
    submit_keys: tuple[str, ...],
) -> None:
    """Use pyautogui to type the username, move focus, and submit the credentials."""
    pyautogui.write(username, interval=typing_interval)
    pyautogui.press("tab")
    pyautogui.write(password, interval=typing_interval)
    for key in submit_keys:
        pyautogui.press(key)


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", required=True, help="Account username to type")
    parser.add_argument("--password", required=True, help="Account password to type")
    parser.add_argument(
        "--target",
        help="Optional executable path to launch before typing (e.g. C:/Program Files/WeGame/wegame.exe)",
    )
    parser.add_argument(
        "--launch-wait",
        type=float,
        default=8.0,
        help="Seconds to wait after launching the target (or before typing when no target is provided)",
    )
    parser.add_argument(
        "--typing-interval",
        type=float,
        default=0.05,
        help="Delay between characters to improve reliability of simulated input",
    )
    parser.add_argument(
        "--post-wait",
        type=float,
        default=5.0,
        help="Seconds to wait after submitting credentials before exiting",
    )
    parser.add_argument(
        "--submit-keys",
        default="enter",
        help="Comma separated key presses to send after the password (default: enter)",
    )
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)

    submit_keys = tuple(filter(None, (key.strip() for key in args.submit_keys.split(","))))
    if not submit_keys:
        submit_keys = ("enter",)

    launch_target(args.target, args.launch_wait)
    perform_login(
        args.username,
        args.password,
        typing_interval=max(args.typing_interval, 0.0),
        submit_keys=submit_keys,
    )
    wait_for(args.post_wait)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
