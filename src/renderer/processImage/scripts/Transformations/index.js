const {BrowserWindow,} =require('electron')
const { PythonShell } = require("python-shell");
const { join } = require("path");
const ShowImageWindow = require("../../../ShowImageWindow");
const { ipcRenderer } = require("electron/renderer");
const ejs = require('ejs');
const path = require('path');
const fs = require('fs')
class Transformations {
  negative(filePath, negativeImageName,filterPath) {
    const optionsPath = {
      args: [filePath, negativeImageName],
    };
    // "./Negative/negative.py"
    const negative = join(__dirname, filterPath);
    const result = PythonShell.run(
      negative,
      optionsPath,
      function (err, results) {
        if (err) throw err;

        console.log("finished",results);
        let win = new BrowserWindow({width: 800, height: 600}); 
        let options = {root: __dirname};
        // ShowImageWindow.selectTarget('negative',results[0])
        const image  =  fs.readFileSync(path.resolve(__dirname,'..','..','..','..','..',results[0])).toString('base64')
        console.log(image[0])
        ejs.renderFile(path.resolve(__dirname,'..','..','..','templates','index.ejs'), {
          image:`data:image/png;base64,${image}`
        }, {}, function (err, str) {
          if (err) {
            console.log(err);
          }
          // Load the rendered HTML to the BrowserWindow.
          win.loadURL('data:text/html;charset=utf-8,' + encodeURI(str));
        });
      }
    );

    return result;
  }

  logarithmic(filePath, logImageName) {
    const optionsPath = {
      args: [filePath, logImageName],
    };

    const logarithmic = join(__dirname, "./Logarithmic/logarithmic.py");
    PythonShell.run(logarithmic, optionsPath, function (err, results) {
      if (err) throw err;
      console.log("finished");
    });
  }

  potency(filePath, potImageName) {
    const optionsPath = {
      args: [filePath, potImageName],
    };

    const potency = join(__dirname, "./Potency/potency.py");
    PythonShell.run(potency, optionsPath, function (err, results) {
      if (err) throw err;
      console.log("finished");
    });
  }

  bitPlaneSlicing(filePath, bpsImageName) {
    const optionsPath = {
      args: [filePath, bpsImageName],
    };

    const bps = join(__dirname, "./BitPlaneSlicing/bitPlaneSlicing.py");
    PythonShell.run(bps, optionsPath, function (err, results) {
      if (err) throw err;
      console.log("finished");
    });
  }

  histogram(filePath, pathHistogram) {
    const optionsPath = {
      args: [filePath, pathHistogram],
    };

    const histogramPath = join(__dirname, "./Histogram/histogram.py");
    PythonShell.run(histogramPath, optionsPath, function (err, results) {
      if (err) throw err;
      console.log("finished");
    });
  }
}

module.exports = new Transformations();
