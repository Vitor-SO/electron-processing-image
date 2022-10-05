const { ipcRenderer } = require("electron");

window.addEventListener("DOMContentLoaded", () => {
  const btnOriginalImage = document.getElementById("btn-choose-image")

  btnOriginalImage?.addEventListener("click", (e) => {
      ipcRenderer.send("original-image",e.target.id)
     });
})