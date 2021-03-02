#!/usr/bin/env python3

# Imports (standard library)
import io
import math
import re
import sys

# Imports (external)
import svgwrite
import yaml

if sys.version_info < (3, 0):
    print("This script requires Python 3.x.")
    sys.exit(1)

# Constants
# A hack to change text color via CSS
# Using the class name would be more proper, but it is mangled by Docusaurus
THEME_TEXT_COLOR = "#000001"
CARD_ROUNDED_CORNER_SIZE = 5
CARD_WIDTH = 70

# Variables
have_rainbow = False
have_whitenum = False
x_offset = 0
y_offset = 0
y_top = 0


# -----------
# Subroutines
# -----------


def draw_play_stacks():
    spacing = 4
    x_offset = 0

    for color_value in yaml_file["stacks"]:
        color, value = next(iter(color_value.items()))

        if value:
            file_name = "{}{}".format(color, value)
        else:
            file_name = "back-{}".format(color)

        draw.add(
            draw.image(
                "/img/pieces/{}.svg".format(file_name),
                x=x_offset,
                y=50,
                width=70,
                height=100,
            )
        )

        x_offset += CARD_WIDTH + spacing

    return x_offset


def draw_textbox(opts, offset):
    if type(opts) == str:
        text = [opts]
        color = text[0].split()[0].lower()
        if color not in (
            "red",
            "yellow",
            "black",
            "purple",
            "blue",
            "green",
            "rainbow",
        ):
            color = "black"
    else:
        text = opts["text"]
        if type(text) == str:
            text = [text]
        color = opts.get("color", "black")

    # TODO: make this widening more generic
    if text[0].startswith("Rainbow"):
        wid = 85
        r = draw.add(
            draw.svg((x_offset - 10, y_offset + offset), (wid, 20 * len(text)))
        )
    else:
        wid = 64
        r = draw.add(draw.svg((x_offset + 3, y_offset + offset), (wid, 20 * len(text))))
    textcolor = "black" if color in ("gold", "rainbow") else "white"

    if color == "rainbow":
        r.add(
            draw.rect(
                (0, 0),
                (wid, 20 * len(text)),
                stroke=textcolor,
                fill="url(#rainbowtext)",
            )
        )
        global have_rainbow
        have_rainbow = True
    else:
        r.add(
            draw.rect(
                (0, 0),
                (wid, 20 * len(text)),
                stroke=textcolor,
                fill=color,
            )
        )

    for i, line in enumerate(text):
        l = r.add(draw.svg((0, 20 * i), (wid, 20)))
        t = l.add(draw.text(line, x=["50%"], y=["50%"], fill=textcolor))
        t["text-anchor"] = "middle"
        t["dominant-baseline"] = "central"

    return 20 * len(text)


def draw_unknown_card(svg, positives):
    rank_pip_width = CARD_WIDTH / 5
    for n in range(1, 6):
        if n in positives:
            rank_pip_rectangle = svg.add(
                draw.svg(((n - 1) * rank_pip_width, 80), (rank_pip_width, 20))
            )
            rank_pip_text_element = rank_pip_rectangle.add(
                draw.text(
                    str(n),
                    x=["50%"],
                    y=["50%"],
                    fill="white",
                    style="filter: url(#shadow)",
                )
            )
            rank_pip_text_element["text-anchor"] = "middle"
            rank_pip_text_element["dominant-baseline"] = "central"
    suit_pips_combined_svg = svg.add(draw.svg((0, 0), (70, 100)))
    suit_pips_combined_svg["viewBox"] = "-35 -50 70 100"
    angle = 2 * math.pi / len(all_colors)
    for i, color in enumerate(all_colors):
        if color in positives:
            suit_pips_combined_svg.add(
                draw.image(
                    "/img/pieces/pip-{}.svg".format(color),
                    x=-6,
                    y=-6,
                    width=12,
                    height=12,
                    style="filter: url(#shadow)",
                    transform="translate({}, {})".format(
                        -20 * math.sin(angle * i), -20 * math.cos(angle * i)
                    ),
                )
            )


# ----
# Main
# ----

# This script reads from standard in, expecting a YAML file
# Decode it to YAML
yaml_file = yaml.load(sys.stdin, Loader=yaml.SafeLoader)

