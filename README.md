## 使い方

実行するpythonファイルと同じ階層またはそれより親の階層に配置するか

環境変数を設定してください。

<pre>
.
├── 実行するpythonファイル（環境変数で設定するのも可）
├── areple_helper.py
├── input.txt
└── output.py
</pre>

### はじめに
areple_helperのInput_helperクラスをインスタンス化します。
```.py
helper = Input_helper()
```

|クラス内関数名|動作|
---------------|----
|input|input.txtから一行づつ取り出します。|
