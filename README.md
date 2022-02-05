# Youtube mp4 다운로드
## 1. 설명
여기서는 파이썬과 youtube-dl (또는 yt-dlp)를 이용하여 유튜브 영상을 다운받습니다.

## 2. 세팅
[파이썬](https://www.python.org/)을 설치후, 터미널 (cmd)에서 다음과 같은 명령어를 입력합니다.
```
pip install youtube-dl
```
각 상황에 따라 해당 명령어로 입력해야 할 수 있습니다.
```
pip install yt-dlp
```
[FFmpeg](https://www.ffmpeg.org/)를 다운받고, 세팅합니다.<br>
FFmpeg는 각 운영체제에 따라 세팅방법이 다르니 [리눅스는 이곳](https://jjeongil.tistory.com/1430)을, [윈도우는 이곳](https://m.blog.naver.com/chandong83/222095346417)을 클릭하여 참고하도록 합니다.

## 3. 사용방법
### 3-1. youtube-dl
youtube-dl를 이용하여 다운받습니다.<br>
컴퓨터에서 터미널 (cmd)를 열고 다음 명령어를 입력합니다.
> 아래 소스코드는 예시입니다.
```
youtube-dl -f "bestvideo+bestaudio" --merge-output-format mkv https://youtu.be/mv8lvQFGQS8
```
> 위 소스코드는 최고의 화질과 최고의 오디오로 다운받습니다. <br>
> MKV 부분에 mp4 등 확장자를 변경할 수 있습니다.
> 아래 소스코드는 예시입니다.
```
youtube-dl -f "bestvideo[height=<1080]+bestaudio" --merge-output-format mkv https://youtu.be/mv8lvQFGQS8
```
> 위 소스코드는 FHD 화질과 최고의 오디오로 다운받습니다.<br>
> MKV 부분에 mp4 등 확장자를 변경할 수 있습니다.

### 3-2. yt-dlp
yt-dlp는 youtube-dl를 이용시 속도가 낮게 나올시 대체하여 사용합니다.
> 아래 소스코드는 예시입니다.
```
yt-dlp -f "bestvideo+bestaudio" --merge-output-format mkv https://youtu.be/mv8lvQFGQS8
```
> 기존 소스코드 앞부분, youtube-dl 부분을 yt-dlp로 변경하여 사용합니다.

* ```위 내용은 기본적인 내용을 다룹니다. 본인 또는 웹사이트에 따라 소스코드를 수정해야 할 수 있습니다. 본인에 맞게 수정하여 사용하십시오.```
