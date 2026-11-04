"""Primitivas gráficas locais; textos finais em curvas e fonte original editável."""
from pathlib import Path
from functools import lru_cache
from html import escape
import base64
import json
import math
import sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'ENTREGA'
sys.path.insert(0,str(ROOT/'.tools/python'))
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

C={'creme':'#F4EFE6','verde':'#203C32','coral':'#E98673','areia':'#D9CCBA','tinta':'#242824'}

@lru_cache(maxsize=16)
def font_data(family='Manrope',weight=400,italic=False):
    name=family+('-Italic' if italic else '')+'.ttf'
    data=(OUT/'06-fontes'/name).read_bytes()
    tt=TTFont(OUT/'06-fontes'/name)
    loc={'wght':weight}
    if family=='Fraunces': loc.update({'SOFT':12,'WONK':0,'opsz':72})
    gs=tt.getGlyphSet(location=loc)
    hfont=hb.Font(hb.Face(data)); hfont.set_variations(loc)
    return tt,gs,hfont,tt['head'].unitsPerEm

def shape(value,size,family='Manrope',weight=400,italic=False,spacing=0):
    tt,gs,hfont,upem=font_data(family,weight,italic)
    buf=hb.Buffer();buf.add_str(value);buf.guess_segment_properties();hb.shape(hfont,buf,{'kern':True,'liga':True})
    scale=size/upem
    advance=sum(p.x_advance*scale for p in buf.glyph_positions)+max(0,len(buf.glyph_positions)-1)*spacing
    return gs,tt.getGlyphOrder(),buf.glyph_infos,buf.glyph_positions,scale,advance

def width(value,size,family='Manrope',weight=400,italic=False,spacing=0):
    return shape(value,size,family,weight,italic,spacing)[-1]

def outlined_text(value,x,y,size,family='Manrope',weight=400,color=None,anchor='start',spacing=0,italic=False):
    gs,order,infos,positions,scale,advance=shape(value,size,family,weight,italic,spacing)
    if anchor=='middle':x-=advance/2
    elif anchor=='end':x-=advance
    pen=SVGPathPen(gs); bounds=BoundsPen(gs)
    cursor=0
    for info,p in zip(infos,positions):
        t=(scale,0,0,-scale,x+cursor+p.x_offset*scale,y-p.y_offset*scale)
        glyph=gs[order[info.codepoint]]
        glyph.draw(TransformPen(pen,t));glyph.draw(TransformPen(bounds,t))
        cursor+=p.x_advance*scale+spacing
    node=f'<g aria-label="{escape(value,quote=True)}"><path fill="{color or C["verde"]}" d="{pen.getCommands()}"/></g>'
    return node,bounds.bounds

def wordmark(x,y,w,color=None):
    # Position y is the top of a 100-unit typographic box.
    initial,_=outlined_text('aurevi',0,0,180,'Fraunces',520)
    _,bbox=outlined_text('aurevi',0,0,180,'Fraunces',520)
    bx,by,bw,bh=bbox[0],bbox[1],bbox[2]-bbox[0],bbox[3]-bbox[1]
    scale=w/bw
    node,_=outlined_text('aurevi',0,0,180,'Fraunces',520,color or C['verde'])
    return f'<g transform="translate({x:.4f} {y:.4f}) scale({scale:.6f}) translate({-bx:.4f} {-by:.4f})">{node}</g>',bh*scale

def symbol(x,y,s,color=None):
    # A and V share the descending diagonal; open top-right curve evokes a fold.
    color=color or C['verde']
    p='M8 88 L38 12 Q40 7 43 12 L76 88 L65 88 L40 29 L18 88 Z M25 65 L59 65 L63 74 L22 74 Z M49 13 L60 13 L81 65 L94 31 Q98 21 109 20 L109 30 Q104 31 102 37 L83 88 L77 88 Z'
    return f'<g transform="translate({x} {y}) scale({s/116})"><path d="{p}" fill="{color}"/></g>'

def motif(x,y,s,color=None,opacity=1):
    return f'<g opacity="{opacity}">{symbol(x,y,s,color)}</g>'

