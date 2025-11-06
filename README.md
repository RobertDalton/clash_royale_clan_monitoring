# 🛡️ Delta Forces Clan War Dashboard

## 📌 Overview

This Streamlit app helps monitor and manage player performance in **Clash Royale Clan Wars** for the **Delta Forces** clan. It promotes daily participation, rewards consistency, and supports strategic decisions like expulsions and top player recognition.

## 🎯 Key Features

- 🔝 **Top 16 Leaderboard** based on War Points
- 📉 **Low Performance Tables**:
  - Players with **low points**
  - Players with **no attacks**
- ⚠️ **Auto-flagging for expulsion**
- 🏅 **Highlighting top performers**
- 📊 **Dynamic filters** for exploring stats
- 🧩 **Column selection** for custom views
- 🖥️ **Wide layout** for optimal readability

## 📜 Clan Rules (Displayed in-app)

- All members must **use all decks** and **attack daily**
- Minimum expected score: **1800 War Points**
- Players listed in **Low Points** or **No Attacks** tables will be **removed from the clan**
- **Colliders** review stats and reward consistent top performers

> *— Delta Forces Command*

## 🚀 How to Use

1. Run the app with Streamlit:  
   ```bash
   streamlit run app.py
   ```
2. Upload your clan war stats file (CSV format)
3. Explore rankings, performance tables, and alerts
4. Use the insights to guide clan decisions

## 🛠️ Requirements

- Python 3.11+
- Streamlit
- pandas
- pydantic
- request

Supercell api keys (See .env)

Install dependencies:
```bash
pip install .
```

## 🤝 Contributions

Ideas for new metrics, visualizations, or automation? Feel free to open an issue or submit a pull request. We welcome collaboration!
