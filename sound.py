import sounddevice as sd
import scipy.io.wavfile as wav
from customtkinter import *
import threading

window = CTk()
window.title('Караоке')
window.geometry('500x300')
window.configure(bg_color='black')

def record_sound():
    global fs,seconds,start_btn
    start_btn.configure(state='disabled',text='Запис розпочато...')
    data = sd.rec(int(seconds*fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    start_btn.configure(state='normal',text='Розпочати запис')
    wav.write('record.wav', fs, data)


title_label = CTkLabel(window, text='Караоке', font=('Arial', 24), text_color='white', bg_color='black')
title_label.pack(pady=20)
start_btn = CTkButton(window, text='Розпочати запис', font=('Arial', 16), command=lambda: threading.Thread(target=record_sound, daemon=True).start(), width=200, height=50)
start_btn.pack(pady=10)

fs = 44100  
seconds = 5

window.mainloop()
