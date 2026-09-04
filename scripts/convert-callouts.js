import fs from 'fs';
import path from 'path';

function walkDir(dir, callback) {
  fs.readdirSync(dir).forEach(f => {
    let dirPath = path.join(dir, f);
    let isDirectory = fs.statSync(dirPath).isDirectory();
    isDirectory ? 
      walkDir(dirPath, callback) : callback(dirPath);
  });
}

const contentDir = path.join(process.cwd(), 'content');
let filesModified = 0;

walkDir(contentDir, (filePath) => {
  if (!filePath.endsWith('.md')) return;

  const originalContent = fs.readFileSync(filePath, 'utf8');
  const lines = originalContent.split('\n');
  const newLines = [];
  
  let inBlock = false;
  let blockType = '';
  let modified = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    // Match opening block, e.g., :::info
    const openMatch = line.match(/^:::([a-zA-Z]+)\s*$/);
    if (openMatch) {
      inBlock = true;
      blockType = openMatch[1].toLowerCase();
      newLines.push(`> [!${blockType}]`);
      modified = true;
      continue;
    }
    
    // Match closing block, e.g., :::
    if (inBlock && line.trim() === ':::') {
      inBlock = false;
      continue;
    }
    
    // Inside block
    if (inBlock) {
      newLines.push(`> ${line}`);
    } else {
      newLines.push(line);
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, newLines.join('\n'), 'utf8');
    filesModified++;
    console.log(`Modified: ${filePath}`);
  }
});

console.log(`Done! Modified ${filesModified} files.`);
