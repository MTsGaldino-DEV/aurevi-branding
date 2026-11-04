from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
import markdown

style='''@font-face{font-family:F;src:url('../06-fontes/Fraunces.ttf');font-weight:100 900}@font-face{font-family:M;src:url('../06-fontes/Manrope.ttf');font-weight:200 800}*{box-sizing:border-box}body{font:14px/1.65 M,sans-serif;color:#203c32;background:#f4efe6;margin:0;padding:50px;max-width:1000px;margin:auto}h1,h2,h3{font-family:F,serif;font-weight:450;line-height:1.2}h1{font-size:42px;margin:0 0 35px}h2{font-size:30px;margin:36px 0 18px;border-top:1px solid #203c3230;padding-top:22px;break-after:avoid}h3{font-size:24px;break-after:avoid;margin:28px 0 12px}p{margin:0 0 13px}blockquote{border-left:4px solid #e98673;background:#e9e0d3;margin:20px 0;padding:20px 26px;break-inside:avoid}blockquote p:last-child{margin:0}pre{white-space:pre-wrap;background:#e9e0d3;padding:18px;font:13px/1.6 M,sans-serif}code{font:inherit}table{border-collapse:collapse;width:100%;font-size:11px;line-height:1.5;margin:20px 0}th,td{border:1px solid #203c3230;text-align:left;padding:9px;vertical-align:top}th{background:#203c32;color:#f4efe6}thead{display:table-header-group}tr{break-inside:avoid}a{color:inherit}li{margin-bottom:8px}.back{font-size:12px;display:block;margin-bottom:30px}@page{size:A4;margin:18mm 17mm 20mm}@media print{body{padding:0;margin:0;max-width:none;background:white}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}.back{display:none}h2,h3{break-after:avoid}p{orphans:3;widows:3}}'''
for name in ['Guia-de-conteudo','Ideias-para-a-loja']:
    path=ROOT/'ENTREGA/04-conteudo'/(name+'.md')
    body=markdown.markdown(path.read_text(encoding='utf-8'),extensions=['tables','fenced_code'])
    html=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aurevi — {name}</title><style>{style}</style></head><body><a class="back" href="../COMECE-AQUI.html">← Manual da marca</a>{body}</body></html>'
    path.with_suffix('.html').write_text(html,encoding='utf-8')
print('Dois guias em HTML criados.')
