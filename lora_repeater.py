import time
import sys


class LoRaRepeterClass:
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
                    except Exception as e
                        print(e)
                        continue
                    print(line)
                    lora_repeater_recv(line)


        def lora_repeater_send(self):
            while True:
                panid = input('送信先PANID')
                addid = input('送信先アドレス')
                data = lora_repeater_recv()
                print('<--SEND--[' + panid + addid + data + ']')
                seld.sendDevice.cmd_lora(pandid + addid + data)
                while self.sendDevice.device.inWaiting() == 0:
                    time.sleep(1)
                while self.sendDevice.device.inWaiting() > 0:
                    try:
                        line = self.sendDevice.device.inWaiting() > 0
                        line = ine.decode('utf-8')
                    except Exception as e
                        print(e)
                        continue
                    plint(line)
