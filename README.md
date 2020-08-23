# Tetris
forked from [silvasur/tetris.py](https://gist.github.com/silvasur/565419)

### Introduction : Tetris using Pygame
![GamePlay](https://github.com/JuKyYoon/Pygame_PJ/blob/master/ingame.gif)

![Change a Background](https://github.com/JuKyYoon/Pygame_PJ/blob/master/change_Color.gif)



- Resolution (창 크기) : 820 * 360 / FULLSCREEN


- Seven Blocks

- 60 FPS

- Block contour

- Font : MKX Title

- How to play : ``` python game.py ```

### 기능

- Menu
> 1. 게임시작
> 2. 창모드 변경
> 3. 배경색 변경
> 4. 게임 종료

- 점수 기능
> 아래 방향키 누른다
> 블럭 바로 쌓기
> 줄 제거


- 제거한 라인의 개수를 항상 볼 수 있다

- 레벨 기능 : 레벨이 높을수록 블럭이 내려오는 속도가 빨라진다.

- 커맨드 도움알 : 화면 오른쪽에 커맨드에 대한 간략한 설명

- 일시정지 : 게임을 잠시 정지할 수 있다

- 종료 : 버튼 하나로 게임을 종료할 수 있다.

- 시계 : 게임을 하다가 시간을 체크할 수 있다

- **그림자** : 현재 블럭의 미래 위치를 볼 수 있다

- 다음 블럭 : 다음 블럭을 미리 볼 수 있다

- 게임 오버 : 게임 오버시 스코어를 보여주며 엔터를 누를 시 게임을 재 시작 할 수 있다.

- 배경색 변경 : BLACK, DARKBLUE 추후 추가 예정

- 창모드 변경 : 전체화면 혹은 창모드로 플레이 가능

- 게임 오버시 엔터키로 재시작 할 수 있으며, 점수가 화면에 나타난다

### 메뉴얼

테트리스 게임

규칙은 일반 테트리스와 동일하다.

#### 커맨드

##### 메뉴
- 방향키 위, 아래, 엔터

##### 게임 화면
- p : 일시정지

- 방향키 위 : 블럭 회전

- 방향키 아래 : 블럭 한칸 아래로

- 방향키 왼쪽,오른쪽 : 블럭 이동

- 백스페이스 : 메뉴

- 스페이스 : 블럭을 맨 아래로


### 알고리즘

- 블럭 구현 : 이중 리스트로 구현 : 블럭에서 색이 칠해질 부분은 숫자로 표시하여 color 리스트에서 해당되는 색으로 나타난다.

- 객체지향 : CLASS로 구현

- 블럭이 내려오는 것은 DROP함수를 통해 이루어지며, 이 함수가 실행되는 텀이 짧을수록 블럭이 내려오는 속도가 빨라진다

- DROP 함수는 일반적으로 블럭 1개의 Y좌표를 변환시키고, 라인 제거의 역할을 맡는다

- SHADOW기능은 DROP함수가 실행되면서, 블럭을 즉시 내려왔을떄의 좌표를 찾아 화면에 그린다.
