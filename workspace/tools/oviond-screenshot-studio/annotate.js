const fs = require('fs');
const sharp = require('sharp');

const BLUE = '#5676FF';
const CYAN = '#75D2DA';
const INK = '#0B1020';

function esc(s='') { return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c])); }
function wrap(text, max=34) {
  const words = String(text).split(/\s+/); const lines=[]; let cur='';
  for (const w of words) { if ((cur+' '+w).trim().length > max && cur) { lines.push(cur); cur=w; } else cur=(cur+' '+w).trim(); }
  if (cur) lines.push(cur); return lines;
}
function calloutSvg({width,height,items=[],title='',subtitle=''}) {
  let svg = `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">`;
  svg += `<defs><filter id="shadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0B1020" flood-opacity="0.18"/></filter><filter id="soft"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0B1020" flood-opacity="0.12"/></filter></defs>`;
  if (title) {
    const w = Math.min(width-64, 810);
    svg += `<rect x="32" y="28" rx="20" width="${w}" height="${subtitle ? 88 : 62}" fill="rgba(255,255,255,0.95)" filter="url(#shadow)"/>`;
    svg += `<text x="60" y="66" font-family="Inter, Arial, sans-serif" font-size="25" font-weight="850" fill="${INK}">${esc(title)}</text>`;
    if (subtitle) svg += `<text x="60" y="96" font-family="Inter, Arial, sans-serif" font-size="15" font-weight="550" fill="#475569">${esc(subtitle)}</text>`;
  }
  for (const [idx, it] of items.entries()) {
    const n = it.number || idx+1;
    const x=it.x, y=it.y, w=it.w, h=it.h;
    const color = it.color || BLUE;
    svg += `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="14" fill="rgba(86,118,255,0.06)" stroke="${color}" stroke-width="5"/>`;
    svg += `<circle cx="${x-1}" cy="${y-1}" r="19" fill="${color}" filter="url(#soft)"/>`;
    svg += `<text x="${x-1}" y="${y+6}" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="18" font-weight="900" fill="white">${n}</text>`;
    if (it.label) {
      const lx = it.labelX ?? Math.min(width-340, x+w+22);
      const ly = it.labelY ?? y;
      const lines = wrap(it.label, it.maxChars || 34);
      const boxH = 26 + lines.length*20;
      svg += `<rect x="${lx}" y="${ly}" rx="15" width="320" height="${boxH}" fill="rgba(255,255,255,0.97)" filter="url(#shadow)"/>`;
      lines.forEach((line,i)=> svg += `<text x="${lx+18}" y="${ly+29+i*20}" font-family="Inter, Arial, sans-serif" font-size="15" font-weight="700" fill="${INK}">${esc(line)}</text>`);
      const ax1 = lx < x ? lx+320 : lx;
      const ax2 = lx < x ? x : x+w;
      svg += `<path d="M ${ax1} ${ly+boxH/2} L ${ax2} ${y+h/2}" stroke="${color}" stroke-width="3" fill="none" stroke-linecap="round" stroke-dasharray="5 8"/>`;
    }
  }
  svg += `</svg>`; return Buffer.from(svg);
}
async function annotate({input,output,title,subtitle,items}) {
  const img = sharp(input); const meta = await img.metadata();
  await img.composite([{input: calloutSvg({width:meta.width,height:meta.height,title,subtitle,items}), top:0,left:0}]).png().toFile(output);
  return {output,width:meta.width,height:meta.height};
}
async function createMockProduct(output) {
  const width=1440, height=980;
  const cards=['Acme Dental','Bluebird Ads','Cape Fitness','Delta Legal','Evergreen SaaS','Finch Retail'];
  const svg = `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="1440" height="980" fill="#F6F8FC"/>
  <rect x="0" y="0" width="260" height="980" fill="#101828"/>
  <text x="34" y="54" font-family="Inter, Arial" font-size="27" font-weight="900" fill="#fff">Oviond</text>
  ${['Clients','Reports','Data Sources','Automations','Templates','Settings'].map((t,i)=>`<rect x="22" y="${104+i*54}" width="216" height="38" rx="10" fill="${i==0?'#243B88':'transparent'}"/><text x="48" y="${129+i*54}" font-family="Inter, Arial" font-size="15" font-weight="750" fill="${i==0?'#fff':'#B8C0D4'}">${t}</text>`).join('')}
  <rect x="300" y="38" width="1090" height="86" rx="24" fill="#fff"/>
  <text x="332" y="78" font-family="Inter, Arial" font-size="26" font-weight="900" fill="#101828">Clients</text>
  <text x="332" y="105" font-family="Inter, Arial" font-size="15" fill="#667085">Manage client workspaces, reporting data, and dashboards.</text>
  <rect x="1215" y="61" width="142" height="42" rx="13" fill="#5676FF"/><text x="1242" y="88" font-family="Inter, Arial" font-size="15" font-weight="850" fill="#fff">Add Client</text>
  <rect x="300" y="154" width="1090" height="70" rx="18" fill="#fff"/><rect x="326" y="174" width="380" height="32" rx="10" fill="#F1F5F9"/><text x="344" y="195" font-family="Inter, Arial" font-size="14" fill="#64748B">Search clients...</text>
  ${cards.map((name,i)=>{const x=300+(i%3)*370,y=254+Math.floor(i/3)*230; return `<g><rect x="${x}" y="${y}" width="340" height="190" rx="22" fill="#fff"/><rect x="${x+24}" y="${y+24}" width="70" height="70" rx="16" fill="${i%2?'#E0F7FA':'#EEF2FF'}"/><text x="${x+112}" y="${y+50}" font-family="Inter, Arial" font-size="20" font-weight="850" fill="#101828">${name}</text><text x="${x+112}" y="${y+78}" font-family="Inter, Arial" font-size="14" fill="#667085">${[4,7,3,9,5,2][i]} projects • ${[3,5,2,6,4,1][i]} data sources</text><rect x="${x+24}" y="${y+122}" width="128" height="34" rx="10" fill="#ECFDF3"/><text x="${x+42}" y="${y+144}" font-family="Inter, Arial" font-size="13" font-weight="750" fill="#027A48">Active</text></g>`}).join('')}
  </svg>`;
  await sharp(Buffer.from(svg)).png().toFile(output);
}
async function createMarketingCard(output) {
  const svg = `<svg width="1600" height="1000" viewBox="0 0 1600 1000" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F8FAFF"/><stop offset="1" stop-color="#EAF7FF"/></linearGradient><filter id="s"><feDropShadow dx="0" dy="24" stdDeviation="24" flood-color="#0B1020" flood-opacity="0.16"/></filter></defs>
  <rect width="1600" height="1000" fill="url(#g)"/><circle cx="1280" cy="170" r="260" fill="#75D2DA" opacity="0.22"/><circle cx="180" cy="840" r="300" fill="#5676FF" opacity="0.12"/>
  <text x="112" y="158" font-family="Inter, Arial" font-size="34" font-weight="900" fill="#5676FF">OVIOND</text>
  <text x="112" y="262" font-family="Inter, Arial" font-size="64" font-weight="900" fill="#0B1020">Client reporting,</text><text x="112" y="334" font-family="Inter, Arial" font-size="64" font-weight="900" fill="#0B1020">beautifully done.</text>
  <text x="116" y="396" font-family="Inter, Arial" font-size="25" font-weight="500" fill="#475569">Build branded dashboards, connect marketing data,</text><text x="116" y="430" font-family="Inter, Arial" font-size="25" font-weight="500" fill="#475569">and automate client-ready reports.</text>
  <rect x="108" y="458" width="250" height="58" rx="18" fill="#5676FF"/><text x="146" y="495" font-family="Inter, Arial" font-size="20" font-weight="850" fill="#fff">Start reporting</text>
  <g filter="url(#s)"><rect x="720" y="150" width="740" height="620" rx="34" fill="#fff"/><rect x="770" y="220" width="260" height="28" rx="10" fill="#E2E8F0"/><rect x="770" y="286" width="620" height="190" rx="24" fill="#F8FAFC"/><path d="M820 425 C930 320 1010 445 1110 350 C1200 265 1290 370 1350 300" fill="none" stroke="#5676FF" stroke-width="14" stroke-linecap="round"/><rect x="770" y="525" width="180" height="120" rx="22" fill="#EEF2FF"/><rect x="990" y="525" width="180" height="120" rx="22" fill="#E0F7FA"/><rect x="1210" y="525" width="180" height="120" rx="22" fill="#ECFDF3"/></g>
  </svg>`;
  await sharp(Buffer.from(svg)).png().toFile(output);
}
async function main(){
  const mode=process.argv[2];
  if(mode==='mock') return createMockProduct(process.argv[3]);
  if(mode==='marketing') return createMarketingCard(process.argv[3]);
  const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
  await annotate(cfg);
}
main().catch(e=>{console.error(e); process.exit(1);});
