import random
import argparse
import textwrap

#!/usr/bin/env python3
"""
poem.py - Simple poem generator

Usage:
    python poem.py            # generate a 4-line nature poem
    python poem.py --theme city --lines 6 --seed 42
"""


WORD_BANKS = {
        "nature": {
                "n": ["river", "pine", "dawn", "hill", "leaf", "cloud", "stone", "meadow", "ocean"],
                "v": ["whispers", "wanders", "sleeps", "breathes", "glows", "cradles", "rests", "rises"],
                "adj": ["quiet", "ancient", "soft", "golden", "lonely", "gentle", "wild", "clear"],
                "prep": ["beneath", "above", "beside", "within", "beyond", "among"]
        },
        "city": {
                "n": ["street", "window", "lamp", "train", "tower", "alley", "coffee", "crowd"],
                "v": ["hums", "hurries", "blinks", "sleeps", "echoes", "fades", "sparks", "lingers"],
                "adj": ["neon", "restless", "narrow", "bright", "rusted", "endless", "warm"],
                "prep": ["under", "through", "behind", "around", "against"]
        },
        "love": {
                "n": ["heart", "hand", "letter", "remembering", "promise", "kiss", "silence"],
                "v": ["keeps", "holds", "remembers", "waits", "longs", "answers", "searches"],
                "adj": ["tender", "faint", "true", "hidden", "soft", "aching"],
                "prep": ["within", "beside", "between", "inside"]
        },
        "random": {}  # will be filled dynamically
}

LINE_TEMPLATES = [
        "The {adj} {n} {v} {prep} the {adj2} {n2}.",
        "{Adj} as a {n}, the {n2} {v}.",
        "I hear the {n} {v} in {prep} the {n2}.",
        "A {adj} {n} {v} like {n2}.",
        "{adj} {n}, {adj2} {n2}, {v} and {v2}.",
        "Tonight the {n} {v} {prep} moonlight."
]


def build_random_bank():
        all_words = []
        for theme in ("nature", "city", "love"):
                bank = WORD_BANKS[theme]
                for lst in bank.values():
                        all_words.extend(lst)
        # simple partitioning: reuse words across categories by choosing nearest matches
        return {
                "n": [w for w in all_words if len(w) <= 7][:60] or all_words[:10],
                "v": [w for w in all_words if w.endswith("s")][:60] or all_words[10:20],
                "adj": [w for w in all_words if len(w) <= 6][:60] or all_words[20:30],
                "prep": ["beneath", "above", "within", "around"]
        }


def choose(bank, key):
        return random.choice(bank[key])


def generate_line(bank):
        tpl = random.choice(LINE_TEMPLATES)
        # ensure we have enough slots
        ctx = {}
        ctx["n"] = choose(bank, "n")
        ctx["n2"] = choose(bank, "n")
        ctx["v"] = choose(bank, "v")
        ctx["v2"] = choose(bank, "v")
        ctx["adj"] = choose(bank, "adj")
        ctx["adj2"] = choose(bank, "adj")
        ctx["prep"] = choose(bank, "prep")
        # some templates expect capitalized Adj
        ctx["Adj"] = ctx["adj"].capitalize()
        return tpl.format(**ctx)


def generate_poem(lines=4, theme="nature", seed=None):
        if seed is not None:
                random.seed(seed)
        theme = theme.lower()
        if theme not in WORD_BANKS:
                theme = "random"
        bank = WORD_BANKS.get(theme)
        if theme == "random" or not bank:
                bank = build_random_bank()
        poem_lines = [generate_line(bank) for _ in range(lines)]
        return "\n".join(poem_lines)


def main():
        p = argparse.ArgumentParser(description="Simple poem generator")
        p.add_argument("--lines", "-l", type=int, default=4, help="number of lines")
        p.add_argument("--theme", "-t", type=str, default="nature", help="theme: nature, city, love, random")
        p.add_argument("--seed", "-s", type=int, default=None, help="random seed for reproducibility")
        args = p.parse_args()

        title = f"{args.theme.capitalize()} Poem"
        border = "-" * len(title)
        poem = generate_poem(lines=max(1, args.lines), theme=args.theme, seed=args.seed)

        output = "\n".join([title, border, poem])
        print(textwrap.dedent(output))


if __name__ == "__main__":
        main()