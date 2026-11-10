#!/usr/bin/env python3
"""Contact sheet of the whole CV family (vector PDF + PNG).

Usage (from source/): python3 overview.py
"""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
ITEMS = [("01 - System Integration v3 (approved master)", "Naor_Larian_CV_System_Integration_v3.pdf")]
for n, label in [("02_RF_Test_Validation", "02 - RF Test & Validation"),
                 ("03_Application_Engineering", "03 - Application Engineering"),
                 ("04_Junior_FPGA", "04 - Junior FPGA / Digital Hardware"),
                 ("05_Google_Hardware_Intern", "05 - Hardware Internship (Google)"),
                 ("06_ImageSat_Ground_Systems", "06 - Ground Systems Integration (ImageSat)"),
                 ("07_Qualcomm_FPGA_Intern", "07 - FPGA / RTL Internship (Qualcomm)")]:
    ITEMS.append((label, f"Phase2_Variants/{n}/Naor_Larian_CV_{n}.pdf"))

W, H, s = 595.3, 841.9, 0.5
w, h = W * s, H * s
gap, pad, lab, cols = 18, 24, 22, 4
doc = pymupdf.open()
pg = doc.new_page(width=pad * 2 + cols * w + (cols - 1) * gap, height=pad * 2 + 2 * (h + lab) + gap + 30)
pg.draw_rect(pg.rect, color=None, fill=(0.93, 0.94, 0.95))
navy = (0.09, 0.17, 0.25)
pg.insert_text((pad, pad + 8), "Naor Larian CV family - 7 versions (01 approved master, 02-07 drafts for review)",
               fontsize=13, fontname="helv", color=navy)
for i, (label, f) in enumerate(ITEMS):
    c, r = i % cols, i // cols
    x, y = pad + c * (w + gap), pad + 30 + r * (h + lab + gap)
    pg.insert_text((x, y + 12), label, fontsize=8.5, fontname="helv", color=navy)
    R = pymupdf.Rect(x, y + lab, x + w, y + lab + h)
    pg.draw_rect(R + (-.5, -.5, .5, .5), color=(.75, .78, .82), width=.5, fill=(1, 1, 1))
    pg.show_pdf_page(R, pymupdf.open(ROOT / f), 0)
out = ROOT / "Phase2_Variants" / "Overview_All_7_CVs"
doc.save(f"{out}.pdf")
pg.get_pixmap(dpi=130).save(f"{out}.png")
print("wrote", out.with_suffix(".pdf"), out.with_suffix(".png"))
