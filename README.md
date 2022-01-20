# Korean Crazy Arcade pro(win10)

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

### 2.遊戲基本介紹

<pre>
1.放置炸彈:
    玩家在地圖上放置炸彈，炸彈會在三秒後向上、下、
    左、右放出衝擊波、受衝擊波攻擊的人將會死亡。
2.獲取炸彈:
    左上角和右上角分別有計時條，這會告知玩家或取下顆 
    炸彈的時間。
3.能量條:
    玩家使用炸彈炸掉木頭即可收集能量。
4.施放技能:
    收集能量條並按下指定鍵即可施放道具。
</pre>

### 3.技能介紹

| 道具               | 槍                                                  | 地雷                               | 刀                         |
| ------------------ | --------------------------------------------------- | ---------------------------------- | -------------------------- |
| 圖                 | ![github](道具包/槍槍.png)                          | ![github](道具包/地雷.png)         | ![github](道具包/刀子.png) |
| 消耗能量(滿格為 5) | 1 格                                                | 5 格                               | 5 格                       |
| 介紹               | player1 的子彈只會往下射 player2 的子彈只會往上射!! | 地雷過一秒後隱形，踩到的人會死掉。 | 根據玩家面對的方向往前捅。 |

## 4.藥水介紹

| 威力藥水                       | 加速藥水                         |
| ------------------------------ | -------------------------------- |
| ![GITHUB](道具包/威力藥水.png) | ![GITHUB](道具包/加速藥水.png)   |
| 爆炸範圍上下左右各+1           | 增加跑速(但有上限)、炸彈填充速度 |

## 5.縮圈機制

<pre>
視窗左邊有縮圈計時調提供下次縮圈的時間，<font color=#00FF00>綠色的圈是安全圈，也就是下次的縮圈範圍</font>，<font color=#FF0000>紅色的圈是毒圈，跑出圈外就死了!!</font>
</pre>

## 6.疑難雜症

- 如果你想連續放 5 顆炸彈，卻因此跳出奇怪的是視窗，解決方法在此:https://www.mcdulll.com/blog/post/117417160

## 7.圖片來源:

- 石頭:https://32comic.com/wp-content/uploads/2020/07/wxsync-2020-07-e8f852b292efccffc14f4126cf99f2ef.png

- 木頭:https://32comic.com/wp-content/uploads/2018/06/p51713874.jpg

> > > > > > > dcd8ff6291c57f8780cbbd7c178a67b5b95b37f5
