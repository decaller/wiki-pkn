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
  
  // Replace instances of '| ### ' or '| ## ' inside tables
  // We can use a regex to replace `|\s*#+\s+` with `| `
  const newContent = originalContent.replace(/\|\s*#+\s+/g, '| ');
  
  if (originalContent !== newContent) {
    fs.writeFileSync(filePath, newContent, 'utf8');
    filesModified++;
    console.log(`Modified: ${filePath}`);
  }
});

console.log(`Done! Modified ${filesModified} files.`);
