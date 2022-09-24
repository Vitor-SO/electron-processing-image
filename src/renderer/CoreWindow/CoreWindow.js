const { ipcRenderer } = require("electron");

window.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll('button')
  
  buttons.forEach(element => {
    element?.addEventListener("click", (e) => {
      console.log(e)
      ipcRenderer.send("filter",e.target.id)
     });
  });
})