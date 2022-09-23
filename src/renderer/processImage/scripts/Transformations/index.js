const { PythonShell } = require("python-shell");
const { join } = require("path");
const ShowImageWindow = require("../../../ShowImageWindow");
const { ipcRenderer } = require("electron/renderer");
class Transformations {
  negative(filePath, negativeImageName) {
    const optionsPath = {
      args: [filePath, negativeImageName],
    };

    const negative = join(__dirname, "./Negative/negative.py");
    const result = PythonShell.run(
      negative,
      optionsPath,
      function (err, results) {
        if (err) throw err;
        console.log("finished");
        // ShowImageWindow.selectTarget('negative',results[0])
        return results[0];
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
