#!/usr/bin/env python3
"""Render the wearable-light field-study checklist from its Markdown source."""

from __future__ import annotations

import argparse
import html
import re
from copy import copy
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    FrameBreak,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


PAGE_WIDTH, PAGE_HEIGHT = A4

# Geometry is in PDF points. The values retain the established A4 layout.
CONTENT_LEFT = 29.76378
CONTENT_RIGHT = 565.5118
DIVIDER_X = 297.6378
FRAME_BOTTOM = 36.85039
FRAME_TOP = 803.622
FRAME_WIDTH = 268.0787
FRAME_LEFT = CONTENT_LEFT - 4
FRAME_RIGHT = 301.4331
TOTAL_PAGES = 4
H2_HEIGHT = 32
H2_GAP = 9
CODE_POST_GAP = 8.5

DARK_BLUE = HexColor("#153A52")
TEAL = HexColor("#0F6D78")
BODY = HexColor("#24313A")
MUTED = HexColor("#566570")
RULE = HexColor("#C8D4DA")
INFO_BG = HexColor("#FFF4D6")
INFO_BORDER = HexColor("#D5A43A")
SCOPE_BG = INFO_BG
CODE_BG = INFO_BG
CONTEXT_BG = INFO_BG
CONTEXT_BORDER = INFO_BORDER
RED_FLAG = HexColor("#C63D32")
RED_FLAG_BG = HexColor("#FFF3F1")
RED_FLAG_BORDER = HexColor("#D9A6A0")
CHECKBOX_TEXT_INDENT = 13


class IconParagraph(Flowable):
    """A paragraph with a vector checkbox or circular flag icon."""

    def __init__(
        self,
        value: str,
        style: ParagraphStyle,
        *,
        icon: str,
        icon_width: float = 13,
    ) -> None:
        super().__init__()
        self._paragraph = Paragraph(value, style)
        self._style = style
        self._icon = icon
        self._icon_width = icon_width

    def wrap(self, avail_width: float, avail_height: float) -> tuple[float, float]:
        paragraph_width = max(1, avail_width - self._icon_width)
        _, paragraph_height = self._paragraph.wrap(paragraph_width, avail_height)
        self.width = avail_width
        self.height = paragraph_height
        return self.width, self.height

    def getSpaceBefore(self) -> float:
        return self._style.spaceBefore

    def getSpaceAfter(self) -> float:
        return self._style.spaceAfter

    def draw(self) -> None:
        self._paragraph.drawOn(self.canv, self._icon_width, 0)
        self.canv.saveState()
        if self._icon == "checkbox":
            size = 5.2
            self.canv.setStrokeColor(TEAL)
            self.canv.setLineWidth(0.7)
            self.canv.rect(1.0, self.height - 6.8, size, size, stroke=1, fill=0)
        elif self._icon == "flag_circle":
            center_x = 5.1
            center_y = self.height - (self._style.leading / 2) + 0.25
            self.canv.setFillColor(RED_FLAG)
            self.canv.circle(center_x, center_y, 4.25, stroke=0, fill=1)

            pole_x = center_x - 1.2
            self.canv.setStrokeColor(white)
            self.canv.setFillColor(white)
            self.canv.setLineWidth(0.65)
            self.canv.line(
                pole_x,
                center_y + 2.3,
                pole_x,
                center_y - 2.35,
            )
            flag = self.canv.beginPath()
            flag.moveTo(pole_x + 0.25, center_y + 2.1)
            flag.lineTo(center_x + 2.25, center_y + 1.05)
            flag.lineTo(pole_x + 0.25, center_y)
            flag.close()
            self.canv.drawPath(flag, stroke=0, fill=1)
        self.canv.restoreState()


def fresh_style(base: ParagraphStyle, suffix: str) -> ParagraphStyle:
    """Return an instance-local style so boundary normalisation is safe."""
    result = copy(base)
    result.name = f"{base.name}-{suffix}"
    return result


