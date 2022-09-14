
window.addEventListener('DOMContentLoaded', ()=>{

    //download image function
    const btnImportImage = document.getElementById('btn-import-image');
    btnImportImage?.addEventListener('click', (e) =>{
      
    ipcRenderer.send('import-image')
    
  })

  

})
