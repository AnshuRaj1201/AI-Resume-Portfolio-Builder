from fpdf import FPDF
import re
import math
 
# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
PAGE_W    = 210
PAGE_H    = 297
MARGIN_L  = 15
MARGIN_R  = 15
MARGIN_T  = 15
MARGIN_B  = 15
USABLE_W  = PAGE_W - MARGIN_L - MARGIN_R   # 180 mm
BOTTOM    = PAGE_H - MARGIN_B              # 282 mm
 
LINE_H        = 7     # body line height mm
SECTION_MIN   = 45    # minimum mm needed at bottom before starting a new ## section
SUBBLOCK_MIN  = 35    # minimum mm needed before starting a ### sub-block
 
# Characters that fit per line at Arial 11 across USABLE_W=180mm
# Empirically: Arial 11 ≈ 2.1mm per char → 180/2.1 ≈ 85 chars
CHARS_PER_LINE = 85
 
# ─────────────────────────────────────────────────────────────────────────────
# UNICODE → LATIN-1 SANITISER
# ─────────────────────────────────────────────────────────────────────────────
UNICODE_MAP = {
    "\u2013": "-",  "\u2014": "-",
    "\u2018": "'",  "\u2019": "'",
    "\u201c": '"',  "\u201d": '"',
    "\u2022": "-",  "\u2026": "...",
    "\u00b7": "-",  "\u2192": "->",
    "\u2190": "<-", "\u2713": "[ok]",
    "\u2715": "[x]","\u00a9": "(c)",
    "\u00ae": "(R)","\u00b0": " deg",
    "\u00bd": "1/2",
}
 
def sanitise(text: str) -> str:
    for ch, rep in UNICODE_MAP.items():
        text = text.replace(ch, rep)
    return text.encode("latin-1", errors="replace").decode("latin-1")
 
# ─────────────────────────────────────────────────────────────────────────────
# MARKDOWN STRIPPER
# ─────────────────────────────────────────────────────────────────────────────
def strip_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"__(.*?)__",     r"\1", text)
    text = re.sub(r"\*(.*?)\*",     r"\1", text)
    text = re.sub(r"_(.*?)_",       r"\1", text)
    text = re.sub(r"`(.*?)`",       r"\1", text)
    text = re.sub(r"~~(.*?)~~",     r"\1", text)
    return text.strip()
 
# ─────────────────────────────────────────────────────────────────────────────
# FULL TEXT CLEANER
# ─────────────────────────────────────────────────────────────────────────────
def clean_text(text: str) -> str:
    for emoji, label in {
        "📧":"Email:","📱":"Phone:","🔗":"LinkedIn:",
        "🌐":"GitHub:","•":"-","📊":"ATS Score:",
        "✅":"[GOOD]","❌":"[IMPROVE]",
    }.items():
        text = text.replace(emoji, label)
    text = re.sub(r"[^\x00-\xFF]", "", text)
    return sanitise(text)
 
# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def _break_long_words(text: str, max_chars: int = CHARS_PER_LINE) -> str:
    words = text.split(" ")
    out = []
    for w in words:
        while len(w) > max_chars:
            out.append(w[:max_chars] + "-")
            w = w[max_chars:]
        out.append(w)
    return " ".join(out)
 
def _line_count(text: str, chars_per_line: int = CHARS_PER_LINE) -> int:
    """How many rendered lines will this text occupy."""
    text = strip_markdown(text).strip()
    if not text:
        return 0
    return max(1, math.ceil(len(text) / chars_per_line))
 
def _remaining(pdf) -> float:
    return BOTTOM - pdf.get_y()
 
def _ensure_space(pdf, needed_mm: float):
    """Add a new page if fewer than needed_mm remain."""
    if _remaining(pdf) < needed_mm:
        pdf.add_page()
 
# ─────────────────────────────────────────────────────────────────────────────
# LINE CLASSIFIER
# ─────────────────────────────────────────────────────────────────────────────
def classify(line: str):
    s = line.strip()
    if not s:
        return ("blank", "")
    if re.match(r"^-{3,}$", s) or re.match(r"^\*{3,}$", s):
        return ("hrule", "")
    if s.startswith("#### "): return ("h3", s[5:])
    if s.startswith("### "):  return ("h3", s[4:])
    if s.startswith("## "):   return ("h2", s[3:])
    if s.startswith("# "):    return ("h1", s[2:])
    if re.match(r"^[-*+]\s+", s):
        return ("bullet", re.sub(r"^[-*+]\s+", "", s))
    if re.match(r"^\d+\.\s+", s):
        return ("bullet", re.sub(r"^\d+\.\s+", "", s))
    return ("text", s)
 
# ─────────────────────────────────────────────────────────────────────────────
# CONTACT DEDUP
# ─────────────────────────────────────────────────────────────────────────────
_CONTACT_SECTION_LABELS = {
    "contact information","contact info","contact details",
    "contact","personal information","personal info",
}
 
def _build_contact_tokens(email, phone, linkedin, github) -> set:
    tokens = set()
    for val in (email, phone, linkedin, github):
        if val:
            v = val.strip().lower()
            tokens.add(v)
            if "@" in v: tokens.add(v.split("@")[0])
            if "/" in v: tokens.add(v.rstrip("/").split("/")[-1])
    return tokens
 
def _is_contact_duplicate(line_text: str, contact_tokens: set) -> bool:
    lowered = line_text.lower()
    return any(tok and tok in lowered for tok in contact_tokens)
 
