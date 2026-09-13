import json,zipfile,html,textwrap
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
root=Path.cwd(); slides=json.loads((root/'.ppt-build/slides.json').read_text(encoding='utf-8'))
A='http://schemas.openxmlformats.org/drawingml/2006/main'; P='http://schemas.openxmlformats.org/presentationml/2006/main'; R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
esc=lambda t:html.escape(str(t),quote=True)
def rels(rows):return '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'+''.join(f'<Relationship Id="{i}" Type="{R}/{k}" Target="{t}"/>' for i,k,t in rows)+'</Relationships>'
def tree():return '<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
def tx(t,x,y,w,h,size,color,bold,id):
 paras=''.join(f'<a:p><a:pPr/><a:r><a:rPr lang="en-US" sz="{int(size*75)}" b="{int(bold)}"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill><a:latin typeface="Arial"/></a:rPr><a:t>{esc(line)}</a:t></a:r><a:endParaRPr lang="en-US"/></a:p>' for line in t.split('\n'))
 return f'<p:sp><p:nvSpPr><p:cNvPr id="{id}" name="Text {id}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{int(x*9525)}" y="{int(y*9525)}"/><a:ext cx="{int(w*9525)}" cy="{int(h*9525)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" lIns="0" rIns="0" tIns="0" bIns="0"/><a:lstStyle/>{paras}</p:txBody></p:sp>'
files={}; types=[]
def put(path,data,typ=None):files[path]=data; types.append((path,typ)) if typ else None
put('_rels/.rels',rels([('rId1','officeDocument','ppt/presentation.xml')]))
put('ppt/presentation.xml',f'<p:presentation xmlns:p="{P}" xmlns:a="{A}" xmlns:r="{R}"><p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId9"/></p:sldMasterIdLst><p:sldIdLst>'+''.join(f'<p:sldId id="{256+i}" r:id="rId{i}"/>' for i in range(1,9))+'</p:sldIdLst><p:sldSz cx="12192000" cy="6858000"/><p:notesSz cx="6858000" cy="9144000"/></p:presentation>','application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml')
put('ppt/_rels/presentation.xml.rels',rels([(f'rId{i}','slide',f'slides/slide{i}.xml') for i in range(1,9)]+[('rId9','slideMaster','slideMasters/slideMaster1.xml')]))
put('ppt/slideMasters/slideMaster1.xml',f'<p:sldMaster xmlns:p="{P}" xmlns:a="{A}" xmlns:r="{R}"><p:cSld><p:spTree>{tree()}</p:spTree></p:cSld><p:clrMap accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" bg1="lt1" bg2="lt2" folHlink="folHlink" hlink="hlink" tx1="dk1" tx2="dk2"/><p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst></p:sldMaster>','application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml')
put('ppt/slideMasters/_rels/slideMaster1.xml.rels',rels([('rId1','slideLayout','../slideLayouts/slideLayout1.xml')]))
put('ppt/slideLayouts/slideLayout1.xml',f'<p:sldLayout xmlns:p="{P}" xmlns:a="{A}" type="blank" preserve="1"><p:cSld name="Blank"><p:spTree>{tree()}</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>','application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml')
put('ppt/slideLayouts/_rels/slideLayout1.xml.rels',rels([('rId1','slideMaster','../slideMasters/slideMaster1.xml')]))
for n,s in enumerate(slides,1):
 bg=s['background']['fill']; im=Image.new('RGB',(1280,720),bg); draw=ImageDraw.Draw(im); body=tree(); rr=[('rId1','slideLayout','../slideLayouts/slideLayout1.xml'),('rId2','notesSlide',f'../notesSlides/notesSlide{n}.xml')]
 for j,e in enumerate(s['elements'],3):
  q=e['position'];x,y,w,h=[q[k] for k in ['left','top','width','height']]
  if e.get('kind')=='image':
   f=(root/'.ppt-build/logos'/e['alt'].split(':',1)[1]) if e['alt'].startswith('logo:') else (root/'docs/screenshots'/f"{e['alt']}.png"); pic=Image.open(f); ratio=min(w/pic.width,h/pic.height);iw,ih=int(pic.width*ratio),int(pic.height*ratio);xx=x+(w-iw)/2; yy=y+(h-ih)/2
   rendered=pic.resize((iw,ih)); im.paste(rendered,(int(xx),int(yy)),rendered if rendered.mode=='RGBA' else None);name=f'image{n}_{j}.png';put('ppt/media/'+name,f.read_bytes());rr.append((f'rId{j}','image','../media/'+name))
   body+=f'<p:pic><p:nvPicPr><p:cNvPr id="{j}" name="{e["alt"]}"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr><p:blipFill><a:blip r:embed="rId{j}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill><p:spPr><a:xfrm><a:off x="{int(xx*9525)}" y="{int(yy*9525)}"/><a:ext cx="{iw*9525}" cy="{ih*9525}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>'
  else:
   st=e['style']; sz=st['fontSize']; color=st['color']; bold=st['bold'];t=e['value'];font=ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),int(sz));lines=[]
   for para in t.split('\n'):
    line=''
    for word in para.split():
     test=(line+' '+word).strip()
     if draw.textlength(test,font=font)>w and line:lines.append(line);line=word
     else:line=test
    lines.append(line)
   if len(lines)*sz*1.18>h+8:print('FIT WARNING',n,t[:35],len(lines)*sz*1.18,h)
   draw.multiline_text((x,y),'\n'.join(lines),font=font,fill=color,spacing=int(sz*.18));body+=tx(t,x,y,w,h,sz,color.strip('#'),bold,j)
 im.save(root/f'.ppt-build/slide-{n}.png')
 put(f'ppt/slides/slide{n}.xml',f'<p:sld xmlns:p="{P}" xmlns:a="{A}" xmlns:r="{R}"><p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="{bg.strip(chr(35))}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg><p:spTree>{body}</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>','application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
 put(f'ppt/slides/_rels/slide{n}.xml.rels',rels(rr))
 notes=tx(s['notes'],40,40,600,900,16,'173F3A',False,2).replace('<p:nvPr/>','<p:nvPr><p:ph type="body" idx="1"/></p:nvPr>',1)
 put(f'ppt/notesSlides/notesSlide{n}.xml',f'<p:notes xmlns:p="{P}" xmlns:a="{A}"><p:cSld><p:spTree>{tree()}{notes}</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:notes>','application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml')
 put(f'ppt/notesSlides/_rels/notesSlide{n}.xml.rels',rels([('rId1','slide',f'../slides/slide{n}.xml')]))
put('[Content_Types].xml','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/>'+''.join(f'<Override PartName="/{p}" ContentType="{t}"/>' for p,t in types)+'</Types>')
out=root/'output/Senior_Travel_Companion_4_Minute_Pitch_v2.pptx'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p,d in files.items():z.writestr(p,d)
script='# Four-minute presentation script\n\n'+ '\n\n'.join(f'## Slide {i}\n\n'+s['notes'].split('\nSources:')[0] for i,s in enumerate(slides,1))
(root/'output/Speaker_Notes_4_Minutes.md').write_text(script,encoding='utf-8')
print(out)
