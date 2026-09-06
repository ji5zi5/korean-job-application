# 한국어 자기소개서 작성·첨삭 스킬

제공한 경험과 사실을 바탕으로 한국어 자기소개서를 작성하고 다듬는 AI 에이전트용 스킬입니다. 경험이 충분하면 바로 초안을 쓰고, 중요한 정보가 빠졌을 때만 질문합니다.

핵심은 `SKILL.md`와 연결된 참고 자료입니다. Codex에서 사용·검증했으며, Claude Code와 Claude의 커스텀 스킬 형식에도 맞는 구조입니다. 다만 Claude에서의 설치·실행과 모델 간 동일한 결과 품질은 아직 검증하지 않았습니다.

## 할 수 있는 일

- 경험 정리와 문항에 맞는 소재 선택
- 채용 공고·복합 문항 분석, 요청한 기업 조사
- 완성 초안과 대안 작성, 진단·부분 첨삭·전체 수정
- 본인 말투를 살린 문장 정리와 분량 조절
- 여러 문항의 소재 배치, 기업별 맞춤, 요청한 MD/TXT 파일·경험 요약 출력

## 설치

설치 대상은 저장소 안의 [`skills/korean-job-application`](skills/korean-job-application) 폴더 전체입니다. `SKILL.md`뿐 아니라 `references/`와 `scripts/`도 함께 유지하세요. 같은 이름의 스킬이 이미 있다면 덮어쓰기 전에 기존 내용을 확인하세요.

### Codex

Codex에서 다음과 같이 요청하세요.

```text
$skill-installer https://github.com/ji5zi5/korean-job-application/tree/main/skills/korean-job-application
```

설치 후 `$korean-job-application`으로 호출합니다. 새 스킬이 목록에 나타나지 않으면 Codex를 재시작하세요. [공식 OpenAI 설치 안내](https://learn.chatgpt.com/docs/build-skills)

### Claude Code

저장소를 내려받은 뒤 `skills/korean-job-application` 폴더를 개인 스킬 경로인 `~/.claude/skills/` 아래에 복사하세요. 최종 진입점은 `~/.claude/skills/korean-job-application/SKILL.md`입니다. 특정 프로젝트에서만 쓰려면 프로젝트의 `.claude/skills/` 아래에 넣으세요.

```text
/korean-job-application
아래 공고와 내 경험으로 지원동기 초안을 작성해줘.
```

새 스킬이 보이지 않으면 Claude Code를 재시작하세요. [Claude Code 공식 설치·호출 안내](https://code.claude.com/docs/en/skills)

### Claude 웹·데스크톱 앱

먼저 개인 계정은 **Settings → Capabilities**에서 **Code execution and file creation**을 켜세요. 조직 계정은 관리자 설정에서 코드 실행·스킬·사용자 생성이 허용되어야 합니다. 이후 다음 순서로 등록합니다.

1. 저장소를 내려받고 `skills/korean-job-application` 폴더를 ZIP으로 압축합니다. 저장소 전체 ZIP을 그대로 올리지 마세요.
2. **Customize → Skills → + → Create skill → Upload a skill**에서 ZIP을 업로드합니다.
3. 등록한 스킬을 활성화하고, 대화에서 “한국어 자기소개서 스킬을 사용해 아래 경험으로 초안을 작성해줘”처럼 요청합니다.

압축 파일을 열었을 때 구조는 다음과 같아야 합니다.

```text
korean-job-application.zip
└── korean-job-application/
    ├── SKILL.md
    ├── references/
    ├── scripts/
    └── …
```

메뉴와 이용 가능 여부는 계정·조직 설정에 따라 달라질 수 있습니다. [Claude 스킬 사용 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [ZIP 구성 안내](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

### 다른 AI 도구

Agent Skills 형식을 지원하는 도구라면 해당 도구의 설치 규칙에 맞춰 같은 폴더를 사용할 수 있는지 확인하세요. 개별 도구의 호환성은 검증하지 않았습니다. 스킬을 지원하지 않는 일반 챗봇에 지침을 붙여넣는 것만으로 참고 자료의 자동 로딩이나 스크립트 실행까지 동일하게 제공되지는 않습니다.

`agents/openai.yaml`은 Codex용 표시·호출 메타데이터이며, 공통 작성 지침은 `SKILL.md`와 `references/`에 있습니다. 검색·파일 저장·글자 수 계산은 각 환경의 도구와 권한에 영향을 받습니다.

## 사용 예시

위 방법으로 스킬을 호출하거나 활성화한 뒤, 다음 요청을 함께 입력하세요.

```text
아래 공고와 내 경험으로 지원동기 초안을 작성해줘.
문항은 “이 직무에 지원한 이유와 준비 과정을 설명하시오”, 공백 포함 700자 이내야.

[공고와 실제 경험 붙여넣기]
```

```text
이 자소서는 아직 고치지 말고, 문항에 답하지 못한 부분만 진단해줘.
```

```text
둘째 문단만 내 말투로 다듬어줘. 사실과 수치는 바꾸지 말고 수정 본문만 보여줘.
```

문항, 분량, 지원 직무, 본인이 한 행동과 확인된 결과를 함께 주면 도움이 됩니다. 숫자 성과가 없어도 산출물이나 실제 피드백을 활용할 수 있습니다.

## 구성

| 자료 | 내용 |
| --- | --- |
| 일반 작법 | 근거와 적용 한계를 정리한 9개 원칙 |
| 공개 사례 분석 | 6개 직무군의 공개 지원서 30편 |
| 문항별 작법 | 지원동기·협업·실패 등 12종 |
| 문제 처방 | 근거·기여·인과·가독성 등을 다루는 36개 카드 |
| 완결 예시 | 독립적으로 만든 합성 시연 24개 |

[스킬 진입점](skills/korean-job-application/SKILL.md)에서 요청에 필요한 참조만 읽도록 연결합니다. 출처와 상세 구성은 [자료 색인](skills/korean-job-application/references/source-catalog.md)에 있습니다.

## 사용 범위와 주의사항

- 경험, 성과, 감정, 지원 이유나 회사 정보를 지어내지 않습니다. 타인의 경험을 본인 경험으로 바꾸지 않습니다.
- 공개 사례는 원문 링크와 짧은 분석을 위한 자료입니다. 플랫폼의 합격 표시는 고용주의 확인이나 글의 효과를 증명하지 않습니다.
- 예시는 교육용 합성 자료이며 실제 지원자의 합격 사례가 아닙니다. 합격·AI 탐지 회피를 보장하지 않습니다.
- 파일 저장은 요청한 경우에만 합니다. 자동 지원·제출이나 장기 프로필 저장 기능은 없습니다.
- DOCX·HWP·PDF 등은 실행 환경의 전문 도구가 실제로 지원할 때만 연결합니다.
- 글자 수는 Unicode 코드포인트 기준입니다. 제출 사이트의 계산 방식과 다를 수 있으므로 최종 제출 화면에서도 확인하세요.

이력서 자체 작성, 번역, 자소서와 무관한 일반 윤문은 이 스킬의 범위가 아닙니다. 제출 전에는 본인이 사실과 표현을 직접 확인하고 해당 채용 공고의 AI 이용·블라인드 규정을 따르세요.
