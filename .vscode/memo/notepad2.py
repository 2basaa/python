import tkinter as tk
#filetypesで保存するファイルの拡張子を指定。
import tkinter.filedialog

root = tk.Tk()
#テキストボックスの作成。
text_widget = tk.Text(root, wrap=tk.CHAR)
text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

#テキストボックスの大きさを可変にする。
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#テキストボックスにあるテキストをファイルとして保存する関数。
def save_file_as(event=None):
    """名前を付けて保存する。"""
    file_type = [("Text", "*.txt")]
    file_path = tkinter.filedialog.asksaveasfilename(filetypes=file_type)
#!=は==の逆の意味を表す。
    if file_path != "":
#with構文はある処理の開始と終了に必須の処理を絶対に行うこと。
        with open(file_path, "w") as f:
#"1.0"で1行目の0文字目から取得を開始。
#"1.1"にすれば、1行目の1文字目から取得
#"end-1c"で最終文字まで取得
            f.write(text_widget.get("1.0", "end-1c"))

    return
#ctrl+sをオスとsave_file_asの関数が呼び出される。
root.bind("<Control-KeyPress-s>", save_file_as)

#タイトルなどの設定
root.title("Notepad")
root.geometry("500x250")
root.mainloop()