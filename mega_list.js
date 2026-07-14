const { File } = require('megajs');
const url = 'https://mega.nz/folder/i1IRkYZL#6uJ3kHuaWG4nGlBYjDN3bw';

async function run() {
  try {
    const rootFolder = File.fromURL(url);
    await rootFolder.loadAttributes();
    
    function printTree(folder, indent = '') {
      if (!folder.children) return;
      for (const child of folder.children) {
        console.log(`${indent}- [${child.directory ? 'DIR' : 'FILE'}] ${child.name}`);
        if (child.directory) {
          printTree(child, indent + '  ');
        }
      }
    }
    
    console.log("Mega Tree:");
    printTree(rootFolder);

  } catch (e) {
    console.error(e);
  }
}
run();
