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

  logarithmic(){
    console.log("logarithmic")
  }

  potency(){
    console.log("potency")
  }

  bitPlaneSlicing(){
    console.log("bitPlaneSlicing")
  }
}

module.exports = new Transformations();