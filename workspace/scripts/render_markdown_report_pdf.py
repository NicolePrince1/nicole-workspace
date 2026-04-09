#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import re
import textwrap
from pathlib import Path

A4_W = 595.28
A4_H = 841.89
LEFT = 54
RIGHT = 541.28
TOP = 790
BOTTOM = 52
CONTENT_W = RIGHT - LEFT

FONTS = {
    "body": ("F1", "Courier", 10.4, 14.0),
    "footer": ("F1", "Courier", 9.0, 11.0),
    "h1": ("F2", "Courier-Bold", 20.0, 24.0),
    "h2": ("F2", "Courier-Bold", 15.0, 19.0),
    "h3": ("F2", "Courier-Bold", 12.0, 16.0),
    "label": ("F2", "Courier-Bold", 11.0, 14.0),
}


def escape_pdf_bytes(data: bytes) -> bytes:
    return data.replace(b"\\", b"\\\\").replace(b"(", b"\\(").replace(b")", b"\\)")


def pdf_text(x: float, y: float, font_key: str, text: str) -> bytes:
    font_ref, _, size, _ = FONTS[font_key]
    raw = escape_pdf_bytes(text.encode("cp1252", errors="replace"))
    return b"BT /%b %.2f Tf %.2f %.2f Td (%b) Tj ET" % (
        font_ref.encode(),
        size,
        x,
        y,
        raw,
    )


def mono_chars(available_width: float, font_size: float) -> int:
    char_width = font_size * 0.6
    return max(10, int(math.floor(available_width / char_width)))


def clean_inline(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = text.replace("\t", " ")
    return re.sub(r"\s+", " ", text).strip()


def parse_markdown(markdown: str):
    blocks = []
    for raw in markdown.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            blocks.append(("blank", ""))
            continue
        if stripped == "---":
            blocks.append(("rule", ""))
            continue
        if line.startswith("# "):
            blocks.append(("h1", clean_inline(line[2:])))
            continue
        if line.startswith("## "):
            blocks.append(("h2", clean_inline(line[3:])))
            continue
        if line.startswith("### "):
            blocks.append(("h3", clean_inline(line[4:])))
            continue
        only_bold = re.fullmatch(r"\*\*(.+?)\*\*", stripped)
        if only_bold:
            blocks.append(("label", clean_inline(only_bold.group(1))))
            continue
        cleaned = clean_inline(line)
        if cleaned.startswith("- "):
            blocks.append(("bullet", cleaned[2:].strip()))
        elif re.match(r"^\d+\.\s+", cleaned):
            n, rest = cleaned.split(".", 1)
            blocks.append(("number", (n + ".", rest.strip())))
        else:
            blocks.append(("p", cleaned))
    return blocks


class PdfBuilder:
    def __init__(self, title: str):
        self.title = title
        self.pages: list[list[bytes]] = [[]]
        self.page_no = 1
        self.y = TOP

    @property
    def page(self) -> list[bytes]:
        return self.pages[-1]

    def new_page(self):
        self._add_footer()
        self.pages.append([])
        self.page_no += 1
        self.y = TOP

    def ensure(self, needed: float):
        if self.y - needed < BOTTOM:
            self.new_page()

    def text(self, x: float, y: float, font_key: str, text: str):
        self.page.append(pdf_text(x, y, font_key, text))

    def rule(self):
        self.ensure(18)
        self.page.append(b"0.7 w %.2f %.2f m %.2f %.2f l S" % (LEFT, self.y, RIGHT, self.y))
        self.y -= 14

    def blank(self, amount: float = 6):
        self.y -= amount

    def add_wrapped(self, font_key: str, text: str, x: float = LEFT, available: float = CONTENT_W, gap_after: float = 3.0):
        _, _, size, leading = FONTS[font_key]
        width = mono_chars(available, size)
        lines = textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False) or [""]
        self.ensure(len(lines) * leading + gap_after)
        for line in lines:
            self.text(x, self.y, font_key, line)
            self.y -= leading
        self.y -= gap_after

    def add_hanging(self, font_key: str, prefix: str, text: str, x: float = LEFT, gap_after: float = 2.0):
        _, _, size, leading = FONTS[font_key]
        prefix_chars = len(prefix)
        total_width = mono_chars(CONTENT_W - (x - LEFT), size)
        body_width = max(10, total_width - prefix_chars)
        wrapped = textwrap.wrap(text, width=body_width, break_long_words=False, break_on_hyphens=False) or [""]
        self.ensure(len(wrapped) * leading + gap_after)
        for i, line in enumerate(wrapped):
            rendered = (prefix if i == 0 else " " * prefix_chars) + line
            self.text(x, self.y, font_key, rendered)
            self.y -= leading
        self.y -= gap_after

    def _add_footer(self):
        footer_y = 28
        self.page.append(pdf_text(LEFT, footer_y, "footer", self.title))
        self.page.append(pdf_text(RIGHT - 12, footer_y, "footer", str(self.page_no)))

    def finish(self):
        self._add_footer()


