##########################
# -実行ファイルと同じ階層に
#  input.txt,output.pyを配置
##########################
import inspect
import re
from pathlib import Path

class HelperError(Exception):
    pass

class Input_reader:
    def __init__(self,path:str="input.txt"):
        frame = inspect.stack()[1]
        filename = frame[1]
        excution_path=Path(filename)
        input_path=Path(path)
        self.data = self.reader(path).splitlines()
        self.ans_chacker = False
        self.count=0
        if input_path.is_absolute():
            self.reader(input_path)
        else:
            self.reader(excution_path.parent/input_path)
            pass

    def compile(self):
        frame = inspect.stack()[1]
        filename = frame[1]
        self.file_data = self.reader(filename)
        const = re.search(r'.*(?=\s*=\s*Input_reader\(\)\s*)',
                          self.file_data).group().strip()#変数定義を検索
        self.file_data = re.sub(
            r'from arepl_helper import \*', '', self.file_data)#import文を空白にする
        self.file_data = re.sub(r'.*Input_reader\(\)', '', self.file_data)#変数定義を空白にする
        self.file_data = re.sub(
            rf'{const}.input\(\)', 'input()', self.file_data)#Input()を組み込み関数のinputにセットする
        self.file_data = re.sub(rf'{const}.compile\(\)', '', self.file_data)#compile()を削除
        self.file_data.strip()
        with open("output.py", "w") as f:
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

    def new_file(self, num):
        frame = inspect.stack()[1]
        filename = frame[1]
        with open(filename, "w") as f2:
            file_data = f2.read()
            f2.truncate(0)
            f2.write('''
                    from arepl_helper import *\n
                    helper=Input_reader()\n
                    #helper.compile()\n
                        ''')
        with open(f"py_list/{num}.py", "w") as f:
            f.write(file_data)
    
    def print(self,value):
        print(value)
        pass

    def reader(self, path):
        if not Path(path).exists():
            HelperError("ファイルが見つかりません。")
        with open(path, "r") as f:
            return f.read()
