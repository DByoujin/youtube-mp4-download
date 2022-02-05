# 이 파일은 실행할 수 없는 파일입니다. 참고용도로 사용해주십시오.

# 1. youtube-dl를 사용
# 1-1. 최고의 화질과 최고의 오디오로 다운로드 (4K, 8K, HDR 지원)
youtube-dl -f "bestvideo+bestaudio" --merge-output-format mkv https://youtu.be/mv8lvQFGQS8
# youtube-dl -f "최고의화질+최고의오디오" --merge-output-format 확장자 유튜브링크

# 1-2. FHD 및 최고의 오디오로 다운로드
youtube-dl -f "bestvideo[height=<1080]+bestaudio" --merge-output-format mkv https://youtu.be/mv8lvQFGQS8
# youtube-dl -f "FHD+최고의오디오" --merge-output-format 확장자 유튜브링크

# 2.yt_dlp를 사용
yt-dlp -f "bestvideo+bestaudio" --merge-output-format mkv https://youtu.be/mv8lvQFGQS8

# youtube-dl를 사용시 일부 기기에서 속도가 느리게 나올 수 있습니다.
# 그럴땐, yt_dlp를 사용하십시오.
# yt_dlp는 다음 명령어로 설치할 수 있습니다.
# pip install yt-dlp