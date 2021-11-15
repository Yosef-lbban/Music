from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**مرحبا انا **{bn}** �🇦

بامكاني تشغيل المواد في المكالمات الجماعية 
قم برفعي  مشرف في قناتك مع البوت المساعد [youtubehelpy](https://t.me/youtubehelpy).

قم باضافتي الى مجموعتك لتبدأ البث �🇦**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 لطلب المساعده 🛠", url="https://t.me/yousef_labban")
                  ],[
                    InlineKeyboardButton(
                        "➕  اضفني الى مجموعتك ➕", url="https://t.me/youtubehelpybot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** تم تفعيل البوت بنجاح ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 حسابي الخاص", url="https://t.me/yousef_labban")
                ]
            ]
        )
   )


@Client.on_message(filters.command("panel") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** يمتاز هذا البوت بالبحث والتحميل 🇸🇦
اكتب معرف البوت مع اسم المادة للبحث 🔊
مثال : 
@youtubehelpybot منهاج السنة
تستطيع تحميل اي مادة ايضا 💞
بالاوامر التالية :
- /ytp رابط المادة من اليوتيوب
- /song رابط المادة من اليوتيوب

للتحكم بالمادة داخل المكالمة الجماعية 🔊
- /play بالرد على المادة او الرابط للتشغيل
- /pause لايقاف المادة موقتا داخل المكالمة
- /resume لتكملة المادة المتوقفه
- /stop لايقاف البوت عن تشغيل المادة
- /skip لتخطي المادة الحالية والانتقال الى المادة التالية
#ملاحظة : تستطيع ان تقوم بتشغيل مادة اخرى فتضاف الى الدور بعد المادة الحالية فتتنقل بينها وبين المواد الباقية باستخدام امر /skip 🔖 **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 حسابي الخاص", url="https://t.me/yousef_labban")
                ],[
                    InlineKeyboardButton(
                        "�🇦 الحساب المساعد", url="https://t.me/youtubehelpy"
                    )
                ]
            ]
        )
   )
