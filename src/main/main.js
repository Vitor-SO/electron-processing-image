require('electron-reload')(__dirname)
const { app, BrowserWindow, shell, ipcMain, dialog } =require('electron')
const { join } =require('path')
const fs =require('fs')
const https =require('node:https')
const Transformations = require('../renderer/processImage/scripts/Transformations/index.js')
const {PythonShell} =  require('python-shell');
const path = require('path')
const Filters = require('../renderer/processImage/scripts/Filters/index.js')
// const Transformations =require('../renderer/processImage/scripts/Transformations/index.js')

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
      fs.writeFileSync(`./src/renderer/processImage/Images/${imageName}`,fs.readFileSync(currentPath.filePath))
    },1500)
    
    // fs.copyFileSync(currentPath.filePath, `./src/Downloads/${filename}`)
  })
  
})

//function import image
ipcMain.on('import-image', ()=>{
  dialog.showOpenDialog({defaultPath: app.getPath("downloads")}).then((currentPath)=>{
    const basename = path.basename(currentPath.filePaths[0])
    fs.writeFileSync(`./src/renderer/processImage/Images/${basename}`, fs.readFileSync(currentPath.filePaths[0]))
  })
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
  

  //core window functions
ipcMain.on('btn-negative', ()=>{
  //get path image for python script
  dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
    //call the negative function
    const filename = path.basename(currentPath.filePaths[0])
    const negativeImageName = filename.split('.')[0]
    Transformations.negative(currentPath.filePaths[0], negativeImageName)
  })

  
})

ipcMain.on('btn-logarithmic', ()=>{
  dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
    //call the log function
    const filename = path.basename(currentPath.filePaths[0])
    const logImageName = filename.split('.')[0]
    Transformations.logarithmic(currentPath.filePaths[0], logImageName)
  })
})

ipcMain.on('btn-potency', ()=>{
  
  dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
    //call the negative function
    const filename = path.basename(currentPath.filePaths[0])
    const potImageName = filename.split('.')[0]
    Transformations.potency(currentPath.filePaths[0], potImageName)
  })


})


ipcMain.on('btn-bitPlaneSlicing', ()=>{
  
  dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
    //call the negative function
    const filename = path.basename(currentPath.filePaths[0])
    const bpsImageName = filename.split('.')[0]
    Transformations.bitPlaneSlicing(currentPath.filePaths[0], bpsImageName)
  })



})

// ipcMain.on('btn-histogram',()=>{
//   dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
//     //call the negative function
//     const filename = path.basename(currentPath.filePaths[0])
//     const bpsImageName = filename.split('.')[0]
//     Transformations.(currentPath.filePaths[0], bpsImageName)
//   })
// })

ipcMain.on('btn-media',()=>{
  dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
    //call the negative function
    const filename = path.basename(currentPath.filePaths[0])
    const mediaImageName = filename.split('.')[0]
    Filters.media(currentPath.filePaths[0], mediaImageName)
  })
})

ipcMain.on('btn-mediana',()=>{
  dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
    //call the negative function
    const filename = path.basename(currentPath.filePaths[0])
    const medianaImageName = filename.split('.')[0]
    Filters.mediana(currentPath.filePaths[0], medianaImageName)
  })
})

// ipcMain.on('btn-laplacian',()=>{
//   dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
//     //call the negative function
//     const filename = path.basename(currentPath.filePaths[0])
//     const bpsImageName = filename.split('.')[0]
//     Filters.laplacian(currentPath.filePaths[0], bpsImageName)
//   })
// })

// ipcMain.on('btn-highboost',()=>{
//   dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
//     //call the negative function
//     const filename = path.basename(currentPath.filePaths[0])
//     const bpsImageName = filename.split('.')[0]
//     Filters.highboost(currentPath.filePaths[0], bpsImageName)
//   })
// })

// ipcMain.on('btn-robert',()=>{
//   dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
//     //call the negative function
//     const filename = path.basename(currentPath.filePaths[0])
//     const bpsImageName = filename.split('.')[0]
//     Filters.robert(currentPath.filePaths[0], bpsImageName)
//   })
// })

// ipcMain.on('btn-sobel',()=>{
//   dialog.showOpenDialog({defaultPath: app.getPath("recent")}).then((currentPath)=>{
//     //call the negative function
//     const filename = path.basename(currentPath.filePaths[0])
//     const bpsImageName = filename.split('.')[0]
//     Filters.sobel(currentPath.filePaths[0], bpsImageName)
//   })
// })

})




