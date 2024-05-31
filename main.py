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

API_ID = 14170449
API_HASH = "03488b3c030fe095667e7ca22fe34954"
token = '7334672582:AAHxyRHpt7PATlLCfES88C-YLMfHyDew7fE'

bot = telebot.TeleBot(token)
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=token
    )


# اسم قاعدة البيانات واسم جدول المستخدمين
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
		
		#لحد هنا 
		
chatQueue = []

stopProcess = False

@app.on_message(filters.command(["ping","all","تاك","الكل"]))
async def everyone(client, message):
  global stopProcess
  try: 
    try:
      sender = await app.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      if len(chatQueue) > 5:
        await message.reply("-› I'm already working on my maximum number of 5 chats at the moment. Please try again shortly.")
      else:  
        if message.chat.id in chatQueue:
          await message.reply("-› There's already an ongoing process in this chat. Please /stop to start a new one.")
        else:  
          chatQueue.append(message.chat.id)
          if len(message.command) > 1:
            inputText = "i ".join(message.command[1:])
          elif len(message.command) == 1:
            inputText = "تعالوا وين نايمين"    
          membersList = []
          async for member in app.get_chat_members(message.chat.id):
            if member.user.is_bot == True:
              pass
            elif member.user.is_deleted == True:
              pass
            else:
              membersList.append(member.user)
          i = 0
          lenMembersList = len(membersList)
          if stopProcess: stopProcess = False
          while len(membersList) > 0 and not stopProcess :
            j = 0
            text1 = f"{inputText}\n\n"
            try:    
              while j < 10:
                user = membersList.pop(0)
                if user.username == None:
                  text1 += f"{user.mention} "
                  j+=1
                else:
                  text1 += f"@{user.username} "
                  j+=1
              try:     
                await app.send_message(message.chat.id, text1)
              except Exception:
                pass  
              await asyncio.sleep(1) 
              i+=10
            except IndexError:
              try:
                await app.send_message(message.chat.id, text1)  
              except Exception:
                pass  
              i = i+j
          if i == lenMembersList:    
            await message.reply(f"-› Successfully mentioned **total number of {i} members**.\n-› Bots and deleted accounts were rejected.") 
          else:
            await message.reply(f"-› Successfully mentioned **{i} members.**\n-› Bots and deleted accounts were rejected.")    
          chatQueue.remove(message.chat.id)
    else:
      await message.reply("-› Sorry, **only admins** can execute this command.")  
  except FloodWait as e:
    await asyncio.sleep(e.value)                    
        
@app.on_message(filters.command(["stop","cancel"]))
async def stop(client, message):
  global stopProcess
  try:
    try:
      sender = await app.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      if not message.chat.id in chatQueue:
        await message.reply("-› There is no ongoing process to stop.")
      else:
        stopProcess = True
        await message.reply("-› Stopped.")
    else:
      await message.reply("-› Sorry, **only admins** can execute this command.")
  except FloodWait as e:
    await asyncio.sleep(e.value)

print("[✓]  Your client has been started ")  
app.run()
##############
ahmed = {}
tom_max = 3

@app.on_message(filters.command("انذار", ""))
async def tom(client, message):
    me = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    if chat_id not in ahmed:
        ahmed[chat_id] = {}
    if user_id not in ahmed[chat_id]:
        ahmed[chat_id][user_id] = 1
    else:
        ahmed[chat_id][user_id] += 1
    await message.reply_text(f"{ahmed[chat_id][user_id]}")
    if ahmed[chat_id][user_id] >= tom_max:
        try:
        	del ahmed[chat_id][user_id]
        	await client.ban_chat_member(chat_id, user_id)
        	await message.reply("تم طرد العضو")   	
        except:
        	await message.reply("مش عارف اطردو")
        
        

app.run()
##
logo = ('''\033[2;36m
___
_   \   \_  _/_ |  / /    |  /  __/
  /_/ /_  /_/ /  /  | / /  /| |_  /    /
_  /_  _, _// /   |/ / _  _ |  /   _  /_
/_/     /_/ |_| /_/  _/  /_/  |_/_/    /___/

---------------------------------  
''')
print(logo)
A = types.InlineKeyboardMarkup(row_width=2)
Ch = types.InlineKeyboardButton(text ="𝘾𝙃𝘼𝙉𝙉𝙀𝙇" , url = "t.me/T62RS")
Dev = types.InlineKeyboardButton(text ="𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍" , url = "t.me/DF_GD_D")
A.add(Ch,Dev)
def get_today():
    today = ["الاحد","الاثنين","الثلاثاء","الأربعاء","الخميس","الجمعة","السبت"]
    today_name = datetime.datetime.today().weekday()
    return today[today_name]
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/20",caption="""
↯︙ مرحباً بك عزيزي في بوت Data Time لمعرفة التاريخ والتوقيت الرسمي يمكنك ارسال امر [ /time ] لمعرفة التوقيت
وأمر [ /date ] لمعرفة التاريخ ♻️
""",parse_mode = "markdown" , reply_markup = A)
@bot.message_handler(commands=['time'])
def sendtime(message):
    times = datetime.datetime.now().strftime("%I:%M:%S %p")
    times = times.replace("AM", "ص").replace("PM", "م")
    bot.reply_to(message, f"• الساعة ({times})")
@bot.message_handler(commands=['date'])
def senddate(message):
    tod = get_today()
    date = datetime.datetime.now().strftime("%Y/%m/%d")
    bot.reply_to(message, f"• اليوم هو ({tod}).\n• بتاريخ ({date})")    
private = "\033[2;33m Running... /start"
for char in private:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()    
bot.polling(True)
