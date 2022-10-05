const { ipcRenderer } = require("electron");

window.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll('button')

  buttons.forEach(element => {
    element?.addEventListener("click", (e) => {
      ipcRenderer.send("process-image",e.target.id)
     });
  });
})