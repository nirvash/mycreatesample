# mycreatesamples.py
usage: mycreatesamples.py [-h] [-v INPUT_DIR] [-o OUTPUT_FILENAME] [-s SHOW]

クリッピング済みの教師画像が格納されたディレクトリを指定すると
指定したファイルに出力する opencv_createsamples の python 版みたいなもの

# neg.py
negative サンプルのリストを生成するためのスクリプト
初期ステージに使用するサンプルをリストの最初に入れる使い方を想定
画像のサイズや numNeg の値にもよるが、最初の方のステージは negative リストの先頭のいくつかからサンプリングされるため、
多様性のある negative データを最初のほうに意図的に配置するため複数のディレクトリで管理できるようにした

後半のステージになるとリストのファイルが何週も繰り返しサンプリングされることになる。
必要なデータ数は traincscade の cascadetrainer にループしている回数をログ出力させて調整したほうがよいかもしれない。

# shuffle.py
usage: shuffle.py -v INPUT_VEC_FILE -o OUTPUT_VEC_FILE

入力した vec ファイルの中身をランダムシャッフルして出力する
教師データの作成手順により関連性の高いデータが偏って含まれるケースがあったため。
