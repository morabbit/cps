# coding=utf-8

########################################################################################################################
# 软件名称：CPS（ChemistryPersonSoftware）
# 版本号：version.alpha.0.0.3
# 用途：原型验证，仅供内部测试
# 代码编写人：谢澍梵，余宗仁， 程鹏
# 代码写述日期：2018年1月7日
# 代码编写环境：pycharm 2017.2.3
# 代码测试环境：windows 10 企业版 2017（x64）
# 软件适用平台：
#   1.windows（windows7及以上版本）
#   2.Linux（推荐ubuntu 14.04 LTS及以上， Fedore22及以上）
#   3.Macintosh OS（MacOS X 10.6 Snow Leopard及以上）
# 本软件依赖环境：
#   1.python3（推荐python3.4及以上，必须64位版）；
#       下载地址：https://www.python.org/
#   2.pyQt5（推荐PyQt5-5.4-gpl-Py3.4-Qt5.4.0-x64及迭代分支版本，必须64位版）；
#       下载地址：https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.4/
# 本软件授权方式：商业软件著作权保护
########################################################################################################################


########################################################################################################################
# 本文件为全软件的启动入口，用于负责维护mian函数的调用，
# 启动方式为：当前文件路径下执行：python main.py
########################################################################################################################

import sys                                                                      # 引入系统关联包
from PyQt5.QtWidgets import *                                                   # 引入PyQt5窗口部件包
from UIModule import mainWindow                                                 # 引入主界面窗口
from CommunionModule.communication_handshake import CommunicationHandShake


# 主函数，本程序入口
def main():
    app = QApplication(sys.argv)        # 创建Qt事件循环机制

    if CommunicationHandShake.communication_hand_shake_with_arduino():
        pass
    else:
        QMessageBox.information(QWidget(), u"警告！", u"请接上Arduino设备")
        quit()

    main = mainWindow.MainWindow()      # 创建主窗口对象
    main.show()                         # 显示主窗口

    app.exec_()                         # 阻塞事件，执行消息循环监听，（没了这句，窗口一闪而过）


# 测试代码，调用主窗口
if __name__ == "__main__":
    main()
