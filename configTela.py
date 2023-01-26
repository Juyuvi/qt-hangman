from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication


def invertSlider():
    inversoDoBotao = not ui.horizontalSlider.isEnabled()
    ui.horizontalSlider.setEnabled(inversoDoBotao)

def sliderValue():
    stringDoValor = str(ui.horizontalSlider.value())
    ui.sliderValor.setText(stringDoValor)

def openLista():
    import os

    os.system("start palavras.txt")

def addPalavra():
    from forcasys import PartidaDeJogoDaForca

    try:
        jogoTeste = PartidaDeJogoDaForca(str(ui.palavraInsert.text()), False, 0, False)

    except:
        ui.avisobox.setText("Palavra contém caracteres inválidos")

    else:
        with open("palavras.txt", "r") as file:
            if not (str(ui.palavraInsert.text()) in file.read()):

                presente = False
            else:
                presente = True
                ui.avisobox.setText("Palavra já está presente na lista")
        file.close()

        if not presente:
            file = open("palavras.txt", "a")
            file.write("\n" + str(ui.palavraInsert.text()))
            file.close()
        else:
            pass



def finishSetup():
    global tentativas, revelar, instaLose

    if ui.tentativasCheckBox.isEnabled():
        tentativas = ui.horizontalSlider.value()
    else:
        tentativas = 0

    revelar = ui.revelarPalavraBool.isEnabled()
    instaLose = ui.instaLoseBool.isEnabled()
    QCoreApplication.instance().quit()




class Ui_janela(object):
    def configTela(self, janela):
        janela.setObjectName("janela")
        janela.resize(390, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(janela.sizePolicy().hasHeightForWidth())
        janela.setSizePolicy(sizePolicy)
        janela.setMinimumSize(QtCore.QSize(390, 430))
        janela.setMaximumSize(QtCore.QSize(390, 430))
        font = QtGui.QFont()
        font.setPointSize(9)
        janela.setFont(font)
        icon = QtGui.QIcon.fromTheme("C:\\Users\\noone\\Desktop\\dev\\python\\hangman\\icon.png")
        janela.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(janela)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 40, 186, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(26)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.valueChanged.connect(sliderValue)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.horizontalSlider)
        self.tentativasCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.tentativasCheckBox.setObjectName("tentativasCheckBox")
        self.tentativasCheckBox.stateChanged.connect(invertSlider)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tentativasCheckBox)
        self.sliderValor = QtWidgets.QLabel(self.formLayoutWidget)
        self.sliderValor.setObjectName("sliderValor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sliderValor)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(230, 40, 181, 111))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.instaLoseBool = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.instaLoseBool.setObjectName("instaLoseBool")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.instaLoseBool)
        self.revelarPalavraBool = QtWidgets.QCheckBox(self.formLayoutWidget_2)
        self.revelarPalavraBool.setObjectName("revelarPalavraBool")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.revelarPalavraBool)
        self.tituloAddPalavra = QtWidgets.QLabel(self.centralwidget)
        self.tituloAddPalavra.setGeometry(QtCore.QRect(30, 170, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tituloAddPalavra.setFont(font)
        self.tituloAddPalavra.setObjectName("tituloAddPalavra")
        self.palavraInsert = QtWidgets.QLineEdit(self.centralwidget)
        self.palavraInsert.setGeometry(QtCore.QRect(30, 220, 201, 22))
        self.palavraInsert.setInputMask("")
        self.palavraInsert.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.palavraInsert.setDragEnabled(False)
        self.palavraInsert.setClearButtonEnabled(True)
        self.palavraInsert.setObjectName("palavraInsert")
        self.palavraAddBtn = QtWidgets.QPushButton(self.centralwidget, clicked=addPalavra)
        self.palavraAddBtn.setGeometry(QtCore.QRect(250, 220, 111, 24))
        self.palavraAddBtn.setObjectName("palavraAddBtn")
        self.abrirListaBtn = QtWidgets.QPushButton(self.centralwidget, clicked=openLista)
        self.abrirListaBtn.setGeometry(QtCore.QRect(30, 260, 331, 24))
        self.abrirListaBtn.setObjectName("abrirListaBtn")
        self.startGameBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startGameBtn.setGeometry(QtCore.QRect(290, 370, 75, 24))
        self.startGameBtn.setObjectName("startGameBtn")
        self.startGameBtn.clicked.connect(finishSetup)
        janela.setCentralWidget(self.centralwidget)
        self.avisobox = QtWidgets.QLabel(self.centralwidget)
        self.avisobox.setGeometry(QtCore.QRect(30, 300, 331, 16))
        self.avisobox.setText("")
        self.avisobox.setObjectName("avisobox")

        self.retranslateUi(janela)
        QtCore.QMetaObject.connectSlotsByName(janela)

    def retranslateConfigTela(self, janela):
        _translate = QtCore.QCoreApplication.translate
        janela.setWindowTitle(_translate("janela", "Jogo da Forca"))
        self.tentativasCheckBox.setText(_translate("janela", "Tentativas"))
        self.sliderValor.setText(_translate("janela", "1"))
        self.instaLoseBool.setText(_translate("janela", "Perder ao errar\n"
"adivinhar palavra"))
        self.revelarPalavraBool.setText(_translate("janela", "Revelar palavra no final"))
        self.tituloAddPalavra.setText(_translate("janela", "Adicionar uma nova palavra"))
        self.palavraInsert.setPlaceholderText(_translate("janela", "palavra"))
        self.palavraAddBtn.setText(_translate("janela", "Adicionar"))
        self.abrirListaBtn.setText(_translate("janela", "Abrir lista de palavras"))
        self.startGameBtn.setText(_translate("janela", "Começar"))



import sys
app = QtWidgets.QApplication(sys.argv)
janela = QtWidgets.QMainWindow()
ui = Ui_janela()
ui.configTela(janela)
janela.show()
sys.exit(app.exec_())
