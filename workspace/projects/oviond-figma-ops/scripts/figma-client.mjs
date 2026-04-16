import fs from 'fs/promises';
import path from 'path';

const BASE_URL = 'https://api.figma.com/v1';

export function getToken() {
  const token = process.env.FIGMA_ACCESS_TOKEN;
  if (!token) {
    throw new Error('FIGMA_ACCESS_TOKEN is missing');
  }
  return token;
}

export async function figmaGet(apiPath, query = {}) {
  const token = getToken();
  const url = new URL(`${BASE_URL}${apiPath}`);
  for (const [key, value] of Object.entries(query)) {
    if (value !== undefined && value !== null && value !== '') {
      url.searchParams.set(key, String(value));
    }
  }

  const response = await fetch(url, {
    headers: {
      'X-Figma-Token': token,
      'User-Agent': 'oviond-figma-ops/0.1'
    }
  });

  const text = await response.text();
  let data;
  try {
    data = JSON.parse(text);
  } catch {
    data = text;
  }

  if (!response.ok) {
    throw new Error(`Figma API ${response.status}: ${typeof data === 'string' ? data : JSON.stringify(data)}`);
  }

  return data;
}

export async function downloadFile(url, outPath) {
  const response = await fetch(url, {
    headers: {
      'User-Agent': 'oviond-figma-ops/0.1'
    }
  });
  if (!response.ok) {
    throw new Error(`Download failed ${response.status}: ${url}`);
  }
  const arrayBuffer = await response.arrayBuffer();
  await fs.mkdir(path.dirname(outPath), { recursive: true });
  await fs.writeFile(outPath, Buffer.from(arrayBuffer));
}

export function pretty(data) {
  console.log(JSON.stringify(data, null, 2));
}
