from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import locale
import webbrowser
from pickle import dump, load
from PyQt5.QtWidgets import QFileDialog

locale.setlocale(locale.LC_ALL, '')
adres = ".\\kayitlar\\kullanici_kayitlari.txt"

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(731, 303)
        Form.setToolTip("")
        Form.setAccessibleName("")
        Form.setAutoFillBackground(False)
        
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 711, 285))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.check_5 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_5.setFont(font)
        self.check_5.setObjectName("check_5")
        self.gridLayout_2.addWidget(self.check_5, 2, 1, 1, 1)
        
        self.check_2 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_2.setFont(font)
        self.check_2.setObjectName("check_2")
        self.gridLayout_2.addWidget(self.check_2, 1, 0, 1, 1)
        
        self.check_4 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_4.setFont(font)
        self.check_4.setObjectName("check_4")
        self.gridLayout_2.addWidget(self.check_4, 2, 0, 1, 1)
        
        self.check_6 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_6.setFont(font)
        self.check_6.setObjectName("check_6")
        self.gridLayout_2.addWidget(self.check_6, 4, 0, 1, 1)
        
        self.check_7 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_7.setFont(font)
        self.check_7.setObjectName("check_7")
        self.gridLayout_2.addWidget(self.check_7, 4, 1, 1, 1)
        
        self.check_0 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_0.setFont(font)
        self.check_0.setObjectName("check_0")
        self.gridLayout_2.addWidget(self.check_0, 0, 0, 1, 1)
        
        self.check_3 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_3.setFont(font)
        self.check_3.setObjectName("check_3")
        self.gridLayout_2.addWidget(self.check_3, 1, 1, 1, 1)
        
        self.check_1 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_1.setFont(font)
        self.check_1.setIconSize(QtCore.QSize(16, 16))
        self.check_1.setChecked(False)
        self.check_1.setAutoRepeat(False)
        self.check_1.setAutoExclusive(False)
        self.check_1.setAutoRepeatInterval(100)
        self.check_1.setTristate(False)
        self.check_1.setObjectName("check_1")
        self.gridLayout_2.addWidget(self.check_1, 0, 1, 1, 1)
        
        self.check_8 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_8.setFont(font)
        self.check_8.setObjectName("check_8")
        self.gridLayout_2.addWidget(self.check_8, 5, 0, 1, 1)
        
        self.check_9 = QtWidgets.QCheckBox(self.layoutWidget)
        self.check_9.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_9.setFont(font)
        self.check_9.setChecked(False)
        self.check_9.setAutoRepeat(False)
        self.check_9.setAutoExclusive(False)
        self.check_9.setTristate(False)
        self.check_9.setObjectName("check_9")
                
        self.check_0.setEnabled(False)
        self.check_1.setEnabled(False)
        self.check_2.setEnabled(False)
        self.check_3.setEnabled(False)
        self.check_4.setEnabled(False)
        self.check_5.setEnabled(False)
        self.check_6.setEnabled(False)
        self.check_7.setEnabled(False)
        self.check_8.setEnabled(False)
        self.check_9.setEnabled(False)

        self.gridLayout_2.addWidget(self.check_9, 5, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 3)
        
        self.what_do_tx = QtWidgets.QLineEdit(self.layoutWidget)
        self.what_do_tx.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.what_do_tx.setFont(font)
        self.what_do_tx.setToolTip("")
        self.what_do_tx.setAutoFillBackground(False)
        self.what_do_tx.setInputMask("")
        self.what_do_tx.setText("")
        self.what_do_tx.setMaxLength(70)
        self.what_do_tx.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.what_do_tx.setClearButtonEnabled(True)
        self.what_do_tx.setObjectName("what_do_tx")
        self.what_do_tx.setPlaceholderText("Ne Yapacaksın...")
        
        self.gridLayout.addWidget(self.what_do_tx, 1, 0, 1, 1)
        
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        
        self.add_buton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_buton.setFont(font)
        self.add_buton.setObjectName("add_buton")
        self.gridLayout.addWidget(self.add_buton, 1, 1, 1, 1)
        
        self.load_buton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.load_buton.setFont(font)
        self.load_buton.setObjectName("load_buton")
        self.load_buton.setEnabled(True)
        self.gridLayout.addWidget(self.load_buton, 3, 0, 1, 1)
        
        self.clear_buton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clear_buton.setFont(font)
        self.clear_buton.setObjectName("clear_buton")
        self.gridLayout.addWidget(self.clear_buton, 1, 2, 1, 1)
        
        self.history_buton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.history_buton.setFont(font)
        self.history_buton.setObjectName("history_buton")
        self.gridLayout.addWidget(self.history_buton, 3, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        an = datetime.datetime.now()
        tarih = datetime.datetime.now()
        dosya = open(adres, "a")
        dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - ***Uygulama Başlatıldı***\n")

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Yapılacaklar Listesi"))
        self.check_5.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_2.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_4.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_6.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_7.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_0.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_3.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_1.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_8.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_9.setText(_translate("Form", "Kontrol Kutusu"))
        self.label.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Yapılacaklar Listesi</p></body></html>"))
        self.add_buton.setText(_translate("Form", "Ekle"))
        self.load_buton.setText(_translate("Form", "Dosya Yükle"))
        self.clear_buton.setText(_translate("Form", "Tümünü Sil"))
        self.history_buton.setText(_translate("Form", "Geçmiş"))
        
        self.add_buton.clicked.connect(self.def_add_buton)        
        self.clear_buton.clicked.connect(self.def_clear_buton)
        self.load_buton.clicked.connect(self.def_load_buton)
        self.history_buton.clicked.connect(lambda:webbrowser.open(adres))

# Check Buttons
        self.check_0.clicked.connect(self.def_check_0)
        self.check_1.clicked.connect(self.def_check_1)
        self.check_2.clicked.connect(self.def_check_2)
        self.check_3.clicked.connect(self.def_check_3)
        self.check_4.clicked.connect(self.def_check_4)
        self.check_5.clicked.connect(self.def_check_5)
        self.check_6.clicked.connect(self.def_check_6)
        self.check_7.clicked.connect(self.def_check_7)
        self.check_8.clicked.connect(self.def_check_8)
        self.check_9.clicked.connect(self.def_check_9)

        self.what_do_tx.returnPressed.connect(self.def_add_buton)  # Enter - Add Buton


# Check Buttons
    def def_check_0(self):
        f = self.check_0.font()
        f.setStrikeOut(self.check_0.isChecked())
        self.check_0.setFont(f)  
        
        ch0 = self.check_0.text()
        if self.check_0.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch0} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch0} yapılmadı olarak işaretlendi.\n")

    def def_check_1(self):
        f = self.check_1.font()
        f.setStrikeOut(self.check_1.isChecked())
        self.check_1.setFont(f)  
        
        ch1 = self.check_1.text()
        if self.check_1.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch1} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch1} yapılmadı olarak işaretlendi.\n")

    def def_check_2(self):
        f = self.check_2.font()
        f.setStrikeOut(self.check_2.isChecked())
        self.check_2.setFont(f)  
        
        ch2 = self.check_2.text()
        if self.check_2.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch2} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch2} yapılmadı olarak işaretlendi.\n")

    def def_check_3(self):
        f = self.check_3.font()
        f.setStrikeOut(self.check_3.isChecked())
        self.check_3.setFont(f)  
        
        ch3 = self.check_3.text()
        if self.check_3.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch3} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch3} yapılmadı olarak işaretlendi.\n")

    def def_check_4(self):
        f = self.check_4.font()
        f.setStrikeOut(self.check_4.isChecked())
        self.check_4.setFont(f)  
        
        ch4 = self.check_4.text()
        if self.check_4.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch4} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch4} yapılmadı olarak işaretlendi.\n")

    def def_check_5(self):
        f = self.check_5.font()
        f.setStrikeOut(self.check_5.isChecked())
        self.check_5.setFont(f)  
        
        ch5 = self.check_5.text()
        if self.check_5.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch5} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch5} yapılmadı olarak işaretlendi.\n")

    def def_check_6(self):
        f = self.check_6.font()
        f.setStrikeOut(self.check_6.isChecked())
        self.check_6.setFont(f)  
        
        ch6 = self.check_6.text()
        if self.check_6.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch6} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch6} yapılmadı olarak işaretlendi.\n")

    def def_check_7(self):
        f = self.check_7.font()
        f.setStrikeOut(self.check_7.isChecked())
        self.check_7.setFont(f)  
        
        ch7 = self.check_7.text()
        if self.check_7.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch7} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch7} yapılmadı olarak işaretlendi.\n")

    def def_check_8(self):
        f = self.check_8.font()
        f.setStrikeOut(self.check_8.isChecked())
        self.check_8.setFont(f)  
        
        ch8 = self.check_8.text()
        if self.check_8.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch8} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch8} yapılmadı olarak işaretlendi.\n")

    def def_check_9(self):
        f = self.check_9.font()
        f.setStrikeOut(self.check_9.isChecked())
        self.check_9.setFont(f)  
        
        ch9 = self.check_9.text()
        if self.check_9.isChecked():
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch9} yapıldı olarak işaretlendi.\n")
        
        else:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {ch9} yapılmadı olarak işaretlendi.\n")


