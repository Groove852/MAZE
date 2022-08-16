import RPi.GPIO as GPIO
import time
import random


class Buzzer:
    def __init__(self, pin):
        self.BuzzerPin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BuzzerPin, GPIO.OUT) 
        GPIO.setwarnings(False)
 
        self.command = ''

        self.Buzz = GPIO.PWM(self.BuzzerPin, 440)  

        self.tmp = [31,33,35,37,39,41,44,46,49,52,55,58,62,65,69,73,78,82,87,93,98,104,110,117,123,131,139,147,156,165,175,185,196,208,220,233,247,262,277,294,311,330,349,370,392,415,440,466,494,523,554,587,622,659,698,740,784,831,880,932,988,1047,1109,1175,1245,1319,1397,1480,1568,1661,1760,1865,1976,2093,2217,2349,2489,2637,2794,2960,3136,3322,3520,3729,3951,4186,4435, 4699, 4978]
        self.tones = {  'C0':16,
                        'C#0':17,
                        'D0':18,
                        'D#0':19,
                        'E0':21,
                        'F0':22,
                        'F#0':23,
                        'G0':24,
                        'G#0':26,
                        'A0':28,
                        'A#0':29,
                        'B0':31,
                        'C1':33,
                        'C#1':35,
                        'D1':37,
                        'D#1':39,
                        'E1':41,
                        'F1':44,
                        'F#1':46,
                        'G1':49,
                        'G#1':52,
                        'A1':55,
                        'A#1':58,
                        'B1':62,
                        'C2':65,
                        'C#2':69,
                        'D2':73,
                        'D#2':78,
                        'E2':82,
                        'F2':87,
                        'F#2':92,
                        'G2':98,
                        'G#2':104,
                        'A2':110,
                        'A#2':117,
                        'B2':123,
                        'C3':131,
                        'C#3':139,
                        'D3':147,
                        'D#3':156,
                        'E3':165,
                        'F3':175,
                        'F#3':185,
                        'G3':196,
                        'G#3':208,
                        'A3':220,
                        'A#3':233,
                        'B3':247,
                        'C4':262,
                        'C#4':277,
                        'D4':294,
                        'D#4':311,
                        'E4':330,
                        'F4':349,
                        'F#4':370,
                        'G4':392,
                        'G#4':415,
                        'A4':440,
                        'A#4':466,
                        'B4':494,
                        'C5':523,
                        'C#5':554,
                        'D5':587,
                        'D#5':622,
                        'E5':659,
                        'F5':698,
                        'F#5':740,
                        'G5':784,
                        'G#5':831,
                        'A5':880,
                        'A#5':932,
                        'B5':988,
                        'C6':1047,
                        'C#6':1109,
                        'D6':1175,
                        'D#6':1245,
                        'E6':1319,
                        'F6':1397,
                        'F#6':1480,
                        'G6':1568,
                        'G#6':1661,
                        'A6':1760,
                        'A#6':1865,
                        'B6':1976,
                        'C7':2093,
                        'C#7':2217,
                        'D7':2349,
                        'D#7':2489,
                        'E7':2637,
                        'F7':2794,
                        'F#7':2960,
                        'G7':3136,
                        'G#7':3322,
                        'A7':3520,
                        'A#7':3729,
                        'B7':3951,
                        'C8':4186,
                        'C#8':4435,
                        'D8':4699,
                        'D#8':4978,
                        'E8':5274,
                        'F8':5588,
                        'F#8':5920,
                        'G8':6272,
                        'G#8':6645,
                        'A8':7040,
                        'A#8':7459,
                        'B8':7902,
                        'C9':8372,
                        'C#9':8870,
                        'D9':9397,
                        'D#9':9956,
                        'E9':10548,
                        'F9':11175,
                        'F#9':11840,
                        'G9':12544,
                        'G#9':13290,
                        'A9':14080,
                        'A#9':14917,
                        'B9':15804}
        self.start = ['D5', 'F5', 'A#4']
        self.allarm = ['F5', 'A7', 'F6']
        self.death = ['E4', 'D4', 'C4', 'B3']
        self.waiting = 'E4'

    def play_waiting(self):
        self.Buzz.start(50)
        self.Buzz.ChangeFrequency(self.tones[self.waiting])
        time.sleep(0.15)
        self.Buzz.ChangeFrequency(1)
        time.sleep(0.2)
        self.Buzz.stop()
    
    def play_start(self):
        self.Buzz.start(50)
        for i in self.start:
            self.Buzz.ChangeFrequency(self.tones[i])
            time.sleep(0.1)  
        self.Buzz.stop()
            
    def play_death(self):
        self.Buzz.start(50)
        for i in self.death:
            self.Buzz.ChangeFrequency(self.tones[i])
            time.sleep(0.1)
        self.Buzz.stop()

    def play_allarm(self):
        self.Buzz.start(50)
        for i in self.allarm:
            self.Buzz.ChangeFrequency(self.tones[i])
            time.sleep(0.15)
            self.Buzz.ChangeFrequency(1)
            time.sleep(0.2)
        self.Buzz.stop()

