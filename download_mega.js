const fs = require('fs');
const { File } = require('megajs');
const url = 'https://mega.nz/folder/i1IRkYZL#6uJ3kHuaWG4nGlBYjDN3bw';

async function run() {
  try {
    console.log("Loading mega root...");
    const root = File.fromURL(url);
    await root.loadAttributes();
    
    let k1Edit;
    function findK1(folder) {
      if (folder.name === 'K1 EDİT') k1Edit = folder;
      if (folder.children) folder.children.forEach(findK1);
    }
    findK1(root);

    if (!k1Edit) {
      console.log("Folder 'K1 EDİT' not found in tree.");
      return;
    }

    const filesToDownload = k1Edit.children.filter(c => !c.directory).slice(0, 7);
    const names = ['hero-mega.jpg', 'hamam-mega.jpg', 'massage-mega.jpg', 'sauna-mega.jpg', 'beauty-mega.jpg', 'reception-mega.jpg', 'fethiye-mega.jpg'];

    console.log(`Found ${filesToDownload.length} files to download.`);

    for (let i = 0; i < filesToDownload.length; i++) {
      const file = filesToDownload[i];
      const dest = `./images/${names[i]}`;
      console.log(`Downloading ${file.name} to ${dest}...`);
      const stream = file.download();
      const writeStream = fs.createWriteStream(dest);
      stream.pipe(writeStream);
      await new Promise((resolve, reject) => {
        writeStream.on('finish', resolve);
        writeStream.on('error', reject);
        stream.on('error', reject);
      });
      console.log(`Finished ${names[i]}`);
    }
    console.log("All downloads complete.");
  } catch (e) {
    console.error("Error:", e);
  }
}
run();
