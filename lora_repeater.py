import time
import sys


class LoraRepeaterClass:
    """
        LoRa中継器用クラス
    """

    def __init__(self, serial_device, set_flag, config):
        self.sendDevice = serial_device
        self.set_flag = set_flag
        self.config = config
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
        if self.set_flag == 'on':
            command = ['b', 'c', 'd', 'e', 'f', 'g']
            for cmd, conf in zip(command, self.config):
                self.sendDevice.cmd_lora(cmd)
                time.sleep(0.1)
                self.sendDevice.cmd_lora(conf)
                time.sleep(0.1)
        else:
            self.sendDevice.cmd_lora('d')
            time.sleep(0.1)
            self.sendDevice.cmd_lora('14')
            time.sleep(0.1)
            self.sendDevice.cmd_lora('g')
            time.sleep(0.1)
            self.sendDevice.cmd_lora('0001')
            time.sleep(0.1)
        self.sendDevice.cmd_lora('y')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('z')

     #ES920LRデータ中継器-受信メソッド
    def lora_repeater_recv(self):
        while True:
            if self.sendDevice.device.inWaiting() > 0:
                try:
                    line = self.sendDevice.device.readline()
                    line = line.decode('utf-8')
                except Exception as e:
                    print(e)
                    continue
                print(line)
                self.sendDevice.cmd_lora(line.encode('utf-8'))
                time.sleep(4)
                if self.sendDevice.device.inWaiting() > 0:
                    try:
                        line_sd = self.sendDevice.device.readline()
                        line_sd = line.decode('utf-8')
                        print("----SEND----[" + line_sd + "]")
                    except Exception as e:
                        print(e)
                        continue
                #while self.sendDevice.device.inWaiting() == 0:
                #    time.sleep(1)

                #def lora_repeater_send():
                    #while True:
                        #panid = input('送信先PANID')
                        #addid = input('送信先アドレス')
                        #data = self.sendDevice.device.inWating() > 0
