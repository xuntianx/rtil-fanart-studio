#!/usr/bin/env python3
"""Fetch the five public reference images locally; Python 3.9+, standard library only."""

import argparse
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request

MAX_BYTES = 20 * 1024 * 1024
ROOT = Path(__file__).resolve().parents[1]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def local_path(root, relative):
    path = Path(relative)
    if path.is_absolute() or path.parts[:2] != ('assets', 'style-references'):
        raise ValueError('Manifest target must be under assets/style-references')
    target = (root / path).resolve()
    if (root / 'assets' / 'style-references').resolve() not in target.parents:
        raise ValueError('Manifest target escapes the reference folder')
    return target


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fetch(item, root, check_only, opener):
    target = local_path(root, item['file'])
    expected = item['sha256']
    if target.exists():
        if digest(target) != expected:
            raise ValueError('Existing file has an unexpected SHA-256; preserved without overwrite')
        return 'verified'
    if check_only:
        raise FileNotFoundError('Reference not downloaded')
    parsed = urllib.parse.urlparse(item['source_image'])
    if parsed.scheme != 'https' or parsed.hostname != 'pbs.twimg.com' or parsed.username or parsed.password:
        raise ValueError('Only HTTPS image URLs on pbs.twimg.com are supported')
    suffix = Path(parsed.path).suffix.lstrip('.')
    if suffix not in ('jpg', 'jpeg', 'png', 'webp'):
        raise ValueError('Unsupported reference format')
    # Hashes correspond to the original-resolution public images.
    url = urllib.parse.urlunparse(parsed._replace(
        path=parsed.path.rsplit('.', 1)[0],
        query=urllib.parse.urlencode({'format': suffix, 'name': 'orig'}), fragment=''))
    request = urllib.request.Request(url, headers={'User-Agent': 'rtil-fanart-studio-reference-fetcher/1.0'})
    with opener.open(request, timeout=30) as response:
        if not response.headers.get('Content-Type', '').startswith('image/'):
            raise ValueError('Source did not return an image')
        data = response.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError('Reference exceeds the 20 MiB limit')
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('Downloaded reference differs from the recorded hash; source may have changed')
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=target.parent, suffix='.part', delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
        temporary.replace(target)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    return 'downloaded and verified'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify local references without network access')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'references' / 'source-manifest.json').read_text(encoding='utf-8'))
    opener = urllib.request.build_opener(NoRedirect())
    failures = 0
    for item in manifest:
        try:
            state = fetch(item, ROOT, args.check, opener)
            print(f"OK {item['file']}: {state}")
        except (OSError, ValueError, urllib.error.URLError) as exc:
            failures += 1
            print(f"ERROR {item['file']}: {exc}", file=sys.stderr)
    print(f'{len(manifest) - failures}/{len(manifest)} references ready.')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
