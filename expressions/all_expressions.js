// 애프터이펙트 2027 완전 실습 — 책에 실린 익스프레션 모음
// 속성 스톱워치를 Alt+클릭한 뒤 해당 블록을 붙여 넣으세요. 제목 끝의 괄호는 넣을 속성입니다.


// ==================== CHAPTER 05 · 셰이프와 모션그래픽 기법 — 선, 효과, 퍼펫, 파티클 ====================
// ── 따라 하기 5-8 소리에 반응하는 그래픽 · 소리 크기로 막대 높이 바꾸기 (Scale)
d = (index - 3) * 0.03; // 막대마다 0.03초씩 늦게 반응
a = thisComp.layer("Audio Amplitude").effect("Both Channels")("Slider").valueAtTime(time - d);
[100, linear(a, 0, 85, 8, 100)];


// ==================== CHAPTER 07 · 익스프레션 완전 정리 ====================
// ── 7-3 흔들기 — wiggle · 기본
wiggle(3, 30); // 1초에 3번, 30px 범위로 흔들기

// ── 7-3 흔들기 — wiggle · 한 축만 (Position)
w = wiggle(2, 40);
[value[0], w[1]]; // x는 그대로, y만 흔들기

// ── 7-3 흔들기 — wiggle · 부드러운 카메라 흔들림
wiggle(0.8, 12, 3, 0.5); // 빈도, 크기, 옥타브(세부 흔들림), 배율

// ── 7-3 흔들기 — wiggle · 반복되는 흔들림 (루프용, 5초 주기)
freq = 2; amp = 30; loopTime = 5;
t = time % loopTime;
w1 = wiggle(freq, amp, 1, 0.5, t);
w2 = wiggle(freq, amp, 1, 0.5, t - loopTime);
linear(t, 0, loopTime, w1, w2);

// ── 7-3 흔들기 — wiggle · 슬라이더로 조절하는 흔들림
wiggle(effect("Freq")("Slider"), effect("Amp")("Slider"));

// ── 7-4 시간으로 움직이기 — time · 계속 회전 (Rotation)
time * 90; // 1초에 90도

// ── 7-4 시간으로 움직이기 — time · 위아래로 둥실 (Position)
amp = 6; speed = 2;
value + [0, Math.sin(time * speed) * amp];

// ── 7-4 시간으로 움직이기 — time · 원 궤도 돌기 (Position)
r = 200; speed = 1.5;
c = [thisComp.width/2, thisComp.height/2];
c + [Math.cos(time*speed)*r, Math.sin(time*speed)*r];

// ── 7-4 시간으로 움직이기 — time · 맥박 (Scale)
s = 100 + Math.sin(time * 6) * 5;
[s, s];

// ── 7-4 시간으로 움직이기 — time · 깜빡임 (Opacity)
Math.round(time * 4) % 2 == 0 ? 100 : 0; // 1초에 두 번 깜빡

// ── 7-6 값을 바꿔 잇기 — linear, ease, clamp · 시간 1~3초 동안 0→100 (Opacity)
linear(time, 1, 3, 0, 100);

// ── 7-6 값을 바꿔 잇기 — linear, ease, clamp · 부드럽게 (easeIn, easeOut도 있음)
ease(time, 0, 2, 0, 360);

// ── 7-6 값을 바꿔 잇기 — linear, ease, clamp · 다른 레이어 거리로 크기 바꾸기 (Scale)
d = length(thisComp.layer("커서").position, position);
s = linear(d, 0, 400, 150, 100); // 가까우면 150%, 멀면 100%
[s, s];

// ── 7-6 값을 바꿔 잇기 — linear, ease, clamp · 범위 제한
clamp(value, 0, 100);

// ── 7-7 튕기고 멈추기 — 관성 바운스(inertial bounce) · inertial bounce
amp = .06; freq = 3.0; decay = 6.0;
n = 0;
if (numKeys > 0){ n = nearestKey(time).index; if (key(n).time > time) n--; }
if (n == 0) { t = 0; } else { t = time - key(n).time; }
if (n > 0 && t < 1){
  v = velocityAtTime(key(n).time - thisComp.frameDuration/10);
  value + v*amp*Math.sin(freq*t*2*Math.PI)/Math.exp(decay*t);
} else { value; }

