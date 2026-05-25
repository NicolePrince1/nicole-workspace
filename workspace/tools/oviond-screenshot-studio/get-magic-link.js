const https=require('https');
const {execFileSync}=require('child_process');
const token=execFileSync('node',['/data/.openclaw/secrets/gws-token.js','gmail.modify'],{encoding:'utf8'}).trim();
function req(path){return new Promise((resolve,reject)=>{https.get({hostname:'gmail.googleapis.com',path,headers:{Authorization:`Bearer ${token}`}},res=>{let b='';res.on('data',d=>b+=d);res.on('end',()=>{if(res.statusCode>=300)return reject(new Error(res.statusCode+' '+b));resolve(JSON.parse(b));});}).on('error',reject);});}
function b64(s){return Buffer.from((s||'').replace(/-/g,'+').replace(/_/g,'/'),'base64').toString('utf8');}
function walk(payload, out=[]){ if(payload.body?.data) out.push(b64(payload.body.data)); for(const p of payload.parts||[]) walk(p,out); return out; }
(async()=>{
 const q=encodeURIComponent('to:nicole@oviond.com newer_than:1d ("magic" OR "sign in" OR "Oviond")');
 const list=await req(`/gmail/v1/users/me/messages?q=${q}&maxResults=10`);
 console.log('found', list.messages?.length||0);
 for(const m of list.messages||[]){
  const msg=await req(`/gmail/v1/users/me/messages/${m.id}?format=full`);
  const headers=Object.fromEntries((msg.payload.headers||[]).map(h=>[h.name.toLowerCase(),h.value]));
  const text=walk(msg.payload).join('\n');
  const links=[...text.matchAll(/https?:\/\/[^\s"'<>]+/g)].map(x=>x[0].replace(/&amp;/g,'&'));
  console.log(JSON.stringify({id:m.id, date:headers.date, from:headers.from, subject:headers.subject, snippet:msg.snippet, links:links.filter(l=>/app\.oviond\.com|supabase|auth|token|verify|signin|sign/i.test(l)).slice(0,10)}, null, 2));
 }
})();
