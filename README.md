# Modulating-ear_phone
## 만드는 이유
듣기싫은 상사의 목소리나 선생님의 목소리를 듣기 좋게 바꿔주어 업무환경을 개선하기위해서 만들것이다.

사용시 [file = r"경로"] 에서 경로를 수정하여 주세요.



```
import numpy as np
import librosa
import librosa.display 
import matplotlib.pyplot as plt

FIG_SIZE = (15, 10)
file = r"C:\Users\zzine\OneDrive\문서\카카오톡 받은 파일\만석로19번길.wav"
sig, sr = librosa.load(file, sr=22050)

print(sig, sig.shape)

fft = np.fft.fft(sig)
```

# 복소공간 값 절댓갑 취해서, magnitude 구하기
magnitude = np.abs(fft) 

print(fft)
# Frequency 값 만들기
f = np.linspace(0,sr,len(magnitude))

# 푸리에 변환을 통과한 specturm은 대칭구조로 나와서 high frequency 부분 절반을 날려고 앞쪽 절반만 사용한다.
left_spectrum = magnitude[:int(len(magnitude)/2)]
left_f = f[:int(len(magnitude)/2)]

plt.figure(figsize=FIG_SIZE)
plt.plot(left_f, left_spectrum)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power spectrum")
plt.show()



plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(y=sig, sr=sr, alpha=0.5)  # 인자명을 명시적으로 지정
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform")
plt.tight_layout()
plt.show()


---
# Installation Guide
