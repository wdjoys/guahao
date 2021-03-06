'''
Author: wdjoys
Date: 2022-04-23 10:24:55
LastEditors: wdjoys
LastEditTime: 2022-04-27 16:21:07
FilePath: \guahao\src\settings.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
'''


# 北京大学第一医院配置
cnfs_bjdxdyyy = {
    # 是否运行
    "active": True,
    'hospital_name': '北京大学第一医院',
    "interval": 30,
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63060012)"
    },
    "cookies": "acw_tc=0bca294a16509322284688174e0179f72b636982ad8c15853022df0a3cfb59; Wx_LinkingCloud=C4F7464B038C6A7CE813134FE0AF8B85FECED5A56B8E8891171434F6FBF0258643E02B80BC9CD6DF6EB5A47E1F3C8ACDAFDD4D04EC2D8296033F74A252EDA10498BA15FFE8B0CD76F52D5506C18D378C9E0C3A7FC663653A7F589A931F2D5B14DC800C3C01E38FBA1F0D4D8E54E89B8C9241412DD7B1746C98C7EE275B1B0F673A18038282C9BCB6F576107CB549D9AFFC6CBA19AEC63DCB0B99BBE7C2A2F333979B7FCC450B5B7F8EFB86363427697DF9E2585942CB3BFA45F55597C6E2AEF42E6825A92A463ACB6C866666D7F49EDAD7B80979B5B4E60182F874E6B808C99D85D2A41158288A559955EB897B34A345F77ADE3713EC245991AAE0EA2A95494CC65448E5EC869110C91D95FC74310386F7397EFE531CCB9CB36CE334ED849219C7B7767D5864EE21B3562C27A758F853D4018EADD38FAED9FF0A143FB80363ED95F8CC30B346C567A88B4B2742D37D98341D1A0C4F0327C01F51A06FC5E65FC8BC3FF9A9CC4775AE21C9A01EFDAE033DF143C15F9007D15A37C8B545E476884D1CE2BBBD48C7A5B18C74BD27C32335FE86AED8519B7594CC2255669FD371C6D8799B4DE6; FuWuChuang=8646C1420227FD17279D8B324F3193505FDAF94896A7184662C7458F6054EA098B4750CE8BF9D00D741C51300067F5D5E5D47DABCC8FE202102EF24B761E6C8C6AD8B90EA60FE93CA6959D087A3BF507A4F532A7D492AD6BB9582F2665F7015B90DBDD2083FC28E4EDAC3D7C3B5CE1B41867F0C44926AD5063DCDA3EC5CFEA1B10A35AE8; SERVERID=21f5842e1a126c92cac2739a52a0fffd|1650932259|1650932228",


    # User hospitalUserID
    "hospitalUserID": "o39LEjl67-mwAa3XdepJxgoQGTG8XS22427001260",
    # 要监控的医生号源
    "docCodes": [
        {'docName': "姜玉武",
         'docCode': 'BJDXDYYY_3_1_746', },
        {'docName': "吴烨",
         'docCode': 'BJDXDYYY_3_1_825', },
        {"docName": "王颖",
         "docCode": "BJDXDYYY_3_1_642", },
        {"docName": "孙国玉",
         "docCode": "BJDXDYYY_3_1_1241", },

    ]

}

ROBOTS = [
    {'ROBOT_PATH': 'hospital.bjdxdyyy',  # 机器人类路径
     'CNFS': 'cnfs_bjdxdyyy'}  # 机器人类配置文件
]


WECHAT_TOKEN = '39f568f9-1ddd-435d-bc2d-322b2597e350'
