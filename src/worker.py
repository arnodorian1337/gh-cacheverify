from __future__ import annotations


def retry_delay(attempt: int) -> int:
    """Return the bounded retry delay used by the reference worker."""
    if attempt < 0:
        raise ValueError("attempt must be non-negative")
    return min(60, 2**attempt)


if __name__ == "__main__":
    print(retry_delay(3))
