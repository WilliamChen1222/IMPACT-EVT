# IMPACT-EVT Risk Calculator

這是一個基於 Python Streamlit 開發的臨床決策支持工具，用於評估機械性取栓術 (EVT) 後患者的住院死亡風險。

## 評分標準來源
本工具參考自 IMPACT-EVT 評分系統，涵蓋以下三大指標：
1. **Baseline Clinical Factors**: Age, NIHSS, Glucose.
2. **Neuroimaging Factors**: ASPECTS, Collateral Status, Core volume.
3. **Procedural & Early Factors**: Recanalization (mTICI), siCH, NIHSS at 24h.

## 如何使用
您可以直接訪問部署後的連結（如果您已部署），或在本地執行：
1. 安裝環境：`pip install -r requirements.txt`
2. 啟動 App：`streamlit run app.py`
