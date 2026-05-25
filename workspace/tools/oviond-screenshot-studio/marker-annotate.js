const fs = require('fs');
const sharp = require('sharp');
const BLUE = '#5676FF';
function markerSvg(w,h,items){
  let s=`<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg"><defs><filter id="s"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0B1020" flood-opacity="0.18"/></filter></defs>`;
  for(const [i,it] of items.entries()){
    const n=it.number||i+1; const color=it.color||BLUE;
    s+=`<rect x="${it.x}" y="${it.y}" width="${it.w}" height="${it.h}" rx="14" fill="rgba(86,118,255,0.07)" stroke="${color}" stroke-width="5"/>`;
    const cx = it.badgeX ?? Math.max(22, Math.min(w-22, it.x + 18));
    const cy = it.badgeY ?? Math.max(22, Math.min(h-22, it.y + 18));
    s+=`<circle cx="${cx}" cy="${cy}" r="19" fill="${color}" filter="url(#s)"/>`;
    s+=`<text x="${cx}" y="${cy+7}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="18" font-weight="900" fill="#fff">${n}</text>`;
  }
  return Buffer.from(s+'</svg>');
}
async function main(){
  const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
  const img=sharp(cfg.input); const meta=await img.metadata();
  await img.composite([{input:markerSvg(meta.width,meta.height,cfg.items),top:0,left:0}]).png().toFile(cfg.output);
  console.log(JSON.stringify({output:cfg.output,width:meta.width,height:meta.height}));
}
main().catch(e=>{console.error(e);process.exit(1);});