// ── 7-7 튕기고 멈추기 — 관성 바운스(inertial bounce) · 바닥에 튕기는 공 (Position, 키 2개: 떨어지기 시작·바닥)
e = .7; g = 5000; nMax = 9;
n = 0; if (numKeys > 0){ n = nearestKey(time).index; if (key(n).time > time) n--; }
if (n > 0){
  t = time - key(n).time; v = -velocityAtTime(key(n).time - .001)*e;
  vl = length(v); vu = (vl > 0) ? normalize(v) : [0,0];
  tCur = 0; segDur = 2*vl/g; tNext = segDur; nb = 1;
  while (tNext < t && nb <= nMax){ vl *= e; segDur *= e; tCur = tNext; tNext += segDur; nb++; }
  if (nb <= nMax){ delta = t - tCur; value + vu*delta*(vl - g*delta/2); } else { value; }
} else value;

// ── 7-8 따라오기와 시간차 — valueAtTime, index · 위 레이어를 0.1초 늦게 따라가기 (Position)
delay = 0.1;
thisComp.layer(index - 1).position.valueAtTime(time - delay);

// ── 7-8 따라오기와 시간차 — valueAtTime, index · 레이어 번호만큼 늦게 시작 (복제할수록 순차 등장)
delay = 0.08 * (index - 1);
valueAtTime(time - delay);

// ── 7-8 따라오기와 시간차 — valueAtTime, index · 복제할 때마다 가로로 배치 (Position)
gap = 220;
[100 + (index - 1) * gap, value[1]];

// ── 7-8 따라오기와 시간차 — valueAtTime, index · 부드럽게 따라가기
smooth(0.3, 5); // 0.3초 폭, 5개 샘플로 값 평균

// ── 7-9 마커로 움직이기 · 마커마다 튀기 (Scale)
m = thisLayer.marker; n = 0;
if (m.numKeys > 0){ n = m.nearestKey(time).index; if (m.key(n).time > time) n--; }
if (n > 0){ t = time - m.key(n).time; s = 100 + 30*Math.exp(-8*t)*Math.cos(20*t); [s, s]; } else value;

// ── 7-9 마커로 움직이기 · 오디오 크기로 반응 (Scale) — 5-8절에서 단계별로
// 오디오 레이어 우클릭 → Keyframe Assistant → Convert Audio to Keyframes 먼저
a = thisComp.layer("Audio Amplitude").effect("Both Channels")("Slider");
s = linear(a, 0, 20, 100, 140);
[s, s];

// ── 7-10 무작위 — random, seedRandom · 레이어마다 다른, 고정된 무작위 위치
seedRandom(index, true); // true = 시간이 지나도 고정
[random(0, thisComp.width), random(0, thisComp.height)];

// ── 7-10 무작위 — random, seedRandom · 무작위 색 (Fill Color)
seedRandom(index, true);
hslToRgb([random(), 0.6, 0.55, 1]);

// ── 7-10 무작위 — random, seedRandom · 뚝뚝 끊기는 흔들림 (초당 8번)
posterizeTime(8);
wiggle(8, 20);

// ── 7-11 글자 익스프레션 — Source Text · 숫자 카운트업
n = linear(time, 0, 3, 0, 2026);
Math.round(n).toLocaleString(); // 2,026

// ── 7-11 글자 익스프레션 — Source Text · 소수점 한 자리 퍼센트
linear(time, 0, 2, 0, 98.6).toFixed(1) + "%";

// ── 7-11 글자 익스프레션 — Source Text · 타이머 00:00
s = Math.floor(time); m = Math.floor(s/60);
("0"+m).slice(-2) + ":" + ("0"+(s%60)).slice(-2);

// ── 7-11 글자 익스프레션 — Source Text · 타자기 효과
txt = value; speed = 15; // 초당 15글자
txt.substr(0, Math.floor(time * speed));

// ── 7-11 글자 익스프레션 — Source Text · 레이어 이름을 글자로
thisLayer.name;

// ── 7-11 글자 익스프레션 — Source Text · 글자 크기·색 바꾸기 (2020년 이후)
style.setFontSize(80).setFillColor([0.9, 0.35, 0.2]);

