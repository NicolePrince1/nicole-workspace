import { figmaGet, pretty } from './figma-client.mjs';

const teamId = process.argv[2];
if (!teamId) {
  console.error('Usage: node team-projects.mjs <team_id>');
  process.exit(1);
}

const data = await figmaGet(`/teams/${teamId}/projects`);
pretty(data);
