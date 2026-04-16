import { figmaGet, pretty } from './figma-client.mjs';

const projectId = process.argv[2];
if (!projectId) {
  console.error('Usage: node project-files.mjs <project_id>');
  process.exit(1);
}

const data = await figmaGet(`/projects/${projectId}/files`);
pretty(data);
