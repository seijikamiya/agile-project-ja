def add():
    """
    ユーザーに2つの数値を入力してもらい、その合計を算出する
    """
    num1 = float(input("加算する最初の数値を入力してください: "))
    num2 = float(input("加算する次の数値を入力してください: "))
    result = num1 + num2
    print(f"計算結果 : {num1} + {num2} = {result} ")

    return result

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

        elif choice == "1":
            result = add()

        elif   choice == "4" :
            num1 = float(input("除算する最初の数値を入力してください: "))
            num2 = float(input("除算する次の数値を入力してください: "))
            result = num1 / num2
            print(f"計算結果 : {num1} / {num2} = {result} ") 

        else:
            print("無効な入力です。")

if __name__ == "__main__":
    calculator()