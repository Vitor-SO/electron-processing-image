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

  highboost(filePath,imghighboost){
    const optionsPath ={
      args: [filePath, imghighboost],
    }

    const high = join(__dirname,'./sharpening/hightbooster/hightbooster.py')
  PythonShell.run(high, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  }

  robert(filePath,robertImageName){
    const optionsPath ={
      args: [filePath, robertImageName],
    }

    const robertPath = join(__dirname,'./sharpening/robert/robert.py')
  PythonShell.run(robertPath, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  
  }

  sobel(filePath,sobelImageName){
    const optionsPath ={
      args: [filePath, sobelImageName],
    }

    const sobelPath = join(__dirname,'./sharpening/sobel/sobel.py')
  PythonShell.run(sobelPath, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  }
}

module.exports = new Filters();