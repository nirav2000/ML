from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / 'index.html'
NOTES = ROOT / 'dashboard_versions' / 'version_notes.json'
OUTPUT = ROOT / 'dashboard.versions.json'
ARCHIVE_DIR = ROOT / 'dashboard_versions'


def get_current_version() -> str:
    text = INDEX.read_text()
    match = re.search(r'data-dashboard-version="([^"]+)"', text)
    if not match:
        raise SystemExit('Could not find data-dashboard-version in index.html')
    return match.group(1)


def main() -> None:
    current = get_current_version()
    data = json.loads(NOTES.read_text())
    versions = []
    for entry in data.get('versions', []):
        version = entry['version']
        app_file = 'index.html' if version == current else f'dashboard_versions/{version}/index.html'
        if version != current and not (ROOT / app_file).exists():
            continue
        versions.append({
            'version': version,
            'label': entry.get('label', ''),
            'appFile': app_file,
            'notes': entry.get('notes', []),
        })
    if not any(v['version'] == current for v in versions):
        raise SystemExit(f'Current version {current} missing from dashboard_versions/version_notes.json')
    OUTPUT.write_text(json.dumps({'app': 'dashboard', 'current': current, 'versions': versions}, indent=2) + '\n')
    print(f'wrote {OUTPUT.relative_to(ROOT)} with current={current} and {len(versions)} entries')


if __name__ == '__main__':
    main()
