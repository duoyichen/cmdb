#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import urllib.request
import urllib.parse

import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)
from conf import settings


def update_test(data):
    """
    创建测试用例
    :return:
    """
    # 将数据打包到一个字典内，并转换为json格式
    data = {"asset_data": json.dumps(data)}
    # 根据settings中的配置，构造url
    url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
    print('正在将数据发送至： [%s]  ......' % url)
    try:
        # 使用Python内置的urllib.request库，发送post请求。
        # 需要先将数据进行封装，并转换成bytes类型
        data_encode = urllib.parse.urlencode(data).encode()
        response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
        print("\033[31;1m发送完毕！\033[0m ")
        message = response.read().decode()
        print("返回结果：%s" % message)
    except Exception as e:
        message = "发送失败"
        print("\033[31;1m发送失败，%s\033[0m" % e)


if __name__ == '__main__':
    windows_data = {
        "os_type": "Windows",
        "os_release": "10 64bit  10.0.17134",
        "os_distribution": "Microsoft",
        "asset_type": "server",
        "cpu_count": 2,
        "cpu_model": "Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz",
        "cpu_core_count": 8,
        "manufacturer": "Hasee Computer",
        "model": "CW65S",
        "wake_up_type": 6,
        "sn": "00330-80000-00000-AA515",
        "ram": [
            {
                "slot": "A1",
                "capacity": 8,
                "model": "Physical Memory",
                "manufacturer": "kingstone ",
                "sn": "456"
            },

        ],
        "physical_disk_driver": [
            {
                "iface_type": "unknown",
                "slot": 0,
                "sn": "3830414130423230343234362020202020202020",
                "model": "KINGSTON SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 128
            },
            {
                "iface_type": "SATA",
                "slot": 1,
                "sn": "383041413042323023234362020102020202020",
                "model": "KINGSTON SV100S264G ATA Device",
                "manufacturer": "(标准磁盘驱动器)",
                "capacity": 2048
            },

        ],
        "nic": [
            {
                "mac": "14:CF:22:FF:48:34",
                "model": "[00000011] Realtek RTL8192CU Wireless LAN 802.11n USB 2.0 Network Adapter",
                "name": 11,
                "ip_address": "10.1.1.11",
                "net_mask": [
                    "255.255.255.0",
                    "64"
                ]
            },
            {
                "mac": "14:CF:22:FF:48:35",
                "model": "Intel Adapter",
                "name": 17,
                "ip_address": "192.168.1.110",
                "net_mask": ""
            },


        ]
    }


    linux_data = {
        "asset_type": "server",
        "manufacturer": "Dell",
        "sn": "66330-80000-00000-AA515",
        "model": "R730xd",
        "uuid": "E8DE611C-4279-495C-9B58-502B6FCED076",
        "wake_up_type": "Power Switch",
        "os_distribution": "Ubuntu",
        "os_release": "Ubuntu 16.04.3 LTS",
        "os_type": "Linux",
        "cpu_count": "2",
        "cpu_core_count": "12",
        "cpu_model": "Intel @ Xeon @ E5-2690 v3 CPU @ 2.60GHz",
        "ram": [
            {
                "slot": "A1",
                "capacity": 32,
            },
            {
                "slot": "B1",
                "capacity": 32,
            }
        ],
        "ram_size": 63.858997344970703,
        "nic": [
            {
                "mac": "66:CF:22:FF:48:35",
                "model": "Intel Adapter",
                "name": 57,
                "ip_address": "10.1.1.11",
                "net_mask": [
                    "255.255.255.0",
                    "24",
                ]
            },
        ],
        "physical_disk_driver": [
            {
                "model": "SSD",
                "size": "500",
                "sn": "SSD-0500-09085302"
            }
        ],
        "physical_disk_driver": [
            {
                "model": "SAS",
                "size": "8192",
                "sn": "SSD-8192-09085302"
            }
        ],
    }

    update_test(linux_data)
    update_test(windows_data)