from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from linking import *
import os

icon_path = os.path.join(os.path.dirname(__file__), r'img\icon.png')
gif_path = os.path.join(os.path.dirname(__file__), r'img\confettiONE.gif')


# Funções da tela de setup.

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
    from PyQt5.QtCore import QCoreApplication
    global tentativas, revelar, instaLose

    if ui.tentativasCheckBox.isChecked():
        tentativas = ui.horizontalSlider.value()
    else:
        tentativas = 0

    revelar = ui.revelarPalavraBool.isChecked()
    instaLose = ui.instaLoseBool.isChecked()
    jogoStart()
    screen1()







# Funções do jogo em si.

def desativadorDeBotoes():

    # O programa crasha se eu tentar usar um método do QPushButton
    # referenciando o atributo de dentro de uma lista ou dicionário
    # APENAS se isso for feito na função screen1().
    # Tudo roda normalmente se a função screen1(), invés de alterar
    # os atributos, chamar essa função que altera os atributos para ela.
    # ???????????????????????????????????????????????????????????

    from linking import clickedButtons

    buttonDict = {
        "A": ui.letraA,
        "B": ui.letraB,
        "C": ui.letraC,
        "D": ui.letraD,
        "E": ui.letraE,
        "F": ui.letraF,
        "G": ui.letraG,
        "H": ui.letraH,
        "I": ui.letraI,
        "J": ui.letraJ,
        "K": ui.letraK,
        "L": ui.letraL,
        "M": ui.letraM,
        "N": ui.letraN,
        "O": ui.letraO,
        "P": ui.letraP,
        "Q": ui.letraQ,
        "R": ui.letraR,
        "S": ui.letraS,
        "T": ui.letraT,
        "U": ui.letraU,
        "V": ui.letraV,
        "W": ui.letraW,
        "X": ui.letraX,
        "Y": ui.letraY,
        "Z": ui.letraZ
    }


    for letra in clickedButtons:
        buttonDict[letra].setDisabled(True)


def screen1():

    ui.gameScreen(janela)
    desativadorDeBotoes()



def screen2():
    ui.adivScreen(janela)


def screen3():
    ui.janelaFinal(janela)

def screen4():
    ui.loseScreen(janela)


def adivPalavra(targetUI, palavra):

    try:
        jogo1.adivinharPalavra(palavra)

    except BaseException as err:
        screen1()
        targetUI.infobox.setText(str(err))
        if (jogo1.perdido) and ((jogo1.limite) or (jogo1.instaLoseAdivPalavra)):
            screen4()

    else:

        screen3()

    finally:
        pass

def adivLetra(letra, targetUI, botao):

    try:
        jogo1.adivinharLetra(letra)

    except BaseException as err:

        if (str(err) == targetUI.infobox.text() and targetUI.infobox.styleSheet() != "color: red; font-size: 9pt"):
            targetUI.infobox.setStyleSheet("color: red; font-size: 9pt")

        else:
            targetUI.infobox.setStyleSheet("font-size: 9pt")
            targetUI.infobox.setText(str(err))


    else:
        targetUI.infobox.setText("")

    finally:
        targetUI.display.setText(jogo1.showDisplay())
        botao.setDisabled(True)
        clickedButtons.append(letra)

        if (jogo1.limite is True):
            targetUI.chancesPainel.setText(f"CHANCES: {jogo1.chances}")


        if (jogo1.showDisplay() == jogo1.palavra):
            jogo1.ganharOJogo()
            screen3()
        elif (jogo1.limite) and (jogo1.perdido is True):
            screen4()

def jogoStart():
    global jogo1


    palavra = choice(listaPalavras)
    print(palavra)
    print(f"revelar={revelar}")
    print(f"tentativas={str(tentativas)}")
    print(f"instalose={instaLose}")
    jogo1 = PartidaDeJogoDaForca(palavra, revelar, tentativas, instaLose)



def revelarPalavra():
    if (jogo1.revelacao):
        return f"a palavra era:\n\"{jogo1.palavra}\""
    else:
        print(f"palavra não será revelada")
        return "palavra não será revelada"

def restart():
    from linking import clickedButtons
    jogoStart()
    clickedButtons.clear()
    screen1()

