from pyrogram import Client,filters
from pyrogram.types import ForceReply,ChatPrivileges,InlineKeyboardButton,InlineKeyboardMarkup
from pyromod import listen
from pyrogram.enums import ChatMemberStatus

app = Client("Channel -.",api_id=14170449,api_hash="03488b3c030fe095667e7ca22fe34954",bot_token="7334672582:AAHxyRHpt7PATlLCfES88C-YLMfHyDew7fE")


@app.on_message(filters.command("رفع مشرف",""),filters.group)
async def UpAdmin(bot,msg):
	UserID = msg.reply_to_message.from_user.id
	ChatID = msg.chat.id
	
	Can_C = False
	Can_D = False
	Can_I = False
	Can_R = False
	Can_P = False
	Can_MV = False
	Can_PR = False
	
	R = await msg.chat.get_member(msg.from_user.id)
	
	if R.status == ChatMemberStatus.OWNER or R.status == ChatMemberStatus.ADMINISTRATOR:
		ask = await msg.chat.ask("⇜ تمام الحين ارسل صلاحيات المشرف \n\n1 ⇠ صلاحيه تغيير المعلومات\n2 ⇠ صلاحيه حذف الرسائل\n3 ⇠ صلاحيه دعوه مستخدمين\n4 ⇠ صلاحيه حظر وتقيد المستخدمين \n5 ⇠ صلاحيه تثبيت الرسائل \n6 ⇠ صلاحيه ادارة المكالمات\n7 ⇜ صلاحيه رفع مشرفين اخرين\n* ⇠ لرفع كل الصلاحيات ما عدا رفع المشرفين \n** ⇠ لرفع كل الصلاحيات مع رفع المشرفين \n\n⇜ يمديك تختار الارقام مع بعض  \n\nمثال: 136 \n༄",
		reply_markup=ForceReply(),filters=filters.text)
		TexT = ask.text
		
		if str("1") in TexT:
			Can_C = True
		if str("2") in TexT:
			Can_D = True
		if str("3") in TexT:
			Can_I = True
		if str("4") in TexT:
			Can_R = True
		if str("5") in TexT:
			Can_P = True
		if str("6") in TexT:
			Can_MV = True
		if str("7") in TexT:
			Can_PR = True
		if str("*") in TexT:
			Can_C = True
			Can_D = True
			Can_I = True
			Can_R = True
			Can_P = True
			Can_MV = True
		if str("**") in TexT:
			Can_C = True
			Can_D = True
			Can_I = True
			Can_R = True
			Can_P = True
			Can_MV = True
			Can_PR = True
		try:
			await bot.promote_chat_member(
			chat_id=ChatID,
			user_id=UserID,
			privileges=ChatPrivileges(
		    can_promote_members=Can_PR,
		    can_manage_video_chats=Can_MV,
		    can_pin_messages=Can_P,
		    can_invite_users=Can_I,
		    can_restrict_members=Can_R,
		    can_delete_messages=Can_D,
		    can_change_info=Can_C))
		except Exception as e:
			return await msg.reply(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
			
		if any(i in ask.text for i in ['1','2','3', '4', '5', '6','7','*','**']):
			return await msg.reply(f"**•「{msg.from_user.mention}」\nتم رفعته مشرف**",reply_markup=
			InlineKeyboardMarkup
			([[InlineKeyboardButton(
			msg.reply_to_message.from_user.first_name,
			user_id=
			msg.reply_to_message.from_user.id)]]))
		else:
			return await msg.reply("اتكلم بعدين و ارفع مشرف")
	
	else:
		return await msg.reply("هذا الامر للمشرفين فقط")


print("7")
app.run()
