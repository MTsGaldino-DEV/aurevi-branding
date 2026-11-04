"""Build a darker-red revision without overwriting the prior color study."""
from pathlib import Path
import shutil,json
import direcao_bordo as assets

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'DIRECAO-VERMELHO-ESCURO'
RED='#450A10'

def main():
    assets.OUT=OUT;assets.BORDO=RED;assets.INK='#26090D'
    assets.main()
    for p in list((OUT/'logos').glob('*-bordo.svg')):
        p.rename(p.with_name(p.name.replace('-bordo.svg','-vermelho-escuro.svg')))
    # Keep the approved layout and shape studies. Update the color, names and image target.
    html=(ROOT/'DIRECAO-BORDO/APRESENTACAO.html').read_text(encoding='utf-8')
    for before,after in [
        ('#681E36',RED),('#681e36',RED.lower()),('#681e36',RED.lower()),
        ('#8b3653','#6b161f'),('#2d1a22','#26090d'),
        ('-bordo.svg','-vermelho-escuro.svg'),('vestido-bordo.png','vestido-vermelho-escuro.png'),
        ('Apresentacao-Aurevi-Bordo.pdf','Apresentacao-Aurevi-Vermelho-Escuro.pdf'),
        ('bordô e ouro','vermelho escuro e ouro'),('Bordô + ouro champagne','Vermelho escuro + ouro champagne'),
        ('Bordô','Vermelho escuro'),('bordô','vermelho escuro'),
        ('A direção de cores vem da preferência apresentada.','A direção foi escurecida para um vermelho sangue fechado, com menos componente arroxeado.'),
    ]:html=html.replace(before,after)
    # Give the longer palette label a slightly smaller display size, preserving the layout.
    html=html.replace('.swatch h2{font-size:52px', '.swatch h2{font-size:46px')
    (OUT/'APRESENTACAO.html').write_text(html,encoding='utf-8')
    palette={'direcao':'Vermelho sangue escuro e ouro','vermelho_escuro':RED,'ouro_champagne':'#CFB77F','marfim':'#FAF6EF','tinta':'#26090D','observacao':'Nova proposta mais escura e menos arroxeada. Códigos sRGB para uso digital; percepção no tecido varia com iluminação.'}
    (OUT/'paleta.json').write_text(json.dumps(palette,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Nova base criada:',RED,'; direção anterior preservada.')

if __name__=='__main__':main()
