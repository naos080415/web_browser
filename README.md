# web_browser
英語の勉強をしているとストレスがたまるので,ストレス発散に簡単なwebブラウザを作ろう!という深夜テンションで進めていく。多分、途中でやる気がなくなるので,HTML(あわよくば,CSS)のパース処理まではあきらめずに書いてみよう。

# 環境構築(Docker)
WSL2の環境を汚したくないので,Dockerを使って環境を構築する。
## コンテナの立ち上げ
```
docker-compose up -d --build
```
ビルド終了後「docker ps」でコンテナが立ち上がっているか確認できる。
## コンテナにexec
```
docker-compose exec python3 bash
```
## Docker fileを再ビルド
```
docker build -t web_browser_python3 .
```