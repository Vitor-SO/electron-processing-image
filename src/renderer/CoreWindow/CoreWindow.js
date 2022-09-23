const { ipcRenderer } = require("electron")

window.addEventListener('DOMContentLoaded', ()=>{
  
  const btnNegative = document.getElementById('btn-negative')
  const btnLogarithmic = document.getElementById('btn-logarithmic')
  const btnPotency = document.getElementById('btn-potency')
  const btnBitPlaneSlicing = document.getElementById('btn-bitPlaneSlicing')

  const btnHistogram = document.getElementById('btn-histogram')

  const btnMedia = document.getElementById('btn-media')
  const btnMediana = document.getElementById('btn-mediana')
  const btnLaplacian = document.getElementById('btn-laplacian')
  const btnHighboost = document.getElementById('btn-highboost')
  const btnRobert = document.getElementById('btn-robert')
  const btnSobel = document.getElementById('btn-sobel')


 btnNegative?.addEventListener('click', (e)=>{
     ipcRenderer.send('btn-negative')
  })

  btnLogarithmic?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-logarithmic')
  })

  btnPotency?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-potency')
  })

  btnBitPlaneSlicing?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-bitPlaneSlicing')
  }) 
  
  btnHistogram?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-histogram')
  }) 

  btnMedia?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-media')
  }) 
  
  btnMediana?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-mediana')
  }) 

  btnLaplacian?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-laplacian')
  }) 

  btnHighboost?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-highboost')
  }) 

  btnRobert?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-robert')
  }) 

  btnSobel?.addEventListener('click', (e)=>{
    ipcRenderer.send('btn-sobel')
  }) 

})
 