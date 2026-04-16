import { figmaGet, pretty } from './figma-client.mjs';

const fileKey = process.argv[2];
const depth = process.argv[3] || '2';
if (!fileKey) {
  console.error('Usage: node file-tree.mjs <file_key> [depth]');
  process.exit(1);
}

const data = await figmaGet(`/files/${fileKey}`, { depth });
pretty({
  name: data.name,
  lastModified: data.lastModified,
  version: data.version,
  pages: data.document?.children?.map(page => ({
    id: page.id,
    name: page.name,
    type: page.type,
    children: (page.children || []).map(child => ({
      id: child.id,
      name: child.name,
      type: child.type
    }))
  }))
});
