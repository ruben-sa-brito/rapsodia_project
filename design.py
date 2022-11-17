# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 614)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-lótus-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.register_2 = QtWidgets.QWidget()
        self.register_2.setObjectName("register_2")
        self.lineEdit = QtWidgets.QLineEdit(self.register_2)
        self.lineEdit.setGeometry(QtCore.QRect(70, 80, 271, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.register_2)
        self.label.setGeometry(QtCore.QRect(110, 10, 281, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.register_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.register_2)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.register_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 120, 271, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.register_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 160, 131, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.register_2)
        self.label_5.setGeometry(QtCore.QRect(0, 200, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.register_2)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 61, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.register_2)
        self.pushButton.setGeometry(QtCore.QRect(70, 290, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.register_2)
        self.comboBox.setGeometry(QtCore.QRect(70, 240, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.register_2)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 61, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.register_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 40, 91, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.register_2)
        self.label_9.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.register_2)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 290, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dateEdit = QtWidgets.QDateEdit(self.register_2)
        self.dateEdit.setGeometry(QtCore.QRect(70, 200, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_22 = QtWidgets.QLabel(self.register_2)
        self.label_22.setGeometry(QtCore.QRect(10, 500, 481, 16))
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.register_2)
        self.cursos = QtWidgets.QWidget()
        self.cursos.setObjectName("cursos")
        self.label_14 = QtWidgets.QLabel(self.cursos)
        self.label_14.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_14.setObjectName("label_14")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.cursos)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 50, 91, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_17 = QtWidgets.QLabel(self.cursos)
        self.label_17.setGeometry(QtCore.QRect(120, 10, 281, 16))
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.cursos)
        self.label_19.setGeometry(QtCore.QRect(20, 210, 61, 16))
        self.label_19.setObjectName("label_19")
        self.course_name = QtWidgets.QLineEdit(self.cursos)
        self.course_name.setGeometry(QtCore.QRect(80, 90, 271, 21))
        self.course_name.setObjectName("course_name")
        self.label_20 = QtWidgets.QLabel(self.cursos)
        self.label_20.setGeometry(QtCore.QRect(-20, 130, 121, 16))
        self.label_20.setObjectName("label_20")
        self.workload = QtWidgets.QLineEdit(self.cursos)
        self.workload.setGeometry(QtCore.QRect(80, 130, 271, 20))
        self.workload.setObjectName("workload")
        self.updatec = QtWidgets.QPushButton(self.cursos)
        self.updatec.setGeometry(QtCore.QRect(180, 250, 81, 23))
        self.updatec.setObjectName("updatec")
        self.mounths = QtWidgets.QLineEdit(self.cursos)
        self.mounths.setGeometry(QtCore.QRect(80, 210, 131, 20))
        self.mounths.setObjectName("mounths")
        self.registerc = QtWidgets.QPushButton(self.cursos)
        self.registerc.setGeometry(QtCore.QRect(80, 250, 81, 23))
        self.registerc.setObjectName("registerc")
        self.label_21 = QtWidgets.QLabel(self.cursos)
        self.label_21.setGeometry(QtCore.QRect(30, 90, 61, 16))
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.cursos)
        self.label_23.setGeometry(QtCore.QRect(10, 170, 71, 16))
        self.label_23.setObjectName("label_23")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.cursos)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 170, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.stackedWidget.addWidget(self.cursos)
        self.update = QtWidgets.QWidget()
        self.update.setObjectName("update")
        self.label_7 = QtWidgets.QLabel(self.update)
        self.label_7.setGeometry(QtCore.QRect(140, 120, 241, 81))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.update)
        self.pay = QtWidgets.QWidget()
        self.pay.setObjectName("pay")
        self.label_8 = QtWidgets.QLabel(self.pay)
        self.label_8.setGeometry(QtCore.QRect(140, 10, 221, 16))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.pay)
        self.label_10.setGeometry(QtCore.QRect(70, 70, 101, 16))
        self.label_10.setObjectName("label_10")
        self.id_alunop = QtWidgets.QLineEdit(self.pay)
        self.id_alunop.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.id_alunop.setObjectName("id_alunop")
        self.pushButtonPay = QtWidgets.QPushButton(self.pay)
        self.pushButtonPay.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.pushButtonPay.setObjectName("pushButtonPay")
        self.parcela = QtWidgets.QLineEdit(self.pay)
        self.parcela.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.parcela.setObjectName("parcela")
        self.label_18 = QtWidgets.QLabel(self.pay)
        self.label_18.setGeometry(QtCore.QRect(110, 100, 47, 13))
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.pay)
        self.search = QtWidgets.QWidget()
        self.search.setObjectName("search")
        self.comboBox_2 = QtWidgets.QComboBox(self.search)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 360, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_11 = QtWidgets.QLabel(self.search)
        self.label_11.setGeometry(QtCore.QRect(10, 360, 71, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.search)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 390, 131, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.search)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 420, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.search)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 360, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.list_course = QtWidgets.QPushButton(self.search)
        self.list_course.setGeometry(QtCore.QRect(250, 400, 91, 23))
        self.list_course.setObjectName("list_course")
        self.textBrowser = QtWidgets.QTextBrowser(self.search)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 511, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.search)
        self.delete_2 = QtWidgets.QWidget()
        self.delete_2.setObjectName("delete_2")
        self.idadel = QtWidgets.QLineEdit(self.delete_2)
        self.idadel.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.idadel.setObjectName("idadel")
        self.label_12 = QtWidgets.QLabel(self.delete_2)
        self.label_12.setGeometry(QtCore.QRect(110, 60, 47, 13))
        self.label_12.setObjectName("label_12")
        self.delA = QtWidgets.QPushButton(self.delete_2)
        self.delA.setGeometry(QtCore.QRect(150, 90, 75, 23))
        self.delA.setObjectName("delA")
        self.label_13 = QtWidgets.QLabel(self.delete_2)
        self.label_13.setGeometry(QtCore.QRect(150, 10, 181, 21))
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.delete_2)
        self.label_15.setGeometry(QtCore.QRect(150, 150, 181, 21))
        self.label_15.setObjectName("label_15")
        self.idcdel = QtWidgets.QLineEdit(self.delete_2)
        self.idcdel.setGeometry(QtCore.QRect(150, 200, 113, 20))
        self.idcdel.setObjectName("idcdel")
        self.delC = QtWidgets.QPushButton(self.delete_2)
        self.delC.setGeometry(QtCore.QRect(150, 230, 75, 23))
        self.delC.setObjectName("delC")
        self.label_16 = QtWidgets.QLabel(self.delete_2)
        self.label_16.setGeometry(QtCore.QRect(110, 200, 47, 13))
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.delete_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCadastrar = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/130manstudent2_100617.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadastrar.setIcon(icon1)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionEmail = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/icons8-mensagem-preenchida-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEmail.setIcon(icon2)
        self.actionEmail.setObjectName("actionEmail")
        self.actionRegistrar = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/icons8-sacar-dinheiro-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegistrar.setIcon(icon3)
        self.actionRegistrar.setObjectName("actionRegistrar")
        self.actionPesquisar = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/systemsearch_104123.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPesquisar.setIcon(icon4)
        self.actionPesquisar.setObjectName("actionPesquisar")
        self.actionExcluir = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/dustbin_120823.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExcluir.setIcon(icon5)
        self.actionExcluir.setObjectName("actionExcluir")
        self.actionCursos = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/icons8-livros-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCursos.setIcon(icon6)
        self.actionCursos.setObjectName("actionCursos")
        self.menumenu.addAction(self.actionCadastrar)
        self.menumenu.addAction(self.actionCursos)
        self.menumenu.addAction(self.actionEmail)
        self.menumenu.addAction(self.actionRegistrar)
        self.menumenu.addAction(self.actionPesquisar)
        self.menumenu.addAction(self.actionExcluir)
        self.menubar.addAction(self.menumenu.menuAction())
        self.toolBar.addAction(self.actionCadastrar)
        self.toolBar.addAction(self.actionCursos)
        self.toolBar.addAction(self.actionEmail)
        self.toolBar.addAction(self.actionRegistrar)
        self.toolBar.addAction(self.actionPesquisar)
        self.toolBar.addAction(self.actionExcluir)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.course_name)
        MainWindow.setTabOrder(self.course_name, self.workload)
        MainWindow.setTabOrder(self.workload, self.mounths)
        MainWindow.setTabOrder(self.mounths, self.registerc)
        MainWindow.setTabOrder(self.registerc, self.updatec)
        MainWindow.setTabOrder(self.updatec, self.id_alunop)
        MainWindow.setTabOrder(self.id_alunop, self.pushButtonPay)
        MainWindow.setTabOrder(self.pushButtonPay, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.list_course)
        MainWindow.setTabOrder(self.list_course, self.idadel)
        MainWindow.setTabOrder(self.idadel, self.delA)
        MainWindow.setTabOrder(self.delA, self.idcdel)
        MainWindow.setTabOrder(self.idcdel, self.delC)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rapsodia"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CADASTRAR/ATUALIZAR ALUNO</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Nome:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Email:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Vencimento:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Telefone:"))
        self.pushButton.setText(_translate("MainWindow", "CADASTRAR"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Curso:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">id:</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "ATUALIZAR"))
        self.label_22.setText(_translate("MainWindow", "Atenção: os campos \'vencimento\' e \'curso\' nao serão modificados ao atualizar registros."))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">id:</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CADASTRAR/ATUALIZAR CURSO</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Meses:</p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Carga Horária:</span></p></body></html>"))
        self.updatec.setText(_translate("MainWindow", "ATUALIZAR"))
        self.registerc.setText(_translate("MainWindow", "CADASTRAR"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nome:</p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "Mensalidade:"))
        self.label_7.setText(_translate("MainWindow", "Esta funcionalidade ainda será implementada"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">REGISTRAR PAGAMENTOS</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"> id do aluno:</p></body></html>"))
        self.pushButtonPay.setText(_translate("MainWindow", "Registrar"))
        self.label_18.setText(_translate("MainWindow", "parcela:"))
        self.label_11.setText(_translate("MainWindow", "pesquisar por:"))
        self.pushButton_4.setText(_translate("MainWindow", "Pesquisar"))
        self.pushButton_5.setText(_translate("MainWindow", "listar atrasados"))
        self.list_course.setText(_translate("MainWindow", "listar cursos"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">id:</p></body></html>"))
        self.delA.setText(_translate("MainWindow", "Deletar"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">EXCLUIR ALUNO</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">EXCLUIR CURSO</span></p></body></html>"))
        self.delC.setText(_translate("MainWindow", "Deletar"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">id:</p></body></html>"))
        self.menumenu.setTitle(_translate("MainWindow", "Menu"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.actionCadastrar.setToolTip(_translate("MainWindow", "Cadastrar alunos no sistema"))
        self.actionEmail.setText(_translate("MainWindow", "Email"))
        self.actionEmail.setIconText(_translate("MainWindow", "Email"))
        self.actionEmail.setToolTip(_translate("MainWindow", "Email de alunos"))
        self.actionRegistrar.setText(_translate("MainWindow", "Registrar "))
        self.actionRegistrar.setIconText(_translate("MainWindow", "Registrar "))
        self.actionRegistrar.setToolTip(_translate("MainWindow", "Registrar pagamentos"))
        self.actionPesquisar.setText(_translate("MainWindow", "Pesquisar"))
        self.actionPesquisar.setToolTip(_translate("MainWindow", "Pesquisar"))
        self.actionExcluir.setText(_translate("MainWindow", "Excluir"))
        self.actionCursos.setText(_translate("MainWindow", "Cursos"))

