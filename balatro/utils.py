from __future__ import annotations

"""Utility helpers for the Balatro CLI project."""

def get_user_input(prompt: str) -> str:
    """Prompt the user for input and allow exiting the game.

    If the user enters ``exit``, ``quit`` or ``q`` (case-insensitive),
    a :class:`SystemExit` is raised so that the program terminates
    gracefully.  Otherwise the raw input string is returned.
    """
    response = input(prompt)
    if response.strip().lower() in {"exit", "quit", "q"}:
        print("Exiting game.")
        raise SystemExit
    return response
