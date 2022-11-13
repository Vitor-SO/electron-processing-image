const { app, BrowserWindow, shell, ipcMain, dialog, ipcRenderer } =require('electron')
const fs =require('fs')
const https =require('node:https')
const path = require('path')
const ImageProcessing = require('../renderer/processImage/scripts/index.js')
const ejs = require('ejs');

let global_pathImage = ''
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



//create core window

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

//show original image 
ipcMain.on("original-image",  () =>{
  dialog.showOpenDialog({
    filters: [
      { name: 'Images', extensions: ['jpg', 'png', 'gif', '.tif'] },
    ]
  }).then((currentPath)=>{
    const currentPathImage = currentPath.filePaths[0]
    let win =null;
  win = new BrowserWindow({
    title: 'Original Image',
  webPreferences: {
    nodeIntegration: true,
    contextIsolation: false,  
    webSecurity: true
  },
  })
  
  const images = []
  const pathImage = [{"url":currentPathImage}]
  pathImage.forEach(function ({url,name}){
    const dataImage = fs.readFileSync(path.resolve(__dirname,'..',url)).toString('base64')
    images.push({url: `data:image/png;base64,${dataImage}`})
  })
  

  ejs.renderFile(path.resolve(__dirname,'..','renderer','templates','originalImage.ejs'), {
    images,
  }, {}, function (err, str) {
    if (err) {
      console.log(err);
    }

    
    win.loadURL('data:text/html;charset=utf-8,' + encodeURI(str));
  });
  
  global_pathImage = currentPathImage
  })

})

// //coreWindow functions
ipcMain.on('process-image',  (event, message) =>{

  const paths = {
    'negative':"/Transformations/Negative/negative.py",
    'logarithmic': "/Transformations/Logarithmic/logarithmic.py",
    'potency': "/Transformations/Potency/potency.py",
    'bitPlaneSlicing': "/Transformations/BitPlaneSlicing/bitPlaneSlicing.py",
    'histogram': "/Transformations/Histogram/histogram.py",
    'equalizacaoGlobal': "/Transformations/Equalizacao/EqualizacaoGlobal/equalizacao_global.py",
    'equalizacaoLocal': "/Transformations/Equalizacao/EqualizacaoLocal/equalizacao_local.py",
    'media': '/Filters/Smoothing/Media/media.py',
    'mediana': '/Filters/Smoothing/Mediana/mediana.py',
    'laplacian': '/Filters/sharpening/Laplacian/laplacian.py',
    'highboost': '/Filters/sharpening/hightbooster/hightbooster.py',
    'robert': '/Filters/sharpening/robert/robert.py',
    'sobel': '/Filters/sharpening/sobel/sobel.py',
    'erode': '/MorphOperators/Erode/erode.py'
  }

    const currentPathImage = global_pathImage
    if(currentPathImage === undefined || currentPathImage === '') {
      console.log('errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrou');
      return
    }
    const filename = path.basename(global_pathImage)
    const imageName = filename.split('.')[0]
    ImageProcessing.execute(currentPathImage, imageName,paths[message])
    
    // fs.win.loadFile(result?.command[0])
})
