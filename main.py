from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from tkinter import filedialog
from scipy import ndimage
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

from ui_main import Ui_MainWindow


class MainScreen(QMainWindow):
    def __init__(self, *args, **argvs):
        super(MainScreen, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fillComboBox()
        self.ui.subtmitButton.clicked.connect(self.operation)
        self.ui.subtmitButton_2.clicked.connect(self.uploadImage)

    def fillComboBox(self):
        imgPath = ""
        items = ["Escolha o método de filtro", "Negativas", "Logarítimicas", "Potência", "Fatiamento em bits", "Equalização", "Histograma", "Média", "Mediana", "Laplaciano", "High boost", "Robert", "Sobel"]
        for x in items:
            self.ui.comboBox.addItem(x, x.lower())

    def operation(self):
        if "imgPath" not in globals():
            return QMessageBox.about(self, "Erro", "É preciso subir uma imagem antes")

        opt = (self.ui.comboBox.currentText()).lower()
        if opt == "negativas":
            self.negative()
            QMessageBox.about(self, "Sucesso", "A imagem com o filtro foi gerada no mesmo diretório do arquivo main do código")
        elif opt == "logarítimicas":
            self.logarithmic()
            QMessageBox.about(self, "Sucesso", "A imagem com o filtro foi gerada no mesmo diretório do arquivo main do código")
        elif opt == "média":
            self.media()
            QMessageBox.about(self, "Sucesso", "A imagem com o filtro foi gerada no mesmo diretório do arquivo main do código")
        elif opt == "mediana":
            self.median()
            QMessageBox.about(self, "Sucesso", "A imagem com o filtro foi gerada no mesmo diretório do arquivo main do código")
        elif opt == "histograma":
            self.histrogram()
            QMessageBox.about(self, "Sucesso", "Gráfico gerado com sucesso")
        elif opt == "equalização":
            self.equalize()
            QMessageBox.about(self, "Sucesso", "Gráfico gerado com sucesso")
        elif opt == "laplaciano":
            self.laplatian()
            QMessageBox.about(self, "Sucesso", "A imagem com o filtro foi gerada no mesmo diretório do arquivo main do código")
        elif opt == "high boost":
            self.highBoost()
            QMessageBox.about(self, "Sucesso", "A imagem com o filtro foi gerada no mesmo diretório do arquivo main do código")
        elif opt == "robert":
            self.robert()
            QMessageBox.about(self, "Sucesso", "A imagem com o filtro foi gerada no mesmo diretório do arquivo main do código")
        elif opt == "sobel":
            self.sobel()
            QMessageBox.about(self, "Sucesso", "A imagem com o filtro foi gerado no mesmo diretório do arquivo main do código")
        else:
            QMessageBox.about(self, "Erro", "Opção inválida")

    def uploadImage(self):
        global imgPath
        fileTypes = [("JPG", "*.jpg"), ("PNG", "*.png"), ("JPEG", "*.jpeg")]
        imgPath = filedialog.askopenfilename(filetypes=fileTypes)

    @staticmethod
    def negative():
        img = cv2.imread(imgPath)
        image = (255-img)
        cv2.imwrite('negative.jpg', image)

    @staticmethod
    def logarithmic():
        img = cv2.imread(imgPath)
        c = 255 / np.log(1 + np.max(img))
        image = c * (np.log(img+1))
        image = np.array(image, dtype=np.uint8)
        cv2.imwrite('logarithmic.jpg', image)

    @staticmethod
    def media():
        size = 5
        img = cv2.imread(imgPath)
        blur = cv2.blur(img, (size, size))
        cv2.imwrite("media.jpg", blur)

    @staticmethod
    def median():
        size = 5
        if size % 2 == 0:
            size += 1

        img = cv2.imread(imgPath)
        median_blur = cv2.medianBlur(img, size)
        cv2.imwrite("median.jpg", median_blur)

    @staticmethod
    def histrogram():
        img = cv2.imread(imgPath)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(histogram, color=col)
            plt.xlim([0, 256])
        plt.title('Histograma: escala BGR')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)
        plt.show()

    @staticmethod
    def equalize():
        print('chablau')

    @staticmethod
    def laplatian():
        img = cv2.imread(imgPath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lap = cv2.Laplacian(img, cv2.CV_64F)
        lap = np.uint8(np.absolute(lap))
        result = np.vstack([img, lap])
        cv2.imwrite("laplatian.jpg", result)

    @staticmethod
    def highBoost():
        img = cv2.imread(imgPath)
        resultant_image = img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for i in range(1, img.shape[0]-1):
            for x in range(1, img.shape[1]-1):
                blur_factor = (img[i-1, x-1] + img[i-1, x] + img[i-1, x+1] + img[i, x-1] + img[i, x] + img[i, x+1] +
                               img[i+1, x+1] + img[i+1, x] + img[i+1, x+1])/9
                mask = 1 * img[i, x] - blur_factor
                resultant_image[i, x] = img[i, x] + mask
        cv2.imwrite("high_boost.jpg", resultant_image)

    @staticmethod
    def robert():
        roberts_cross_v = np.array([[1, 0], [0, -1]])
        roberts_cross_h = np.array([[0, 1], [-1, 0]])
        img = cv2.imread(imgPath, 0).astype('float64')
        img /= 255.0
        vertical = ndimage.convolve(img, roberts_cross_v)
        horizontal = ndimage.convolve(img, roberts_cross_h)
        edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
        edged_img *= 255
        cv2.imwrite("robert.jpg", edged_img)

    @staticmethod
    def sobel():
        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(gray, (3, 3), 0)
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
        cv2.imwrite("sobelx.jpg", sobelx)
        cv2.imwrite("sobely.jpg", sobely)


app = QApplication(sys.argv)
if QDialog.Accepted:
    window = MainScreen()
    window.show()

sys.exit(app.exec_())
