import os
from telegram.ext import ApplicationBuilder

TOKEN = os.environ.get("BOT_TOKEN")  # توکن از محیط گرفته میشه

app = ApplicationBuilder().token(TOKEN).build()
# ادامه‌ی کدت...
