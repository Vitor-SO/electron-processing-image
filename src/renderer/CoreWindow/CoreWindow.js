const { ipcRenderer } = require("electron")

window.addEventListener('DOMContentLoaded', ()=>{
  const btnNegative = document.getElementById('btn-negative')
  const btnLogarithmic = document.getElementById('btn-logarithmic')
  const btnPotency = document.getElementById('btn-potency')
  const btnBitPlaneSlicing = document.getElementById('btn-bitPlaneSlicing')
  
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
})
 