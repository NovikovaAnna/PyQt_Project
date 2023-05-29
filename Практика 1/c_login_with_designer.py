from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(351, 200)
        LoginForm.setMinimumSize(QSize(350, 200))
        LoginForm.setMaximumSize(QSize(351, 200))
        self.verticalLayout = QVBoxLayout(LoginForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labeleLogin = QLabel(LoginForm)
        self.labeleLogin.setObjectName(u"labeleLogin")
        self.labeleLogin.setMinimumSize(QSize(45, 0))

        self.horizontalLayout_2.addWidget(self.labeleLogin)

        self.lineEditLogin = QLineEdit(LoginForm)
        self.lineEditLogin.setObjectName(u"lineEditLogin")

        self.horizontalLayout_2.addWidget(self.lineEditLogin)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelPassword = QLabel(LoginForm)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setMinimumSize(QSize(45, 0))

        self.horizontalLayout_3.addWidget(self.labelPassword)

        self.lineEditPassword = QLineEdit(LoginForm)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_3.addWidget(self.lineEditPassword)



        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButtonRegistration = QPushButton(LoginForm)
        self.pushButtonRegistration.setObjectName(u"pushButtonRegistration")

        self.horizontalLayout_4.addWidget(self.pushButtonRegistration)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pushButtonOk = QPushButton(LoginForm)
        self.pushButtonOk.setObjectName(u"pushButtonOk")

        self.horizontalLayout_5.addWidget(self.pushButtonOk)

        self.pushButtonCancel = QPushButton(LoginForm)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout_5.addWidget(self.pushButtonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"\u041e\u043a\u043d\u043e \u0432\u0445\u043e\u0434\u0430", None))
        self.labeleLogin.setText(QCoreApplication.translate("LoginForm", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEditLogin.setPlaceholderText(QCoreApplication.translate("LoginForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.labelPassword.setText(QCoreApplication.translate("LoginForm", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("LoginForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButtonRegistration.setText(QCoreApplication.translate("LoginForm", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButtonOk.setText(QCoreApplication.translate("LoginForm", u"\u041e\u043a", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("LoginForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi