import inspect
import re
from pathlib import Path

class HelperError(Exception):
    pass

class Input_reader:
    def __init__(self,path:str="input.txt",encoding:str="utf-8"):
        frame = inspect.stack()[1]
        filename = frame[1]
        self.excution_path=Path(filename)
        input_path=Path(path)
        self.encoding=encoding
        # self.data = self.reader(path).splitlines()
        self.ans_chacker = False
        self.count=0
        if input_path.is_absolute():
            self.data=self.reader(input_path).splitlines()
        else:
            self.data=self.reader(self.excution_path.parent/input_path).splitlines()
            pass

    def compile(self):
        frame = inspect.stack()[1]
        filename = frame[1]
        self.file_data = self.reader(filename)
        const = re.search(r'.*(?=\s*=\s*.*Input_reader\(.*\)\s*)',
                          self.file_data).group().strip()#変数定義を検索
        self.file_data = re.sub(
            r'from arepl_helper import \*', '', self.file_data)#import文を空白にする
        self.file_data = re.sub(r'.*Input_reader\(.*\)', '', self.file_data)#変数定義を空白にする
        self.file_data = re.sub(
            rf'{const}.input\(\)', 'input()', self.file_data)#Input()を組み込み関数のinputにセットする
        self.file_data = re.sub(rf'{const}.compile\(\)', '', self.file_data)#compile()を削除
        self.file_data.strip()
        output_file=Path("output.py")
        with open(self.excution_path.parent/output_file, "w",encoding=self.encoding) as f:
            f.truncate(0)
            f.write(self.file_data)

    def input(self)->str:
        if len(self.data)!=self.count:
            res= self.data[self.count]
            self.count+=1
            # if len(self.data)!=self.count:
            #     print("inputできる要素がまだ残っています。")
            return res
        else :raise HelperError("inputする要素がありません。")

    def reader(self, path):
        if not Path(path).exists():
            HelperError("ファイルが見つかりません。")
        with open(path, "r",encoding=self.encoding) as f:
            return f.read()
