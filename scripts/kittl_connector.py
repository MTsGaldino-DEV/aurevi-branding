"""Use the authenticated local Codex app-server MCP connection without reading credentials.

No model turn is started. This is an ordinary JSON-RPC client for the configured
Kittl connector; authentication remains managed by Codex.
"""
from pathlib import Path
from urllib.parse import urlsplit,urlunsplit
import json,subprocess,threading,queue,sys,time,shutil
ROOT=Path(__file__).resolve().parents[1]
STATE=ROOT/'.tools/kittl'
STATE.mkdir(parents=True,exist_ok=True)

class Bridge:
 def __init__(self):
  self.p=subprocess.Popen([shutil.which('codex'),'app-server','--stdio'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=(STATE/'server.log').open('a',encoding='utf-8'),text=True,encoding='utf-8',bufsize=1)
  self.q=queue.Queue();self.n=0
  def read():
   for line in self.p.stdout:
    try:self.q.put(json.loads(line))
    except ValueError:pass
  threading.Thread(target=read,daemon=True).start()
  self.call('initialize',{'clientInfo':{'name':'aurevi-kittl-connector','version':'1.0.0'},'capabilities':{'experimentalApi':True}})
  self.send({'method':'initialized'})
  result=self.call('thread/start',{'cwd':str(ROOT),'ephemeral':True,'approvalPolicy':'never'})
  self.thread=result['thread']['id']
 def send(self,x):self.p.stdin.write(json.dumps(x,ensure_ascii=False)+'\n');self.p.stdin.flush()
 def call(self,method,params,timeout=180):
  self.n+=1;rid=self.n;self.send({'id':rid,'method':method,'params':params})
  end=time.time()+timeout
  while time.time()<end:
   r=self.q.get(timeout=max(1,end-time.time()))
   if r.get('id')==rid:
    if 'error'in r:raise RuntimeError(json.dumps(r['error'],ensure_ascii=False))
    return r['result']
   if 'id'in r and 'method'in r:
    # Never silently approve a new elicitation or security request.
    self.send({'id':r['id'],'error':{'code':-32000,'message':'Interactive approval requires the user; no automatic response supplied.'}})
 def tools(self):return self.call('mcpServerStatus/list',{'threadId':self.thread,'serverName':'kittl','detail':'toolsAndAuthOnly'})
 def tool(self,name,args):return self.call('mcpServer/tool/call',{'threadId':self.thread,'server':'kittl','tool':name,'arguments':args},600)
 def close(self):self.p.terminate()

def main():
 b=Bridge()
 try:
  if len(sys.argv)==1 or sys.argv[1]=='list':
   r=b.tools();(STATE/'tools.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
   for s in r.get('data',[]):
    print('server:',s.get('name'),'auth:',s.get('authStatus'))
    tools=s.get('tools',{})
    if isinstance(tools,dict):
     for k,v in tools.items():print(k,':',v.get('description','')[:220])
    else:
     for t in tools:print(t.get('name'),':',t.get('description','')[:220])
  elif sys.argv[1]=='batch':
   jobs=json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
   for job in jobs:
    r=b.tool(job['tool'],job.get('arguments',{}))
    (STATE/job['output']).write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
    print(job['output'],json.dumps(safe(r),ensure_ascii=False)[:1800])
  else:
   args=json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
   r=b.tool(sys.argv[1],args)
   result=STATE/(sys.argv[3] if len(sys.argv)>3 else 'last-result.json')
   result.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
   print(str(result));print(json.dumps(safe(r),ensure_ascii=False)[:12000])
 finally:b.close()

def safe(value):
 if isinstance(value,dict):
  if value.get('type')=='image':return {'type':'image','data':'[image bytes omitted]'}
  return {k:safe(v) for k,v in value.items()}
 if isinstance(value,list):return [safe(v) for v in value]
 if isinstance(value,str):
  if value.startswith('data:') or len(value)>50000:return '[large asset omitted]'
  try:return safe(json.loads(value))
  except (ValueError,TypeError):pass
  if value.startswith('http') and '?'in value:
   u=urlsplit(value);return urlunsplit((u.scheme,u.netloc,u.path,'[query omitted]',''))
 return value
if __name__=='__main__':main()
