import numpy as np


def file2array(filename = '3d.txt', sp = 4):
    A = np.zeros((128, sp), dtype=float)  # 先创建一个 3x3的全零方阵A，并且数据的类型设置为float浮点型
    f = open(filename)  # 打开数据文件文件
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中

    A_row = 0  # 表示矩阵的行，从0行开始

    for line in lines:  # 把lines中的数据逐行读取出来
        if filename == '3d.txt':
            list = line.strip('\n').split('\t')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
        elif filename == 'image.txt':
            list = line.strip('\n').split(' ')
        else:
            return
        A[A_row, :] = list[0:sp]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
        A_row += 1  # 然后方阵A的下一行接着读

    return  A[1:,1:]
