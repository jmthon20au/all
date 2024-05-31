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