def build_pdf(markdown_path: Path, output_path: Path):
    blocks = parse_markdown(markdown_path.read_text())
    title = markdown_path.stem.replace("-", " ")
    pdf = PdfBuilder(title="Oviond Rebuild Report and Action Plan")

    for kind, value in blocks:
        if kind == "blank":
            pdf.blank(6)
        elif kind == "rule":
            pdf.rule()
        elif kind == "h1":
            pdf.blank(2)
            pdf.add_wrapped("h1", value, gap_after=6)
        elif kind == "h2":
            pdf.blank(2)
            pdf.add_wrapped("h2", value, gap_after=5)
        elif kind == "h3":
            pdf.blank(1)
            pdf.add_wrapped("h3", value, gap_after=4)
        elif kind == "label":
            pdf.add_wrapped("label", value, gap_after=2)
        elif kind == "bullet":
            pdf.add_hanging("body", "- ", value)
        elif kind == "number":
            prefix, text = value
            pdf.add_hanging("body", prefix + " ", text)
        elif kind == "p":
            pdf.add_wrapped("body", value)

    pdf.finish()
    write_pdf(pdf.pages, output_path)


def write_pdf(page_streams: list[list[bytes]], output_path: Path):
    objects: list[bytes] = []

    def add_obj(data: bytes) -> int:
        objects.append(data)
        return len(objects)

    font_regular = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>")
    font_bold = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier-Bold >>")
    pages_placeholder = add_obj(b"<< >>")

    page_ids = []
    for page_cmds in page_streams:
        stream = b"\n".join(page_cmds)
        content_id = add_obj(b"<< /Length %d >>\nstream\n%b\nendstream" % (len(stream), stream))
        page_id = add_obj(
            b"<< /Type /Page /Parent %d 0 R /MediaBox [0 0 %.2f %.2f] /Resources << /Font << /F1 %d 0 R /F2 %d 0 R >> >> /Contents %d 0 R >>"
            % (pages_placeholder, A4_W, A4_H, font_regular, font_bold, content_id)
        )
        page_ids.append(page_id)

    objects[pages_placeholder - 1] = (
        b"<< /Type /Pages /Count %d /Kids [%b] >>"
        % (len(page_ids), b" ".join(f"{pid} 0 R".encode() for pid in page_ids))
    )
    catalog_id = add_obj(b"<< /Type /Catalog /Pages %d 0 R >>" % pages_placeholder)

    parts = [b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"]
    offsets = [0]
    for idx, obj in enumerate(objects, start=1):
        offsets.append(sum(len(p) for p in parts))
        parts.append(f"{idx} 0 obj\n".encode())
        parts.append(obj)
        parts.append(b"\nendobj\n")

    xref_pos = sum(len(p) for p in parts)
    parts.append(f"xref\n0 {len(objects) + 1}\n".encode())
    parts.append(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        parts.append(f"{off:010d} 00000 n \n".encode())
    parts.append(
        f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode()
    )

    output_path.write_bytes(b"".join(parts))


def main():
    parser = argparse.ArgumentParser(description="Render a markdown report into a metric-safe PDF.")
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    build_pdf(args.source, args.output)


if __name__ == "__main__":
    main()
