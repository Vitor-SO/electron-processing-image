const { PythonShell } =require('python-shell');
const {join} = require('path')

class Filters{

  media(filePath, mediaImageName){

    const optionsPath ={
      args: [filePath, mediaImageName],
    }

    const media = join(__dirname,'./Smoothing/Media/media.py')
  PythonShell.run(media, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  }

  // mediana(filePath, logImageName){
  //   const optionsPath ={
  //     args: [filePath, logImageName],
  //   }

  //   const logarithmic = join(__dirname,'./Logarithmic/logarithmic.py')
  // PythonShell.run(logarithmic, optionsPath, function (err,results) {
  //     if (err) throw err;
  //     console.log('finished');
  //   });
  // }

  // laplacian(filePath,potImageName){
  //   const optionsPath ={
  //     args: [filePath, potImageName],
  //   }

  //   const potency = join(__dirname,'./Potency/potency.py')
  // PythonShell.run(potency, optionsPath, function (err,results) {
  //     if (err) throw err;
  //     console.log('finished');
  //   });
  // }

  // highboost(filePath,bpsImageName){
  //   const optionsPath ={
  //     args: [filePath, bpsImageName],
  //   }

  //   const bps = join(__dirname,'./BitPlaneSlicing/bitPlaneSlicing.py')
  // PythonShell.run(bps, optionsPath, function (err,results) {
  //     if (err) throw err;
  //     console.log('finished');
  //   });
  // }

  // robert(filePath,robertImageName){
  //   const optionsPath ={
  //     args: [filePath, robertImageName],
  //   }

  //   const robert = join(__dirname,'./BitPlaneSlicing/bitPlaneSlicing.py')
  // PythonShell.run(robert, optionsPath, function (err,results) {
  //     if (err) throw err;
  //     console.log('finished');
  //   });
  
  // }

  // sobel(filePath,bpsImageName){
  //   const optionsPath ={
  //     args: [filePath, bpsImageName],
  //   }

  //   const bps = join(__dirname,'./BitPlaneSlicing/bitPlaneSlicing.py')
  // PythonShell.run(bps, optionsPath, function (err,results) {
  //     if (err) throw err;
  //     console.log('finished');
  //   });
  // }
}

module.exports = new Filters();