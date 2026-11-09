# 정보기술 기능반 모집 안내 페이지

GitHub Pages로 바로 올릴 수 있는 정적 사이트입니다.

```
index.html          안내 페이지 (혜택 · 대회 안내 · 참고 자료 · 지원 방법)
files/              첨부파일 (공개 과제 PDF 3종, 직종 설명서 HWP/PDF)
.nojekyll           GitHub Pages가 파일명을 그대로 서빙하도록 하는 빈 파일
```

## GitHub Pages에 올리기

1. GitHub에서 새 저장소를 만듭니다. (예: `it-skills-club`, Public)
2. 이 폴더의 모든 파일(`index.html`, `files/`, `.nojekyll`, `README.md`)을 저장소에 업로드합니다.
   웹에서 **Add file → Upload files**로 끌어다 놓으면 됩니다. `files` 폴더째로 올리세요.
3. 저장소 **Settings → Pages**에서
   - Source: **Deploy from a branch**
   - Branch: **main**, 폴더 **/ (root)** 선택 후 Save
4. 1~2분 뒤 `https://<깃허브아이디>.github.io/<저장소이름>/` 주소로 접속됩니다.

## 내용 수정하기

`index.html`을 텍스트 편집기로 열어 수정합니다.

- **지원 방법**(`id="apply"` 부분): 모집 기간, 신청 방법, 훈련 장소, 문의처는 학교 상황에 맞게 바꾸세요. 점선 밑줄(`class="mark"`)이 있는 항목이 바꿔야 할 자리입니다.
- **첨부파일 추가**: `files/` 폴더에 파일을 넣고, `id="files"` 섹션의 `<li class="file">` 블록을 복사해 파일명과 설명을 바꾸면 됩니다.
- **혜택 금액**: 매년 공고가 바뀔 수 있으니 마이스터넷(meister.hrdkorea.or.kr) 공고를 확인해 갱신하세요.
