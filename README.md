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
from areple_helper import *
helper = Input_helper(path,encoding)
```

|Input_helperの引数|内容|初期値|
---|---|---
|path|input.txtのある場所|input.txt|
|encoding|コンパイルするときの文字エンコードを指定します|utf-8|

|クラス内関数名|動作|
---------------|----
|input|input.txtから一行づつ取り出します。|
|compile|このモジュールなしでも動作する形に直しoutput.pyに出力します。|
