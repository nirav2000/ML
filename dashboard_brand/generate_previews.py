from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "preview_manifest.json"
OUT_DIR = ROOT / "previews"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    data = json.loads(MANIFEST.read_text())
    for entry in data.get("previews", []):
        svg = build_svg(entry)
        (OUT_DIR / f"{entry['slug']}.svg").write_text(svg)
        print(f"wrote {entry['slug']}.svg")


def build_svg(entry: dict) -> str:
    variant = entry.get("variant", "generic")
    title = escape(entry.get("title", "App Preview"))
    subtitle = escape(entry.get("subtitle", "Interactive app preview"))
    tag = escape(entry.get("tag", "Preview"))
    accent = {
        "ml": ("#78a6ff", "#5fe2c2"),
        "evolution": ("#78a6ff", "#ffc76b"),
        "rl": ("#5fe2c2", "#78a6ff"),
        "compare": ("#ffc76b", "#5fe2c2"),
    }.get(variant, ("#78a6ff", "#5fe2c2"))
    art = {
        "ml": ml_art(),
        "evolution": evolution_art(),
        "rl": rl_art(),
        "compare": compare_art(),
    }.get(variant, generic_art())
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 760" role="img" aria-label="{title} preview">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0a1426"/>
      <stop offset="100%" stop-color="#07111f"/>
    </linearGradient>
    <radialGradient id="glowA" cx="0.15" cy="0.1" r="0.8">
      <stop offset="0%" stop-color="{accent[0]}" stop-opacity="0.32"/>
      <stop offset="100%" stop-color="{accent[0]}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowB" cx="0.9" cy="0.15" r="0.7">
      <stop offset="0%" stop-color="{accent[1]}" stop-opacity="0.24"/>
      <stop offset="100%" stop-color="{accent[1]}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="760" rx="44" fill="url(#bg)"/>
  <rect width="1200" height="760" rx="44" fill="url(#glowA)"/>
  <rect width="1200" height="760" rx="44" fill="url(#glowB)"/>
  <rect x="44" y="42" width="1112" height="676" rx="34" fill="#0d182b" stroke="#ffffff" stroke-opacity="0.12"/>
  <rect x="72" y="68" width="256" height="44" rx="22" fill="rgba(120,166,255,0.14)" stroke="#78a6ff" stroke-opacity="0.24"/>
  <text x="104" y="97" font-family="Arial, sans-serif" font-size="21" font-weight="700" fill="{accent[0]}">{tag}</text>
  <text x="72" y="174" font-family="Arial, sans-serif" font-size="62" font-weight="700" fill="#f3f7ff">{title}</text>
  <text x="72" y="225" font-family="Arial, sans-serif" font-size="28" font-weight="700" fill="#a6b5cf">{subtitle}</text>
  <g transform="translate(0 8)">{art}</g>
</svg>'''


def ml_art() -> str:
    return '''
    <rect x="72" y="286" width="320" height="360" rx="26" fill="#eef3ff"/>
    <rect x="430" y="286" width="640" height="212" rx="28" fill="#13284a"/>
    <polyline points="470,452 548,392 614,420 698,334 782,370 872,298 948,346 1024,254" fill="none" stroke="#78a6ff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="1024" cy="254" r="14" fill="#5fe2c2"/>
    <rect x="430" y="534" width="290" height="112" rx="24" fill="#f8fbff"/>
    <rect x="780" y="534" width="290" height="112" rx="24" fill="#f8fbff"/>
    <rect x="114" y="332" width="180" height="18" rx="9" fill="#bed1ff"/>
    <rect x="114" y="376" width="220" height="16" rx="8" fill="#dfe9ff"/>
    <rect x="114" y="412" width="220" height="16" rx="8" fill="#dfe9ff"/>
    <rect x="114" y="448" width="188" height="16" rx="8" fill="#dfe9ff"/>
    <rect x="114" y="510" width="198" height="52" rx="26" fill="#78a6ff"/>
    '''


def evolution_art() -> str:
    return '''
    <rect x="98" y="284" width="980" height="354" rx="32" fill="#08182c" stroke="#284b75"/>
    <line x1="588" y1="314" x2="588" y2="606" stroke="#dce9ff" stroke-width="10" stroke-dasharray="16 18" opacity="0.9"/>
    <rect x="142" y="402" width="24" height="120" rx="12" fill="#78a6ff"/>
    <rect x="1004" y="438" width="24" height="120" rx="12" fill="#5fe2c2"/>
    <circle cx="642" cy="446" r="18" fill="#ffffff"/>
    <path d="M742 348 C820 370, 874 438, 904 520" fill="none" stroke="#ffc76b" stroke-width="12" stroke-linecap="round"/>
    <path d="M770 370 L742 348 L780 340" fill="none" stroke="#ffc76b" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    <rect x="120" y="314" width="180" height="54" rx="20" fill="#102540" stroke="#284b75"/>
    <rect x="876" y="314" width="180" height="54" rx="20" fill="#102540" stroke="#284b75"/>
    <text x="182" y="349" font-family="Arial, sans-serif" font-size="26" font-weight="700" fill="#dce9ff">12</text>
    <text x="940" y="349" font-family="Arial, sans-serif" font-size="26" font-weight="700" fill="#dce9ff">18</text>
    <rect x="120" y="562" width="286" height="54" rx="20" fill="#0f2139" stroke="#284b75"/>
    <rect x="436" y="562" width="588" height="54" rx="20" fill="#0f2139" stroke="#284b75"/>
    <text x="152" y="597" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#5fe2c2">Generation 148</text>
    <text x="468" y="597" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#dce9ff">Mutation · Selection · Improvement</text>
    '''


def rl_art() -> str:
    return '''
    <rect x="92" y="286" width="470" height="342" rx="30" fill="#08182c" stroke="#29536b"/>
    <rect x="602" y="286" width="476" height="342" rx="30" fill="#0c1730" stroke="#29536b"/>
    <line x1="326" y1="318" x2="326" y2="596" stroke="#dce9ff" stroke-width="8" stroke-dasharray="14 18" opacity="0.9"/>
    <rect x="126" y="398" width="18" height="106" rx="9" fill="#78a6ff"/>
    <rect x="492" y="366" width="18" height="106" rx="9" fill="#5fe2c2"/>
    <circle cx="356" cy="448" r="15" fill="#ffffff"/>
    <polyline points="662,540 714,500 766,512 818,430 870,392 922,348 974,334 1026,320" fill="none" stroke="#5fe2c2" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="1026" cy="320" r="11" fill="#ffc76b"/>
    <rect x="636" y="318" width="162" height="56" rx="20" fill="#102540" stroke="#284b75"/>
    <rect x="820" y="318" width="232" height="56" rx="20" fill="#102540" stroke="#284b75"/>
    <text x="662" y="353" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#dce9ff">Episode 320</text>
    <text x="846" y="353" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#dce9ff">ε = 0.08</text>
    <rect x="636" y="558" width="190" height="42" rx="16" fill="#0f2139" stroke="#284b75"/>
    <rect x="842" y="558" width="190" height="42" rx="16" fill="#0f2139" stroke="#284b75"/>
    <text x="666" y="585" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#5fe2c2">Reward ↑</text>
    <text x="874" y="585" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#ffc76b">Q-table</text>
    '''


def compare_art() -> str:
    return '''
    <rect x="86" y="286" width="486" height="342" rx="30" fill="#0c1730" stroke="#29536b"/>
    <rect x="628" y="286" width="486" height="342" rx="30" fill="#0c1730" stroke="#29536b"/>
    <text x="116" y="334" font-family="Arial, sans-serif" font-size="26" font-weight="700" fill="#78a6ff">Evolution lane</text>
    <text x="658" y="334" font-family="Arial, sans-serif" font-size="26" font-weight="700" fill="#5fe2c2">RL lane</text>
    <line x1="330" y1="362" x2="330" y2="596" stroke="#dce9ff" stroke-width="8" stroke-dasharray="14 18" opacity="0.8"/>
    <line x1="872" y1="362" x2="872" y2="596" stroke="#dce9ff" stroke-width="8" stroke-dasharray="14 18" opacity="0.8"/>
    <rect x="126" y="422" width="18" height="112" rx="9" fill="#78a6ff"/>
    <rect x="510" y="448" width="18" height="112" rx="9" fill="#ffc76b"/>
    <rect x="668" y="390" width="18" height="112" rx="9" fill="#5fe2c2"/>
    <rect x="1052" y="430" width="18" height="112" rx="9" fill="#78a6ff"/>
    <circle cx="362" cy="470" r="15" fill="#ffffff"/>
    <circle cx="904" cy="470" r="15" fill="#ffffff"/>
    <text x="148" y="586" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#ffc76b">Population score</text>
    <text x="688" y="586" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#5fe2c2">Episode reward</text>
    '''


def generic_art() -> str:
    return '<rect x="92" y="286" width="1016" height="342" rx="30" fill="#0c1730" stroke="#29536b"/>'


def escape(value: str) -> str:
    return (value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


if __name__ == '__main__':
    main()
