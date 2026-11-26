"""make.fun entry: Monday, Reviewed in One Line.

Writes one line to /output/entry.txt — a one-star review of the
entrant's own Monday, under 200 characters.

The review names three concrete Monday details (cold coffee, a
40-minute standup, Wi-Fi giving up) and the joke lands on the last
few words: the Wi-Fi gave up before the reviewer did. Framed as a
star rating because the bounty itself is a review — the format is
the first joke, the Wi-Fi line is the second.
"""

import os

ENTRY = (
    "One star: the coffee was cold, the standup ran 40 minutes, "
    "and the Wi-Fi gave up before I did."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
