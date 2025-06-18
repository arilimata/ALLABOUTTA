import sys
import dat_parser
import txt_parser
# import dji_drone_parser
import dji_drone_parser_v2
import dji_drone_parser_v3
import userinfo_parser


if __name__ == '__main__':
    print(sys.argv)
    argv_length = len(sys.argv)
    if argv_length != 2:
        print("缺少参数...")
    elif sys.argv[1] == "-a": # 同时解析dat，txt，mmkv
        print("开始解析用户信息...")
        userinfo_parser.ParseUserInfos()
        print("开始解析DATS...")
        dat_parser.ParseDats()
        print("开始解析txtS...")
        txt_parser.ParseTxts()
    elif sys.argv[1] == "-d":# 只解析dat 
        print("开始解析DATS...")
        dat_parser.ParseDats()
    elif sys.argv[1] == "-x":# 只解析datv2
        print("开始解析DATSv2...")
        dji_drone_parser_v2.TesDRDP()
    elif sys.argv[1] == "-z":# 只解析datv3
        print("开始解析DATSv3...")
        dji_drone_parser_v3.TesDRDP()
    elif sys.argv[1] == "-t":# 只解析txt    
        print("开始解析txtS...")
        txt_parser.ParseTxts()
    elif sys.argv[1] == "-u":# 只解析mmkv文件
        print("开始解析用户信息...")
        userinfo_parser.ParseUserInfos()