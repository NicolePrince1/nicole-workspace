import path from 'path';
import { figmaGet, downloadFile, pretty } from './figma-client.mjs';

const fileKey = process.argv[2];
const nodeIds = process.argv[3];
const format = process.argv[4] || 'png';
const scale = process.argv[5] || '2';

if (!fileKey || !nodeIds) {
  console.error('Usage: node export-images.mjs <file_key> <node_ids_csv> [format] [scale]');
  process.exit(1);
}

const data = await figmaGet(`/images/${fileKey}`, {
  ids: nodeIds,
  format,
  scale
});

const exportsDir = path.resolve('projects/oviond-figma-ops/exports');
const written = [];
for (const [nodeId, url] of Object.entries(data.images || {})) {
  if (!url) continue;
  const safeNodeId = nodeId.replace(/[:/\\]/g, '_');
  const outPath = path.join(exportsDir, `${safeNodeId}.${format}`);
  await downloadFile(url, outPath);
  written.push({ nodeId, outPath });
}

pretty({ ok: true, written, raw: data });
