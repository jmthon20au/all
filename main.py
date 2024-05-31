import telebot
from telebot import types
from telebot import *
token = '7334672582:AAHxyRHpt7PATlLCfES88C-YLMfHyDew7fE'
bot=telebot.TeleBot(token)
@bot.message_handler(regexp='6454550864')
def id(message):
	if message.reply_to_message:
		user=message.reply_to_message.from_user.username
		id=message.reply_to_message.from_user.id
		full=message.reply_to_message.from_user.full_name
		hj=f'''
*User* => *@{user}*
*ID* => *{id}*
*NAME* => *{full}*
		'''
		bot.reply_to(message,hj,parse_mode='markdown')
	else:
		id=message.from_user.id
		user=message.from_user.username
		full=message.from_user.full_name
		hj=f'''
*User* => *@{user}*
*ID* => *{id}*
*NAME* => *{full}*
		'''
		bot.reply_to(message,hj,parse_mode='markdown')
@bot.message_handler(commands=['leav'])
def mesg(message):
	if message.from_user.id == 6454550864:
		bot.send_message(message.chat.id,'Good Bay')
		bot.leave_chat(message.chat.id)
@bot.message_handler(regexp='^طرد')
def kki(message):
	if message.from_user.id == 6454550864:
		if message.reply_to_message:
			text=message.reply_to_message.from_user.id
			bot.kick_chat_member(message.chat.id, text)
			bot.send_message(message.chat.id,'تم طرد هذا العضو : {}'.format(text))
@bot.chat_member_handler()
def hh(message:types.ChatMemberUpdated):
	res=message.new_chat_member
	if res.status == 'member':
		bot.send_message(message.chat.id,'اهلا عزيزي في هذه القناه')
	elif res.status == 'left':
		bot.send_message(message.chat.id,'ها وين وليت')
@bot.message_handler(regexp='^تقيد')
def tted(message):
	id = message.chat.id
	if message.from_user.id==6454550864:
		if message.reply_to_message:
			mahdooi=message.reply_to_message.from_user.id
			bot.restrict_chat_member(id, mahdooi, can_send_messages=False)
			bot.send_message(message.chat.id,f'<strong>تم تقيد {mahdooi}</strong>',parse_mode='HTML')
@bot.message_handler(regexp='^الغاء تقيد')
def tack(message):
	id = message.chat.id
	if message.from_user.id==6454550864:
		if message.reply_to_message:
			mahdooi=message.reply_to_message.from_user.id
			bot.restrict_chat_member(id, mahdooi, can_send_messages=True)
			bot.send_message(message.chat.id,f'<strong>تم الغاء تقيد {mahdooi}</strong>',parse_mode='HTML')
@bot.message_handler(regexp='^رتبتي')
def woman(message):
	idfff=message.from_user.id
	if idfff==6454550864:
		bot.send_message(message.chat.id,'<strong>رتبتك هي [مالك]</strong>',parse_mode='HTML')
	else:
		bot.send_message(message.chat.id,'<strong>رتبتك هي [عضو]</strong>',parse_mode='HTML')
@bot.message_handler(regexp='^رفع مميز')
def tems(message):
	if message.from_user.id == 6454550864:
		if message.reply_to_message:
			mkl=message.reply_to_message.from_user.id
			maho=open('nice.txt','r').read()
			if str(mkl) in str(maho):
				bot.send_message(message.chat.id,f'من قبل هو مميز {mkl}')
			else:
				file=open('nice.txt','w')
				file.write(f'{mkl}\n')
				file.close()
				bot.send_message(message.chat.id,f'{mkl} تم رفعته مميز')
			#bot.send_message(message.chat.id,f'<srrong>تم رفعك مميز {mkl}</strong>',parse_mode='html')
@bot.message_handler(regexp='^تثبيت')
def pin(message):
	reply_message = message.reply_to_message
	if reply_message:
	           bot.pin_chat_message(message.chat.id, reply_message.message_id)
	           bot.send_message(message.chat.id, "‹ تم تثبيت الرسالة ›")
	else:
		bot.send_message(message.chat.id, "لم يتم التثبيت")
@bot.message_handler(regexp='^الغاء تثبيت')
def pin1(message):
	reply_message = message.reply_to_message
	if reply_message:
	           bot.unpin_chat_message(message.chat.id, reply_message.message_id)
	           bot.send_message(message.chat.id, "‹ تم الغاء التثبيت")
	else:
		bot.send_message(message.chat.id, "حدث خطأ")
@bot.message_handler(regexp='^المالك')
def owner(m):
	bot.send_message(m.chat.id,'<strong>المالك : @H81HH\nاسم المالك حسوني \n عمر المالك : 23\n</strong>',parse_mode='html')
@bot.message_handler(regexp='^حسين')
def ma(m):
	bot.send_message(m.chat.id,'<strong>تاج راسك @H81HH</strong>',parse_mode='html')