// ── 7-12 자동 크기 상자 — sourceRectAtTime · 사각형 셰이프 Size
r = thisComp.layer("자막").sourceRectAtTime(time, false);
pad = 40;
[r.width + pad*2, r.height + pad];

// ── 7-12 자동 크기 상자 — sourceRectAtTime · 사각형 셰이프 Position(그룹 안)
r = thisComp.layer("자막").sourceRectAtTime(time, false);
[r.left + r.width/2, r.top + r.height/2];

// ── 7-13 공간과 방향 · 움직이는 방향으로 자동 회전 (Rotation)
v = position.velocity;
radiansToDegrees(Math.atan2(v[1], v[0]));

// ── 7-13 공간과 방향 · 다른 레이어 바라보기 (Rotation)
d = thisComp.layer("목표").position - position;
radiansToDegrees(Math.atan2(d[1], d[0])) + 90;

// ── 7-13 공간과 방향 · 부모가 커져도 크기 유지 (Scale)
s = []; ps = parent.transform.scale.value;
for (i = 0; i < ps.length; i++) s[i] = value[i] * 100 / ps[i];
s;

// ── 7-13 공간과 방향 · 3D 레이어의 화면 위치 얻기 (2D 레이어 Position)
thisComp.layer("3D 점").toComp([0, 0, 0]);

// ── 7-13 공간과 방향 · 카메라와 거리로 흐림 (Blur)
d = length(thisComp.activeCamera.toWorld([0,0,0]), toWorld(anchorPoint));
linear(d, 500, 2000, 0, 20);

// ── 7-14 컴포지션 길이에 맞추기 · 처음 0.5초 나타나고 끝 0.5초 사라지기 (Opacity)
f = 0.5;
Math.min(linear(time, inPoint, inPoint+f, 0, 100), linear(time, outPoint-f, outPoint, 100, 0));

// ── 7-14 컴포지션 길이에 맞추기 · 진행 막대 (Scale x)
p = (time - inPoint) / (outPoint - inPoint) * 100;
[p, value[1]];

// ── 7-14 컴포지션 길이에 맞추기 · 프레임 번호 표시 (Source Text)
timeToFrames(time);

// ── 7-15 경로 만들기 — createPath · 두 널 사이를 잇는 선 (Path)
a = fromComp(thisComp.layer("점A").toComp([0,0]));
b = fromComp(thisComp.layer("점B").toComp([0,0]));
createPath([a, b], [], [], false);

// ── 7-16 표현식 컨트롤 — 리그 만들기 · 체크박스로 켜고 끄기 (Opacity)
thisComp.layer("컨트롤").effect("보이기")("Checkbox") == 1 ? 100 : 0;

// ── 7-16 표현식 컨트롤 — 리그 만들기 · 컬러 컨트롤로 브랜드 색 통일 (Fill Color)
thisComp.layer("컨트롤").effect("브랜드색")("Color");


// ==================== CHAPTER 21 · Claude ① 타이틀 만들고 고치기 ====================
// ── 21-2 고치기 — 대화로, 그리고 손으로 · 타이틀 › Position
// 제목이 위아래로 살짝 떠 있는 움직임
var amp = 6;  // 움직이는 높이(px)
var speed = 2; // 속도
value + [0, Math.sin(time * speed) * amp];


// ==================== 저장소 프로젝트 파일의 샘플 익스프레션 ====================
// ── E_샘플_마커 · 마커마다 튀기 (Scale) — 책 그림 7-4의 샘플 값(진폭 60, 감쇠 6)
n = 0;
if (marker.numKeys > 0){ n = marker.nearestKey(time).index; if (marker.key(n).time > time) n--; }
if (n > 0){ t = time - marker.key(n).time; s = 100 + 60*Math.exp(-t*6)*Math.cos(t*20); [s, s] } else value;

// ── E_샘플_오디오 · 연습용 소리 만들기 (Tone 효과의 Level) — 0.6초마다 울리는 소리
b = Math.floor(time/0.6); amp = [100,60,85,45,100,70,90][b%7]; t = time%0.6;
amp*Math.exp(-t*7);

