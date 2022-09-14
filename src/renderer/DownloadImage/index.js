const { dialog, ipcRenderer } = require("electron");

window.addEventListener('DOMContentLoaded', ()=>{

    //download image function
    const btnDownloadImage = document.getElementById('btn-download-image');
    btnDownloadImage?.addEventListener('click', (e) =>{
    const url = document.getElementById('input-url').value;
    const imageName = document.getElementById('image-name').value
      
    ipcRenderer.send('download-image', url, imageName)
    
  })

  

})
