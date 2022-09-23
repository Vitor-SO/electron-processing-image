const { ipcRenderer } = require("electron")

  window.addEventListener('DOMContentLoaded', ()=>{

    const btnShowImage = document.getElementById('btn-show-image')
    btnShowImage?.addEventListener('click', ()=>{
      ipcRenderer.send('create-show-image-win')
    })

  })
