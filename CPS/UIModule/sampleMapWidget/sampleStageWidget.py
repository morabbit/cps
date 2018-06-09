# coding=utf8
from math import pi, cos, sin

import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


# 绘制样品转盘类
class sampleStageWidget(QWidget):
    def __init__(self, parent=None):
        # 调用父类初始化
        super(sampleStageWidget, self).__init__(parent)

        # 本类对象属性变量初始化
        self._angle = 0.0                                            # 旋转角度（弧度制）
        self._sample_stage_number = 8                                # 样品台数量
        self._sample_stage_position = []                             # 样品台位置布局
        self._sample_stage_color_normal = QColor(0, 0, 255)          # 样品台颜色（普通状态）
        self._sample_stage_color_selected = QColor(255, 0, 0)        # 样品台颜色（选中状态）

        # 初始化样品台的坐标
        self.set_sample_stage_postion()

    # 重载界面重绘事件，当界面大小发生改变的时候，就会重新绘制圆
    def paintEvent(self, e):
        self._sample_stage_position = []
        self.set_sample_stage_postion()
        painter = QPainter()
        painter.begin(self)
        self.drawEllipse(painter)
        painter.end()

    # 画样品台
    def drawEllipse(self, painter):
        painter.setBrush(self._sample_stage_color_normal)           # 准备笔刷颜色
        radius = min(self.width(), self.height()) / 25.0            # 设置样品半径

        for position in self._sample_stage_position:
            position_x = position[0] - radius / 2
            position_y = position[1] - radius / 2
            painter.drawEllipse(position_x, position_y, radius, radius)

    # 计算样品台位置
    def set_sample_stage_postion(self):
        # 设置布局参数
        sample_stage_angle_step = pi * 2 / self._sample_stage_number        # 样品间距角度（弧度制）
        sample_stage_radius = min(self.width(), self.height()) * 0.2        # 样品分布半径

        # 将布局列表放入内存中
        for step in range(self._sample_stage_number):
            self._sample_stage_position.append([sample_stage_angle_step * step, sample_stage_radius])

        # 首先使用极坐标进行布局（旋转功能）
        self._sample_stage_position = list(map(self.rotate_polar_coordinates, self._sample_stage_position))

        # 将极坐标转换为笛卡尔坐标
        self._sample_stage_position = list(map(self.translate_polar_to_descartes_coordinates, self._sample_stage_position))

        # 平移坐标
        self._sample_stage_position = list(map(self.translation_descartes_coordinates, self._sample_stage_position))

    # 旋转布局
    def rotate_polar_coordinates(self, coodinates_list):
        # 极坐标参数
        angle = coodinates_list[0] + self._angle          # 极坐标角度（弧度制）
        radius = coodinates_list[1]                       # 极坐标半径

        # 返回值
        return [angle, radius]

    # 将极坐标转换为笛卡尔坐标
    def translate_polar_to_descartes_coordinates(self, coodinates_list):
        # 极坐标参数
        angle = coodinates_list[0]      # 极坐标角度（弧度制）
        radius = coodinates_list[1]     # 极坐标半径

        # 转换
        x = radius * cos(angle)
        y = radius * sin(angle)

        # 返回值
        return [x, y]

    # 平移坐标
    def translation_descartes_coordinates(self, coodinates_list):
        # 计算平移量
        x_offset = self.width() / 2
        y_offset = self.height() / 2

        # 平移
        x_position = coodinates_list[0] + x_offset
        y_position = coodinates_list[1] + y_offset

        # 返回值
        return [x_position, y_position]


def main():
    app = QApplication(sys.argv)
    mainWindow = sampleStageWidget()
    mainWindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
