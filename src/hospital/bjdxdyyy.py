'''
Author: wdjoys
Date: 2022-04-23 00:13:41
LastEditors: wdjoys
LastEditTime: 2022-04-23 13:17:27
FilePath: \guahao\src\hospital\bjdxdyyy.py
Description:

Copyright (c) 2022 by github/wdjoys, All Rights Reserved.
'''


from requests import Session


class Robot():
    def __init__(self, cnfs):
        self.session = Session()
        self.session.headers.update(cnfs['headers'])
        cookies_dict = {cookie.split("=")[0]: cookie.split(
            "=")[1] for cookie in cnfs['cookies'].split("; ")}
        self.session.cookies.update(cookies_dict)
        self.docCodes = cnfs['docCodes']

    def get_hospital_resource(self):
        #
        for docCode in self.docCodes:
            #
            url = f'https://fwcbj.linkingcloud.cn/App/dist/index.html#/guahao/doctor?docCode={docCode}'
            # 访问挂号页面
            # self.session.get(url)

            # 请求医生号源API
            url = 'https://fwcbj.linkingcloud.cn/GuaHao/OrderDocNoSources'
            res = self.session.post(url, data={"docCode": docCode['docCode']})
            OrderDocNoSources = res.json()

            # print(docCode['docName'], "====="*10)

            for docResourceResource in OrderDocNoSources['docResourceResourceList']:
                resourceMemo = docResourceResource['resourceMemo']
                amount = docResourceResource['amount']
                day = docResourceResource['day']
                registLevel1 = docResourceResource['registLevel1']
                timeEnd = docResourceResource['timeEnd']

                time = f'{day} {timeEnd}'

                enable = False if resourceMemo in "已满停止预约" else True

                yield {
                    # 格式必选
                    "time": time,
                    "enable": enable,
                    "docName": docCode['docName'],
                    "other_information": {
                        "registLevel": registLevel1,
                        "amount": amount,
                        "resourceMemo": resourceMemo
                    }
                }

    def resource_analyse(self, resource):
        if resource['enable']:
            print(resource['time'], resource['docName'], resource['other_information']['registLevel'],
                  resource['other_information']['amount'], resource['other_information']['resourceMemo'])


if __name__ == '__main__':
    bjdxdyyy = {
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63060012)"
        },
        "cookies": "acw_tc=0bca30f216506403191788042e016bad98aaebdcad124ca4231e73dc087111; Wx_LinkingCloud=490E19AD69251BF681884891C0D6C2B50F3D8D02112135673DE8C7620A566A166CFB88CE02FC558B4F72F172EFEAD419F6513916DD9D91C147F7CA10453ABAA788D32DDCA40B42C3421579471A4133B3B6FD9E39DB3C2054FE65CD710B84DCA41369457C1849E84A657259707BD1F57EAC2F2CB0D1DD6812E51E064EB1525651DDC9E7AB0E8302D38FA6C4240DC17AFEA77C761D76705CF1C100194C053A8861FA5455CF791226E3D60A0ABFBC1B1C1814E932BEA299D01B37F1827E42B2BF1D7978ADE747B383355ED32362F00494853B1ADDFD61DD8F3FCF661D5A3517BC01761B691A453A316F04C03EB8E8F38B14E0973FFAA78FE0E0617FFB564CB512C02C9CB42AD4F2F2EF2877B45A98FED0306817552E8D5C263B9028230DA2F2A336AD32C081A791F9344D966529CD2F4262ACB9B474A496043D2D724A8EA96C0031F3FCCA424CD2DE6E7C2DCCB2B731FF7101981BDE50FF2CD708D0B6CDFC3F73814607715A40841E1A52006B35F3FBC85FF07D62EE62AC5512479249BF0BE08AF6BF17693C343AF5A9716B418E4940D0CB5445539A33396389CE0F340E0509DFA50A3B8DB9; FuWuChuang=184B37F1409F1D8F11329FCD008B0C222679F0CDBE9AD57B786C419614515C3B15BB82A54491C17E065BBDECF663E23AD8EE3DBB1E21222C970CBBEFEA28253B4C2373D4A4154C6B579846FF62598FD862FDD7CCE6553C42F7660C2A334D7A3037738EA71919419C150AEF006E73C4DA8818A1E532B21A65FA413409EA1D9E1F7DE39595; SERVERID=0e312ef9d7f59da5ab24bbf87ae38d9d|1650641325|1650640319",
        "docCodes": [
            {'docName': "姜玉武",
             'docCode': 'BJDXDYYY_3_1_746', },
            {'docName': "吴烨",
             'docCode': 'BJDXDYYY_3_1_825', }

        ]

    }

    robot = Robot(bjdxdyyy["headers"],
                  bjdxdyyy["cookies"], bjdxdyyy["docCodes"])
    robot.get_hospital_resource()