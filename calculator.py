import math

def add():
    """
    ユーザーに2つの数値を入力してもらい、その合計を算出する
    """
    num1 = input("加算する最初の数値を入力してください: ")
    num2 = input("加算する次の数値を入力してください: ")
    if is_numeric(num1) and is_numeric(num2):
        result = float(num1) + float(num2)
        print(f"計算結果 : {num1} + {num2} = {result} ")
        return result
    else:
        print("入力値が正しくありません")

def subtract():
    """
    ユーザーに２つの数値を入力してもらい、それを減算する。
    """
    num1 = input("引かれる数値を入力してください: ")
    num2 = input("引く数値を入力してください: ")
    if is_numeric(num1) and is_numeric(num2):
        result = float(num1) - float(num2)
        print(f"計算結果 : {num1} - {num2} = {result} ")
        return result
    else:
        print("入力値が正しくありません")

def root():
    """
    ユーザーに値を入力してもらい、平方根を返す
    """
    num = input("平方根を求めたい数値を入力してください: ")
    if not is_numeric(num):
        print("入力値が正しくありません")
    elif float(num) < 0:
        print("入力値が正しくありません。正の値を入力して下さい")
    else:
        result = math.sqrt(float(num))
        print(f"計算結果 : √{num} = {result} ") 
        return result

def multi():
    """
    ユーザーに値を入力してもらい、乗算を返す
    """
    num1 = input("乗算される最初の数値を入力してください: ")
    num2 = input("乗算する次の数値を入力してください: ")
    if is_numeric(num1) and is_numeric(num2):
        result = round((float(num1) * float(num2)),5)
        print(f"計算結果 : {num1} * {num2} = {result} ") 
        return result
    else:
        print("入力値が正しくありません")
        
def div():
    """
    ユーザーに値を入力してもらい、除算を返す
    """

    num1 = input("除算する最初の数値を入力してください: ")
    num2 = input("除算する次の数値を入力してください: ")
    if is_numeric(num1) and is_numeric(num2):
        if float(num2) == 0:
            print("0で割ることはできません")
        else:
            result = float(num1) / float(num2)
            print(f"計算結果 : {num1} / {num2} = {result} ")
            return result
    else:
        print("入力値が正しくありません")

def exp():
    """
    ユーザーに値を入力してもらい、指数計算を返す
    """
    num1 = input("指数計算したい底の数値を入力してください: ")
    num2 = input("指数計算したい指数の数値を入力してください: ")
    if is_numeric(num1) and is_numeric(num2):
        result = float(num1) ** float(num2)
        print(f"計算結果 : {num1} ^ {num2} = {result} ") 
        return result
    else:
        print("入力値が正しくありません")

def calculate_twice(result):
    """
    ユーザーに処理したい演算と値を入力してもらい、直前の演算結果に対する演算結果を返す（演算は、加算・減算・乗算・除算の中から選択）
    """
    sub_choice = input("演算項目を選択してください(1-4): ")
    pre_result = result
    if sub_choice in ["1", "2", "3", "4"]:
        num = input("演算を行う数値を入力してください: ")
        if is_numeric(num):
            if sub_choice == "1":
                result += float(num)
            elif sub_choice == "2":
                result -= float(num)
            elif sub_choice == "3":
                result *= float(num)
            elif sub_choice == "4":
                result /= float(num)
            print(f"計算結果 : 直前の結果 {pre_result} に対する演算 {sub_choice} を行った結果 = {result}")
            return result
        else:
            print("入力値が正しくありません")
    else:
        print("入力値が正しくありません")
    
def is_numeric(s):
    """文字列が数値かを判定する関数

    Args:
        s (str): 判定する文字列

    Returns:
        文字列が数値の場合はTrue, それ以外の場合はFalse
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculator():
    """
    計算機能を提供するプログラム
    """
    # 直前の計算結果を保持するための変数
    
    result = None

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
            result = div()
            
        elif choice == "5" :
            result = exp()

        elif choice == "6":
            result = root()
        
        elif choice == "7":
            if result != None:
                result = calculate_twice(result)
            else:
                print("直前の結果が存在しません")

        else:
            print("無効な入力です。")

if __name__ == "__main__":
    calculator()