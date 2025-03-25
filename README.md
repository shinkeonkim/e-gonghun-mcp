# 독립유공자 공훈록 MCP 서버

국가보훈부 공훈전자사료관의 독립유공자 공훈록 및 공적조서를 조회할 수 있는 MCP(Model Context Protocol) 서버입니다.

<a href="https://glama.ai/mcp/servers/@shinkeonkim/e-gonghun-mcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@shinkeonkim/e-gonghun-mcp/badge" alt="독립유공자 공훈록 서버 MCP server" />
</a>

## 준비사항

시작하기 전에 다음 도구들이 필요합니다:
* macOS 또는 Windows
* Claude Desktop 최신 버전
* uv 0.4.18 이상 (`uv --version`로 확인)

### macOS 환경 설정

```bash
# Homebrew 사용
brew install uv

# 또는 직접 다운로드:
# uv: https://docs.astral.sh/uv/
```

### Windows 환경 설정

```powershell
# winget 사용
winget install --id=astral-sh.uv -e

# 또는 직접 다운로드:
# uv: https://docs.astral.sh/uv/
```

## 설치 방법

```bash
# 프로젝트 복제
git clone https://github.com/국가보훈부/e-gonghun-mcp.git
cd e-gonghun-mcp

# 패키지 설치
uv pip install -e .
```

## 환경 변수 설정

`.env.sample` 파일을 `.env`로 복사하고 필요한 설정을 작성합니다.

```bash
cp .env.sample .env
```

## Claude Desktop에서 사용 방법

Claude Desktop에서 이 도구를 사용하려면 다음 설정이 필요합니다:

### macOS 설정

1. 설정 파일 열기:

```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

2. 다음 설정 추가:

```json
{
  "mcpServers": {
    "e_gonghun_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/사용자이름/projects/e-gonghun-mcp",
        "run",
        "gonghun-mcp"
      ]
    }
  }
}
```

### Windows 설정

1. 설정 파일 열기:

```powershell
code $env:AppData\Claude\claude_desktop_config.json
```

2. 다음 설정 추가:

```json
{
  "mcpServers": {
    "e_gonghun_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\사용자이름\\projects\\e-gonghun-mcp",
        "run",
        "gonghun-mcp"
      ]
    }
  }
}
```

3. Claude Desktop를 재시작합니다.

## 기능

- 독립유공자 공훈록 목록 조회
- 독립유공자 공적조서 조회
- 훈격, 운동계열 등 코드 정보 제공

## API 사용법

Model Context Protocol을 통해 다음 도구를 사용할 수 있습니다:

1. `get_merit_list` - 독립유공자 공훈록 목록을 조회합니다
   - 이름, 생년월일, 훈격, 운동계열 등으로 검색 가능
2. `get_public_report` - 독립유공자 공적조서를 조회합니다
3. `get_hunkuk_codes` - 훈격 코드 정보를 조회합니다
4. `get_workout_affil_codes` - 운동계열 코드 정보를 조회합니다
5. `clear_cache` - 캐시된 데이터를 초기화합니다

## 사용 예시

Claude Desktop에서 다음과 같이 질문해보세요:

```
3.1운동을 이천에서 참여한 독립유공자 목록을 가져와줘
```

## 동작 원리

Model Context Protocol을 통한 Claude Desktop 상호작용은 다음과 같이 진행됩니다:
1. **서버 발견**: Claude Desktop은 시작 시 설정된 MCP 서버에 연결하고 각 서버의 기능을 확인합니다.
2. **프로토콜 핸드셰이크**: 적절한 MCP 서버를 선택하고 프로토콜을 통한 기능 협상 후 서버에 데이터나 작업을 요청합니다.
3. **모델 컨텍스트 확장**: MCP 서버는 Claude 모델에 추가 컨텍스트와 데이터를 제공하여 더 정확하고 상세한 응답을 생성할 수 있게 합니다.
4. **상호작용 흐름**: Claude Desktop에서 쿼리 요청을 수행하면 MCP 서버가 데이터를 처리하고 결과를 반환합니다.
5. **보안**: MCP 서버는 특정 기능만 제공하고 로컬에서만 실행되며 중요 작업은 사용자 확인이 필요합니다.

## 라이선스

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

이 리포지토리는 Anthropic의 Claude 3.7 Sonnet을 사용하여 작성되었습니다.