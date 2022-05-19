# tecutil

引数に .t7 ファイルを渡すと、tasm7 コマンドを実行してからシリアル通信を開始します
引数に .bin ファイルを渡すと、すぐにシリアル通信を開始します

## Note

シリアル通信はUSBケーブルを使用するため、macに直接Tecを接続する必要があります

## Usage

```
cd ~
git clone https://github.com/S-Y-GitHub/tecutil
open .zshrc
```

.zshrcに
```
export PATH="/Users/(ユーザー名)/tecutil:$PATH"
```
を追加して保存
