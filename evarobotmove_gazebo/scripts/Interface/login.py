#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import sys

from interface import Ui_MainWindow
from signup import Ui_Signup

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from motar_mini.msg import dprm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sqlite3
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(589, 373)
        Dialog.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(149, 79))
        self.label.setMaximumSize(QtCore.QSize(149, 79))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setMinimumSize(QtCore.QSize(94, 24))
        self.u_name_label.setMaximumSize(QtCore.QSize(94, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.horizontalLayout_2.addWidget(self.u_name_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setMinimumSize(QtCore.QSize(128, 24))
        self.uname_lineEdit.setMaximumSize(QtCore.QSize(128, 24))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.horizontalLayout_2.addWidget(self.uname_lineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setMinimumSize(QtCore.QSize(94, 24))
        self.pass_label.setMaximumSize(QtCore.QSize(94, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.horizontalLayout_4.addWidget(self.pass_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setMinimumSize(QtCore.QSize(128, 24))
        self.pass_lineEdit.setMaximumSize(QtCore.QSize(128, 24))
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.horizontalLayout_4.addWidget(self.pass_lineEdit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.splitter_3 = QtWidgets.QSplitter(Dialog)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.login_btn = QtWidgets.QPushButton(self.splitter_3)
        self.login_btn.setMinimumSize(QtCore.QSize(90, 28))
        self.login_btn.setMaximumSize(QtCore.QSize(90, 28))
        self.login_btn.setObjectName("login_btn")
        self.signup_btn = QtWidgets.QPushButton(self.splitter_3)
        self.signup_btn.setMinimumSize(QtCore.QSize(90, 28))
        self.signup_btn.setMaximumSize(QtCore.QSize(90, 28))
        self.signup_btn.setObjectName("signup_btn")
        self.horizontalLayout_3.addWidget(self.splitter_3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #Login and Signup
        self.login_btn.clicked.connect(lambda: self.Login_btn(0))
        self.signup_btn.clicked.connect(lambda: self.Login_btn(1))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login Form"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME "))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
    
    def warningBox(self,title,message):
        msg= QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    def Login_btn(self,x):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()
        if not username:
            self.warningBox("Warning",'Username Missing!')
        elif not password:
            self.warningBox("Warning",'Password Missing!')
        else:
            connection = sqlite3.connect("login.db")
            result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
            if(len(result.fetchall()) > 0):
                if x==0:
                    Dialog.close()
                    self.InterfaceShow()
                elif x==1:
                    self.signUpShow()
            else:
                self.warningBox('Warning','Invalid Username And/Or Password')
            connection.close()

    def InterfaceShow(self):
        self.Interface = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Interface)
        self.Interface.show()
        
    def signUpShow(self):
        self.signUpWindow=QtWidgets.QDialog()
        self.ui=Ui_Signup()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()

if __name__ == "__main__":
    rospy.init_node('motar_interface')
    velocity_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    point_pub = rospy.Publisher("motar_mini/dprm", dprm, queue_size=10)
    #odom_sub = rospy.Subscriber("odom",Odometry,odomsub)
    #velocity_sub =rospy.Subscriber('motar/point',Point, velocitysub)
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
