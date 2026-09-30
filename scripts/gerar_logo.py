"""Gera os arquivos da logo do WORCOMP em assets/img.

Uso, a partir da raiz do repositório: python3 scripts/gerar_logo.py
"""
from pathlib import Path

SAIDA = Path(__file__).resolve().parent.parent / "assets" / "img"
D, L, T = "#19413a", "#9bb93b", "#00656e"   # escuro, verde Ufopa, petróleo
G = "#5b7a16"
SW = 7
def g(x, d, cor, extra=""):
    return f'<path transform="translate({x} 0)" d="{d}" stroke="{cor}" {extra}/>'
O = "M17 0a17 20 0 1 0 0 40a17 20 0 1 0 0-40z"
R = "M0 40V0h15a11.5 11.5 0 0 1 0 23H0m13 0l13 17"
C = "M31 8.5A18 20 0 1 0 31 31.5"
M = "M0 40V0l15 24L30 0v40"
P = "M0 40V0h15a12 12 0 0 1 0 24H0"
V1, V2 = "M0 0l13 40L26 0", "M26 0l13 40L52 0"
MASK = f'<mask id="corte" maskUnits="userSpaceOnUse" x="-10" y="-10" width="80" height="60"><rect x="-10" y="-10" width="80" height="60" fill="#fff"/><path d="{V1}" fill="none" stroke="#000" stroke-width="{SW + 5.5}" stroke-linecap="round" stroke-linejoin="round"/></mask>'

def dublo_v(c1, c2):
    return f'{MASK}<path d="{V2}" stroke="{c2}" mask="url(#corte)"/><path d="{V1}" stroke="{c1}"/>'

def wordmark(c_w1, c_w2, c_or, c_comp, x0=0):
    parts = [dublo_v(c_w1, c_w2),
             g(x0 + 64, O, c_or), g(x0 + 110, R, c_or),
             g(x0 + 150, C, c_comp), g(x0 + 193, O, c_comp), g(x0 + 239, M, c_comp), g(x0 + 281, P, c_comp),
             f'<rect x="{x0 + 314}" y="36.5" width="17" height="7" rx="1.5" fill="{c_w2}" stroke="none"/>']
    return "\n    ".join(parts)

def svg(w, h, body, vb=None):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb or f"0 0 {w} {h}"}" role="img" aria-label="WORCOMP 2026">\n{body}\n</svg>\n'

grp = f'fill="none" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round"'
# A: marca horizontal, fundo claro
A = svg(368, 84, f'''  <g {grp} transform="translate(12 10)">
    {wordmark(D, L, D, G)}
  </g>
  <text x="12" y="76" font-family="'Fira Sans', 'Helvetica Neue', Arial, sans-serif" font-size="11.5" font-weight="700" letter-spacing="4.15" fill="#53636b">UFOPA · SANTARÉM · 2026</text>''')
# A2: fundo escuro
A2 = svg(368, 84, f'''  <rect width="368" height="84" rx="10" fill="{D}"/>
  <g {grp} transform="translate(12 10)">
    {wordmark("#ffffff", L, "#ffffff", L)}
  </g>
  <text x="12" y="76" font-family="'Fira Sans', 'Helvetica Neue', Arial, sans-serif" font-size="11.5" font-weight="700" letter-spacing="4.15" fill="#c3d1c9">UFOPA · SANTARÉM · 2026</text>''')
# ícone
ICON = svg(64, 64, f'''  <rect width="64" height="64" rx="14" fill="{D}"/>
  <g {grp} transform="translate(12.5 15.5) scale(0.75 0.825)">
    {dublo_v("#ffffff", L)}
  </g>''')
ICON_CLARO = svg(64, 64, f'''  <g {grp} transform="translate(12.5 15.5) scale(0.75 0.825)">
    {dublo_v(D, L)}
  </g>''')
for n, s in (("logo-horizontal", A), ("logo-horizontal-escuro", A2), ("logo", ICON), ("logo-claro", ICON_CLARO)):
    (SAIDA / (n + ".svg")).write_text(s, encoding="utf-8")
