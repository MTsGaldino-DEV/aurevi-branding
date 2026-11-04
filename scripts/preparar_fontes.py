from pathlib import Path
from urllib.request import urlopen
from urllib.parse import quote
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools/python'))
from fontTools.ttLib import TTFont

def main():
    dest = ROOT / 'ENTREGA/06-fontes'
    dest.mkdir(parents=True, exist_ok=True)
    files = {
        'Fraunces.ttf': 'fraunces/Fraunces[SOFT,WONK,opsz,wght].ttf',
        'Fraunces-Italic.ttf': 'fraunces/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf',
        'Manrope.ttf': 'manrope/Manrope[wght].ttf',
        'Fraunces-LICENCA.txt': 'fraunces/OFL.txt',
        'Manrope-LICENCA.txt': 'manrope/OFL.txt',
    }
    for name, remote in files.items():
        target = dest / name
        if not target.exists():
            url = 'https://raw.githubusercontent.com/google/fonts/main/ofl/' + quote(remote, safe='/')
            target.write_bytes(urlopen(url, timeout=30).read())
        if name.endswith('.ttf'):
            font = TTFont(target)
            assert all(ord(c) in font.getBestCmap() for c in 'AureviçãéíóúÁÊ'), name
            print(name, target.stat().st_size, 'bytes; caracteres PT-BR OK')
        else:
            assert 'SIL OPEN FONT LICENSE' in target.read_text(encoding='utf-8')
            print(name, 'OFL OK')

if __name__ == '__main__':
    main()
