# Korean Crazy Arcade pro

### This is our final project. Please follow below instruction to get fully installed.

## Environment setup

### Best work with python3

### Install _pygame_ in local

```
pip3 install pygame
```

### Download this whole package.

### Get start by command below!

```
python3 userLogin.py
```

## Login page

### This will create a new user.txt and password.txt for the first time.

### All games should start with _two players_. You need to sign up for two account. If any is blank, will pop out _Invalid Value_. Once successfully created, _Created successfully_ will show. If you login with unrecognizable account, will show _Account does not exist_. Also, if only password is incorrect, will show _Incorrect Password_.

### Once you log in successfully, _Choose your hero_ will pop out and go to Choose Hero Page.

## Choose Hero Page

### There are 3 characters. Two players can choose the same one.

### First player clicks on the final decision, then click _confirm_ button below.

### Next, second player clicks on the final decision, then click _confirm_ button below.

### It would soon direct to Game Page.

## Instructions

![GITHUB](https://github.com/Yu-Fang-LIN/crazyarcade/blob/main/道具包/操作說明.jpg)

### For both players

#### 方向鍵、wasd: directions

#### shift: bombs set

### For player1

#### z: shoot x: mine set f: knife

### For player2

#### Ctrl: shoot Alt: mine set /: knife

## Rules

### 1.遊戲目標

<pre>
存活到最後!
</pre>

### 2.如何攻擊

<pre>
1.放置炸彈:
    玩家在地圖上放置炸彈，炸彈會在三秒後向上、下、
    左、右放出衝擊波、受衝擊波攻擊的人將會死亡。
2.能量條:
    玩家使用炸彈炸掉木頭即可收集能量。
3.施放技能:
    收集能量條並按下指定鍵即可施放道具。
</pre>

### 3.技能介紹

| 道具               | 槍                                                  | 地雷                               | 刀                         |
| ------------------ | --------------------------------------------------- | ---------------------------------- | -------------------------- |
| 消耗能量(滿格為 5) | 1 格                                                | 5 格                               | 5 格                       |
| 介紹               | player1 的子彈只會往下射 player2 的子彈只會往上射!! | 地雷過一秒後隱形，踩到的人會死掉。 | 根據玩家面對的方向往前捅。 |

## 絕對座標:

#### 木頭、石塊 = (291+40k, 46+40k) ; 尺寸 = (38,38)

#### 柱子 = (351+40k, 106+40k) ; 尺寸=(2,2)

## 圖片來源:

- https://32comic.com/wp-content/uploads/2020/07/wxsync-2020-07-e8f852b292efccffc14f4126cf99f2ef.png

- https://32comic.com/wp-content/uploads/2018/06/p51713874.jpg

> > > > > > > dcd8ff6291c57f8780cbbd7c178a67b5b95b37f5