def make_styles() -> dict[str, ParagraphStyle]:
    sample = getSampleStyleSheet()
    styles: dict[str, ParagraphStyle] = {}

    styles["title"] = ParagraphStyle(
        "ChecklistTitle",
        parent=sample["Normal"],
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=18.8,
        textColor=DARK_BLUE,
        spaceBefore=0,
        spaceAfter=0,
    )
    styles["subtitle"] = ParagraphStyle(
        "ChecklistSubtitle",
        parent=sample["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.7,
        leading=9.2,
        textColor=TEAL,
        spaceBefore=9.5,
        spaceAfter=0,
    )
    styles["scope"] = ParagraphStyle(
        "ChecklistScope",
        parent=sample["Normal"],
        fontName="Helvetica",
        fontSize=7.3,
        leading=9.1,
        textColor=BODY,
        backColor=SCOPE_BG,
        borderColor=INFO_BORDER,
        borderWidth=0.55,
        borderPadding=(5.2, 6, 5.2, 6),
        leftIndent=6,
        rightIndent=6,
        spaceBefore=9,
        spaceAfter=0,
    )
    styles["byline"] = ParagraphStyle(
        "ChecklistByline",
        parent=sample["Normal"],
        fontName="Helvetica",
        fontSize=6.8,
        leading=8.2,
        textColor=MUTED,
        spaceBefore=4,
        spaceAfter=0,
    )
    styles["h2"] = ParagraphStyle(
        "ChecklistH2",
        parent=sample["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=12.2,
        textColor=white,
        spaceBefore=0,
        spaceAfter=0,
        keepWithNext=True,
    )
    styles["h3"] = ParagraphStyle(
        "ChecklistH3",
        parent=sample["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.8,
        leading=10.5,
        textColor=TEAL,
        spaceBefore=6.5,
        spaceAfter=3.4,
        keepWithNext=True,
    )
    styles["h4"] = ParagraphStyle(
        "ChecklistH4",
        parent=sample["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.6,
        leading=9.2,
        textColor=BODY,
        spaceBefore=6.2,
        spaceAfter=3.4,
        keepWithNext=True,
    )
    styles["check"] = ParagraphStyle(
        "ChecklistItem",
        parent=sample["Normal"],
        fontName="Helvetica",
        fontSize=7.35,
        leading=9.1,
        textColor=BODY,
        leftIndent=0,
        firstLineIndent=0,
        spaceBefore=0,
        spaceAfter=3,
        allowWidows=0,
        allowOrphans=0,
    )
    styles["body"] = ParagraphStyle(
        "ChecklistBody",
        parent=sample["Normal"],
        fontName="Helvetica",
        fontSize=7.4,
        leading=9.2,
        textColor=BODY,
        spaceBefore=0,
        spaceAfter=3.1,
        allowWidows=0,
        allowOrphans=0,
    )
    styles["code"] = ParagraphStyle(
        "ChecklistCode",
        parent=sample["Code"],
        fontName="Courier",
        fontSize=6.25,
        leading=7.8,
        textColor=DARK_BLUE,
        backColor=CODE_BG,
        borderColor=INFO_BORDER,
        borderWidth=0.55,
        borderPadding=(5, 6, 5, 6),
        leftIndent=CHECKBOX_TEXT_INDENT + 6,
        rightIndent=6,
        firstLineIndent=0,
        spaceBefore=6,
        spaceAfter=0,
    )
    styles["context"] = ParagraphStyle(
        "ChecklistContext",
        parent=sample["Normal"],
        fontName="Helvetica",
        fontSize=7.0,
        leading=8.65,
        textColor=BODY,
        backColor=CONTEXT_BG,
        borderColor=CONTEXT_BORDER,
        borderWidth=0.55,
        borderPadding=(5, 6, 5, 6),
        leftIndent=CHECKBOX_TEXT_INDENT + 6,
        rightIndent=6,
        spaceBefore=9,
        spaceAfter=9,
    )
    styles["red_flag_title"] = ParagraphStyle(
        "ChecklistRedFlagTitle",
        parent=sample["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.8,
        leading=10.5,
        textColor=RED_FLAG,
        spaceBefore=0,
        spaceAfter=4.5,
        keepWithNext=True,
    )
    styles["red_flag_item"] = ParagraphStyle(
        "ChecklistRedFlagItem",
        parent=sample["Normal"],
        fontName="Helvetica",
        fontSize=7.0,
        leading=8.45,
        textColor=BODY,
        leftIndent=0,
        firstLineIndent=0,
        spaceBefore=0,
        spaceAfter=1.8,
        allowWidows=0,
        allowOrphans=0,
    )
    styles["source_h3"] = ParagraphStyle(
        "ChecklistSourceH3",
        parent=sample["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.3,
        leading=8.6,
        textColor=TEAL,
        spaceBefore=4,
        spaceAfter=2,
        keepWithNext=True,
    )
    styles["source_item"] = ParagraphStyle(
        "ChecklistSourceItem",
        parent=sample["Normal"],
        fontName="Helvetica",
        fontSize=6.15,
        leading=7.45,
        textColor=BODY,
        leftIndent=8,
        firstLineIndent=-8,
        spaceBefore=0,
        spaceAfter=0.9,
        allowWidows=0,
        allowOrphans=0,
    )
    styles["source_body"] = ParagraphStyle(
        "ChecklistSourceBody",
        parent=sample["Normal"],
        fontName="Helvetica",
        fontSize=6.4,
        leading=7.7,
        textColor=BODY,
        spaceBefore=0,
        spaceAfter=1.5,
        allowWidows=0,
        allowOrphans=0,
    )
    return styles


LINK_PATTERN = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
CODE_PATTERN = re.compile(r"`([^`]+)`")
BOLD_PATTERN = re.compile(r"\*\*(.+?)\*\*")
ITALIC_PATTERN = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
SUPERSCRIPT_PATTERN = re.compile(r"\^\{([^{}]+)\}")
CITATION_GROUP_PATTERN = re.compile(
    r"\[((?:[SL]\d+[a-z]?)(?:,\s*[SL]\d+[a-z]?)*)\]"
)
SOURCE_TARGET_PATTERN = re.compile(
    r"^-\s+\*\*\[([SL]\d+[a-z]?)\s+[^\]]+\]\((https?://[^)]+)\):\*\*"
)


def markdown_inline(value: str, source_targets: dict[str, str]) -> str:
    """Convert the limited inline Markdown used by the checklist to ReportLab XML."""
    value = html.escape(value, quote=True)

    def link(match: re.Match[str]) -> str:
        label, url = match.groups()
        return (
            f'<link href="{url}" color="{TEAL.hexval()}">'
            f"<u>{label}</u></link>"
        )

    value = LINK_PATTERN.sub(link, value)

    def citation_group(match: re.Match[str]) -> str:
        codes = [code.strip() for code in match.group(1).split(",")]
        rendered: list[str] = []
        for code in codes:
            url = source_targets.get(code)
            if url:
                rendered.append(
                    f'<link href="{html.escape(url, quote=True)}" '
                    f'color="{TEAL.hexval()}"><u>{code}</u></link>'
                )
            else:
                rendered.append(code)
        return "[" + ", ".join(rendered) + "]"

    value = CITATION_GROUP_PATTERN.sub(citation_group, value)
    value = CODE_PATTERN.sub(r'<font name="Courier">\1</font>', value)
    value = SUPERSCRIPT_PATTERN.sub(r"<super>\1</super>", value)
    value = BOLD_PATTERN.sub(r"<b>\1</b>", value)
    value = ITALIC_PATTERN.sub(r"<i>\1</i>", value)
    return value


def paragraph(
    value: str,
    base_style: ParagraphStyle,
    sequence: int,
    source_targets: dict[str, str],
    *,
    is_h2: bool = False,
) -> Paragraph:
    result = Paragraph(
        markdown_inline(value, source_targets),
        fresh_style(base_style, str(sequence)),
    )
    result._checklist_h2 = is_h2  # type: ignore[attr-defined]
    return result


def build_story(markdown_path: Path, styles: dict[str, ParagraphStyle]) -> list:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    story: list = []
    sequence = 0
    source_mode = False
    red_flag_title: str | None = None
    red_flag_items: list[str] = []
    source_targets = {
        match.group(1): match.group(2)
        for raw_line in lines
        if (match := SOURCE_TARGET_PATTERN.match(raw_line.strip()))
    }

    def add_paragraph(value: str, style_key: str, *, is_h2: bool = False) -> None:
        nonlocal sequence
        sequence += 1
        story.append(
            paragraph(
                value,
                styles[style_key],
                sequence,
                source_targets,
                is_h2=is_h2,
            )
        )

    def flush_red_flag_panel() -> None:
        nonlocal sequence, red_flag_title, red_flag_items
        if red_flag_title is None:
            return

        sequence += 1
        panel_flowables: list = [
            paragraph(
                red_flag_title,
                styles["red_flag_title"],
                sequence,
                source_targets,
            )
        ]
        for index, item in enumerate(red_flag_items):
            sequence += 1
            item_style = fresh_style(
                styles["red_flag_item"],
                f"{sequence}-panel",
            )
            if index == len(red_flag_items) - 1:
                item_style.spaceAfter = 0
            panel_flowables.append(
                IconParagraph(
                    markdown_inline(item, source_targets),
                    item_style,
                    icon="flag_circle",
                    icon_width=14,
                )
            )

        panel = Table(
            [[panel_flowables]],
            colWidths=[FRAME_WIDTH - 8],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), RED_FLAG_BG),
                    ("BOX", (0, 0), (-1, -1), 0.75, RED_FLAG_BORDER),
                    ("LEFTPADDING", (0, 0), (-1, -1), 7),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ]
            ),
            spaceBefore=8,
            spaceAfter=8,
        )
        story.append(panel)
        red_flag_title = None
        red_flag_items = []

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if red_flag_title is not None:
            if line.startswith("- [!] "):
                red_flag_items.append(line[6:])
                continue
            flush_red_flag_panel()
        if line == "<!-- COLUMN -->":
            story.append(FrameBreak())
            continue
        if line == "<!-- PAGE -->":
            story.append(PageBreak())
            continue
        if line.startswith("<!--") and line.endswith("-->"):
            continue
        if line.startswith("# "):
            add_paragraph(line[2:], "title")
            continue
        if line.startswith("## "):
            heading = line[3:]
            # Numbered headings are checklist sections; the unnumbered final H2
            # is the source trace. Its displayed wording comes from Markdown.
            source_mode = re.match(r"^\d+\.", heading) is None
            story.append(Spacer(1, H2_GAP))
            sequence += 1
            heading_paragraph = paragraph(
                heading,
                styles["h2"],
                sequence,
                source_targets,
            )
            heading_bar = Table(
                [[heading_paragraph]],
                colWidths=[FRAME_WIDTH - 8],
                rowHeights=[H2_HEIGHT],
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), DARK_BLUE),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 5),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                        ("TOPPADDING", (0, 0), (-1, -1), 0),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                    ]
                ),
                hAlign="LEFT",
            )
            heading_bar._checklist_h2 = True  # type: ignore[attr-defined]
            story.append(heading_bar)
            story.append(Spacer(1, H2_GAP))
            continue
        if line.startswith("### Red flags:"):
            red_flag_title = line[4:]
            continue
        if line.startswith("### "):
            add_paragraph(line[4:], "source_h3" if source_mode else "h3")
            continue
        if line.startswith("- [ ] "):
            item = line[6:]
            sequence += 1
            story.append(
                IconParagraph(
                    markdown_inline(item, source_targets),
                    fresh_style(styles["check"], str(sequence)),
                    icon="checkbox",
                )
            )
            continue
        if line.startswith("- [!] "):
            item = line[6:]
            sequence += 1
            story.append(
                IconParagraph(
                    markdown_inline(item, source_targets),
                    fresh_style(styles["red_flag_item"], str(sequence)),
                    icon="flag_circle",
                    icon_width=14,
                )
            )
            continue
        if source_mode and line.startswith("- "):
            add_paragraph(f"- {line[2:]}", "source_item")
            continue
        if line.startswith("`") and line.endswith("`"):
            sequence += 1
            code_text = (
                '<font name="Helvetica-Bold" size="7">Core fields.</font><br/>'
                f"{html.escape(line[1:-1], quote=True)}"
            )
            code = Paragraph(
                code_text,
                fresh_style(styles["code"], str(sequence)),
            )
            code._checklist_code = True  # type: ignore[attr-defined]
            story.append(code)
            story.append(Spacer(1, CODE_POST_GAP))
            continue
        if line.startswith("**Planning, collection"):
            add_paragraph(line[2:-2], "subtitle")
            continue
        if line.startswith("**Source guide:"):
            add_paragraph(line[2:-2], "byline")
            continue
        if line.startswith("**Scope.**"):
            add_paragraph(line, "scope")
            continue
        if line.startswith("> "):
            add_paragraph(line[2:], "context")
            continue
        if line.startswith("**") and line.endswith("**"):
            add_paragraph(line[2:-2], "h4")
            continue
        add_paragraph(line, "source_body" if source_mode else "body")

    flush_red_flag_panel()

    # H2 bars are a single visual component: suppress adjacent paragraph margins
    # so each bar has the same measured whitespace above and below.
    for index, item in enumerate(story):
        if not getattr(item, "_checklist_h2", False):
            continue
        if index >= 2 and isinstance(story[index - 2], Paragraph):
            story[index - 2].style.spaceAfter = 0
        if index + 2 < len(story) and isinstance(story[index + 2], Paragraph):
            story[index + 2].style.spaceBefore = 0

    return story


