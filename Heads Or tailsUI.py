import random
import time
import sys
import winsound
import  tkinter as tk
from tkinter import ttk

consectuive_heads = 0
total_attempts = 0
Coinsides = ["HEADS","TAILS"]
buttonpress = False
heads_count = 0
tails_count = 0
best_streak = 0
win_count = 0
consectuive_tails = 0


def color_text(text, r, g, b):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def play_win_sound():
    winsound.PlaySound("CorrectSound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def play_fail_sound():
    winsound.PlaySound("MetalPipeSound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def CoinFlipSound():
    winsound.PlaySound("CoinFlipSound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def update_stats():
    total = heads_count + tails_count
    # Calculate percentage (preventing a 0 division error)
    win_pct = (heads_count / total * 100) if total > 0 else 0
    win_pct2 = (tails_count / total * 100) if total > 0 else 0

    total_lbl.config(text=f"Total Clicks: {total}")
    heads_lbl.config(text=f"Heads: {heads_count}")
    tails_lbl.config(text=f"Tails: {tails_count}")
    percent_lbl.config(text=f"Heads Rate: {win_pct:.1f}%")
    percent_lbl2.config(text=f"Tails Rate: {win_pct2:.1f}%")
    best_lbl.config(text=f"Best Streak: {best_streak}")
    best_lbl.config(text=f"Best Streak: {best_streak}")
    Wincount_lbl.config(text=f"Total Wins: {win_count}")
    

def ButtonClick():
    global consectuive_heads, total_attempts,heads_count,tails_count,best_streak,win_count,IconHeads,IconSide,IconTails,consectuive_tails
    CoinFlipSound()
    text.tag_config("green_text", foreground="green")
    text.tag_config("red_text", foreground="red")
    text.tag_config("win_text", foreground="orange")

    try:
        CoinFlip = random.choice(Coinsides)
        total_attempts += 1
        CoinFlipSound()

        root.iconphoto(False, IconSide)
        # We start with just the text string
        display_line = f"{CoinFlip} | Streak: {consectuive_heads} | Attempts: {total_attempts}\n"

        if CoinFlip == "HEADS":
            CoinFlipSound()
            consectuive_heads += 1
            consectuive_tails = 0
            heads_count += 1
            display_line = f"{CoinFlip} | Streak: {consectuive_heads} | Attempts: {total_attempts}\n"
            play_win_sound()
            text.insert("end", display_line, "green_text")

            if consectuive_heads > best_streak:
                best_streak = consectuive_heads
            final_icon = IconHeads if CoinFlip == "HEADS" else IconTails
            root.after(100, lambda: root.iconphoto(False, final_icon))

        else:
            CoinFlipSound()
            consectuive_heads = 0
            consectuive_tails += 1
            play_fail_sound()
            # Insert with the 'red_text' tag
            text.insert("end", display_line, "red_text")
            tails_count += 1

        text.see("end")


        if consectuive_heads == 10:
            winner_msg = f"\n🏆 WINNER! 🏆\n10-roll streak in {total_attempts} tries!\n"
            text.insert("end", winner_msg, "win_text")
            win_count += 1

        if consectuive_tails == 10:
            loser_msg = f"\n 🤣 LOSER 🤣 \n 10 tails in a row loser!\n"
            text.insert("end", loser_msg, "win_text")
            win_count -= 1



        update_stats()
    except Exception as e:
        print(f"An error occurred: {e}")

root = tk.Tk()
root.title("CoinFlip")
root.geometry("800x400")
root.configure(bg="#1e1e1e")
IconHeads = tk.PhotoImage(file="Coinheads.png")
IconSide = tk.PhotoImage(file="Coinside.png")
IconTails = tk.PhotoImage(file="Cointails.png")
try:
    IconHeads = tk.PhotoImage(file="Coinheads.png")
    root.iconphoto(False, IconHeads)
except Exception:
    pass

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


frame = tk.Frame(root,bg="black")
frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


frame.columnconfigure(0, weight=1) 
frame.rowconfigure(0, weight=0)
frame.rowconfigure(1, weight=0)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=0)

Get10HEADS = tk.Text(frame,bg="black",fg="yellow",height=1, borderwidth=0)
Get10HEADS.tag_configure("center", justify='center')
Get10HEADS.grid(row=0, column=0,sticky="ew") 
Get10HEADS.insert("1.0", "🏆GET 10 HEADS IN A ROW TO WIN🏆")
Get10HEADS.tag_add("center", "1.0", "end")
Get10HEADS.config(state="disabled")


entrybtn = tk.Button(frame, text="FLIP COIN", command=ButtonClick,bg="black",fg="white",height=2)
entrybtn.grid(row=1, column=0, pady=(0, 10), ipady=20, sticky="ew") 

text_frame = tk.Frame(frame)
text_frame.grid(row=2, column=0, sticky="nsew")
text_frame.columnconfigure(0, weight=1)
text_frame.rowconfigure(0, weight=1)

text = tk.Text(text_frame, height=15, width=50, 
               font=("Consolas", 12),
               bg="black", 
               fg="white", 
               insertbackground="white")
text.grid(row=0, column=0, sticky="nsew")


scrollbar = ttk.Scrollbar(text_frame, command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
text['yscrollcommand'] = scrollbar.set


def ClearHistory():
    text.config(state="normal")
    text.delete("1.0", "end")

clear_btn = tk.Button(frame, text="Clear History", command=ClearHistory,bg="black",fg="white")
clear_btn.grid(row=3, column=0, pady=(10, 0), sticky="e")

stats_frame = tk.LabelFrame(root, text=" Statistics ",bg="black",fg="white")
stats_frame.grid(row=0, column=1, sticky="ns", padx=10, pady=10)

heads_lbl = ttk.Label(stats_frame, text="Heads: 0")
heads_lbl.pack(anchor="w", padx=10, pady=10)

tails_lbl = ttk.Label(stats_frame, text="Tails: 0")
tails_lbl.pack(anchor="w", padx=10, pady=10)

total_lbl = ttk.Label(stats_frame, text=f"Total Clicks: 0")
total_lbl.pack(anchor="w", padx=10, pady=10)

Wincount_lbl = ttk.Label(stats_frame, text=f"Total Wins: 0")
Wincount_lbl.pack(anchor="w", padx=10, pady=10)

percent_lbl = ttk.Label(stats_frame, text="Heads Rate: 0%")
percent_lbl.pack(anchor="w", padx=10, pady=10)

percent_lbl2 = ttk.Label(stats_frame, text="Tails Rate: 0%")
percent_lbl2.pack(anchor="w", padx=10, pady=10)



best_lbl = ttk.Label(stats_frame, text="Best Streak: 0")
best_lbl.pack(anchor="w", padx=10, pady=30)

root.mainloop()