import argparse
from collections import defaultdict


def get_keyboard(layout):
    if layout == "qwerty":
        return {
            "q": (0, 0), "w": (1, 0), "e": (2, 0), "r": (3, 0), "t": (4, 0),
            "y": (5, 0), "u": (6, 0), "i": (7, 0), "o": (8, 0), "p": (9, 0),

            "a": (0.5, 1), "s": (1.5, 1), "d": (2.5, 1), "f": (3.5, 1),
            "g": (4.5, 1), "h": (5.5, 1), "j": (6.5, 1), "k": (7.5, 1),
            "l": (8.5, 1),

            "z": (1, 2), "x": (2, 2), "c": (3, 2), "v": (4, 2),
            "b": (5, 2), "n": (6, 2), "m": (7, 2)
        }

    return {
        "q": (0, 0), "w": (1, 0), "e": (2, 0), "r": (3, 0), "t": (4, 0),
        "z": (5, 0), "u": (6, 0), "i": (7, 0), "o": (8, 0), "p": (9, 0),

        "a": (0.5, 1), "s": (1.5, 1), "d": (2.5, 1), "f": (3.5, 1),
        "g": (4.5, 1), "h": (5.5, 1), "j": (6.5, 1), "k": (7.5, 1),
        "l": (8.5, 1),

        "y": (1, 2), "x": (2, 2), "c": (3, 2), "v": (4, 2),
        "b": (5, 2), "n": (6, 2), "m": (7, 2)
    }


def build_neighbors(keys):
    neighbors = defaultdict(set)

    for a, (x1, y1) in keys.items():
        for b, (x2, y2) in keys.items():
            if a != b:
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

                if distance <= 1.1:
                    neighbors[a].add(b)

    return neighbors


def find_longest_path(word, keys, neighbors):
    word = word.lower()

    longest = ""

    for start in range(len(word)):
        path = ""
        used = set()

        for char in word[start:]:
            if char not in keys:
                break

            if char in used:
                break

            if path and char not in neighbors[path[-1]]:
                break

            path += char
            used.add(char)

            if len(path) > len(longest):
                longest = path

    return longest


def main():
    parser = argparse.ArgumentParser(
        description="find keyboard paths inside words."
    )

    parser.add_argument(
        "wordlist",
        help="word list file"
    )

    layout = parser.add_mutually_exclusive_group()

    layout.add_argument(
        "--qwerty",
        action="store_true",
        help="use qwerty keyboard layout"
    )

    layout.add_argument(
        "--qwertz",
        action="store_true",
        help="use qwertz keyboard layout"
    )

    args = parser.parse_args()

    keyboard_layout = "qwerty" if args.qwerty else "qwertz"

    keys = get_keyboard(keyboard_layout)
    neighbors = build_neighbors(keys)

    results = []

    with open(args.wordlist, encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()

            path = find_longest_path(
                word,
                keys,
                neighbors
            )

            if len(path) >= 3:
                results.append(
                    (len(path), path, word)
                )

    results.sort(
        key=lambda x: (-x[0], x[1], x[2])
    )

    print(f"keyboard-path-finder | {args.wordlist} | {keyboard_layout}\n")

    for length, path, word in results[:20]:
        print(f"{length} {path:<15} {word}")


if __name__ == "__main__":
    main()
