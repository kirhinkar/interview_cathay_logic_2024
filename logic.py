# -*- coding: UTF-8 -*-


def calculate_side_coordinates(middle_coordinate: int, height: int):
    """
    建立 generator 來計算每一行 * 符號的座標, 並逐次以 list 回傳
    """    
    for i in range(height):
        if i == height - 1:
            yield [i for i in range(middle_coordinate - i, middle_coordinate + i + 1, 2)]
        else:
            yield [middle_coordinate - i, middle_coordinate + i]


def draw_triangle(height: int) -> None:
    """
    輸入為數字，輸出則為*符號為輸入數字邊長的空心正三角形
    """
    if type(height) != int:
        raise Exception(f"Invalid 'height': '{height}'")
    
    base_length = (height - 1)*2 + 1  # 底邊長度
    middle_coordinate = height - 1  # 中心點位置
    
    star_coordinates_generator = calculate_side_coordinates(middle_coordinate, height)
    
    # 開始畫圖
    for star_coordinates in star_coordinates_generator:
        simble_line = ""
        for j in range(base_length):
            simble_line += "*" if j in star_coordinates else " "
        print(simble_line)


def odd_even_order(random_number: str) -> str:
    """
    重新排序亂數並按照規則:
        規則 1: 奇數都在偶數前面
        規則 2: 偶數升冪排序
        規則 3: 奇數降冪排序
    """
    print(f"Input: '{random_number}'")
    reordered_number = ""
    count_list = [0]*10

    # 因可預期所有數值都是 0~9 的整數, 直接採用計數排序法, 先統計每個整數出現的次數
    for digit_str in random_number:
        digit = int(digit_str)
        count_list[digit] += 1
    
    # 先將奇數依照降冪排列塞入字串
    for i in range(9, -1, -2):
        reordered_number += str(i) * count_list[i]
    
    # 再將偶數依照升冪排列塞入字串
    for i in range(0, 10, 2):
        reordered_number += str(i) * count_list[i]
    
    print(f"Output: '{reordered_number}'")
    return reordered_number


if __name__ == '__main__':

    print('Q1 ---')
    draw_triangle(3)

    print('\nQ2 ---')
    odd_even_order("417324689435")
    