class Canvas:
    def __init__(self,w,h,title,bg=None):
        self.w=w;self.h=h;self.title=title;self.parts=[];self.defs=[];self.texts=[]
        if bg:self.rect(0,0,w,h,bg)
    def rect(self,x,y,w,h,fill,rx=0,stroke=None,sw=1):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
    def line(self,x1,y1,x2,y2,color,sw=1,dash=None):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
    def circle(self,x,y,r,fill,stroke=None,sw=1):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
    def path(self,d,fill,stroke=None,sw=1):
        self.parts.append(f'<path d="{d}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if stroke else '')+'/>')
    def text(self,value,x,y,size=28,family='Manrope',weight=400,color=None,anchor='start',spacing=0,italic=False):
        color=color or C['verde']
        node,bbox=outlined_text(value,x,y,size,family,weight,color,anchor,spacing,italic)
        font=family
        editable=f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" font-style="{"italic" if italic else "normal"}" text-anchor="{anchor}" letter-spacing="{spacing}" fill="{color}" style="font-variation-settings:\'SOFT\' 12,\'WONK\' 0,\'opsz\' 72">{escape(value)}</text>'
        self.parts.append((node,editable));self.texts.append({'text':value,'bounds':bbox,'font':family,'size':size})
    def lines(self,values,x,y,size=28,leading=None,**kwargs):
        for i,v in enumerate(values):self.text(v,x,y+i*(leading or size*1.2),size,**kwargs)
    def logo(self,x,y,w,color=None):
        node,h=wordmark(x,y,w,color);self.parts.append(node);return h
    def sym(self,x,y,s,color=None):self.parts.append(symbol(x,y,s,color))
    def image(self,filename,x,y,w,h,fit='xMidYMid slice'):
        data=Path(filename).read_bytes();mime='image/png' if data[:8]==b'\x89PNG\r\n\x1a\n' else 'image/jpeg'
        self.parts.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" overflow="hidden"><image href="data:{mime};base64,{base64.b64encode(data).decode()}" width="{w}" height="{h}" preserveAspectRatio="{fit}"/></svg>')
    def svg(self,editable=False,physical=None):
        style=''
        if editable:
            css=[]
            for fam,italic in [('Fraunces',False),('Fraunces',True),('Manrope',False)]:
                data=(OUT/'06-fontes'/(fam+('-Italic' if italic else '')+'.ttf')).read_bytes()
                css.append('@font-face{font-family:"'+fam+'";font-weight:100 900;font-style:'+('italic' if italic else 'normal')+';src:url(data:font/ttf;base64,'+base64.b64encode(data).decode()+')}')
            style='<style>'+''.join(css)+'</style>'
        attrs=f'width="{self.w}" height="{self.h}"' if not physical else f'width="{physical[0]}mm" height="{physical[1]}mm"'
        return f'<svg xmlns="http://www.w3.org/2000/svg" {attrs} viewBox="0 0 {self.w} {self.h}" role="img"><title>{escape(self.title)}</title><defs>{style}{"".join(self.defs)}</defs>'+''.join(p[1 if editable else 0] if isinstance(p,tuple) else p for p in self.parts)+'</svg>'
    def save(self,relative,editable=False,physical=None):
        target=OUT/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(self.svg(False,physical),encoding='utf-8')
        if editable:
            ep=target.parent/'editaveis'/target.name;ep.parent.mkdir(exist_ok=True);ep.write_text(self.svg(True,physical),encoding='utf-8')
        return {'file':str(target.relative_to(OUT)).replace('\\','/'),'width':self.w,'height':self.h,'title':self.title,'text_bounds':self.texts,'physical_mm':physical}

def pill(c,label,x,y,w=None,color=None,bg=None,size=22):
    w=w or width(label,size,'Manrope',600)+56
    c.rect(x,y,w,54,bg or C['coral'],27)
    c.text(label,x+w/2,y+35,size,weight=600,color=color or C['verde'],anchor='middle')
    return w

def footer(c,num,color=None):
    color=color or C['verde'];c.line(72,c.h-105,c.w-72,c.h-105,color,1)
    c.text('@use_aurevi',72,c.h-58,20,weight=500,color=color)
    c.text(num,c.w-72,c.h-58,18,weight=600,color=color,anchor='end')
