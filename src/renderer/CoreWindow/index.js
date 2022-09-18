const { ipcRenderer } = require("electron")

  window.addEventListener('DOMContentLoaded', ()=>{

    const btnProcessImage = document.getElementById('btn-process-image')
    btnProcessImage?.addEventListener('click', ()=>{
      ipcRenderer.send('create-coreWindow')
    })

  })