def setDisplay(targetUI):
    targetUI.display.setText(jogo1.showDisplay())


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
        icon = QtGui.QIcon.fromTheme(icon_path)
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

        self.retranslateConfigTela(janela)
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


    def gameScreen(self, janela):
        janela.setObjectName("janela")
        janela.resize(800, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(janela.sizePolicy().hasHeightForWidth())
        janela.setSizePolicy(sizePolicy)
        janela.setMinimumSize(QtCore.QSize(800, 420))
        janela.setMaximumSize(QtCore.QSize(800, 420))
        font = QtGui.QFont()
        font.setPointSize(9)
        janela.setFont(font)
        icon = QtGui.QIcon.fromTheme(icon_path)
        janela.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(janela)
        self.centralwidget.setObjectName("centralwidget")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(10, 230, 781, 171))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.letraX = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("X", ui, self.letraX))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraX.setFont(font)
        self.letraX.setObjectName("letraX")
        self.gridLayout.addWidget(self.letraX, 1, 10, 1, 1)
        self.letraZ = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("Z", ui, self.letraZ))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraZ.setFont(font)
        self.letraZ.setObjectName("letraZ")
        self.gridLayout.addWidget(self.letraZ, 1, 12, 1, 1)
        self.letraN = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("N", ui, self.letraN))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraN.setFont(font)
        self.letraN.setObjectName("letraN")
        self.gridLayout.addWidget(self.letraN, 0, 13, 1, 1)
        self.letraH = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("H", ui, self.letraH))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraH.setFont(font)
        self.letraH.setObjectName("letraH")
        self.gridLayout.addWidget(self.letraH, 0, 7, 1, 1)
        self.letraW = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("W", ui, self.letraW))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraW.setFont(font)
        self.letraW.setObjectName("letraW")
        self.gridLayout.addWidget(self.letraW, 1, 9, 1, 1)
        self.letraF = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("F", ui, self.letraF))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraF.setFont(font)
        self.letraF.setObjectName("letraF")
        self.gridLayout.addWidget(self.letraF, 0, 5, 1, 1)
        self.letraI = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("I", ui, self.letraI))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraI.setFont(font)
        self.letraI.setObjectName("letraI")
        self.gridLayout.addWidget(self.letraI, 0, 8, 1, 1)
        self.letraY = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("Y", ui, self.letraY))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraY.setFont(font)
        self.letraY.setObjectName("letraY")
        self.gridLayout.addWidget(self.letraY, 1, 11, 1, 1)
        self.letraO = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("O", ui, self.letraO))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraO.setFont(font)
        self.letraO.setObjectName("letraO")
        self.gridLayout.addWidget(self.letraO, 1, 1, 1, 1)
        self.letraG = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("G", ui, self.letraG))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraG.setFont(font)
        self.letraG.setObjectName("letraG")
        self.gridLayout.addWidget(self.letraG, 0, 6, 1, 1)
        self.letraM = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("M", ui, self.letraM))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraM.setFont(font)
        self.letraM.setObjectName("letraM")
        self.gridLayout.addWidget(self.letraM, 0, 12, 1, 1)
        self.letraU = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("U", ui, self.letraU))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraU.setFont(font)
        self.letraU.setObjectName("letraU")
        self.gridLayout.addWidget(self.letraU, 1, 7, 1, 1)
        self.letraD = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("D", ui, self.letraD))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraD.setFont(font)
        self.letraD.setObjectName("letraD")
        self.gridLayout.addWidget(self.letraD, 0, 3, 1, 1)
        self.letraQ = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("Q", ui, self.letraQ))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraQ.setFont(font)
        self.letraQ.setObjectName("letraQ")
        self.gridLayout.addWidget(self.letraQ, 1, 3, 1, 1)
        self.letraB = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("B", ui, self.letraB))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraB.setFont(font)
        self.letraB.setObjectName("letraB")
        self.gridLayout.addWidget(self.letraB, 0, 1, 1, 1)
        self.letraA = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("A", ui, ui.letraA))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraA.setFont(font)
        self.letraA.setObjectName("letraA")
        self.gridLayout.addWidget(self.letraA, 0, 0, 1, 1)
        self.letraE = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("E", ui, self.letraE))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraE.setFont(font)
        self.letraE.setObjectName("letraE")
        self.gridLayout.addWidget(self.letraE, 0, 4, 1, 1)
        self.letraC = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("C", ui, self.letraC))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraC.setFont(font)
        self.letraC.setObjectName("letraC")
        self.gridLayout.addWidget(self.letraC, 0, 2, 1, 1)
        self.letraJ = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("J", ui, self.letraJ))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraJ.setFont(font)
        self.letraJ.setObjectName("letraJ")
        self.gridLayout.addWidget(self.letraJ, 0, 9, 1, 1)
        self.letraV = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("V", ui, self.letraV))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraV.setFont(font)
        self.letraV.setObjectName("letraV")
        self.gridLayout.addWidget(self.letraV, 1, 8, 1, 1)
        self.letraL = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("L", ui, self.letraL))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraL.setFont(font)
        self.letraL.setObjectName("letraL")
        self.gridLayout.addWidget(self.letraL, 0, 11, 1, 1)
        self.letraS = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("S", ui, self.letraS))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraS.setFont(font)
        self.letraS.setObjectName("letraS")
        self.gridLayout.addWidget(self.letraS, 1, 5, 1, 1)
        self.letraR = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("R", ui, self.letraR))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraR.setFont(font)
        self.letraR.setObjectName("letraR")
        self.gridLayout.addWidget(self.letraR, 1, 4, 1, 1)
        self.letraK = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("K", ui, self.letraK))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraK.setFont(font)
        self.letraK.setObjectName("letraK")
        self.gridLayout.addWidget(self.letraK, 0, 10, 1, 1)
        self.letraP = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("P", ui, self.letraP))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraP.setFont(font)
        self.letraP.setObjectName("letraP")
        self.gridLayout.addWidget(self.letraP, 1, 2, 1, 1)
        self.letraT = QtWidgets.QPushButton(self.gridFrame, clicked=lambda: adivLetra("T", ui, self.letraT))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.letraT.setFont(font)
        self.letraT.setObjectName("letraT")
        self.gridLayout.addWidget(self.letraT, 1, 6, 1, 1)
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(30, 70, 731, 111))
        font = QtGui.QFont()
        font.setPointSize(37)
        font.setBold(True)
        self.display.setFont(font)
        self.display.setText("")
        self.display.setAlignment(QtCore.Qt.AlignCenter)
        self.display.setObjectName("label")

        self.adivinharPalavra = QtWidgets.QPushButton(self.centralwidget, clicked=screen2)
        self.adivinharPalavra.setGeometry(QtCore.QRect(20, 200, 161, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.adivinharPalavra.setFont(font)
        self.adivinharPalavra.setObjectName("adivinharPalavra")

        if (jogo1.limite is True):
            self.chancesPainel = QtWidgets.QLabel(self.centralwidget)
            self.chancesPainel.setGeometry(QtCore.QRect(20, 20, 131, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            self.chancesPainel.setFont(font)
            self.chancesPainel.setObjectName("chancesPainel")


        janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(janela)
        QtCore.QMetaObject.connectSlotsByName(janela)

        self.infobox = QtWidgets.QLabel(self.centralwidget)
        self.infobox.setGeometry(QtCore.QRect(150, 20, 501, 21))
        self.infobox.setText("")
        self.infobox.setAlignment(QtCore.Qt.AlignCenter)
        self.infobox.setObjectName("infobox")



        setDisplay(ui)

    def retranslateUi(self, janela):
        _translate = QtCore.QCoreApplication.translate
        janela.setWindowTitle(_translate("janela", "Jogo da Forca"))
        self.letraX.setText(_translate("janela", "X"))
        self.letraZ.setText(_translate("janela", "Z"))
        self.letraN.setText(_translate("janela", "N"))
        self.letraH.setText(_translate("janela", "H"))
        self.letraW.setText(_translate("janela", "W"))
        self.letraF.setText(_translate("janela", "F"))
        self.letraI.setText(_translate("janela", "I"))
        self.letraY.setText(_translate("janela", "Y"))
        self.letraO.setText(_translate("janela", "O"))
        self.letraG.setText(_translate("janela", "G"))
        self.letraM.setText(_translate("janela", "M"))
        self.letraU.setText(_translate("janela", "U"))
        self.letraD.setText(_translate("janela", "D"))
        self.letraQ.setText(_translate("janela", "Q"))
        self.letraB.setText(_translate("janela", "B"))
        self.letraA.setText(_translate("janela", "A"))
        self.letraE.setText(_translate("janela", "E"))
        self.letraC.setText(_translate("janela", "C"))
        self.letraJ.setText(_translate("janela", "J"))
        self.letraV.setText(_translate("janela", "V"))
        self.letraL.setText(_translate("janela", "L"))
        self.letraS.setText(_translate("janela", "S"))
        self.letraR.setText(_translate("janela", "R"))
        self.letraK.setText(_translate("janela", "K"))
        self.letraP.setText(_translate("janela", "P"))
        self.letraT.setText(_translate("janela", "T"))
        self.adivinharPalavra.setText(_translate("janela", "ADIVINHAR PALAVRA"))

        if (jogo1.limite is True):
            self.chancesPainel.setText(_translate("janela", f"CHANCES: {jogo1.chances}"))

    def adivScreen(self, janela):
        janela.setObjectName("janela")
        janela.resize(800, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(janela.sizePolicy().hasHeightForWidth())
        janela.setSizePolicy(sizePolicy)
        janela.setMinimumSize(QtCore.QSize(800, 420))
        janela.setMaximumSize(QtCore.QSize(800, 420))
        font = QtGui.QFont()
        font.setPointSize(9)
        janela.setFont(font)
        icon = QtGui.QIcon.fromTheme(icon_path)
        janela.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(janela)
        self.centralwidget.setObjectName("centralwidget")
        self.telinhaQueAdivinha = QtWidgets.QLineEdit(self.centralwidget)
        self.telinhaQueAdivinha.setGeometry(QtCore.QRect(50, 140, 691, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.telinhaQueAdivinha.setFont(font)
        self.telinhaQueAdivinha.setObjectName("telinhaQueAdivinha")
        self.tentar = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: adivPalavra(ui, self.telinhaQueAdivinha.text()))
        self.tentar.setGeometry(QtCore.QRect(80, 280, 231, 58))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.tentar.setFont(font)
        self.tentar.setObjectName("tentar")
        self.voltar = QtWidgets.QPushButton(self.centralwidget, clicked=screen1)
        self.voltar.setGeometry(QtCore.QRect(490, 280, 231, 58))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.voltar.setFont(font)
        self.voltar.setObjectName("voltar")
        self.infobox = QtWidgets.QLabel(self.centralwidget)
        self.infobox.setGeometry(QtCore.QRect(150, 40, 501, 21))
        self.infobox.setText("")
        self.infobox.setAlignment(QtCore.Qt.AlignCenter)
        self.infobox.setObjectName("infobox")
        janela.setCentralWidget(self.centralwidget)

        self.retraduzir(janela)
        QtCore.QMetaObject.connectSlotsByName(janela)


    def retraduzir(self, janela):
        _translate = QtCore.QCoreApplication.translate
        janela.setWindowTitle(_translate("janela", "Jogo da Forca"))
        self.tentar.setText(_translate("janela", "TENTAR"))
        self.voltar.setText(_translate("janela", "VOLTAR"))


    def janelaFinal(self, janela):
        janela.setObjectName("janela")
        janela.resize(800, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(janela.sizePolicy().hasHeightForWidth())
        janela.setSizePolicy(sizePolicy)
        janela.setMinimumSize(QtCore.QSize(800, 420))
        janela.setMaximumSize(QtCore.QSize(800, 420))
        font = QtGui.QFont()
        font.setPointSize(9)
        janela.setFont(font)
        icon = QtGui.QIcon.fromTheme(icon_path)
        janela.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(janela)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 361))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        janela.setCentralWidget(self.centralwidget)

        self.displayFinal = QtWidgets.QLabel(self.centralwidget)
        self.displayFinal.setGeometry(QtCore.QRect(0, 0, 791, 361))
        font = QtGui.QFont()
        font.setPointSize(37)
        font.setBold(True)
        self.displayFinal.setFont(font)
        self.displayFinal.setText(jogo1.palavra)
        self.displayFinal.setAlignment(QtCore.Qt.AlignCenter)

        janela.setCentralWidget(self.centralwidget)

        # add label to main window
        janela.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)
        self.movie.start()

        self.infoboxFinal = QtWidgets.QLabel(self.centralwidget)
        self.infoboxFinal.setGeometry(QtCore.QRect(250, 280, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.infoboxFinal.setFont(font)
        self.infoboxFinal.setAlignment(QtCore.Qt.AlignCenter)
        self.infoboxFinal.setObjectName("infoboxFinal")
        self.sairbtn = QtWidgets.QPushButton(self.centralwidget, clicked=exit)
        self.sairbtn.setGeometry(QtCore.QRect(640, 370, 131, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.sairbtn.setFont(font)
        self.sairbtn.setObjectName("sairbtn")
        self.againbtn = QtWidgets.QPushButton(self.centralwidget, clicked=restart)
        self.againbtn.setGeometry(QtCore.QRect(640, 340, 131, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.againbtn.setFont(font)
        self.againbtn.setObjectName("pushButton_2")
        janela.setCentralWidget(self.centralwidget)


        self.retraduzirFinal(janela)
        QtCore.QMetaObject.connectSlotsByName(janela)



    def retraduzirFinal(self, janela):
        _translate = QtCore.QCoreApplication.translate
        janela.setWindowTitle(_translate("janela", "Jogo da Forca"))
        self.infoboxFinal.setText(_translate("janela", "VOCÊ GANHOU!"))
        self.sairbtn.setText(_translate("janela", "SAIR"))
        self.againbtn.setText(_translate("janela", "JOGAR DE NOVO"))

    def loseScreen(self, janela):
        janela.setObjectName("janela")
        janela.resize(800, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(janela.sizePolicy().hasHeightForWidth())
        janela.setSizePolicy(sizePolicy)
        janela.setMinimumSize(QtCore.QSize(800, 420))
        janela.setMaximumSize(QtCore.QSize(800, 420))
        font = QtGui.QFont()
        font.setPointSize(9)
        janela.setFont(font)
        icon = QtGui.QIcon.fromTheme(icon_path)
        janela.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(janela)
        self.centralwidget.setObjectName("centralwidget")
        self.infoboxFinal = QtWidgets.QLabel(self.centralwidget)
        self.infoboxFinal.setGeometry(QtCore.QRect(250, 60, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.infoboxFinal.setFont(font)
        self.infoboxFinal.setAlignment(QtCore.Qt.AlignCenter)
        self.infoboxFinal.setObjectName("infoboxFinal")
        self.sairbtn = QtWidgets.QPushButton(self.centralwidget, clicked=exit)
        self.sairbtn.setGeometry(QtCore.QRect(640, 370, 131, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.sairbtn.setFont(font)
        self.sairbtn.setObjectName("sairbtn")
        self.againbtn = QtWidgets.QPushButton(self.centralwidget, clicked=restart)
        self.againbtn.setGeometry(QtCore.QRect(640, 340, 131, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.againbtn.setFont(font)
        self.againbtn.setFlat(False)
        self.againbtn.setObjectName("againbtn")
        self.palavrareveal = QtWidgets.QLabel(self.centralwidget)
        self.palavrareveal.setGeometry(QtCore.QRect(250, 210, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.palavrareveal.setFont(font)
        self.palavrareveal.setAlignment(QtCore.Qt.AlignCenter)
        self.palavrareveal.setObjectName("palavrareveal")
        janela.setCentralWidget(self.centralwidget)

        self.retranslateLoseScreen(janela)
        QtCore.QMetaObject.connectSlotsByName(janela)

    def retranslateLoseScreen(self, janela):
        _translate = QtCore.QCoreApplication.translate
        janela.setWindowTitle(_translate("janela", "Jogo da Forca"))
        self.infoboxFinal.setText(_translate("janela", "VOCÊ PERDEU"))
        self.sairbtn.setText(_translate("janela", "SAIR"))
        self.againbtn.setText(_translate("janela", "JOGAR DE NOVO"))
        self.palavrareveal.setText(_translate("janela", revelarPalavra()))


import sys



app = QtWidgets.QApplication(sys.argv)
janela = QtWidgets.QMainWindow()
ui = Ui_janela()
ui.configTela(janela)

janela.show()
sys.exit(app.exec_())