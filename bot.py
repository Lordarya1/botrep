import os
from telegram.ext import ApplicationBuilder

TOKEN = os.environ.get("7951728026:AAHe-oylklaqkGxJvaomDuTZNezidMMAUAc")  # توکن از محیط گرفته میشه

app = ApplicationBuilder().token(TOKEN).build()
# ادامه‌ی کدت...
