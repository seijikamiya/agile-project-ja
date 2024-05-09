import math

def add():
    """
    ユーザーに2つの数値を入力してもらい、その合計を算出する
    """
    num1 = float(input("加算する最初の数値を入力してください: "))
    num2 = float(input("加算する次の数値を入力してください: "))
    result = num1 + num2
    print(f"計算結果 : {num1} + {num2} = {result} ")

    return result

def subtract():
    """
    ユーザーに２つの数値を入力してもらい、それを減算する。
    """
    num1 = float(input("引かれる数値を入力してください: "))
    num2 = float(input("引く数値を入力してください: "))
    result = num1 - num2
    print(f"計算結果 : {num1} - {num2} = {result} ") 
    
    return result

def root():
    """
    ユーザーに値を入力してもらい、平方根を返す
    """
    num = float(input("平方根を求めたい数値を入力してください: "))
    result = math.sqrt(num)
    print(f"計算結果 : √{num} = {result} ") 

    return math.sqrt(num)

def multi():
    num1 = input("乗算される最初の数値を入力してください: ")
    num2 = input("乗算する次の数値を入力してください: ")
    if num1.isdecimal() and num2.isdecimal():
        result = float(num1) * float(num2)
        print(f"計算結果 : {num1} * {num2} = {result} ") 
        return result
    else:
        return "入力値が正しくありません"

def exp():
    num1 = input("指数計算したい底の数値を入力してください: ")
    num2 = input("指数計算したい指数の数値を入力してください: ")
    if num1.isdecimal() and num2.isdecimal():
        result = float(num1) ** float(num2)
        print(f"計算結果 : {num1} ^ {num2} = {result} ") 
        return result
    else:
        return "入力値が正しくありません"

# 途中テスト用
# num1 = input("please input first number: ")
# num2 = input("please input second number: ")
# print(multi(num1,num2))

def calculator():
    """
    計算機能を提供するプログラム
    """
    # 直前の計算結果を保持するための変数
    
    result = 0

    while True:
        print("計算メニュー：")
        print("1. add")
        print("2. sub")
        print("3. multi")
        print("4. div")
        print("5. exp")
        print("6. root")
        print("7. 直前の結果に対する演算")
        print("0. end")

        choice = input("計算項目を選択してください(0-7): ")

        if choice == "0":
            print("計算アプリを終了します。")
            break

        elif choice == "1" :
            result = add()
        
        elif choice == "2" :
            result = subtract()

        elif choice == "3" :
            result = multi()

        elif choice == "4" :
            num1 = float(input("除算する最初の数値を入力してください: "))
            num2 = float(input("除算する次の数値を入力してください: "))
            result = num1 / num2
            print(f"計算結果 : {num1} / {num2} = {result} ")

        elif choice == "5" :
            result = exp()

        elif choice == "6":
            result = root()

        else:
            print("無効な入力です。")

if __name__ == "__main__":
    calculator()