# Load Buton
    def def_load_buton(self):
        fname = QFileDialog.getOpenFileName(directory="C:\\Users\\ESAD\\Desktop\\IDLE\\kayitlar\\yukleme_yeri")[0]
        if not fname:
            self.what_do_tx.setPlaceholderText("Dosya Seçiniz!")
        else:
            yukle = open(fname, "rb")
            gelen_sozluk = load(yukle)
            yukle.close()
            self.veriyi_isle(gelen_sozluk)
            
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - [DOSYA YÜKLENDİ]\n")
        self.n = len(gelen_sozluk)

    def veriyi_isle(self, veri):
        self.check_0.setEnabled(False)
        self.check_1.setEnabled(False)
        self.check_2.setEnabled(False)
        self.check_3.setEnabled(False)
        self.check_4.setEnabled(False)
        self.check_5.setEnabled(False)
        self.check_6.setEnabled(False)
        self.check_7.setEnabled(False)
        self.check_8.setEnabled(False)
        self.check_9.setEnabled(False)
        self.check_0.setChecked(False)
        self.check_1.setChecked(False)
        self.check_2.setChecked(False)
        self.check_3.setChecked(False)
        self.check_4.setChecked(False)
        self.check_5.setChecked(False)
        self.check_6.setChecked(False)
        self.check_7.setChecked(False)
        self.check_8.setChecked(False)
        self.check_9.setChecked(False)
        _translate = QtCore.QCoreApplication.translate
        self.check_5.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_2.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_4.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_6.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_7.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_0.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_3.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_1.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_8.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_9.setText(_translate("Form", "Kontrol Kutusu"))
        f = self.check_0.font()
        f.setStrikeOut(False)
        self.check_0.setFont(f)   
        
        f = self.check_1.font()
        f.setStrikeOut(False)
        self.check_1.setFont(f)   

        f = self.check_2.font()
        f.setStrikeOut(False)
        self.check_2.setFont(f)   

        f = self.check_3.font()
        f.setStrikeOut(False)
        self.check_3.setFont(f)   

        f = self.check_4.font()
        f.setStrikeOut(False)
        self.check_4.setFont(f)   

        f = self.check_5.font()
        f.setStrikeOut(False)
        self.check_5.setFont(f)   

        f = self.check_6.font()
        f.setStrikeOut(False)
        self.check_6.setFont(f)   

        f = self.check_7.font()
        f.setStrikeOut(False)
        self.check_7.setFont(f)   

        f = self.check_8.font()
        f.setStrikeOut(False)
        self.check_8.setFont(f)   

        f = self.check_9.font()
        f.setStrikeOut(False)
        self.check_9.setFont(f)

        _translate = QtCore.QCoreApplication.translate
        checkboxlar = [self.check_0, self.check_1, self.check_2, self.check_3, self.check_4, self.check_5, self.check_6, self.check_7, self.check_8, self.check_9]
        kac_tane = len(veri)
        adlar = []
        isaretler = []
        
        for check_adları in veri:
            adlar.append(check_adları)
        
        for check_isareti in veri.values():
            isaretler.append(check_isareti)

        for check, isaret, ad in zip(checkboxlar, isaretler, adlar):
            check.setText(_translate("Form", ad))
            check.setChecked(isaret)
            check.setEnabled(True)

        f = self.check_0.font()
        f.setStrikeOut(self.check_0.isChecked())
        self.check_0.setFont(f)  
                
        f = self.check_1.font()
        f.setStrikeOut(self.check_1.isChecked())
        self.check_1.setFont(f)  
        
        f = self.check_2.font()
        f.setStrikeOut(self.check_2.isChecked())
        self.check_2.setFont(f)  

        f = self.check_3.font()
        f.setStrikeOut(self.check_3.isChecked())
        self.check_3.setFont(f)  
        
        f = self.check_4.font()
        f.setStrikeOut(self.check_4.isChecked())
        self.check_4.setFont(f)  
        
        f = self.check_5.font()
        f.setStrikeOut(self.check_5.isChecked())
        self.check_5.setFont(f)  
        
        f = self.check_6.font()
        f.setStrikeOut(self.check_6.isChecked())
        self.check_6.setFont(f)  
        
        f = self.check_7.font()
        f.setStrikeOut(self.check_7.isChecked())
        self.check_7.setFont(f)  
        
        f = self.check_8.font()
        f.setStrikeOut(self.check_8.isChecked())
        self.check_8.setFont(f)  
        
        f = self.check_9.font()
        f.setStrikeOut(self.check_9.isChecked())
        self.check_9.setFont(f)  
        

