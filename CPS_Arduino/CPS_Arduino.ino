/*
# 软件名称：CPS_Arduino_test（ChemistryPersonSoftware_arduino_test）
# 版本号：version.alpha.0.0.1
# 用途：原型验证，仅供内部测试
# 代码编写人：谢澍梵，程鹏，余宗仁
# 代码写述日期：2017年10月30日
# 代码编写环境：Arduino_IDE
# 代码测试环境：Arduino_UNO_R3
*/

//pin脚命名
const int led = 13;

//初始化函数
void setup() 
{
  //串口初始化设置
  Serial.begin(9600);

  //设置pin脚
  pinMode(led, OUTPUT);
}

//循环体
void loop() 
{
  //读取串口信息
  while(Serial.read()>= 0)
  {
    //如果串口收到消息的话，板载LED闪烁
    blink();
  }
}

//板载led灯闪烁
void blink()
{
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);                       // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(500);                       // wait for a second
}

