const input = process.argv[2];
if (!input) {
  console.error('Usage: node parse-url.mjs <figma_url>');
  process.exit(1);
}

const url = new URL(input);
const parts = url.pathname.split('/').filter(Boolean);
const result = { url: input };

const teamIndex = parts.indexOf('team');
if (teamIndex >= 0 && parts[teamIndex + 1]) {
  result.team_id = parts[teamIndex + 1];
}

const fileIndex = parts.findIndex(part => part === 'file' || part === 'design' || part === 'board');
if (fileIndex >= 0 && parts[fileIndex + 1]) {
  result.file_key = parts[fileIndex + 1];
}

const projectIndex = parts.indexOf('project');
if (projectIndex >= 0 && parts[projectIndex + 1]) {
  result.project_id = parts[projectIndex + 1];
}

const nodeId = url.searchParams.get('node-id');
if (nodeId) {
  result.node_id = nodeId;
}

console.log(JSON.stringify(result, null, 2));
