import fs from 'fs';

const API_URL = 'https://outline.insantaqwa.org/api';
const API_KEY = 'ol_api_pnodjdUre7qQhzzT2IgdB6flw2DJvm9y6fo7NR';

async function fetchAPI(endpoint, body = {}) {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${API_KEY}`,
      'Accept': 'application/json'
    },
    body: JSON.stringify(body)
  });
  
  if (!res.ok) {
    throw new Error(`API Error ${res.status} on ${endpoint}: ${await res.text()}`);
  }
  
  return (await res.json()).data;
}

async function main() {
  try {
    console.log("Fetching collections...");
    const collections = await fetchAPI('/collections.list');
    console.log(`Found ${collections.length} collections.`);
    
    const fullBackup = {};

    for (const collection of collections) {
      console.log(`Fetching structure for collection: ${collection.name} (${collection.id})`);
      const structure = await fetchAPI('/collections.documents', { id: collection.id });
      
      fullBackup[collection.id] = {
        collection: collection,
        structure: structure
      };
    }

    fs.writeFileSync('outline_structure_backup.json', JSON.stringify(fullBackup, null, 2));
    console.log("Successfully saved structure to outline_structure_backup.json!");
  } catch (err) {
    console.error("Failed to backup structure:", err);
  }
}

main();
