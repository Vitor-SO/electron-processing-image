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

  mediana(filePath, medianaImageName){
    const optionsPath ={
      args: [filePath, medianaImageName],
    }

    const mediana = join(__dirname,'./Smoothing/Mediana/mediana.py')
  PythonShell.run(mediana, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  }

  laplacian(filePath,laplacianImageName){
    const optionsPath ={
      args: [filePath, laplacianImageName],
    }

    const potency = join(__dirname,'./sharpening/Laplacian/laplacian.py')
  PythonShell.run(potency, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  }

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