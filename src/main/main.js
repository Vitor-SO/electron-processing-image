const { app, BrowserWindow, shell, ipcMain, dialog } =require('electron')
const { join } =require('path')
const fs =require('fs')
const https =require('node:https')
const transformations = require('../processImage/scripts/transformations')
require('electron-reload')(__dirname)
// import ImageProcessCore from '../../src/Components/ImageProcessCore'
// import CoreWindow from '../../src/Components/ImageProcessCore/CoreWindow'

let win = null
async function createWindow() {
  win = new BrowserWindow({
    title: 'Image Processing Program',
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      webSecurity: true
    },
  })
    win.loadFile('src/main/index.html')

  // Test actively push message to the Electron-Renderer
  win.webContents.on('did-finish-load', () => {
    win?.webContents.send('main-process-message', new Date().toLocaleString())
  })

  // Make all links open with the browser, not with the application
  win.webContents.setWindowOpenHandler(({ url }) => {
    if (url.startsWith('https:')) shell.openExternal(url)
    return { action: 'deny' }
  })

}

// win.webContents.session.webRequest.onBeforeSendHeaders(
//   (details, callback) => {
//     callback({ requestHeaders: { Origin: '*', ...details.requestHeaders } });
//   },
// );

// win.webContents.session.webRequest.onHeadersReceived((details, callback) => {
//   callback({
//     responseHeaders: {
//       'Access-Control-Allow-Origin': ['*'],
//       ...details.responseHeaders,
//     },
//   });
// });

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  win = null
  if (process.platform !== 'darwin') app.quit()
})

app.on('second-instance', () => {
  if (win) {
    // Focus on the main window if the user tried to open another
    if (win.isMinimized()) win.restore()
    win.focus()
  }
})

app.on('activate', () => {
  const allWindows = BrowserWindow.getAllWindows()
  if (allWindows.length) {
    allWindows[0].focus()
  } else {
    createWindow()
  }
})


// //mudar para ipcRenderer dentro do button e fazer o ipcMain.on dentro da funcao criada
// //function download image
ipcMain.on("download-image",(event, url,imageName) => {
  dialog.showSaveDialog({defaultPath: imageName}).then((currentPath)=>{
    https.get(url,(res)=>{
      var imageStream = fs.createWriteStream(currentPath.filePath)
      res.pipe(imageStream)
    })


    // 
    setTimeout(()=>{
      fs.writeFileSync(`./src/Downloads/${imageName}`,fs.readFileSync(currentPath.filePath))
    },1500)
    
    // fs.copyFileSync(currentPath.filePath, `./src/Downloads/${filename}`)
  })
  
})

//function import image
ipcMain.on('import-image', ()=>{
  dialog.showOpenDialog({defaultPath: app.getPath("downloads")}).then((currentPath)=>{
    fs.writeFileSync('./src/Downloads/image.png', fs.readFileSync(currentPath.filePaths[0]))
  })
})


//core process images functions

ipcMain.on('create-coreWindow', ()=>{
  let win =null;
  win = new BrowserWindow({
    title: 'Image Processing Functions',
  webPreferences: {
    nodeIntegration: true,
    contextIsolation: false,  
    webSecurity: true
  },
  })

  win.loadFile('src/renderer/CoreWindow/CoreWindow.html')
  
})

ipcMain.on('btn-negative', ()=>{transformations.negative()})
ipcMain.on('btn-logarithmic', ()=>{transformations.logarithmic()})
ipcMain.on('btn-potency', ()=>{transformations.potency()})
ipcMain.on('btn-bitPlaneSlicing', ()=>{transformations.bitPlaneSlicing()})