# ─────────────────────────────────────────────────────────────────────────────
# RENDERERS
# ─────────────────────────────────────────────────────────────────────────────
def draw_header(pdf, name, template, email="", phone="", linkedin="", github=""):
    """Name + contact block. Splits contact into 2 rows if 4 items to avoid cutoff."""
    name = sanitise(strip_markdown(name))
 
    if template == "Modern":
        pdf.set_font("Arial", "B", 22)
        pdf.cell(USABLE_W, 12, name, ln=True, align="C")
        y = pdf.get_y()
        pdf.set_draw_color(80, 80, 80)
        pdf.set_line_width(0.6)
        pdf.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
        pdf.ln(3)
    elif template == "Classic":
        pdf.set_font("Arial", "B", 18)
        pdf.cell(USABLE_W, 10, name, ln=True, align="C")
        pdf.ln(3)
    else:  # Minimal
        pdf.set_font("Arial", "B", 16)
        pdf.cell(USABLE_W, 10, name, ln=True)
        pdf.ln(2)
 
    # Build contact items
    contacts = []
    if email:    contacts.append(f"Email: {sanitise(email)}")
    if phone:    contacts.append(f"Phone: {sanitise(phone)}")
    if linkedin: contacts.append(f"LinkedIn: {sanitise(linkedin)}")
    if github:   contacts.append(f"GitHub: {sanitise(github)}")
 
    if not contacts:
        pdf.ln(4)
        return
 
    pdf.set_font("Arial", "", 10)
    align = "C" if template in ("Modern", "Classic") else "L"
 
    # ── FIX: split into 2 rows when 4 items (prevents right-side cutoff) ──
    if len(contacts) == 4:
        row1 = "   |   ".join(contacts[:2])   # Email | Phone
        row2 = "   |   ".join(contacts[2:])   # LinkedIn | GitHub
        pdf.cell(USABLE_W, 5, row1, ln=True, align=align)
        pdf.cell(USABLE_W, 5, row2, ln=True, align=align)
    else:
        row = "   |   ".join(contacts)
        pdf.cell(USABLE_W, 5, row, ln=True, align=align)
 
    pdf.ln(4)
 
 
def draw_h2(pdf, text):
    """## section heading — always gets minimum space check before rendering."""
    text = sanitise(strip_markdown(text))
    # Guaranteed space: section heading + at least 2 lines of content below it
    _ensure_space(pdf, SECTION_MIN)
    pdf.ln(2)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(USABLE_W, 8, text, ln=True)
    y = pdf.get_y()
    pdf.set_draw_color(160, 160, 160)
    pdf.set_line_width(0.3)
    pdf.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
    pdf.ln(3)
 
 
def draw_h3(pdf, text):
    """### project/sub-section heading."""
    text = sanitise(strip_markdown(text))
    # Ensure h3 + at least 1 bullet below it don't get orphaned
    _ensure_space(pdf, SUBBLOCK_MIN)
    pdf.ln(2)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(USABLE_W, 7, text, ln=True)
    pdf.ln(1)
 
 
def draw_bullet(pdf, text, indent=4):
    text = sanitise(strip_markdown(_break_long_words(text)))
    # If even one line won't fit, start a new page
    _ensure_space(pdf, LINE_H * 1.5)
    pdf.set_font("Arial", "", 11)
    pdf.set_x(MARGIN_L + indent)
    pdf.cell(5, LINE_H, "-", ln=False)
    pdf.set_x(MARGIN_L + indent + 5)
    pdf.multi_cell(USABLE_W - indent - 5, LINE_H, text, align="L")
 
 
def draw_hrule(pdf):
    pdf.ln(2)
    y = pdf.get_y()
    pdf.set_draw_color(200, 200, 200)
    pdf.set_line_width(0.2)
    pdf.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
    pdf.ln(3)
 
 
def draw_text(pdf, text):
    text = sanitise(strip_markdown(_break_long_words(text)))
    lines = _line_count(text)
    _ensure_space(pdf, lines * LINE_H + 2)
    pdf.set_font("Arial", "", 11)
    pdf.set_x(MARGIN_L)
    pdf.multi_cell(USABLE_W, LINE_H, text, align="J")
 
# ─────────────────────────────────────────────────────────────────────────────
# MAIN ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────
def create_pdf(resume_text: str, template: str = "Classic",
               email: str = "", phone: str = "",
               linkedin: str = "", github: str = "") -> str:
 
    pdf = FPDF()
    pdf.set_margins(MARGIN_L, MARGIN_T, MARGIN_R)
    pdf.set_auto_page_break(auto=False)   # manual page breaks only
    pdf.add_page()
 
    resume_text = clean_text(resume_text)
    contact_tokens = _build_contact_tokens(email, phone, linkedin, github)
 
    h1_seen = False
 
    for raw_line in resume_text.split("\n"):
        kind, content = classify(raw_line)
 
        # Skip contact section labels in any form
        cleaned_label = strip_markdown(content).strip().lower().rstrip(":")
        if cleaned_label in _CONTACT_SECTION_LABELS:
            continue
 
        # Skip duplicate contact bullets/text
        if kind in ("bullet", "text") and \
                _is_contact_duplicate(strip_markdown(content), contact_tokens):
            continue
 
        # First h1 = name header
        if kind == "h1":
            if not h1_seen:
                draw_header(pdf, content, template, email, phone, linkedin, github)
                h1_seen = True
                continue
            else:
                kind = "h2"
 
        # Render
        if   kind == "blank":   pdf.ln(2)
        elif kind == "hrule":   draw_hrule(pdf)
        elif kind == "h2":      draw_h2(pdf, content)
        elif kind == "h3":      draw_h3(pdf, content)
        elif kind == "bullet":  draw_bullet(pdf, content)
        elif kind == "text":    draw_text(pdf, content)
 
    pdf.output("resume.pdf")
    return "resume.pdf"
 