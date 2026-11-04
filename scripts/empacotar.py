from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'ENTREGA'
target=ROOT/'Aurevi-Kit-Identidade.zip'
files=sorted(p for p in OUT.rglob('*') if p.is_file())
with ZipFile(target,'w',compression=ZIP_DEFLATED,compresslevel=7) as z:
 for p in files:z.write(p,'Aurevi/'+p.relative_to(OUT).as_posix())
with ZipFile(target) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(files)
 assert not any('/pesquisa/'in n or '/.tools/'in n for n in z.namelist())
 assert 'Aurevi/COMECE-AQUI.html' in z.namelist()
 for n in z.namelist():
  local=OUT/n.removeprefix('Aurevi/')
  assert hashlib.sha256(z.read(n)).digest()==hashlib.sha256(local.read_bytes()).digest(),n
report={'file':target.name,'files':len(files),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'crc':'passed','all_files_match':'passed'}
(ROOT/'docs/pacote-final.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
