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
        "duel": ("#ff8a7a", "#78a6ff"),
    }.get(variant, ("#78a6ff", "#5fe2c2"))
    art = {
        "ml": ml_art(),
        "evolution": evolution_art(),
        "rl": rl_art(),
        "compare": compare_art(),
        "duel": duel_art(),
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
  <rect width="1200" height="760" rx="44" fill="url(#glowA)">
    <animate attributeName="opacity" values="0.72;1;0.72" dur="8s" repeatCount="indefinite"/>
  </rect>
  <rect width="1200" height="760" rx="44" fill="url(#glowB)">
    <animate attributeName="opacity" values="0.55;0.85;0.55" dur="9s" repeatCount="indefinite"/>
  </rect>
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
    <rect x="114" y="322" width="236" height="236" rx="20" fill="#ffffff" stroke="#d4e3ff"/>
    <path d="M173 381 H291 M173 440 H291 M173 499 H291 M232 322 V558" stroke="#dfe9ff" stroke-width="8"/>
    <rect x="122" y="330" width="102" height="102" rx="18" fill="#edf5ff">
      <animate attributeName="fill" values="#edf5ff;#dbe9ff;#edf5ff" dur="4s" repeatCount="indefinite"/>
    </rect>
    <rect x="240" y="448" width="102" height="102" rx="18" fill="#dcfaf2">
      <animate attributeName="fill" values="#dcfaf2;#ccf4e9;#dcfaf2" dur="4s" repeatCount="indefinite"/>
    </rect>
    <circle r="16" fill="#5fe2c2">
      <animateMotion dur="6s" repeatCount="indefinite" path="M173 381 L291 381 L291 499 L232 499 L232 558" />
      <animate attributeName="opacity" values="0.9;1;0.9" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <polyline points="470,452 548,392 614,420 698,334 782,370 872,298 948,346 1024,254" fill="none" stroke="#78a6ff" stroke-width="16" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="820" stroke-dashoffset="820">
      <animate attributeName="stroke-dashoffset" values="820;0;0" dur="6s" repeatCount="indefinite"/>
    </polyline>
    <circle cx="1024" cy="254" r="14" fill="#5fe2c2">
      <animate attributeName="r" values="10;15;10" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <rect x="430" y="534" width="290" height="112" rx="24" fill="#f8fbff"/>
    <rect x="780" y="534" width="290" height="112" rx="24" fill="#f8fbff"/>
    <rect x="114" y="590" width="198" height="18" rx="9" fill="#e5edff"/>
    <rect x="114" y="332" width="180" height="18" rx="9" fill="#bed1ff"/>
    <rect x="114" y="590" width="140" height="18" rx="9" fill="#78a6ff">
      <animate attributeName="width" values="70;170;140;190;120;70" dur="5.5s" repeatCount="indefinite"/>
    </rect>
    <text x="458" y="592" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#17345d">Gridworld policy</text>
    <text x="812" y="592" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#17345d">Learning loop</text>
    '''


def evolution_art() -> str:
    return '''
    <rect x="98" y="284" width="980" height="354" rx="32" fill="#08182c" stroke="#284b75"/>
    <line x1="588" y1="314" x2="588" y2="606" stroke="#dce9ff" stroke-width="10" stroke-dasharray="16 18" opacity="0.9"/>
    <rect x="142" y="402" width="24" height="120" rx="12" fill="#78a6ff">
      <animate attributeName="y" values="390;444;390" dur="3.8s" repeatCount="indefinite"/>
    </rect>
    <rect x="1004" y="438" width="24" height="120" rx="12" fill="#5fe2c2">
      <animate attributeName="y" values="452;372;452" dur="4.1s" repeatCount="indefinite"/>
    </rect>
    <circle r="18" fill="#ffffff">
      <animateMotion dur="3.2s" repeatCount="indefinite" path="M642 446 L920 338 L1042 464 L710 558 L398 488 L210 372 L642 446"/>
    </circle>
    <path d="M742 348 C820 370, 874 438, 904 520" fill="none" stroke="#ffc76b" stroke-width="12" stroke-linecap="round" stroke-dasharray="240" stroke-dashoffset="240">
      <animate attributeName="stroke-dashoffset" values="240;0;0" dur="4.5s" repeatCount="indefinite"/>
    </path>
    <path d="M770 370 L742 348 L780 340" fill="none" stroke="#ffc76b" stroke-width="12" stroke-linecap="round" stroke-linejoin="round">
      <animateTransform attributeName="transform" type="rotate" values="0 742 348;8 742 348;0 742 348" dur="2.8s" repeatCount="indefinite"/>
    </path>
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
    <rect x="126" y="398" width="18" height="106" rx="9" fill="#78a6ff">
      <animate attributeName="y" values="420;360;458;420" dur="4s" repeatCount="indefinite"/>
    </rect>
    <rect x="492" y="366" width="18" height="106" rx="9" fill="#5fe2c2">
      <animate attributeName="y" values="352;470;392;352" dur="4s" repeatCount="indefinite"/>
    </rect>
    <circle r="15" fill="#ffffff">
      <animateMotion dur="3.4s" repeatCount="indefinite" path="M356 448 L506 350 L478 540 L148 410 L356 448"/>
    </circle>
    <polyline points="662,540 714,500 766,512 818,430 870,392 922,348 974,334 1026,320" fill="none" stroke="#5fe2c2" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="500" stroke-dashoffset="500">
      <animate attributeName="stroke-dashoffset" values="500;0;0" dur="5s" repeatCount="indefinite"/>
    </polyline>
    <circle cx="1026" cy="320" r="11" fill="#ffc76b">
      <animate attributeName="cy" values="320;304;320" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <rect x="636" y="318" width="162" height="56" rx="20" fill="#102540" stroke="#284b75"/>
    <rect x="820" y="318" width="232" height="56" rx="20" fill="#102540" stroke="#284b75"/>
    <text x="662" y="353" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#dce9ff">Episode 320</text>
    <text x="846" y="353" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#dce9ff">ε = 0.08</text>
    <rect x="636" y="558" width="190" height="42" rx="16" fill="#0f2139" stroke="#284b75"/>
    <rect x="636" y="558" width="122" height="42" rx="16" fill="#5fe2c2" fill-opacity="0.28">
      <animate attributeName="width" values="72;150;110;170;122;72" dur="5s" repeatCount="indefinite"/>
    </rect>
    <rect x="842" y="558" width="190" height="42" rx="16" fill="#0f2139" stroke="#284b75"/>
    <rect x="842" y="558" width="86" height="42" rx="16" fill="#ffc76b" fill-opacity="0.24">
      <animate attributeName="width" values="48;96;128;86;48" dur="5s" repeatCount="indefinite"/>
    </rect>
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
    <rect x="126" y="422" width="18" height="112" rx="9" fill="#78a6ff">
      <animate attributeName="y" values="420;356;452;420" dur="4.1s" repeatCount="indefinite"/>
    </rect>
    <rect x="510" y="448" width="18" height="112" rx="9" fill="#ffc76b">
      <animate attributeName="y" values="462;394;448;462" dur="4.1s" repeatCount="indefinite"/>
    </rect>
    <rect x="668" y="390" width="18" height="112" rx="9" fill="#5fe2c2">
      <animate attributeName="y" values="372;454;402;372" dur="3.6s" repeatCount="indefinite"/>
    </rect>
    <rect x="1052" y="430" width="18" height="112" rx="9" fill="#78a6ff">
      <animate attributeName="y" values="444;384;430;444" dur="3.6s" repeatCount="indefinite"/>
    </rect>
    <circle r="15" fill="#ffffff">
      <animateMotion dur="3s" repeatCount="indefinite" path="M362 470 L520 390 L502 560 L160 430 L362 470"/>
    </circle>
    <circle r="15" fill="#ffffff">
      <animateMotion dur="2.6s" repeatCount="indefinite" path="M904 470 L1060 410 L1024 560 L702 402 L904 470"/>
    </circle>
    <rect x="126" y="566" width="170" height="18" rx="9" fill="#ffc76b" fill-opacity="0.28">
      <animate attributeName="width" values="90;152;124;170;100;90" dur="4.3s" repeatCount="indefinite"/>
    </rect>
    <rect x="668" y="566" width="170" height="18" rx="9" fill="#5fe2c2" fill-opacity="0.28">
      <animate attributeName="width" values="110;88;148;126;166;110" dur="4.3s" repeatCount="indefinite"/>
    </rect>
    <text x="148" y="610" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#ffc76b">Population score</text>
    <text x="688" y="610" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#5fe2c2">Episode reward</text>
    '''


def duel_art() -> str:
    return '''
    <rect x="86" y="286" width="1028" height="342" rx="30" fill="#0c1730" stroke="#29536b"/>
    <line x1="600" y1="320" x2="600" y2="598" stroke="#dce9ff" stroke-width="8" stroke-dasharray="14 18" opacity="0.8"/>
    <rect x="126" y="404" width="18" height="118" rx="9" fill="#ff8a7a"/>
    <rect x="1056" y="416" width="18" height="118" rx="9" fill="#78a6ff"/>
    <circle cx="600" cy="468" r="16" fill="#ffffff"/>
    <path d="M450 364 C510 338, 560 338, 600 372" fill="none" stroke="#ff8a7a" stroke-width="12" stroke-linecap="round"/>
    <path d="M750 364 C690 338, 640 338, 600 372" fill="none" stroke="#78a6ff" stroke-width="12" stroke-linecap="round"/>
    <rect x="118" y="316" width="220" height="54" rx="20" fill="#102540" stroke="#284b75"/>
    <rect x="862" y="316" width="220" height="54" rx="20" fill="#102540" stroke="#284b75"/>
    <text x="150" y="350" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#ffb2a8">Evolution</text>
    <text x="940" y="350" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#a9c4ff">RL</text>
    <rect x="400" y="552" width="400" height="48" rx="18" fill="#0f2139" stroke="#284b75"/>
    <text x="456" y="583" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#dce9ff">Shared arena · direct matchup</text>
    '''



def generic_art() -> str:
    return '''
    <rect x="92" y="286" width="1016" height="342" rx="30" fill="#0c1730" stroke="#29536b"/>
    <circle r="16" fill="#5fe2c2">
      <animateMotion dur="4s" repeatCount="indefinite" path="M180 448 L1040 448 L620 360 L180 448"/>
    </circle>
    '''


def escape(value: str) -> str:
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


if __name__ == '__main__':
    main()
