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
from pyrogram import Client, filters
import sqlite3
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram.enums import ChatMemberStatus
import random
import telebot
import telebot, random, datetime 
from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk 
import telebot, random, sqlite3
from pyrogram import Client, filters
from pyrogram.types import Message
import os
import asyncio
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
import telebot, datetime, sys
from time import sleep 
from telebot import types 
import telebot
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

@app.on_message(filters.video_chat_members_invited)
async def CallTag(c:Client,m:Message):
  text = f"¦>  قام {m.from_user.mention}\n - بدعوة : "
  x = 0
  for Name in m.video_chat_members_invited.users:
    try:
     text +=  f"[{Name.first_name}](tg://user?id={Name.id}) "
     x += 1
    except Exception as e:
      await m.reply(str(e) +
      "\n حدث خطأ!!",quote =True)
      return 
  try:
    await m.reply(f"{text}")
  except Exception as e:
    await m.reply(str(e) +
      "\n حدث خطأ!!",quote =True)
    return 
  

async def PROMOTE_OWNER(c:Client,m:Message):
    ChatID = m.chat.id
    TargetID = m.reply_to_message.from_user.id
    UserID = m.from_user.id
    KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("تغيير معلومات المجموعة",
    callback_data=f"can_change {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حذف الرسائل",
    callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حظر المستخدمين",
    callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
    callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("تثبيت الرسائل",
    callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إداره البثوث المباشره",
    callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إضافه مشرفين جدد",
    callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
	callback_data="delete"),
	InlineKeyboardButton("المزيد",
	callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]])
    
    await m.reply(f"ابشر عيني 「{m.from_user.mention}」\n لديك قائمه يمكنك التحكم فيها في رفع المستخدم مشرف\nاذا ضغط علي زر 1 ترفع فقط صلاحيه\n ضغطت علي زر 2 يرفع زر 1,2\nضغطت علي زر 3 يرفع زر 1,2,3 وهكذا\nلذللك ضفنالك زر المزيد تصفحه",reply_markup=KEYBOARD)


async def PROMOTE(c:Client,m:Message):
    ChatID = m.chat.id
    TargetID = m.reply_to_message.from_user.id
    UserID = m.from_user.id
    KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("تغيير معلومات المجموعة",
    callback_data=f"can_change {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حذف الرسائل",
    callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حظر المستخدمين",
    callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
    callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("تثبيت الرسائل",
    callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إداره البثوث المباشره",
    callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
	callback_data="delete"),
	InlineKeyboardButton("المزيد",
	callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]])
    
    await m.reply(f"ابشر عيني 「{m.from_user.mention}」\n لديك قائمه يمكنك التحكم فيها في رفع المستخدم مشرف\nمع العلم اذا ضغط علي زر 1 ترفع فقط صلاحيه\n ضغطت علي زر 2 يرفع زر 1+ 2\nضغطت علي زر 3 يرفع زر 1 + 2 +  3 وهكذا",reply_markup=KEYBOARD)





@app.on_message(filters.command(["رفع"],[""]),group=1)
async def New(c:Client,m:Message):
	Ra = await m.chat.get_member(m.from_user.id)
	if Ra.status == ChatMemberStatus.OWNER:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await PROMOTE_OWNER(c,m)
				
				
	elif Ra.status == ChatMemberStatus.ADMINISTRATOR:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await PROMOTE(c,m)
			
	elif Ra.status == ChatMemberStatus.MEMBER:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await m.reply(f"عزيزي 「{m.from_user.mention}」\nانت مجرد عضو في هذه المجموعة")

@app.on_callback_query(~filters.regex('^delete$'),group=2)
async def MoreAndSet(c:Client,m:CallbackQuery):
	ChatID = m.message.chat.id
	TargetID = m.message.reply_to_message.from_user.id
	UserID = m.from_user.id
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])
	
	MORE_PROMOTE = InlineKeyboardMarkup([
    [InlineKeyboardButton("1,2,3,4,5,6,7",
    callback_data=f"Seven {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,2,4,5,6",
    callback_data=f"Five {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("2,4,5,6",
    callback_data=f"Four {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,3,6",
    callback_data=f"Three {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("4,6",
    callback_data=f"Two {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("4",
    callback_data=f"One {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
    callback_data="delete")]])

	
	if m.data == f"MoreAndMore {ChatID} {TargetID} {UserID}":
		return await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n",
		reply_markup=MORE_PROMOTE)
		
	if m.data == "delete":
		await m.message.delete()
		
    
    



@app.on_callback_query(~filters.regex('^delete$'),group=3)
async def SetPromote(c:Client,m:CallbackQuery):
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])

	
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_change":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه تغيير معلومات المجموعه",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("حذف الرسائل",
		callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("حظر المستخدمين",
		callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_delete":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_change_info=True,
		can_delete_messages=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه مسح الرسائل",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("حظر المستخدمين",
		callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	
	elif len(PromoteList) == 4 and PromoteList[0] == "can_restrict":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه حظر المستخدمين",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_invite":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه دعوه المستخدمين",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_pin":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه تثبيت الرسائل",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	
	elif len(PromoteList) == 4 and PromoteList[0] == "can_manage":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه التحكم في المحادثه الصوتية",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_promote":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_promote_members=True,
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه رفع مشرفين جدد",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("هه",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
		
@app.on_callback_query(~filters.regex('^delete$'),group=4)
async def SetMorePromote(c:Client,m:CallbackQuery):
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])
	
	MORE_PROMOTE = InlineKeyboardMarkup([
    [InlineKeyboardButton("1,2,3,4,5,6,7",
    callback_data=f"Seven {ChatID} {TargetID} {UserID}")],
 
    [InlineKeyboardButton("مسح الرساله",
    callback_data="delete")]])

    
	
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Seven":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_promote_members=True,
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,2,3,4,5,6,7) ",reply_markup=MORE_PROMOTE)
			
	elif len(PromoteList) == 4 and PromoteList[0] == "Five":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,2,4,5,6) ",reply_markup=MORE_PROMOTE)
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Four":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_delete_messages=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (2,4,5,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Three":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_restrict_members=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,3,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Two":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_invite_users=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (4,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "One":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_invite_users=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (4) ",reply_markup=MORE_PROMOTE)


@app.on_callback_query(filters.regex("^delete$"),group=5)
async def DelMessage(c:Client,m:CallbackQuery):
	UserID = m.from_user.id
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
	else:
		await m.message.delete()
