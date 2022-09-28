const {BrowserWindow,} =require('electron')
const { PythonShell } = require("python-shell");
const { join } = require("path");
const ejs = require('ejs');
const path = require('path');
const fs = require('fs')

class ImageProcessing {
  execute(filePath, imageName,filterPath) {
    const optionsPath = {
      args: [filePath, imageName],
    };

    const script = join(__dirname, filterPath);
    const result = PythonShell.run(script, optionsPath,
      function (err, results) {
        if (err) {
          return console.log(err.traceback)
        }
        console.log('finished');

        let win = new BrowserWindow({width: 800, height: 600,webPreferences: {
          nodeIntegration: true,
          contextIsolation: false,
          webSecurity: true
        },}); 
        const images  =  []
        const nameImage = results?.pop()
        const resultJSON = JSON.parse(results[0])
        resultJSON.forEach(function ({url,name}){
          const dataImage = fs.readFileSync(path.resolve(__dirname,'..','..','..','..',url)).toString('base64')
          images.push({url: `data:image/png;base64,${dataImage}`, name})
        })
        
        ejs.renderFile(path.resolve(__dirname,'..','..','templates','index.ejs'), {
          images,
          nameImage
        }, {}, function (err, str) {
          if (err) {
            console.log(err);
          }
          // Load the rendered HTML to the BrowserWindow.
          win.loadURL('data:text/html;charset=utf-8,' + encodeURI(str));
        });
        
        return results[0];
      }
    );
    return result;
  }

  // logarithmic(filePath, logImageName) {
  //   const optionsPath = {
  //     args: [filePath, logImageName],
  //   };

  //   const logarithmic = join(__dirname, "./Logarithmic/logarithmic.py");
  //   PythonShell.run(logarithmic, optionsPath, function (err, results) {
  //     if (err) throw err;
  //     console.log("finished");
  //   });
  // }

  // potency(filePath, potImageName) {
  //   const optionsPath = {
  //     args: [filePath, potImageName],
  //   };

  //   const potency = join(__dirname, "./Potency/potency.py");
  //   PythonShell.run(potency, optionsPath, function (err, results) {
  //     if (err) throw err;
  //     console.log("finished");
  //   });
  // }

  // bitPlaneSlicing(filePath, bpsImageName) {
  //   const optionsPath = {
  //     args: [filePath, bpsImageName],
  //   };

  //   const bps = join(__dirname, "./BitPlaneSlicing/bitPlaneSlicing.py");
  //   PythonShell.run(bps, optionsPath, function (err, results) {
  //     if (err) throw err;
  //     console.log("finished");
  //   });
  // }

  // histogram(filePath, pathHistogram) {
  //   const optionsPath = {
  //     args: [filePath, pathHistogram],
  //   };

  //   const histogramPath = join(__dirname, "./Histogram/histogram.py");
  //   PythonShell.run(histogramPath, optionsPath, function (err, results) {
  //     if (err) throw err;
  //     console.log("finished");
  //   });
  // }
}

module.exports = new ImageProcessing();