# Clear Button
    def def_clear_buton(self):
        self.check_0.setEnabled(False)
        self.check_1.setEnabled(False)
        self.check_2.setEnabled(False)
        self.check_3.setEnabled(False)
        self.check_4.setEnabled(False)
        self.check_5.setEnabled(False)
        self.check_6.setEnabled(False)
        self.check_7.setEnabled(False)
        self.check_8.setEnabled(False)
        self.check_9.setEnabled(False)
        self.check_0.setChecked(False)
        self.check_1.setChecked(False)
        self.check_2.setChecked(False)
        self.check_3.setChecked(False)
        self.check_4.setChecked(False)
        self.check_5.setChecked(False)
        self.check_6.setChecked(False)
        self.check_7.setChecked(False)
        self.check_8.setChecked(False)
        self.check_9.setChecked(False)
        _translate = QtCore.QCoreApplication.translate
        self.check_5.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_2.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_4.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_6.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_7.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_0.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_3.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_1.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_8.setText(_translate("Form", "Kontrol Kutusu"))
        self.check_9.setText(_translate("Form", "Kontrol Kutusu"))
        f = self.check_0.font()
        f.setStrikeOut(False)
        self.check_0.setFont(f)   
        
        f = self.check_1.font()
        f.setStrikeOut(False)
        self.check_1.setFont(f)   

        f = self.check_2.font()
        f.setStrikeOut(False)
        self.check_2.setFont(f)   

        f = self.check_3.font()
        f.setStrikeOut(False)
        self.check_3.setFont(f)   

        f = self.check_4.font()
        f.setStrikeOut(False)
        self.check_4.setFont(f)   

        f = self.check_5.font()
        f.setStrikeOut(False)
        self.check_5.setFont(f)   

        f = self.check_6.font()
        f.setStrikeOut(False)
        self.check_6.setFont(f)   

        f = self.check_7.font()
        f.setStrikeOut(False)
        self.check_7.setFont(f)   

        f = self.check_8.font()
        f.setStrikeOut(False)
        self.check_8.setFont(f)   

        f = self.check_9.font()
        f.setStrikeOut(False)
        self.check_9.setFont(f)
        
        if self.n > 0:
            an = datetime.datetime.now()
            tarih = datetime.datetime.now()
            dosya = open(adres, "a")
            dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - [TEMİZLENDİ] \n")
            self.what_do_tx.setPlaceholderText("Ne Yapacaksın...")

        else:
            self.what_do_tx.setText("")
            self.what_do_tx.setPlaceholderText("Bir Şey Ekleyiniz!")            

        self.n = 0   


