# 252RCOSE4440

이 저장소는 여러 과제(assignment)로 구성된 프로젝트입니다.

## 프로젝트 구조

```
.
├── assignment2/          # Flask 백엔드/프론트엔드 메시지 관리 시스템
│   ├── backend/         # Flask REST API 서버
│   ├── frontend/        # Flask 웹 프론트엔드
│   ├── data/            # 메시지 데이터 저장소
│   └── venv/            # Python 가상환경
├── assignment3/         # AWS Lambda 리뷰 처리 시스템
│   ├── lambda_function/ # AWS Lambda 함수
│   ├── request_generator.py  # 리뷰 요청 생성기
│   └── venv/           # Python 가상환경
└── README.md
```

## Assignment 2: Flask 메시지 관리 시스템

Flask를 사용한 백엔드 API와 프론트엔드 웹 애플리케이션으로 구성된 메시지 관리 시스템입니다.

### 구조
- **backend**: REST API 서버 (포트 5001)
  - `/api/message` (GET): 메시지 조회
  - `/api/message` (POST): 메시지 업데이트
  - `/api/health` (GET): 헬스 체크
- **frontend**: 웹 인터페이스 (포트 5000)
  - 메시지 조회 및 업데이트 기능

### 실행 방법

#### Docker를 사용한 실행

```bash
# Backend 빌드 및 실행
cd assignment2/backend
docker build -t backend .
docker run -d -p 5001:5001 -v $(pwd)/../data:/data backend

# Frontend 빌드 및 실행
cd assignment2/frontend
docker build -t frontend .
docker run -d -p 5000:5000 --link backend frontend
```

#### 로컬 실행

```bash
# 가상환경 활성화
cd assignment2
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate    # Windows

# Backend 실행
cd backend
python app.py

# Frontend 실행 (새 터미널)
cd frontend
python app.py
```

브라우저에서 `http://localhost:5000`으로 접속하여 웹 인터페이스를 사용할 수 있습니다.

## Assignment 3: AWS Lambda 리뷰 처리 시스템

AWS Lambda를 사용하여 리뷰를 처리하고 감정 분석을 수행하는 서버리스 애플리케이션입니다.

### 구조
- **lambda_function**: AWS Lambda 함수
  - 리뷰 수신 및 처리
  - TextBlob를 사용한 감정 분석
  - DynamoDB에 결과 저장
  - 긍정적인 리뷰에 대한 이메일 알림 전송
- **request_generator.py**: 리뷰 요청 생성기
  - 다양한 감정의 리뷰를 생성하여 API에 전송

### 실행 방법

#### Lambda 함수 배포

```bash
cd assignment3/lambda_function
docker build -t lambda-function .
# AWS ECR에 푸시하거나 Lambda에 직접 배포
```

#### 리뷰 생성기 실행

```bash
# 가상환경 활성화
cd assignment3
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate     # Windows

# 환경 변수 설정
export API_URL="your-lambda-api-url"

# 리뷰 생성기 실행
python request_generator.py
```

### 환경 변수

- `API_URL`: Lambda 함수의 API Gateway 엔드포인트 URL

## 기술 스택

### Assignment 2
- **Backend**: Flask 3.1.2, Python 3.11
- **Frontend**: Flask 3.1.2, Jinja2, Requests
- **Containerization**: Docker

### Assignment 3
- **Lambda Function**: Python 3.11, TextBlob, boto3
- **Request Generator**: aiohttp, Faker, python-dotenv
- **AWS Services**: Lambda, DynamoDB, SES

## 주의사항

- 각 assignment의 `venv/` 폴더는 Git에서 무시됩니다.
- AWS 자격 증명 파일(`.aws/`)은 Git에 커밋하지 마세요.
- 환경 변수 파일(`.env`)은 Git에 커밋하지 마세요.
