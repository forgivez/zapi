# ⚡ Zapi - Lightning-fast API Tester

Zapi는 간단한 HTTP 요청 테스트 도구입니다.  
PyQt 기반 GUI로 멀티탭, JSON 트리 응답 뷰, 저장/불러오기 기능까지 제공하여 빠르게 API를 테스트할 수 있습니다.

---

## ✅ 주요 기능

- 📡 GET / POST / PUT / DELETE 요청 전송
- 🧾 헤더 및 바디 JSON 입력 지원
- 🗂️ 요청 정보 저장 및 불러오기 (`*.req.json`)
- 🌳 JSON 응답 TreeView 시각화
- 🗂️ 탭 기반 다중 요청 테스트
- 🖼️ 스플래시 로딩 화면 및 커스텀 아이콘

---

## 🚀 실행 방법

### 1. Python 개발 환경에서 실행
```bash
pip install -r requirements.txt
python app.py
```
---
### 2. Windows 실행파일(.exe)로 실행
빌드된 dist/Zapi.exe 파일을 직접 실행하면 됩니다.
아이콘 및 로딩화면 포함 상태로 실행됩니다.
---
### 3. 🧑‍💻 사용법
- URL 입력
- 요청 방식 선택 (GET/POST 등)
- 헤더/바디 JSON 입력
- ✅ [통신 보내기] 버튼 클릭
- 📥 응답은 JSON Tree 형태로 아래에 표시됨
- 💾 요청은 저장하여 추후 재사용 가능
- TIP: [예시 보기] 버튼을 누르면 요청 방식에 맞는 예제가 자동 채워집니다.
---
### 4. 프로젝트 구조
## 📁 프로젝트 구조

```text
Zapi/
├── app.py                          # 메인 실행 파일
├── request_tab.py                  # 요청 탭 UI 로직
├── utils.py                        # 저장/불러오기, 예시 요청 유틸
├── requirements.txt                # 실행에 필요한 Python 패키지
├── .gitignore                      # Git 제외 파일 목록
├── build_zapi.bat                  # .exe 빌드 자동화 스크립트
├── README.md                       # 프로젝트 설명 문서
├── icon/                           # 아이콘 및 스플래시 리소스
│   ├── zapi_icon.ico               # 앱 및 실행파일 아이콘
│   └── splash_dark_small.png       # 실행 시 로딩 스플래시 이미지
├── dist/                           # 빌드 결과 폴더
│   └── Zapi.exe                    # 빌드된 실행 파일 (생성됨)
└── build/                          # PyInstaller 임시 폴더 (자동 생성됨)
```

### 4. 빌드방법(Windows용)
- 자동화된 .bat 빌드 스크립트 사용 : build_zapi.bat을 이용
- 직접 명령어로 빌드할 경우 :
```bash
pyinstaller app.py --noconsole --onefile --name Zapi ^
 --icon=icon\zapi_icon.ico ^
 --add-data "icon\zapi_icon.ico;icon" ^
 --add-data "icon\splash_dark_small.png;icon"
```

