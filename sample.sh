# 仮想環境作成
python3 -m venv test_env
. test_env/bin/activate

# パッケージインストール
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

pytest $1
