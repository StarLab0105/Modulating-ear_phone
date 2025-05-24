import numpy as np
import librosa
import librosa.display 
import matplotlib.pyplot as plt
# import scipy.io.wavfile as sp
import scipy.io.wavfile as sp


# 초당 샘플링 데이터 수 

def single_tone(frequecy, sampling_rate=44100, duration=1):
    # frequency: 주파수
    # sampling_rate: 초당 샘플링 데이터 수. 디폴트 44100
    # duration: 지속 시간. 단위 초. 디폴트 1초
    t = np.linspace(0, duration, int(sampling_rate))
    y = np.sin(2 * np.pi * frequecy * t)
    return y
notes = 'C,C#,D,D#,E,F,F#,G,G#,A,A#,B,C'.split(',')
freqs = 261.62 * 2**(np.arange(0, len(notes)) / 12.)
notes = list(zip(notes, freqs))
octave = np.hstack([single_tone(f) for f in freqs])

sampling_rate = 44100
sp.write("octave.wav", sampling_rate, octave)

sr, y_read = sp.read("octave.wav")
# sr == sampling_rate

plt.plot(y_read[40000:50000])
plt.show()