# Use the stack colors to determine the available colors in this particular
# variant
all_colors = [next(iter(color_pair)) for color_pair in yaml_file["stacks"]]

# Create a new SVG file
draw = svgwrite.Drawing()

# Draw the play stacks on the top-left part of the image
x_offset = draw_play_stacks()

# Add a bit of spacing between the play stacks and the player hands
x_offset += 72

x_offset_of_players_first_card = x_offset
x_max = x_offset_of_players_first_card

for line_dict in yaml_file["players"]:
    if "text" in line_dict:
        draw.add(
            draw.text(
                line_dict["text"],
                x=[x_offset_of_players_first_card + 40],
                y=[y_offset],
                dy=[20],
                fill=THEME_TEXT_COLOR,
            )
        )
        y_offset += 30
    else:
        draw.add(
            draw.text(
                line_dict["name"],
                x=[x_offset_of_players_first_card],
                y=[y_offset],
                dy=[50],
                fill=THEME_TEXT_COLOR,
            )
        )
        if "cluegiver" in line_dict:
            draw.add(
                draw.text(
                    "(clue",
                    x=[x_offset_of_players_first_card],
                    y=[y_offset],
                    dy=[70],
                    fill=THEME_TEXT_COLOR,
                )
            )
            draw.add(
                draw.text(
                    "giver)",
                    x=[x_offset_of_players_first_card],
                    y=[y_offset],
                    dy=[90],
                    fill=THEME_TEXT_COLOR,
                )
            )
        x_offset = x_offset_of_players_first_card + 60
        y_below = 5
        negatives = set()
        for card in line_dict["cards"]:
            if "negate" in card:
                negatives.add(card["negate"])
                continue
            t = str(card["type"])
            if t == "x":
                s = draw.add(draw.svg((x_offset, y_offset + 10), (70, 100)))
                s.add(
                    draw.rect(
                        (0, 0),
                        (70, 100),
                        fill="gray",
                        rx=CARD_ROUNDED_CORNER_SIZE,
                        ry=CARD_ROUNDED_CORNER_SIZE,
                    )
                )
                draw_unknown_card(s, (set(all_colors) | set(range(1, 6))) - negatives)
            else:
                numbers = set(t) & {"1", "2", "3", "4", "5"}
                if numbers:
                    numbers = set(int(i) for i in numbers)
                else:
                    numbers = set(range(1, 6)) - negatives
                colors = set(t) & set(
                    next(iter(color_pair)) for color_pair in yaml_file["stacks"]
                )
                if not colors:
                    colors = (
                        set(
                            next(iter(color_pair)) for color_pair in yaml_file["stacks"]
                        )
                        - negatives
                    )
                draw.add(
                    draw.rect(
                        (x_offset - 1, y_offset - 1),
                        (72, 102),
                        fill="orange",
                        rx=CARD_ROUNDED_CORNER_SIZE,
                        ry=CARD_ROUNDED_CORNER_SIZE,
                    )
                )
                if len(numbers) > 1 and len(colors) > 1:
                    s = draw.add(draw.svg((x_offset, y_offset), (70, 100)))
                    s.add(
                        draw.rect(
                            (0, 0),
                            (70, 100),
                            fill="gray",
                            rx=CARD_ROUNDED_CORNER_SIZE,
                            ry=CARD_ROUNDED_CORNER_SIZE,
                        )
                    )
                    draw_unknown_card(s, numbers | colors)
                elif len(numbers) == 1 and len(colors) > 1:
                    s = draw.add(draw.svg((x_offset, y_offset), (70, 100)))
                    s.add(
                        draw.image(
                            "/img/pieces/{}.svg".format(next(iter(numbers))),
                            x=0,
                            y=0,
                            width=70,
                            height=100,
                        )
                    )
                    draw_unknown_card(s, colors)
                elif len(numbers) > 1 and len(colors) == 1:
                    s = draw.add(draw.svg((x_offset, y_offset), (70, 100)))
                    s.add(
                        draw.image(
                            "/img/pieces/{}.svg".format(next(iter(colors))),
                            x=0,
                            y=0,
                            width=70,
                            height=100,
                        )
                    )
                    draw_unknown_card(s, numbers)
                else:
                    draw.add(
                        draw.image(
                            "/img/pieces/{}.svg".format(t),
                            x=x_offset,
                            y=y_offset,
                            width=70,
                            height=100,
                        )
                    )
            if "clue" in card:
                draw.add(
                    draw.image(
                        "/img/pieces/arrow.svg",
                        x=x_offset + 10,
                        y=y_offset - 40,
                        width=50,
                        height=70,
                    )
                )
                color = {
                    "r": "red",
                    "b": "blue",
                    "g": "lightgreen",
                    "y": "yellow",
                    "p": "blueviolet",
                }.get(card["clue"], "black")
                draw.add(
                    draw.circle(
                        (x_offset + 35, y_offset - 15),
                        r=15,
                        fill=color,
                        stroke="white" if color == "black" else "black",
                        **{"stroke-width": 2}
                    )
                )
                img = draw.add(
                    draw.image(
                        "/img/pieces/pip-{}.svg".format(card["clue"]),
                        x=x_offset + 27,
                        y=y_offset - 23,
                        width=16,
                        height=16,
                    )
                )
                if card["clue"] in range(1, 6):
                    img["style"] = "filter: url(#whitenum)"
                    have_whitenum = True
                else:
                    img["style"] = "filter: url(#shadow)"

                if y_offset < 20:
                    y_top = -20
            if "above" in card:
                draw_textbox(card["above"], 0)
            if "below" in card:
                yb = draw_textbox(card["below"], 105)
                if yb > y_below:
                    y_below = yb
            if "ontop" in card:
                color = {
                    "(R)": "red",
                    "(B)": "cyan",
                    "(G)": "lightgreen",
                    "(Y)": "yellow",
                    "(P)": "violet",
                }.get(card["ontop"], "white")
                draw.add(
                    draw.text(
                        card["ontop"],
                        x=[x_offset + 35],
                        y=[y_offset],
                        dy=[30],
                        fill=color,
                        stroke=color,
                        style="filter: url(#shadow)",
                    )
                )
            x_offset += 74
        y_offset += 120 + y_below
        if x_offset > x_max:
            x_max = x_offset

