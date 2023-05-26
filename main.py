# 方式1：调用函数接口打开串口时传入配置参数
import time

import keyboard
import serial
import xlsxwriter as xw


def read_serial():
    data = ser.read()  # 读一个字
    return data


def send_hex(hex_str):
    ser.write(bytes.fromhex(hex_str))


def convert_byte_to_weight(byte_input):
    """
    这个函数接收一个字节串作为输入，然后返回反转的浮点数体重。

    :param byte_input: 字节串输入，格式例如：b'5.96000'
    :return: 浮点数体重，例如：69.5
    """
    # step 1: decode bytes to string
    str_input = byte_input.decode("utf-8")
    # step 2: reverse the string
    reversed_str = str_input[::-1]
    # step 3: trim leading zeros and trailing dot
    trimmed_str = reversed_str.lstrip('0')
    if trimmed_str[0] == '.':
        trimmed_str = trimmed_str[1:]
    # step 4: convert string to floata
    try:
        weight = float(trimmed_str)  # minght be ValueError
    except  ValueError:  # if ValueError, return 0.0
        weight = 0.0
    return weight


# keyboard control below
get_weight_mod = 0


def test_a():
    global get_weight_mod
    get_weight_mod = 1


def test_b():
    global get_weight_mod
    get_weight_mod = 2


def test_c():
    global get_weight_mod
    get_weight_mod = 3


def test_d():
    global get_weight_mod
    get_weight_mod = 4


ser = serial.Serial("COM10", 9600)  # 打开COM10，将波特率配置为115200，其余参数使用默认值
# the different weight type
gross_weight = 0.0
tare_weight = 0.0
# init the keyboard
keyboard.add_hotkey('a', test_a)
keyboard.add_hotkey('b', test_b)
keyboard.add_hotkey('s', test_c)
keyboard.add_hotkey('esc', test_d)

if __name__ == '__main__':
    line = 2  # start from line 2
    # init the excel
    system_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    system_time = system_time.replace(":", "_")
    system_time = system_time.replace(" ", "_")
    fileName = system_time + '_数据记录.xlsx'
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['序号', '毛重(kg）', '皮重(kg)', '净重(kg）']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    while True:
        A = read_serial()
        if A == b'=':
            weight = ser.read(7)
            weight_float = convert_byte_to_weight(weight)
            if float(weight_float) > 0.0:
                if get_weight_mod == 1:
                    tare_weight = weight_float
                    get_weight_mod = 0
                elif get_weight_mod == 2:
                    gross_weight = weight_float
                    get_weight_mod = 0
            print(weight_float,"毛重:", gross_weight, "kg 皮重:", tare_weight, "kg 净重:",gross_weight - tare_weight, "kg")
        if get_weight_mod == 3:
            data = [str(line - 1), gross_weight, tare_weight, gross_weight - tare_weight]  # data
            worksheet1.write_row('A' + str(line), data)  # start form A
            line += 1  # to the next line
            get_weight_mod = 0
        elif get_weight_mod == 4:
            break
            # print(weight, weight_float,"毛重：",gross_weight,"皮重：",tare_weight,"净重：",gross_weight-tare_weight,get_weight_mod)


    workbook.close()  # turn off the excel.it can save this excel

#absbsbsabbsbsabsbsabsbsbsabsbsbs