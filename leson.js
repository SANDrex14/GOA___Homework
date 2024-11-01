import fs from "fs";

const kidsHelp = (x) => {
  const handleFileCreate = (x, fileName, content) => {
    const filePath = `./${x}/${fileName}`;
    try {
      fs.writeFileSync(filePath, content);
      console.log("File created successfully:", fileName);
    } catch (err) {
      console.error("Error creating file:", err);
    }
  };

  const handleDirMake = (dirPath) => {
    try {
      fs.mkdirSync(dirPath, { recursive: true });
    } catch (err) {
      console.error("Error creating directory:", err);
      return;
    }
  };

  for (let i = 1; i <= 31; i++) {
    let fileNum = String(i).padStart(2, "0");
    handleDirMake(`level ${fileNum}`);
    handleDirMake(`level ${fileNum}/homework`);
    handleFileCreate(`level ${fileNum}/homework`, "homework.txt", "No homework");
    handleDirMake(`level ${fileNum}/classwork`);
    handleFileCreate(`level ${fileNum}/classwork`, "classwork.txt", "No classwork");
  }
};

kidsHelp(40);