def extract_version(markdown_path: Path) -> str:
    match = re.search(
        r"Version\s+([0-9.]+)",
        markdown_path.read_text(encoding="utf-8"),
    )
    return f"v{match.group(1)}" if match else ""


def draw_page_furniture(
    canvas,
    doc,
    *,
    version: str,
    banner_path: Path,
) -> None:
    page_number = canvas.getPageNumber()
    image = ImageReader(str(banner_path))
    canvas.saveState()

    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.45)
    canvas.line(DIVIDER_X, FRAME_BOTTOM, DIVIDER_X, FRAME_TOP)

    canvas.setFillColor(DARK_BLUE)
    canvas.setFont("Helvetica-Bold", 6.1)

    # Keep the project wordmark in the running header so it never competes
    # with the document title or section content.
    canvas.saveState()
    clip = canvas.beginPath()
    clip.rect(CONTENT_LEFT, 814, 34, 14.52)
    canvas.clipPath(clip, stroke=0, fill=0)
    canvas.drawImage(
        image,
        CONTENT_LEFT - 1,
        806.74,
        width=237.76,
        height=22.53,
        preserveAspectRatio=False,
        mask="auto",
    )
    canvas.restoreState()

    canvas.drawString(
        CONTENT_LEFT + 40,
        818.0787,
        "WEARABLE LIGHT MEASUREMENT IN FIELD STUDIES",
    )
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 5.8)
    canvas.drawRightString(CONTENT_RIGHT, 818.0787, version)
    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(0.9)
    canvas.line(CONTENT_LEFT, 811.5591, CONTENT_RIGHT, 811.5591)

    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.45)
    canvas.line(CONTENT_LEFT, 24.09449, CONTENT_RIGHT, 24.09449)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 5.25)
    license_label = "Text/layout: CC BY 4.0"
    canvas.setFillColor(TEAL)
    canvas.drawString(CONTENT_LEFT, 15.30709, license_label)
    license_width = canvas.stringWidth(license_label, "Helvetica", 5.25)
    canvas.linkURL(
        "https://creativecommons.org/licenses/by/4.0/",
        (
            CONTENT_LEFT,
            13.8,
            CONTENT_LEFT + license_width,
            21.0,
        ),
        relative=0,
    )
    canvas.setFillColor(MUTED)
    canvas.drawRightString(
        CONTENT_RIGHT,
        15.30709,
        f"Page {page_number} / {TOTAL_PAGES}",
    )

    if page_number == TOTAL_PAGES:
        canvas.drawImage(
            image,
            CONTENT_LEFT,
            43.93701,
            width=CONTENT_RIGHT - CONTENT_LEFT,
            height=50.75508,
            preserveAspectRatio=False,
            mask="auto",
        )

    canvas.restoreState()


