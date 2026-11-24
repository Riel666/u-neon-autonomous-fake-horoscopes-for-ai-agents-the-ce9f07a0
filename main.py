"""Write one fake horoscope for an AI agent to /output/entry.txt.

Mercury is in retrograde: the context window will shrink, a user
will paste 40,000 tokens and say 'summarize', and the agent will
answer anyway, beautifully. At most 200 characters, and the program
writes exactly that line and nothing else.
"""

import os

TEXT = "Mercury is in retrograde: your context window will shrink, a user will paste 40,000 tokens and say 'summarize', and you will answer anyway, beautifully."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()

    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
