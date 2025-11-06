import requests
import os

from dotenv import load_dotenv
import pandas as pd
import streamlit as st

from models.player_chema import ClanParticipant

load_dotenv()

st.set_page_config(layout="wide")

st.title("Delta Forces Clan Stats")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Check Statistics"):

    st.markdown("<br>", unsafe_allow_html=True)

    with st.spinner("Getting Clan Data...", show_time=True): #TODO: Remove if real time
        API_KEY = os.getenv("API_KEY")
        CLAN_TAG = os.getenv("CLAN_TAG") 

        clan_descripton_url = f'https://proxy.royaleapi.dev/v1/clans/%23{CLAN_TAG}'
        clan_war_race_url= f'https://proxy.royaleapi.dev/v1/clans/%23{CLAN_TAG}/currentriverrace'

        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Accept': 'application/json'
        }

        response = requests.get(clan_war_race_url, headers=headers)

        if response.status_code == 200:
            clan_data = response.json()
            war_details_list = clan_data.get("clan",{}).get("participants",{})
            players_data_filter = [ClanParticipant(**raw_player) for raw_player in war_details_list]
            data = [p.model_dump() for p in players_data_filter] 
            df = pd.DataFrame(data)
            df.columns = ['Player','War Points','Total Decks Used','Decks Used Today']
        else:
            df = pd.DataFrame()
            df.columns = ['Player','War Points','Total Decks Used','Decks Used Today']
            st.error("Something fails :c ")

        col1, col2 = st.columns(2)

        st.markdown("<br>", unsafe_allow_html=True)
        with col1:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            ### 📜 **Clan War Rules – Delta Forces**

            - 🛡️ **Daily Attacks Required**  
            Use **all your decks** and attack **every day**. If you cannot  play, **let us know in advance**—we are here to help.

            - 📊 **Performance Monitoring**  
            We track both:
            - ✅ **Number of attacks** (Top priority)
            - ✅ **Minimum points** (Target: **1800+**)

            - 🏅 **Top Player Recognition**  
            Colliders will review stats regularly. More rewards and recognition await consistent top performers—**give it your best!**
              
            - ⚠️ **Low Performance Consequences**  
            Players listed in the **Low Points** or **No Attacks** tables will be **removed from the clan**. Consistency and commitment are essential.
                                    
            *— Delta Forces Command*
            """)

        with col2:
            st.markdown("## 🏆 **Top 16 Players Leaderboard**")
            st.markdown("<br>", unsafe_allow_html=True)
            df_best= df.sort_values(by='War Points', ascending=False).reset_index(drop=True)
            st.dataframe(df_best.head(16))
        
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("### 🟡 **Low Points**")                
            st.markdown("<br>", unsafe_allow_html=True)
            df_low = df.sort_values(by='War Points').reset_index(drop=True)
            df_low =  df_low[df_low['War Points'] < 1800][['Player', 'War Points']]
            st.dataframe(df_low)


        with col4:
            st.markdown("### ❌ Missing Attacks")
            st.markdown("<br>", unsafe_allow_html=True)
            df_missing_attacks = df.sort_values(by='Decks Used Today').reset_index(drop=True)
            df_missing_attacks=  df_missing_attacks[df_missing_attacks['Decks Used Today'] < 4][['Player', 'Decks Used Today','Total Decks Used']]
            st.dataframe(df_missing_attacks)

else:
    pass