draw["width"] = x_max
draw["height"] = y_offset - y_top
draw["viewBox"] = "0 {} {} {}".format(y_top, x_max, y_offset)

out = io.StringIO()
draw.write(out, pretty=True)
out = out.getvalue()
# workround stupid docusaurus/react error similar to this one:
# https://github.com/facebook/docusaurus/issues/3689
out = re.sub(r'xmlns:ev="(?:.*?)"', "", out)
# add shadow filter manually, because svgwrite's API for it is awkward
out = re.sub(
    r"<defs/>",
    """<defs>
    <filter id="shadow">
    <feOffset in="SourceAlpha" dx="2" dy="2" result="offsetblur"/>
    <feComponentTransfer result="shadow">
        <feFuncA type="linear" slope="0.5"/>
    </feComponentTransfer>
    <feMorphology in="SourceAlpha" operator="dilate" radius="1" result="border"/>
    <feMerge>
        <feMergeNode in="shadow"/>
        <feMergeNode in="border"/>
        <feMergeNode in="SourceGraphic"/>
    </feMerge>
    </filter>"""
    + (
        """
      <filter id="whitenum">
      <feComponentTransfer>
        <feFuncR type="linear" slope="100"/>
        <feFuncG type="linear" slope="100"/>
        <feFuncB type="linear" slope="100"/>
      </feComponentTransfer>
    </filter>
        """
        if have_whitenum
        else ""
    )
    + (
        """
    <linearGradient id="rainbowtext" x1="0" y1="0" x2="100%" y2="0">
    <stop offset="0" stop-color="#ff7777"></stop>
    <stop offset="0.25" stop-color="#ffff77"></stop>
    <stop offset="0.5" stop-color="#77ff77"></stop>
    <stop offset="0.75" stop-color="#77ffff"></stop>
    <stop offset="1" stop-color="#7777ff"></stop>
    </linearGradient>"""
        if have_rainbow
        else ""
    )
    + """
</defs>""",
    out,
    count=1,
)

# Write the resulting SVG to stdout
print(out)