# Add Button   
    n = 0
    def def_add_buton(self):
        _translate = QtCore.QCoreApplication.translate
        job = self.what_do_tx.text()

        if len(job) <= 1:
            self.what_do_tx.setText("")
            self.what_do_tx.setPlaceholderText("Bir Şey Yazınız!")

        else:
            if self.n > 9:
                self.what_do_tx.setText("")
                self.what_do_tx.setPlaceholderText("Liste Dolu.")            
            else:
                if self.n == 0:
                    self.check_0.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)

                elif self.n == 1:
                    self.check_1.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)

                elif self.n == 2:
                    self.check_2.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)
                    self.check_2.setEnabled(True)

                elif self.n == 3:
                    self.check_3.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)
                    self.check_2.setEnabled(True)
                    self.check_3.setEnabled(True)

                elif self.n == 4:
                    self.check_4.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)
                    self.check_2.setEnabled(True)
                    self.check_3.setEnabled(True)
                    self.check_4.setEnabled(True)

                elif self.n == 5:
                    self.check_5.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)
                    self.check_2.setEnabled(True)
                    self.check_3.setEnabled(True)
                    self.check_4.setEnabled(True)
                    self.check_5.setEnabled(True)

                elif self.n == 6:
                    self.check_6.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)
                    self.check_2.setEnabled(True)
                    self.check_3.setEnabled(True)
                    self.check_4.setEnabled(True)
                    self.check_5.setEnabled(True)
                    self.check_6.setEnabled(True)

                elif self.n == 7:
                    self.check_7.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)
                    self.check_2.setEnabled(True)
                    self.check_3.setEnabled(True)
                    self.check_4.setEnabled(True)
                    self.check_5.setEnabled(True)
                    self.check_6.setEnabled(True)
                    self.check_7.setEnabled(True)

                elif self.n == 8:
                    self.check_8.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)
                    self.check_2.setEnabled(True)
                    self.check_3.setEnabled(True)
                    self.check_4.setEnabled(True)
                    self.check_5.setEnabled(True)
                    self.check_6.setEnabled(True)
                    self.check_7.setEnabled(True)
                    self.check_8.setEnabled(True)

                elif self.n == 9:
                    self.check_9.setText(_translate("Form", job))
                    self.n += 1
                    self.check_0.setEnabled(True)
                    self.check_1.setEnabled(True)
                    self.check_2.setEnabled(True)
                    self.check_3.setEnabled(True)
                    self.check_4.setEnabled(True)
                    self.check_5.setEnabled(True)
                    self.check_6.setEnabled(True)
                    self.check_7.setEnabled(True)
                    self.check_8.setEnabled(True)
                    self.check_9.setEnabled(True)
                
                self.what_do_tx.setText("")
                self.what_do_tx.setPlaceholderText("What To Do...")
        
                an = datetime.datetime.now()
                tarih = datetime.datetime.now()
                dosya = open(adres, "a")
                dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - {job} listeye eklendi.\n")
   
    def keep_alive(self):    
        _translate = QtCore.QCoreApplication.translate
        job = self.what_do_tx.text()
        an = datetime.datetime.now()

        if self.n > 0:
            sozluk = {}
            checkboxlar = [self.check_0, self.check_1, self.check_2, self.check_3, self.check_4, self.check_5, self.check_6, self.check_7, self.check_8, self.check_9]

            for check in checkboxlar[:self.n]:
                sozluk[check.text()] = check.isChecked()

            kayit_adi = datetime.datetime.strftime(an, '%c').replace(":", "_")
            kayit_yeri = open(f"C:\\Users\\ESAD\\Desktop\\IDLE\\kayitlar\\yukleme_yeri\\{kayit_adi}", "wb")
            dump(sozluk, kayit_yeri)

        tarih = datetime.datetime.now()
        dosya = open(adres, "a")
        dosya.write(f"{datetime.datetime.strftime(an, '%d %b %Y %a %X')} - ***Uygulama Kapatıldı***\n\n")
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)


    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.lastWindowClosed.connect(ui.keep_alive)
    sys.exit(app.exec_())
