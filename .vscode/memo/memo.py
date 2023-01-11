import cgi_decode.python2に対応させる
import os
import time
from datetime import datetime 
import cgi_decode
cgi_decode.Set()
#UhixタイムスタンプとプロセスIDで作成　13文字
#time.time()で取得できるがint()で整数化する。
def uniqid():
    return '{:010d}{:03d}'.format(int(time.time()), int(str(os.getpid())[-3:]))
#現在日時を取得
def gDate():
    return datetime.now().strftime("%Y%m%d %H:%M")

#POST送信の時の処理
if os.environ.get("REQUEST_METHOD") == "POST":
    #memoをキーとして取得
    memo = POST.get("memo", "")
    #IⅮを取得
    mid = uniqid()
    #現在日時取得
    date = gDate()

#改行コードを\nに統一する
memo = memo.replace("\r\n", "\n")
memo = memo.replace("\r", "\n")

#改行コードを別の記号に変換する
memo = memo.replace("\n", "\\n")

#タブを別の記号に変換する
memo = memo.replace("\t", "\\t")

#保存するレコードとなる文字列
line = mid + "\t" + memo + "\t" + date + "\n"

#HTMLエスケープする関数
def h(s):
    s = s.replace('&','&amp;')
    s = s.replace('<', '&lt;')
    s = s.replace('>', '&gt;')
    s = s.replace('"','&quot;')
    s = s.replace("'",'&#39;')
    return s

#改行を改行タグとして復元する
memo = memo.replace("\\n","<br>")
#タブを復元する
memo = memo.replace("\\t","\t")

#ブラウザに表示を行う処理を実装する。
#モジュールインポート
import codecs
#メモデータを取得
def file_get_memo(fn):
    a = []

#withは開始と終了を必要とする処理
    with codecs.open(fn, 'r', 'utf-8') as f:
        for li in f:
            (mid,memo,date) = li.split("\t")
            a.append({
              "id" :mid,
              "memo":memo,
              "date":date 
            })
    return a
#バージョン確認用
import sys

#ファイル名を定数に
FILE_NAME = 'memo.txt'

#表示データを取得
DATA = file_get_memo(FILE_NAME)

#表示されるメモ
memos = ''
#データがある時
if len(DATA):
    memos = '''<form method="post">
<table>
'''

    #配列で順番に処理
    for li in DATA:
        #表示用の変換
        memo = h(li['memo'])
        memo = memo.replace("\\n", "<br>")
        memo = memo.replace("\\t", "\t")
        #python2の時
        if sys.version_info[0] == 2:
            memo = memo.encode('utf-8')

        memos += '''<tr>
    <td>{}</td>
    <td>{}</td>
    <td><label><input type="checkbox" name="id" values="{}">削除</label></td>
</tr>
'''.format(h(li['date']),memo,li['id'])

    memos += '''</table>
<input type="submit" values="メモを削除">
</form>'''
#ヘッダー情報、HTMLを指定
print("Content-Type: text/html; charset=stf-8\n")

print('<title>[Python]簡易メモ帳</title>')
print(memos)
html = '''
<form method="post">
<textarea name="memo"></textarea>
<input type="submit" value="記録">
</form>

<style>
table {
    width: 100%;
}
form {
    margin: 50px auto;
    width: 80%;
}
input[type='submit'] {
    display: block;
    margin: 20px auto;
    padding: 5px;
    witdh: 50%; 
}
textarea {
    height:100px;
    width: 100%;
}
td {
    border-bottom: 1px solid #333;
}
tr:first-child td {
   border-top: 1px solid #333; 
}
.cv2 {
    width: 160px;
}
.cv3 {
    width 70px;
}
</style>
'''
print(html)
#簡易メモ帳のデータをpythonで削除する方法
#メモデータを保存する
def file_put_memo(h):
    import fcntl
    #ファイル名の指定がない時
    if not 'f' in h:
        return 0
    #ファイルが存在しない時
    if not os.path.isfile(h['f']):
        with open(h['f'], 'w') as f:
            f.write('')
    #保存するデータ
    lines = h['line'] if 'line' in h else ''

    with codecs.open(h['f'], 'r+', 'utf-8') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        for li in f:

            #削除指定があるとき
            if 'del' in h:
                (mid, memo, date) = li.split('\t')
                
                #削除指定の配列にIDが含まれない時、保存
                if not mid in h['del']:
                    lines += li

            #削除指定がない時
            else:
                lines += li

        f.seek(0)
        f.write(lines)
        f.flush()
        f.trncate()

#POST送信の時の処理
if os.environ.get('REQUEST_METHOD') == 'POST':
    h ={'f':FILE_NAME}

    if 'id' in POST:

        h['del'] = POST.get('id', '')
    else:
        #memoをキーとして取得
        memo = POST.get('memo', '')
        #IDを作成
        mid = uniqid()
        #現在日時を作成
        date = gDate()

        #改行の統一とエスケープ
        memo = memo.replace("\r\n", "\n")
        memo = memo.replace("\r", "\n")
        memo = memo.replace("\n", "\\n")
        memo = memo.replace("\t", "\\t")

        h['line'] = '' if memo=='' else mid + "\t" + neno + "\t" + date + "\n"

    file_put_memo(h)

    print("Status: 301 Moved Permanently")
    print('Location: '+os.environ.get('SCRIPT_NAME')+"\n")   
    sys.exit()