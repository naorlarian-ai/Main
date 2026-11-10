#!/usr/bin/env python3
"""Side-by-side comparison of the reference CV and a new variant.

Usage: python3 compare.py <reference.pdf> <new.pdf> <out_basename> [left_label] [right_label]
Writes <out_basename>.pdf (vector) and <out_basename>.png (preview).
"""
import sys
import pymupdf

ref, new, out = sys.argv[1:4]
left_label = sys.argv[4] if len(sys.argv) > 4 else "BEFORE  ·  Approved reference — Naor_Larian_CV(5).pdf"
right_label = sys.argv[5] if len(sys.argv) > 5 else "AFTER  ·  System Integration v1 — CV_Design_Master_2026_11"
W, H = 595.3, 841.9
gap, pad, label_h = 28, 24, 34
page_w = pad * 2 + W * 2 + gap
page_h = pad * 2 + H + label_h

doc = pymupdf.open()
pg = doc.new_page(width=page_w, height=page_h)
pg.draw_rect(pg.rect, color=None, fill=(0.93, 0.94, 0.95))

for i, (path, label) in enumerate([(ref, left_label), (new, right_label)]):
    x = pad + i * (W + gap)
    y = pad + label_h
    pg.insert_text((x, pad + 16), label, fontsize=13, fontname="helv",
                   color=(0.09, 0.17, 0.25))
    frame = pymupdf.Rect(x, y, x + W, y + H)
    pg.draw_rect(frame + (-0.6, -0.6, 0.6, 0.6), color=(0.75, 0.78, 0.82), width=0.6, fill=(1, 1, 1))
    src = pymupdf.open(path)
    pg.show_pdf_page(frame, src, 0)
    src.close()

doc.save(out + ".pdf")
doc[0].get_pixmap(dpi=110).save(out + ".png")
print("wrote", out + ".pdf", out + ".png")
