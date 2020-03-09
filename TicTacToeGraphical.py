import tkinter as tk
from TicTacToeGame import TicTacToeGame

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("500x500")

game = TicTacToeGame()

text_frame = tk.Frame(root, width=500, height=100)
text_frame.pack(side="top")

player_info_text = tk.StringVar()
player_info_text.set("Player to move: " + str(game.player_turn))
player_info = tk.Label(text_frame, textvariable=player_info_text, font=('arial', 30), height=2)
player_info.pack()

buttons_frame = tk.Frame(root, width=300, height=300, bg="yellow")
buttons_frame.pack()


def btn_click(btn_text, number):
    game_ended, made_move, result, player_turn, player_sign = game.make_move_graphical(number)

    if game_ended != 1:
        if made_move:
            btn_text.set(player_sign)
            game.change_player()
            player_info_text.set("Player to move: " + str(game.player_turn))
    else:
        btn_text.set(player_sign)
        for button in btn_list:
            button.config(state='disabled')
        player_info_text.set(result)


btn_list = []

btn1_text = tk.StringVar()
btn1 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn1_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn1_text, 1))
btn1.grid(row=0, column=0)

btn2_text = tk.StringVar()
btn2 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn2_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn2_text, 2))
btn2.grid(row=0, column=1)

btn3_text = tk.StringVar()
btn3 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn3_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn3_text, 3))
btn3.grid(row=0, column=2)

btn4_text = tk.StringVar()
btn4 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn4_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn4_text, 4))
btn4.grid(row=1, column=0)

btn5_text = tk.StringVar()
btn5 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn5_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn5_text, 5))
btn5.grid(row=1, column=1)

btn6_text = tk.StringVar()
btn6 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn6_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn6_text, 6))
btn6.grid(row=1, column=2)

btn7_text = tk.StringVar()
btn7 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn7_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn7_text, 7))
btn7.grid(row=2, column=0)

btn8_text = tk.StringVar()
btn8 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn8_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn8_text, 8))
btn8.grid(row=2, column=1)

btn9_text = tk.StringVar()
btn9 = tk.Button(buttons_frame, padx=2, pady=2, bd=4, width=3, textvariable=btn9_text, font=('arial', 30),
                 bg="lightgrey", command=lambda: btn_click(btn9_text, 9))
btn9.grid(row=2, column=2)

btn_list.append(btn1)
btn_list.append(btn2)
btn_list.append(btn3)
btn_list.append(btn4)
btn_list.append(btn5)
btn_list.append(btn6)
btn_list.append(btn7)
btn_list.append(btn8)
btn_list.append(btn9)


root.mainloop()
