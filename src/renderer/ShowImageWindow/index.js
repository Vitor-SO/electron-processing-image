const { ipcRenderer } = require("electron");


class ShowImageWindow{
  negative = ''
  logarithmic = ''
  potency = ''
  bps = ''

  // constructor(target, path){
    
  //   this.selectTarget(target, path)
    
  // }



  selectTarget(target,path){
    if(target ==='negative'){
      this.negative = path
      
    }
    if(target ==='logarithmic'){this.logarithmic = path}
    if(target ==='potency'){this.potency = path}
    if(target ==='bps'){this.bps = path}
  }



}


module.exports = new ShowImageWindow();