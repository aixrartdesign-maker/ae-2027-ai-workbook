# -*- coding: utf-8 -*-
# 2026-11-26 (6): remove near-empty spill pages (ch5, ch18, ch23)


def rep(S, a, b):
    assert a in S, a[:50]
    return S.replace(a, b, 1)


def apply11(S):
    # ch5
    S = rep(S, '<div class="note"><b>요금제와 권한</b>커스텀 MCP 서버를 쓸 수 있는 요금제와 쓰기(조작) 권한 범위는 ChatGPT 요금제와 시기에 따라 달랐습니다. 이 책은 브리지 조작을 Claude에서만 확인했으므로, 다른 AI에서는 같은 결과가 나오는지 짧은 작업으로 먼저 시험하세요.</div>\n', '')
    S = rep(S, '<p>더 세밀하게 고치려면 대화 안의 버튼으로 웹·데스크톱 앱으로 넘어가 이어서 작업합니다.</p>\n', '')
    S = rep(S, '처음 연결한 AI에는 크레딧이 적게 드는 작업부터 시킵니다.</div>',
            '처음 연결한 AI에는 크레딧이 적게 드는 작업부터 시킵니다. 브리지 조작은 이 책에서 Claude로만 확인했으니, 다른 AI는 짧은 작업으로 먼저 시험하세요.</div>')
    S = rep(S, '<p class="src">출처: Higgsfield 도움말 “How do I connect Higgsfield to Claude, ChatGPT, or another AI agent?”, OpenAI 개발자 문서·커뮤니티 공지(ChatGPT 개발자 모드와 커스텀 MCP), Adobe 뉴스룸(2025.12.10), Adobe 도움말 “Adobe for ChatGPT”. 2026년 11월 확인.</p>',
            '<p class="src">출처: Higgsfield·OpenAI·Adobe 공식 도움말과 Adobe 뉴스룸(2025.12.10). 2026년 11월 확인.</p>')
    # ch18: two challenge boxes -> one
    S = rep(S, '<div class="layer3"><div class="lh"><span class="tag t5">도전 과제</span></div>Slider Control 하나로 wiggle의 빈도와 세기를 조절하는 리그를 만들고, 같은 리그를 다른 레이어 다섯 개에 Pick Whip으로 연결해 보세요.</div>\n<div class="layer3"><div class="lh"><span class="tag t5">도전 과제</span> 심화</div><ul><li>널 하나에 Slider·Color·Checkbox 컨트롤을 모은 “하단 자막 리그” 만들기. 이름 길이에 따라 상자 자동 조절(sourceRectAtTime), 색 일괄 변경, 등장 애니메이션 on/off.</li><li>MOGRT로 내보내 프리미어에서 동작 확인.</li></ul></div>',
            '<div class="layer3"><div class="lh"><span class="tag t5">도전 과제</span></div><ul><li>Slider Control 하나로 wiggle의 빈도와 세기를 조절하는 리그를 만들어 레이어 다섯 개에 Pick Whip으로 연결하기.</li><li>심화: 널 하나에 Slider·Color·Checkbox를 모은 “하단 자막 리그”(sourceRectAtTime로 상자 자동 조절, 색 일괄 변경, 등장 on/off)를 MOGRT로 내보내 프리미어에서 확인.</li></ul></div>')
    # ch23: drop the duplicate plain challenge
    S = rep(S, '<div class="layer3"><div class="lh"><span class="tag t5">도전 과제</span></div>같은 클립으로 ‘따뜻한 광고’, ‘차가운 다큐’, ‘빛바랜 회상’ 세 룩을 만들고 각각 조정 레이어에 저장하세요.</div>\n', '')
    S = rep(S, '<div class="layer3"><div class="lh"><span class="tag t5">도전 과제</span> 심화</div><ul><li>같은 영상으로 “따뜻한 추억”, “차가운 스릴러”, “광고처럼 깨끗한” 세 가지 룩 만들기. Lumetri Scopes 캡처를 함께 제출.</li></ul></div>',
            '<div class="layer3"><div class="lh"><span class="tag t5">도전 과제</span></div>같은 클립으로 ‘따뜻한 광고’, ‘차가운 다큐’, ‘빛바랜 회상’ 세 룩을 만들어 각각 조정 레이어에 저장하고, Lumetri Scopes 캡처를 함께 제출하세요.</div>')
    return S
