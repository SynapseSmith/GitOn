# GitOn MCP

이 저장소는 GitOn 플랫폼용 MCP 서버 확장 도구 모음입니다.

## 구조

- `app/main.py`: 서버 실행 진입점
- `app/mcp_server.py`: FastMCP 서버 및 도구 등록
- `app/tools/`: GitOn API 연동 도구(사용자, 이슈, PR, 레이블 등)
- `app/utils/http_util.py`: GitOn API 호출 헬퍼

## 사용법

1. `.env`에 `giton_url`과 인증 토큰 설정
2. `python -m app.main` 실행
3. FastMCP 문서에 따라 도구 호출

## 주의

- 대형 데이터 파일은 GitHub 100MB 제한 때문에 저장소에 포함하지 않습니다.
- 필요시 Git LFS를 사용하세요.
