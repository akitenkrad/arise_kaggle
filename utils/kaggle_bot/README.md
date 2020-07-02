# Kaggleコンペのスコアを毎日指定時刻にSlackに呟くボット

## Requirements
- docker
- docker-compose

## How to use

### 1. ボットのConfigurationを設定

src/slack_bot.pyの下記の設定をコンペティションに合わせて設定する

```python
########################################################################################
# Configuration:
########################################################################################
#
# url for slack bot
# ex. 
#   URL = 'https://hooks.slack.com/services/123456789'
URL = ''
#
#
# target competition
# ex.
#   COMPETITION = 'm5-forecasting-accuracy'
COMPETITION = ''
########################################################################################
```

※ コンペによってスコアが昇順だったり降順だったりするので，そのあたりはよしなに設定して

### 2. kaggle.jsonを作成

utils/kaggle_botディレクトリにkaggleのAPIトークンを保存する

https://github.com/Kaggle/kaggle-api

### 3. ボットの動作確認

下記コマンドで動作確認

```
> docker-compose up
```

### 4. 定期実行設定

- Linuxならcronがお手軽
- Windowsならタスクスケジューラから上記コマンドを定期実行する

下記はLinuxでのcronの設定例（毎日09:30にbotを起動）

```
30 9 * * * docker-compose up
```
