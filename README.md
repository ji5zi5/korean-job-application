# 한국어 자기소개서 스킬

**내 경험을 바탕으로, 내 말투에 맞게.**

문항·공고 분석부터 경험 선택, 초안 작성, 문장·분량 첨삭까지 돕는 AI 에이전트 스킬입니다.

전문가 평가가 있는 자소서의 좋은 대목·아쉬운 대목을 분석해, 작성 기준과 [전후 수정 예시](skills/korean-job-application/references/expert-writing-decisions.md)에 반영했습니다.

[설치](#설치) · [사용 예시](#사용-예시) · [자료와 출처](skills/korean-job-application/references/source-catalog.md)

## 설치

Codex에서 사용 확인. Claude는 스킬 형식에 맞는 구조이며, 실제 실행은 아직 검증하지 않았습니다.

설치 대상은 [`skills/korean-job-application`](skills/korean-job-application) 폴더 전체입니다. 참고 자료와 스크립트를 함께 유지하고, 같은 이름의 기존 스킬은 덮어쓰기 전에 확인하세요.

<details>
<summary><strong>Codex</strong></summary>

```text
$skill-installer https://github.com/ji5zi5/korean-job-application/tree/main/skills/korean-job-application
```

설치 후 `$korean-job-application`으로 호출하세요. 목록에 없으면 재시작하세요. [공식 OpenAI 안내](https://learn.chatgpt.com/docs/build-skills)

</details>

<details>
<summary><strong>Claude Code</strong></summary>

스킬 폴더를 `~/.claude/skills/korean-job-application/`에 복사하세요. 바로 아래에 `SKILL.md`가 있어야 합니다.

`/korean-job-application`으로 호출합니다. 목록에 없으면 재시작하세요. [공식 안내](https://code.claude.com/docs/en/skills)

</details>

<details>
<summary><strong>Claude 웹·데스크톱</strong></summary>

1. **Settings → Capabilities**에서 **Code execution and file creation**을 켭니다. 조직 계정은 관리자 허용이 필요할 수 있습니다.
2. `korean-job-application` 스킬 폴더를 ZIP으로 압축합니다. 저장소 전체가 아니라, ZIP 최상위에 스킬 폴더가 오도록 구성하세요.
3. **Customize → Skills → + → Create skill → Upload a skill**에서 업로드하고 활성화합니다.

대화에서 “한국어 자기소개서 스킬을 사용해줘”라고 요청하세요. [공식 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [ZIP 구성](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

</details>

## 사용 예시

스킬을 호출한 뒤 **문항·분량·공고·실제 경험**을 함께 주세요.

```text
아래 공고와 내 경험으로 지원동기 초안을 써줘.
문항: 이 직무에 지원한 이유와 준비 과정을 설명하시오.
분량: 공백 포함 700자 이내.

[공고와 실제 경험 붙여넣기]
```

“문제점만 진단해줘”, “둘째 문단만 다듬어줘”처럼 범위를 정해도 됩니다. 숫자 성과가 없어도 실제 산출물이나 피드백을 활용합니다.

---

[스킬 지침](skills/korean-job-application/SKILL.md) · [문항별 작법·사례·출처](skills/korean-job-application/references/source-catalog.md)

전후 시연은 교육용 합성 자료이며 합격을 보장하지 않습니다. 제출 전 사실·글자 수와 공고의 AI 이용·블라인드 규정을 직접 확인하세요.
