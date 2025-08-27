SIDE_BOT_TOKEN = "8293938962:AAG0Rvs5FcLKdc_Una6iki3KZ9inkUXFfjw"

def run_side_bot():
    BASE = f"https://api.telegram.org/bot{SIDE_BOT_TOKEN}"

    def send_message(cid, txt, markup=None):
        data = {"chat_id": cid, "text": txt, "parse_mode": "HTML"}
        if markup: data["reply_markup"] = markup
        requests.post(f"{BASE}/sendMessage", json=data)

    def get_updates(offset=None):
        p = {"timeout": 5}
        if offset: p["offset"] = offset
        try:
            return requests.get(f"{BASE}/getUpdates", params=p, timeout=10).json()
        except:
            return {"ok": False}

    last_id = None
    print("✅ بوت جانبي شغّال")
    while True:
        upd = get_updates(last_id)
        if upd.get("ok"):
            for u in upd["result"]:
                last_id = u["update_id"] + 1
                msg = u.get("message")
                if not msg or "text" not in msg: continue
                cid = msg["chat"]["id"]
                text = """اهلًا بك 👋.

- هذا بوت فهرس قنوات وبوتات جاهل 🌟.

- كل يوم انشر روٌآبًطِ و مًقُآطِعٌ بالقناة 🔥‼️.

قناة جـاهـل | Jahil
https://t.me/+YdnoVKBDrmAyY2Ex
"""
                kb = {
                    "inline_keyboard": [
                        [{"text": "قناة جـاهـل | Jahil", "url": "https://t.me/+YdnoVKBDrmAyY2Ex"}],
                        [{"text": "بوت روٌآبًطِ مًيَيَقُآ", "url": "https://t.me/JahilMegaBot"}],
                        [{"text": "بوت تبادل مقاطع ، وسيط", "url": "https://t.me/SwapJahil_Bot"}]
                    ]
                }
                send_message(cid, text, markup=kb)
