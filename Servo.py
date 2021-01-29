import RPi.GPIO as GPIO
## setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# 舵机参数
PIN_Servo_01 = 8
PIN_Servo_02 = 10
HZ_Servo = 50
GPIO.setup(PIN_Servo_01, GPIO.OUT)
GPIO.setup(PIN_Servo_02, GPIO.OUT)
## 08 一号舵机

def Servo_init(PIN_Servo):
    PWM_Servo = GPIO.PWM(PIN_Servo, HZ_Servo)
    PWM_Servo.start(0)
    PWM_Servo.ChangeDutyCycle(0)
    return PWM_Servo
# ## start up
def Servo_action(Servo, action):
    Servo.ChangeDutyCycle((action - 6) % 13)

def Servo_destroy(Servo):
    Servo.stop()

if __name__ == '__main__':
    Servo1 = Servo_init(PIN_Servo_01)
    Servo2 = Servo_init(PIN_Servo_02)
    for i in range(0,13):
        Servo_action(Servo1,i)
        Servo_action(Servo2,i)
    GPIO.cleanup()
    quit()