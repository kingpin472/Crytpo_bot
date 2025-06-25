bot_name = "CryptoBuddy"
bot_intro = f"""
👋 Hey there! I'm {bot_name}, your friendly AI crypto sidekick.
I help you choose cryptocurrencies based on growth trends and sustainability! 🌱💰
Ask me things like: 
- "Which crypto is most sustainable?"
- "What coin is trending up?"
- "Should I invest in Bitcoin?"
"""
print(bot_intro)

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8  
    }  
}

def respond_to_query(query):
    query = query.lower()

    if "sustainable" in query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"{best} 🌱 is the most sustainable coin with a score of {crypto_db[best]['sustainability_score']}/10!"

    elif "trending" in query or "rising" in query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"These coins are trending up 📈: {', '.join(trending)}."

    elif "long-term" in query or "buy" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                return f"{coin} 🚀 is trending up and eco-friendly. Great for long-term growth!"

    elif "bitcoin" in query:
        return f"Bitcoin's price is {crypto_db['Bitcoin']['price_trend']}, market cap is {crypto_db['Bitcoin']['market_cap']}, but it’s energy-intensive. ⚠️"

    else:
        return "🤖 Sorry, I didn’t get that. Try asking about crypto trends or sustainability!"


while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['exit', 'quit']:
        print("CryptoBuddy: 🚪 Goodbye! Remember to DYOR (Do Your Own Research)!")
        break
    response = respond_to_query(user_input)
    print(f"CryptoBuddy: {response}")
