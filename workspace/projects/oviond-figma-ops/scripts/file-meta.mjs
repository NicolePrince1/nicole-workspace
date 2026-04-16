import { figmaGet, pretty } from './figma-client.mjs';

const fileKey = process.argv[2];
if (!fileKey) {
  console.error('Usage: node file-meta.mjs <file_key>');
  process.exit(1);
}

const data = await figmaGet(`/files/${fileKey}/meta`);
pretty(data);
