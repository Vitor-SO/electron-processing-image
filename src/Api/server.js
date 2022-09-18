// const express=require('express');
// const app=express();
 
// //Import PythonShell module.
// const {PythonShell} =require('python-shell');
 
// //Router to handle the incoming request.
// app.get("/", (req, res, next)=>{
//     //Here are the option object in which arguments can be passed for the python_test.js.
//     let options = {
//         mode: 'text',
//         pythonOptions: ['-u'], // get print results in real-time
//           scriptPath: '../renderer/processImage/scripts/Transformations/Negative/negative.py', //If you are having python_test.py script in same folder, then it's optional.
//     };
     
 
//     PythonShell.run('negative.py', options, function (err, result){
//           if (err) throw err;
//           // result is an array consisting of messages collected
//           //during execution of script.
//           console.log('result: ', result.toString());
//           res.send(result.toString())
//     });
// });
 
// //Creates the server on default port 8000 and can be accessed through localhost:8000
// const port=8000;
// app.listen(port, ()=>console.log(`Server connected to ${port}`));