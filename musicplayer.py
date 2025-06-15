import tkinter as tk
from tkinter import filedialog
import pygame


pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("300x200")
        self.filename = None

        self.open_btn = tk.Button(root, text="Open", command=self.open_file)
        self.open_btn.pack(pady=10)

        self.play_btn = tk.Button(root, text="Play", command=self.play_music)
        self.play_btn.pack(pady=10)

        self.pause_btn = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_btn.pack(pady=10)

        self.stop_btn = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_btn.pack(pady=10)

        self.paused = False

    def open_file(self):
        self.filename = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if self.filename:
            pygame.mixer.music.load(self.filename)

    def play_music(self):
        if self.filename:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused = False

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
