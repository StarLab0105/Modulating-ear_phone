# Modulating-ear_phone
## 만드는 이유
듣기싫은 상사의 목소리나 선생님의 목소리를 듣기 좋게 바꿔주어 업무환경을 개선하기위해서 만들것이다.

## 유의사항

사용시 [file = r"경로"] 에서 경로를 수정하여 주세요.\
*file = r"C:\Users\zzine\OneDrive\문서\카카오톡 받은 파일\만석로19번길.wav"*



```python
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
```python
magnitude = np.abs(fft) 

print(fft)
```
# Frequency 값 만들기
```python
f = np.linspace(0,sr,len(magnitude))
```

# 푸리에 변환을 통과한 specturm은 대칭구조로 나와서 high frequency 부분 절반을 날려고 앞쪽 절반만 사용한다.
```python
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
```

---
# Installation Guide

### matplotlib.pyplot 모듈

matplotlib.pyplot 모듈은 MATLAB과 유사한 명령어 스타일로 작동하는 함수 모음입니다. 이 모듈의 각 함수를 사용하면 그래프를 간편하게 생성하고 수정할 수 있습니다. 예를 들어, 그래프 영역을 만들고, 선을 추가하며, 레이블을 사용하여 그래프를 꾸밀 수 있습니다.

설치 방법 (터미널 또는 cmd):
```
pip install matplotlib
```
### librosa 라이브러리

librosa는 음악 및 오디오 신호 처리를 위한 Python 라이브러리입니다. 이 라이브러리는 음악 분석, 오디오 신호 변환 및 다양한 오디오 처리 작업을 위한 기능을 제공합니다.
또한 머신 러닝 및 딥 러닝 모델에서 음악 분석 및 처리에 널리 사용되며, 음악 정보 검색, 음악 생성, 음악 추천 시스템 등 다양한 분야에 응용됩니다.

설치 방법 (터미널 또는 cmd):
```
pip install librosa
```
### NumPy 라이브러리

NumPy(Numerical Python)는 Python에서 고성능 수치 계산을 위한 핵심 라이브러리입니다. 벡터 및 행렬 연산을 포함한 다양한 수학적 기능을 빠르고 간편하게 사용할 수 있도록 지원합니다.

설치 방법 (터미널 또는 cmd):
```
pip install numpy
```