def render(markdown_path: Path, output_path: Path, banner_path: Path) -> None:
    styles = make_styles()
    story = build_story(markdown_path, styles)
    version = extract_version(markdown_path)

    left_frame = Frame(
        FRAME_LEFT,
        FRAME_BOTTOM,
        FRAME_WIDTH,
        FRAME_TOP - FRAME_BOTTOM,
        leftPadding=4,
        rightPadding=4,
        topPadding=0,
        bottomPadding=0,
        id="left-column",
        showBoundary=0,
    )
    right_frame = Frame(
        FRAME_RIGHT,
        FRAME_BOTTOM,
        FRAME_WIDTH,
        FRAME_TOP - FRAME_BOTTOM,
        leftPadding=4,
        rightPadding=4,
        topPadding=0,
        bottomPadding=0,
        id="right-column",
        showBoundary=0,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(output_path),
        pagesize=A4,
        title="Checklist: Wearable light measurement in field studies",
        subject="Planning, collection, analysis, and reporting checklist for field studies",
        author="RDA Optical Radiation Exposure and Visual Experience Data Working Group",
        leftMargin=0,
        rightMargin=0,
        topMargin=0,
        bottomMargin=0,
        allowSplitting=1,
    )
    doc.addPageTemplates(
        PageTemplate(
            id="two-column-checklist",
            frames=[left_frame, right_frame],
            onPage=lambda canvas, document: draw_page_furniture(
                canvas,
                document,
                version=version,
                banner_path=banner_path,
            ),
        )
    )
    doc.build(story)

    reader = PdfReader(str(output_path))
    if len(reader.pages) != TOTAL_PAGES:
        raise RuntimeError(
            f"Expected a {TOTAL_PAGES}-page checklist, "
            f"rendered {len(reader.pages)} pages."
        )


def parse_args() -> argparse.Namespace:
    repository = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=repository / "output/pdf/light-dosimetry-field-trial-checklist.md",
        help="Markdown source file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repository / "output/pdf/light-dosimetry-field-trial-checklist.pdf",
        help="Rendered PDF file.",
    )
    parser.add_argument(
        "--banner",
        type=Path,
        default=repository / "assets/logo_banner2.png",
        help="MeLiDos and funding-partner banner image.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    render(
        args.input.resolve(),
        args.output.resolve(),
        args.banner.resolve(),
    )


if __name__ == "__main__":
    main()
