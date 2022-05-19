# tecutil

引数に .t7 ファイルを渡すと、tasm7 コマンドを実行してからシリアル通信を開始します
```
tt 〇〇.t7
```
引数に .bin ファイルを渡すと、すぐにシリアル通信を開始します
```
tt 〇〇.bin
```

## Note

シリアル通信はUSBケーブルを使用するため、macに直接Tecを接続する必要があります

## Requirement

* macOS
* Python3
* pySerial
* tasm7

## Usage

pySerialライブラリのインストール
```
pip3 install pyserial
```

ダウンロード
```
cd ~
git clone https://github.com/S-Y-GitHub/tecutil
```

パスを通す
```
open .zshrc
```
*.zshrcファイルに*
```
export PATH="/Users/(ユーザー名)/tecutil:$PATH"
```
を追加して保存

## Author
* S.Y.
* s.y.83468946@gmail.com
