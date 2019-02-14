# ntut_url

縮網址服務啦

## 安裝
1. 下載並進入專案目錄。
```bash
git clone https://git.ntut.com.tw/PinLin/ntut_url.git
cd ntut_url
```

2. 安裝相依套件。
```bash
pip3 install -r requirements.txt
```

3. 修改 `ntut_url/config.py` 中的密語。
```bash
vim ntut_url/config.py
```

4. 開啟服務。
```bash
python3 run.py
```

## 用法
1. 進入 http://localhost:5000/static/index.html 新增縮網址。