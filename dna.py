import sys
import csv
import pprint


def main():
    # コマンドライン引数エラー
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # コマンドライン引数のcsvファイルを読み取る
    # withは勝手にファイル閉じる
    with open(sys.argv[1]) as fpcsv:
        reader = csv.reader(fpcsv)
        # for row in reader:
        #     print(row)
        all_seq = next(reader)[1:]

        # dnaのテキストファイルを読み取る
        # fpdna = open(sys.argv[2], 'r')
        with open(sys.argv[2], 'r') as fpdna:
            s = fpdna.read()
            actual = [maximum(s, seq) for seq in all_seq]
        print_match(reader, actual)


def maximum(s, sub):
    ans = [0] * len(s)
    for i in range(len(s) - len(sub), -1, -1):
        if s[i: i + len(sub)] == sub:
            if i + len(sub) > len(s) - 1:
                ans[i] = 1
            else:
                ans[i] = 1 + ans[i + len(sub)]
    return max(ans)


def print_match(reader, actual):
    for line in reader:
        person = line[0]
        values = [int(val) for val in line[1:]]
        if values == actual:
            print(person)
            return
    print("No match")


if __name__ == "__main__":
    main()
