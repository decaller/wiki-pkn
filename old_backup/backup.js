import fs from 'fs';
import path from 'path';

const API_URL = 'https://outline.insantaqwa.org/api';
// We'll read it from .env or fallback to the provided key
const API_KEY = process.env.OUTLINE_API_KEY || 'ol_api_pnodjdUre7qQhzzT2IgdB6flw2DJvm9y6fo7NR';
const BACKUP_DIR = '/home/deck/Projects/wiki-pkn/old_backup/export';

async function outlinePost(endpoint, body = {}) {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify(body)
  });
  const data = await res.json();
  if (!data.ok) {
    throw new Error(`Outline API error on ${endpoint}: ${data.error || data.message || JSON.stringify(data)}`);
  }
  return data;
}

function sanitize(name) {
  return name.replace(/[^a-z0-9\-_ ]/gi, '_').trim();
}

async function main() {
  console.log('Starting manual backup process (since Admin role is missing for export_all)...');
  fs.mkdirSync(BACKUP_DIR, { recursive: true });

  const collectionsData = await outlinePost('/collections.list');
  const collections = collectionsData.data;
  console.log(`Found ${collections.length} collections.`);

  for (const collection of collections) {
    const colDir = path.join(BACKUP_DIR, sanitize(collection.name));
    fs.mkdirSync(colDir, { recursive: true });
    console.log(`Backing up collection: ${collection.name}`);

    // Fetch documents in this collection
    let offset = 0;
    let hasMore = true;
    while (hasMore) {
      const docsData = await outlinePost('/documents.list', {
        collectionId: collection.id,
        limit: 100,
        offset
      });

      const documents = docsData.data;
      if (!documents || documents.length === 0) break;

      for (const doc of documents) {
        console.log(`  Fetching document: ${doc.title}`);
        try {
          const docInfo = await outlinePost('/documents.info', { id: doc.id });
          const text = docInfo.data.text;
          const docTitle = sanitize(doc.title) || doc.id;
          fs.writeFileSync(path.join(colDir, `${docTitle}.md`), text);
        } catch (err) {
          console.error(`  Failed to fetch doc ${doc.title}:`, err.message);
        }
      }

      offset += 100;
      hasMore = docsData.pagination && offset < docsData.pagination.total;
    }
  }

  console.log(`Backup complete! Files saved in ${BACKUP_DIR}`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
