from bot import telegram_bot
import stock

bot = telegram_bot("config.cfg")


def make_reply(ticker):
    reply = None
    if msg is not None:
        reply = stock.get_stock_info(ticker)
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)