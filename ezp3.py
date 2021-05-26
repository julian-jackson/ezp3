import os, pygame, tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory

pygame.init()
pygame.mixer.init()

window = tk.Tk()
window.title("ezp3")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

class Pause(object):
    def __init__(self):
        self.paused = pygame.mixer.music.get_busy()

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
        if not self.paused:
            pygame.mixer.music.pause()
        self.paused = not self.paused

def play():
	pygame.mixer.music.load(play_list.get(tk.ACTIVE))
	current_song.set(play_list.get(tk.ACTIVE))
	pygame.mixer.music.play()
	
def stop():
	pygame.mixer.music.stop()

pause = Pause()
current_song = tk.StringVar() 

play_list = tk.Listbox(window, font="Helvetica 12 bold", bg="dark gray", selectmode=tk.SINGLE)
for item in song_list:
	pos = 0
	play_list.insert(pos, item)
	pos += 1

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
playbar = tk.Frame(window, bd=2)
playbarwide = tk.Frame(window, bd=2)

btn_play = tk.Button(playbar, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="gray", fg="white")
btn_music = tk.Button(fr_buttons, text="Music")
btn_settings = tk.Button(fr_buttons, text="Settings")
btn_pause = tk.Button(playbarwide, width=5, height=3, font="Helvetica 12 bold", text="||", command=pause.toggle, bg="gray", fg="white")
btn_rewind = tk.Button(playbarwide, width=5, height=3, font="Helvetica 12 bold", text="<l", command=pause.toggle, bg="gray", fg="white")
btn_forward = tk.Button(playbarwide, width=5, height=3, font="Helvetica 12 bold", text="l>", command=pause.toggle, bg="gray", fg="white")

btn_play.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_music.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_settings.grid(row=1, column=0, sticky="ew", padx=5)
btn_rewind.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
btn_pause.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
btn_forward.grid(row=2, column=3, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
play_list.grid(row=0, column=1, sticky="nsew")
playbar.grid(row=1, column=0, sticky="ns")
playbarwide.grid(row=1, column=1, sticky="ns")

window.mainloop()
