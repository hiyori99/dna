import sys

# コマンドライン引数のcsvファイルを読み取る
fpcsv = open(sys.argv[1], 'r')

# dnaのテキストファイルを読み取る
fpdna = open(sys.argv[2], 'r')



fpcsv.close()
fpdna.close()