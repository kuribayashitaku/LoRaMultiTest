 # -*- coding: utf-8 -*-
import time
import sys


class LoraRecvClass:
    """
        LoRa受信用クラス
    """

    def __init__(self, serial_device, set_flag, config):
        self.sendDevice = serial_device
        self.set_flag = set_flag
        self.config = config
        self.sendDevice.reset_lora()
        time.sleep(0.5)
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('a')
        time.sleep(0.1)
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
        self.sendDevice.cmd_lora('p')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('1')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('y')
        time.sleep(0.1)
        self.sendDevice.cmd_lora('z')

    """ES920LRデータ受信メソッド"""
    def lora_recv(self):
        while True:
            if self.sendDevice.device.inWaiting() > 0:
                try:
                    line = self.sendDevice.device.readline()
                    line = line.decode('utf-8')
                except Exception as e:
                    print(e)
                    continue
                print(line)
                if line.find("RSSI") >= 0:
                    log = line
                    with open('log_recv.csv', 'a') as f:
                        f.write(log)
                time.sleep(0.5)
                if line.find('Ack Timeout') >= 0:
                    continue
                if line.find('exit') >= 0:
                    sys.exit()
