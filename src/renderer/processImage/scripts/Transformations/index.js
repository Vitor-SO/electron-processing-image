const { PythonShell } =require('python-shell');
const {join} = require('path')
class Transformations{

  negative(filePath, negativeImageName){

    const optionsPath ={
      args: [filePath, negativeImageName],
    }

    const negative = join(__dirname,'./Negative/negative.py')
  PythonShell.run(negative, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  }

  logarithmic(filePath, logImageName){
    const optionsPath ={
      args: [filePath, logImageName],
    }

    const logarithmic = join(__dirname,'./Logarithmic/logarithmic.py')
  PythonShell.run(logarithmic, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  }

  potency(filePath,potImageName){
    const optionsPath ={
      args: [filePath, potImageName],
    }

    const potency = join(__dirname,'./Potency/potency.py')
  PythonShell.run(potency, optionsPath, function (err,results) {
      if (err) throw err;
      console.log('finished');
    });
  }

  bitPlaneSlicing(){
    console.log("bitPlaneSlicing")
  }
}

module.exports = new Transformations();