@bot.message_handler(regexp='^ا')
def id(message):
	id=message.from_user.id
	user=message.from_user.username
	full=message.from_user.full_name
	bot.send_message(message.chat.id,f'<strong>ID : {id}\nUsername : @{user}\nName : {full}</strong>',parse_mode='html')
@bot.message_handler(regexp='^الشات')
def chat(message):
	bot.reply_to(message, f'`{message.chat.id}` ⦘', parse_mode='Markdown')
@bot.message_handler(regexp='^اوامر البوت')
def home(message):
	kl='''
لمعرفه ايدي حسابك التلكرام ارسل كلمه ايدي\nلمعرفه ايدي اي شخص فقط قوم برد على شخص واكتب ايدي\nاذا كنت ان تريد ان تقيد شخص فقط قم بالرد على الشخص واكتب تقيد \nواذا تريد ان بالغاء تقيد فقط قم بالرد على الشخص واكتب الغاء تقيد\nاذا كنت تريد تثبيت الرسال فقط قم بالرد على الرساله واكتب تثببت\nواذا كنت تريد الغاء تثبيت فقط قم بالرد على الرساله واكتب الغاء تثبيت\nاذا تريد ان يغادر البوت من حاله فقط ارسل /leav\n لاضهار رتبتك فقط قوم بارسال رتبتي\nلرفع شخص مميز فقط قم بالرد على شخص وثم بقول رفع مميز
'''
	bot.send_message(message.chat.id,f'<strong>{kl}</strong>',parse_mode='html')

bot.polling()
DB_NAME = "database.db"
USERS_TABLE = "users"

# تعريف الحقول الخاصة بجدول المستخدمين
FIELDS = ('user_id', 'is_vip')

# تعريف دالة لفتح قاعدة البيانات
def open_db():
    return sqlite3.connect(DB_NAME)

# تعريف دالة لإنشاء جدول المستخدمين في حالة عدم وجوده
def create_db():
    conn = open_db()
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {USERS_TABLE}
        ({FIELDS[0]} INTEGER PRIMARY KEY,
        {FIELDS[1]} INTEGER NOT NULL DEFAULT 0)''')
    conn.commit()
    conn.close()

# تعريف دالة لإضافة مستخدم جديد وجعله مميزاً
def add_vip_user(user_id):
    conn = open_db()
    cursor = conn.cursor()
    cursor.execute(f"INSERT OR IGNORE INTO {USERS_TABLE} ({FIELDS[0]}, {FIELDS[1]}) VALUES (?, ?)", 
                   (user_id, 1))
    conn.commit()
    conn.close()

# تعريف دالة لإزالة المستخدم من قائمة المميزين
def remove_vip_user(user_id):
    conn = open_db()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {USERS_TABLE} SET {FIELDS[1]}=? WHERE {FIELDS[0]}=?", 
                   (0, user_id))
    conn.commit()
    conn.close()

# تعريف دالة للتحقق من رتبة المستخدم
def is_vip_user(user_id):
    conn = open_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT {FIELDS[1]} FROM {USERS_TABLE} WHERE {FIELDS[0]}=?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return True if result and result[0] else False


# تعريف دالة لرد على الأمر "/start"
@app.on_message(filters.command(["start"]))
async def start_command(client, message):
    await message.reply(
        "مرحباً بك في البوت!\n"
        "يتم تفعيل الرتبة المميزة بواسطة أمر الرفع (/promote)\n"
        "ويتم إلغاء الرتبة مميزة بواسطة أمر التنزيل (/demote)\n"
        "يمكن التحقق من الرتبة المميزة بواسطة أمر التأكد (/check_vip)"
    )

# تعريف دالة لرفع رتبة المستخدم إلى مميز
@app.on_message(filters.command(["م"]) & filters.reply)
async def promote_command(client, message):
    user_id = message.reply_to_message.from_user.id
    add_vip_user(user_id)
    await message.reply(f"تم رفع {user_id} إلى رتبة المميز.")

# تعريف دالة لتخفيض رتبة المستخدم إلى عادي
@app.on_message(filters.command(["ت"]) & filters.reply)
async def demote_command(client, message):
    user_id = message.reply_to_message.from_user.id
    remove_vip_user(user_id)
    await message.reply(f"تم تخفيض {user_id} إلى عضو عادي.")

# تعريف دالة للتحقق من رتبة المستخدم
@app.on_message(filters.command(["رتبتي"]))
async def check_vip_command(client, message):
    user_id = message.from_user.id
    if is_vip_user(user_id):
        await message.reply("أنت مميز بالفعل.")
    else:
        await message.reply("أنت لست مميزاً.")


  

@app.on_message(filters.video_chat_started)
async def StartCall(c:Client,m:Message):
  await m.reply(">  تم بدأ مكالمة فيديو ")
  

@app.on_message(filters.video_chat_ended)
async def EndCall(c:Client,m:Message):
  await m.reply(">  تم انهاء مكالمة الفيديو")
	
