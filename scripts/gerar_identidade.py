from vetor import *

def main():
    items=[]
    for name,color in [('verde',C['verde']),('creme',C['creme']),('preto','#000000'),('branco','#FFFFFF')]:
        c=Canvas(1600,530,'Aurevi — logo '+name)
        h=c.logo(100,80,1400,color)
        items.append(c.save('01-logos/logo-'+name+'.svg'))
        c=Canvas(1600,660,'Aurevi — assinatura '+name)
        c.logo(100,90,1400,color)
        c.text('MODA FEMININA',800,580,38,weight=500,color=color,anchor='middle',spacing=9)
        items.append(c.save('01-logos/assinatura-'+name+'.svg'))
        c=Canvas(600,600,'Aurevi — símbolo AV '+name)
        c.sym(56,80,488,color)
        items.append(c.save('01-logos/simbolo-'+name+'.svg'))
    c=Canvas(1080,1080,'Aurevi — avatar',C['verde'])
    c.sym(275,295,530,C['creme'])
    c.circle(800,795,26,C['coral'])
    items.append(c.save('01-logos/avatar.svg'))
    # A graphic mark family; always independent from the research references.
    c=Canvas(1200,1200,'Aurevi — padrão de dobras',C['creme'])
    for row in range(4):
        for col in range(4):
            x=25+col*300;y=15+row*300
            c.sym(x,y,245,C['verde'] if (row+col)%3 else C['coral'])
    items.append(c.save('01-logos/padrao-dobras.svg'))
    (OUT/'cores.json').write_text(json.dumps({'brand':'Aurevi','direction':'Essencial com personalidade','colors':C,'ratios':{'verde/creme':10.45,'tinta/creme':13.06,'verde/coral':4.63,'verde/areia':7.58,'creme/coral':2.26},'screen':'sRGB','print':'Converter com perfil indicado pela gráfica; validar prova física.'},indent=2,ensure_ascii=False),encoding='utf-8')
    (ROOT/'docs/manifesto-logos.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(items)} artes vetoriais de marca criadas; logo e assinaturas em curvas.')

if __name__=='__main__':main()
