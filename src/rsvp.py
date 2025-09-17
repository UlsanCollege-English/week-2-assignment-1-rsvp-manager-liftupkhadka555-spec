from typing import List, Tuple


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """Return a new list with duplicate emails removed, preserving first seen.

    Treat emails case-insensitively ("ALICE@x.com" == "alice@x.com").
    Keep the first form you saw.

    Ignore entries that do not contain an '@' character.
    """
    seen = set()
    result = []
    for email in emails:
        if "@" not in email:
            continue
        lower = email.lower()
        if lower not in seen:
            seen.add(lower)
            result.append(email)
    return result


def first_with_domain(emails: List[str], domain: str) -> int | None:
    """Return the index of the first email whose domain matches `domain`.

    Examples:
        emails=["a@x.com","b@y.com"], domain="y.com" -> 1
        no match -> None
    Comparison is case-insensitive.
    """
    target = domain.lower()
    for i, email in enumerate(emails):
        if "@" not in email:
            continue
        _, _, dom = email.partition("@")
        if dom.lower() == target:
            return i
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """Return (domain, count) pairs sorted by domain (A..Z), case-insensitive.

    Skip malformed entries without an '@'.
    Example: ["a@x.com","b@x.com","c@y.com"] -> [("x.com", 2), ("y.com", 1)]
    """
    counts = {}
    for email in emails:
        if "@" not in email:
            continue
        _, _, dom = email.partition("@")
        dom_lower = dom.lower()
        counts[dom_lower] = counts.get(dom_lower, 0) + 1

    return sorted(counts.items(), key=lambda x: x[0].lower())
