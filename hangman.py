# http://tinyurl.com/j7rb8or

# 文字列を使ったゲーム、ハングマン

import random

def hangman(word):
    wrong = 0
    stages = [
        "",
        "__________          ",
        "|                   ",
        "|         |         ",
        "|         0         ",
        "|        /|\        ",
        "|        / \        ",
        "|                   "
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        char = input("1文字を予想してね : ")
        if len(char) != 1:
            continue
        if char in rletters:  # あってる！
            print("その文字は含まれています！")
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:                 # あってない…
            print("その文字は含まれていません！")
            wrong += 1
        print("あなたが当てるべき文字列(全%d文字)->「 " %len(word), end = "")
        print(" ".join(board), end="")
        print(" 」")
        e = wrong + 1
        print("\n".join(stages[0:e]))  # ハングマンの状態を表示(完成したら負け)
        if "_" not in board:           # 文字をすべて当てた！
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は %s.\n" %word)

words = ["cat", "dog", "python", "java", "windows",
"ibaraki", "tokyo", "linux"]
idx = random.randint(0, len(words) - 1)
hangman(words[idx])