/* PC-24 Memory Trainer — service worker
 *
 * Strategy: cache-first so the app opens instantly and works with no signal
 * (sim building, hotel, airplane), with a background revalidate so a new
 * version is picked up the next time you have a connection. The page shows an
 * "Update available" banner rather than swapping content mid-session — you
 * should never have a card change out from under you while drilling.
 *
 * To ship an update: bump CACHE_VERSION. That is the only required change —
 * the old cache is deleted on activate, so a stale card set cannot survive.
 */

const CACHE_VERSION = 'v1';
const CACHE_NAME = `pc24-trainer-${CACHE_VERSION}`;

const PRECACHE = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-180.png',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      // Individual addAll failures would abort the whole install, so fetch each
      // entry on its own and let optional assets fail without breaking offline.
      .then(cache => Promise.all(
        PRECACHE.map(url =>
          cache.add(new Request(url, { cache: 'reload' })).catch(() => null)
        )
      ))
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k.startsWith('pc24-trainer-') && k !== CACHE_NAME)
            .map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then(cached => {
      const network = fetch(req)
        .then(res => {
          if (res && res.ok) {
            const copy = res.clone();
            caches.open(CACHE_NAME).then(c => c.put(req, copy)).catch(() => {});
          }
          return res;
        })
        .catch(() => null);

      if (cached) {
        // Serve the cache immediately; the network copy refreshes it for next launch.
        network.catch(() => {});
        return cached;
      }

      return network.then(res => {
        if (res) return res;
        // Offline with nothing cached: fall back to the app shell for navigations.
        if (req.mode === 'navigate') {
          return caches.match('./index.html', { ignoreSearch: true });
        }
        return new Response('Offline and not cached', {
          status: 503,
          headers: { 'Content-Type': 'text/plain' },
        });
      });
    })
  );
});

self.addEventListener('message', event => {
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
  if (event.data === 'GET_VERSION') {
    event.source && event.source.postMessage({ type: 'VERSION', version: CACHE_VERSION });
  }
});
