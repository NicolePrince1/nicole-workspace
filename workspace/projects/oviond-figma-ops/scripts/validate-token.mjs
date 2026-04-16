import { figmaGet, pretty } from './figma-client.mjs';

const data = await figmaGet('/me');
pretty({
  ok: true,
  id: data.id,
  handle: data.handle,
  email: data.email,
  img_url: data.img_url
});
