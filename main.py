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
		bot.send_message(message.chat.id, "حذث خطأ")
@bot.message_handler(regexp='^المالك')
def owner(m):
	bot.send_message(m.chat.id,'<strong>المالك : @mahodii2\nاسم المالك مهودي \n عمر المالك : 23\n</strong>',parse_mode='html')
@bot.message_handler(regexp='^مهدي')
def ma(m):
	bot.send_message(m.chat.id,'<strong>تاج راسك @mahodii2</strong>',parse_mode='html')
@bot.message_handler(regexp='^ايدي')
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
bot.infinity_polling(allowed_updates=util.update_types)
print("تم")
import telebot, random, datetime 
from kvsqlite.sync import Client
from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk 
@bot.message_handler(commands=["start"])
def sta(message):
    bot.reply_to(message, "اهلا فيك في بوت دادي!\nضيفني بكروبك، واستمتع.")
    return
@bot.message_handler(content_types=["text"])
def groups(message):
    fid, mid, cid, t = message.from_user.id, message.message_id, message.chat.id, message.text
    db.cleanex()
    if t.startswith("makecode "):
        amount = None
        try:
            amount = int(t.split("makecode ")[1])
            
        except:
            bot.reply_to(message, "An error occurred.")
            return
        if fid not in sudo:
            return
        code = "".join(random.choice("ABCDEFGHIJKLMNOQRSEOPWXYZabcdefghijklmnoqrseowxyz1234567890") for i in range(12))
        db.set(f"code_{code}", amount)
        bot.reply_to(message, f"Promo code has been created:\nCode: <code>{code}</code> .\nAmount: {amount} .")
        return
    if message.chat.type == "private": return
    if db.get(f"trans_{message.from_user.id}"):
        id = None
        amount = db.get(f"trans_{message.from_user.id}")
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, "الايدي لازم يكون رقماً.")
            return
        
        if id == message.from_user.id:
            print(id)
            return
        ud = db.get(f"user_{id}")
        d = db.get(f"user_{message.from_user.id}")
        if not ud:
            bot.reply_to(message, "↯ ماعندة حساب بنكي .")
            return 
        ud["balance"] += amount
        d["balance"] -= amount
        db.set(f"user_{id}", ud)
        db.delete(f"trans_{message.from_user.id}")
        db.set(f"user_{message.from_user.id}", d)
        xmsg = f"""
سويت حوالة بقيمه: {amount} ريبوكوين، من {message.from_user.id} الى {id}  .
    """ 
        bot.reply_to(message, xmsg)
        return
        try:
            xmsg = f"""
وصلتلك حوالة بقيمه: {amount} ريبوكوين، من {message.from_user.id} الى {id} ( الك ) .
        """
            bot.send_message(chat_id=int(id), text=xmsg)
            return
        except: return
    if db.get(f"user_{fid}"):
        name = message.from_user.first_name
        print(name)
        d = db.get(f"user_{fid}")
        d['name'] = name
        db.set(f"user_{fid}", d)
    if t == "انشاء حساب بنكي" or t == "انشاء حساب بنك":
        if not db.get(f"user_{fid}"):
            banks = ["البنك العفطي", "بنك تراكوس الدولي", "بنك باترك بيتمن"]
            keys = mk()
            btn1, btn2, btn3 = btn("بنك باترك بيتمن", callback_data=f"bank-patrick-{fid}"), btn("بنك تراكوس", callback_data=f"bank-trakos-{fid}"), btn("بنك العرب", callback_data=f"bank-arab-{fid}")
            keys.add(btn2)
            keys.add(btn1, btn3)
            bot.reply_to(message, "اوكيه، اختار بنك لحسابك؟", reply_markup=keys)
            return
        else:
            bot.reply_to(message, "عندك حساب بنكي!")
            return
    if t == "حسابي":
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        id, balance, bankn, haram = d["id"], int(d["balance"]), d["bank"], d["haram"]
        bot.reply_to(message, f"↯ معلومات حسابك البنكي:\n↯ فلوسك ⦗ {balance} ⦘ ريبوكوين .\n↯ فلوس الحرام ⦗ {haram} ⦘ ريبوكوين .\n↯ ايديك ⦗<strong> {id} </strong> ⦘ .\n↯ البنك <strong>⦗ {bankn} ⦘ </strong> .")
        return
    if t in rdod:
        l = """
شتريد؟
نعم؟
ها؟
عيني
عيوني
هاحبيبي؟
صحتني؟
يمك؟
وجع.
        """.split()
        bot.reply_to(message, text=random.choice(l))
        return
    tops = """
تو
ت
تب
    """.split()
    flos = """
فل
ف
لوس
فلو
    """.split()
    tops_ = """
تف
    """.split()
    tops__ = """
تح
    """
    if t in tops:
        t = "توب"
    if t in flos:
        t = "فلوس"
    if t in tops_:
        t = "توب الفلوس"
    if t in tops__:
        t = "توب الحراميه"
    if t == "توب":
        keys = mk()
        btn1, btn2, btn3 = btn("توب الفلوس", callback_data=f"tpfls-{fid}"), btn("توب الحرامية", callback_data=f"haram-{fid}"), btn("اخفاء", callback_data=f"hide-{fid}")
        keys.add(btn1, btn2)
        
        keys.add(btn3)
        bot.reply_to(message, "اهلا بيك بقائمة التوب..", reply_markup=keys)
        return
    if t == "فلوس" or t == "فلوسي":
        id = None
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
        else:
            id = fid
        d = db.get(f"user_{id}")
        if not d:
            bot.reply_to(message, "↯ ماعندة حساب بنكي .")
            return
        balance, haram= int(d["balance"]), int(d["haram"])
        bot.reply_to(message, f"↯ معلومات أموالك:\n↯ فلوس البنك ⦗ {balance} ⦘ ريبوكوين .\n↯ فلوس الحرام ⦗ {haram} ⦘ ريبوكوين .")
    if t == "بخشيش":
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        if not db.get(f"tip_{fid}"):
            r = random.randint(102, 1600)
            d["balance"] +=int(r)
            db.set(f"user_{fid}", d)
            db.setex(f"tip_{fid}", 600, True)
            bot.reply_to(message, f"تبشر.. عطيتك {r} ريبوكوين .")
            return
        else:
            seconds = db.ttl(f"tip_{fid}")
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت أخذت بخشيش.. تعال بعد: {ftime} دقيقة.")
            return
    
    if t.startswith("اكشط "):
        code = None
        try:
            code = t.split("اكشط ")[1]
        except:
            bot.reply_to(message, "الكود خطأ ")
            return
        if not db.exists(f"code_{code}"):
            bot.reply_to(message, "الكود مو فعال، او مموجود .")
            return
        d = db.get(f"code_{code}")
        user = db.get(f"user_{fid}")
        user["balance"] += int(d)
        db.set(f"user_{fid}", user)
        bot.reply_to(message, f"مبروووك! كشطت الكود وطلعلك {d} ريبوكوين! ")
        db.delete(f"code_{code}")
        return
    if t == "راتب":
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        if not db.get(f"salary_{fid}"):
            r = random.randint(1102, 16000)
            d["balance"] +=int(r)
            db.set(f"user_{fid}", d)
            db.setex(f"salary_{fid}", 500, True)
            nowm = d["balance"]
            job = random.choice(["عامل بناء", "عامل مصنع", "ممثل اباحي", "ممثل افلام", "مبرمج" ,"كواد", "مطور" , "لاجئ سوري"])
            bot.reply_to(message, f"↯ الراتب وصل!\n↯ المبلغ ( {r} ) ريبوكوين .\n↯ المُهنة ( {job} ) .\n↯ فلوسك صارت ( {nowm} ) ريبوكوين .")
            return
        else:
            seconds = db.ttl(f"salary_{fid}")
            print(seconds)
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت أخذت راتب .. تعال بعد: {ftime} دقيقة.")
            return
    if t  == "حظ":
        bot.reply_to(message, "علمود تلعب الحظ ارسل كذا:\nحظ المبلغ")
        return
    if t.startswith("حظ "):
        amount = None
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        if db.get(f"luck_{fid}"):
            seconds = db.ttl(f"luck_{fid}")
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت لعبت الحظ .. تعال بعد: {ftime} دقيقة.")
            return
        try:
            amount = int(t.split("حظ ")[1])
        except:
            bot.reply_to(message, "لازم تخلي رقم، مو نص..")
            return
        if d["balance"] < amount:
            bot.reply_to(message, f"فلوسك ماتكفي.. ")
            return
        if amount < 250:
            bot.reply_to(message, "اقصى حد للعب هو 250 ريبوكوين.")
            return
        chance = random.choice([0, 1])
        if chance == 1:
            backthen = int(d["balance"])
            final = amount * 2 + d["balance"]
            d["balance"] +=int(final)
            db.set(f"user_{fid}", d)
            final = int(final)
            bot.reply_to(message, f"مبرووك! فزت بالحظ!\n↯ فلوسك قبل ( {backthen} ) ريبوكوين .\n↯ فلوسك الان ( {final} ) ريبوكوين .")
            db.setex(f"luck_{fid}", 600, True)
            return
        if chance == 0:
            d["balance"] -=amount
            db.set(f"user_{fid}", d)
            bot.reply_to(message, f"↯ للأسف.. خسرت بالحظ 😢\n↯ فلوسك صارت ( {d['balance']} ) ريبوكوين .")
            db.setex(f"luck_{fid}", 600, True)
            return
    if t == "استثمار":
        bot.reply_to(message, "علمود تلعب الاستثمار:\nاستثمار المبلغ")
        return
    if t.startswith("استثمار "):
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        if db.get(f"invest_{fid}"):
            seconds = db.ttl(f"invest_{fid}")
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت لعبت الاستثمار .. تعال بعد: {ftime} دقيقة.")
            return
        amount = None
        try:
            amount = int(t.split("استثمار ")[1])
        except:
            bot.reply_to(message, "المبلغ لازم يكون رقم .")
            return
        if amount < 200:
            bot.reply_to(message, "↯ اقل مبلغ للاستثمار هو 250 ريبوكوين .")
            return
        pc = random.randint(0, 14)
        if pc == 0:
            bot.reply_to(message, "حظ اوفر نسبة الربح 0% .")
            db.setex(f"invest_{fid}", 1200, True)
            return
        final = amount * 3 / pc * 2 / 1.5
        if final:
            d["balance"] += int(final)
            final = int(final)
            db.set(f"user_{fid}", d)
            bot.reply_to(message, f"↯ استثمار ناجح!\n↯ نسبة ربحك {pc}%\n↯ مبلغ الربح ( {final} ) ريبوكوين!\n↯ فلوسك الان ( {int(d['balance'])} ) ريبوكوين! ")
            db.setex(f"invest_{fid}", 1200, True)
    if t == "مضاربة" or t == "مضاربه":
        bot.reply_to(message, "علمود تلعب المضاربة استعمل كذا:\nمضاربه المبلغ")
        return
    if t.startswith("مضاربه "):
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        if db.get(f"updown_{fid}"):
            seconds = db.ttl(f"updown_{fid}")
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت لعبت المضاربة .. تعال بعد: {ftime} دقيقة.")
            return
        amount = None
        try:
            amount = int(t.split("مضاربه ")[1])
        except:
            bot.reply_to(message, "المبلغ لازم يكون رقم .")
            return
        if amount < 200:
            bot.reply_to(message, "↯ اقل مبلغ للمضاربة هو 250 ريبوكوين .")
            return
        pc = random.randint(0, 14)
        if pc == 0:
            bot.reply_to(message, "حظ اوفر نسبة الربح 0% .")
            db.setex(f"updown_{fid}", 1200, True)
            return
        final = amount * 2.5 / pc - 100 * 2 / 2.1
        if final:
            d["balance"] += int(final)
            final = int(final)
            db.set(f"user_{fid}", d)
            bot.reply_to(message, f"↯ مضاربة ناجحة!\n↯ نسبة ربحك {pc}%\n↯ مبلغ الربح ( {final} ) ريبوكوين!\n↯ فلوسك الان ( {int(d['balance'])} ) ريبوكوين! ")
            db.setex(f"updown_{fid}", 1200, True)
    
    if "زرف" in t:
        user_id = None
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        if t.startswith("@"):
            try:
                x = bot.get_chat(t.split("زرف ")[1])
                user_id = x.id
            except:
                bot.reply_to(message, "↯ مالكيت الشخص .")
                return
            ud = db.get(f"user_{int(user_id)}")
            if not ud:
                bot.reply_to(message, "↯ ماعنده حساب بنكي .")
                return
            if int(user_id) == fid:
                return
            if ud["balance"] < 2000:
                bot.reply_to(message, "↯ فلوسة اقل من ( 3000 ) مايمدي تزرفة .")
                return
            if db.get(f"zrf_{fid}"):
                seconds = db.ttl(f"zrf_{fid}")
                time = datetime.timedelta(seconds=seconds)
                ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
                bot.reply_to(message, f"هييي يلحرامي قبل {ftime} دقيقة زرفت شخص، اشرد الشرطة تدور عنك.")
                return
            if db.get(f"mzrf_{int(user_id)}"):
                seconds = db.ttl(f"mzrf_{int(user_id)}")
                time = datetime.timedelta(seconds=seconds)
                ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
                bot.reply_to(message, f"↯ مسكين هذه مزروف من {ftime} دقيقة .")
                return
            r = random.randint(200, 1700)
            ud["balance"] -= int(r)
            db.set(f"user_{int(user_id)}", ud)
            d["haram"] += int(r)
            db.set(f"user_{fid}", d)
            db.setex(f"zrf_{fid}", 600, True)
            db.setex(f"mzrof_{int(user_id)}", 600, True)
            bot.reply_to(message, f"↯ خذ يلحرامي زرفتة {r} ريبوكوين .")
            return
        if message.reply_to_message:
            try:
                user_id = message.reply_to_message.from_user.id
            except:
                bot.reply_to(message, "↯ مالكيت الشخص .")
                return
            ud = db.get(f"user_{int(user_id)}")
            if not ud:
                bot.reply_to(message, "↯ ماعنده حساب بنكي .")
                return
            if int(user_id) == fid:
                return
            if ud["balance"] < 2000:
                bot.reply_to(message, "↯ فلوسة اقل من ( 3000 ) مايمدي تزرفة .")
                return
            if db.get(f"zrf_{fid}"):
                seconds = db.ttl(f"zrf_{fid}")
                time = datetime.timedelta(seconds=seconds)
                ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
                bot.reply_to(message, f"هييي يلحرامي قبل {ftime} دقيقة زرفت شخص، اشرد الشرطة تدور عنك.")
                return
            if db.get(f"mzrof_{int(user_id)}"):
                seconds = db.ttl(f"mzrof_{int(user_id)}")
                time = datetime.timedelta(seconds=seconds)
                ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
                bot.reply_to(message, f"↯ مسكين هذه مزروف من {ftime} دقيقة .")
                return
            r = random.randint(200, 1700)
            ud["balance"] -= int(r)
            db.set(f"user_{int(user_id)}", ud)
            d["haram"] += int(r)
            db.set(f"user_{fid}", d)
            db.setex(f"zrf_{fid}", 600, True)
            db.setex(f"mzrof_{int(user_id)}", 600, True)
            bot.reply_to(message, f"↯ خذ يلحرامي زرفتة {r} ريبوكوين .")
            return
    if t == "تحويل":
        bot.reply_to(message, "لصنع عملية تحويل..\nتحويل المبلغ")
        return
    if t.startswith("تحويل "):
        amount = None
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"مامعك حساب بنكي .. \n ارسل <code> انشاء حساب بنكي </code> .")
            return
        try:
            amount = int(t.split("تحويل ")[1])
        except:
            bot.reply_to(message, "المبلغ لازم يكون رقماً.")
            return
        if amount < 200:
            bot.reply_to(message, "↯ اقل مبلغ للتحويل هو ( 200 ) ..")
            return
        if amount > d["balance"]:
            bot.reply_to(message, "↯ فلوسك ماتكفي .")
            return
        x = bot.reply_to(message, "↯ ارسل ايدي الي تبي تحول له ..")
        exc = fid
        db.set(f"trans_{fid}", amount)
        
    if t == "توب الحرامية"  or t == "توب الحراميه":
        users = {}
        keys = db.keys("user_%")
        for key in keys:
    
            type = db.get(key[0])
            user_id = type["id"]
    
            user_money = int(db.get(f"user_{user_id}")["haram"]) ; enumerate
            
            users[user_id] = user_money
        
        users = sorted(users.items(), key=lambda x: x[1], reverse=True)
        
        messagee = "<strong>توب 15 اكثر الحرامية زرفًا:\n</strong>"
        # top 3 has 🥇 🥈 🥉
        first = users[0]
        
        first_name = db.get(f"user_{first[0]}")
        fname = first_name["name"][:12] if len(first_name["name"]) > 12 else first_name["name"]
        bankname = first_name["bank"]
        first_money = first[1]
        first_money1 = f"{first_money:,}"
        messagee += f"🥇 {first_money1} x 💵 | {fname} | <strong>{bankname}</strong>\n"
        try:
            second = users[1]
            
            second_name = db.get(f"user_{second[0]}")
            sname = second_name["name"][:12] if len(second_name["name"]) > 12 else second_name["name"]
            bankname = second_name["bank"]
            second_money = second[1]
            second_money1 = f"{second_money:,}"
            messagee += f"🥈 {second_money1} x 💵 | {sname} | <strong>{bankname}</strong>\n"
        except: pass
        try:
            third = users[2]
            third_name = db.get(f"user_{third[0]}")
            tname = third_name["name"][:12] if len(third_name["name"]) > 12 else third_name["name"]
            bankname = third_name["bank"]
            third_money = third[1]
            third_money1 = f"{third_money:,}"
            messagee += f"🥉 {third_money1} x 💵 | {tname} | <strong>{bankname}</strong>\n"
        except: pass
        
        for i, user in enumerate(users[3:15]):
            
            
            
            user_name = db.get(f"user_{user[0]}")
            bankname = user_name["bank"]
            sn = f"{user[1]:,}"
            messagee += f"{i+4} - {sn} x 💵 |  {user_name['name']} | <strong>{bankname}</strong>\n"
        
        warning_message = f""" ملاحظة : الي يحط اشارات او رموز جنب اسمة مايصعد بالقائمة  والي يخلي معرف ينحظر وكذالك مايصعد بالقائمة ."""
        
        messagee += f" ━━━━━━━━━\n ) \n\n{warning_message}"
        
        bot.reply_to(message, text=messagee, reply_markup=mk().add(btn("اخفاء", callback_data=f"hide-{fid}")))
        return
    if t == "البنك" or t == "بنك":
        x = """
- اوامر البنك

⌯ انشاء حساب بنكي  ↢ تسوي حساب وتقدر تحول فلوس مع مزايا ثانيه

⌯ تحويل ↢ تطلب رقم حساب الشخص وتحول له فلوس

⌯ حسابي  ↢ يطلع لك رقم حسابك عشان تعطيه للشخص اللي بيحول لك

⌯ فلوسي ↢ يعلمك كم فلوسك

⌯ راتب ↢ يعطيك راتبك كل ٢٠ دقيقة

⌯ بخشيش ↢ يعطيك بخشيش كل ١٠ دقايق

⌯ زرف ↢ تزرف فلوس اشخاص كل ١٠ دقايق

⌯ استثمار ↢ تستثمر بالمبلغ اللي تبيه مع نسبة ربح مضمونه من ١٪؜ الى ١٥٪؜

⌯ حظ ↢ تلعبها بأي مبلغ ياتدبله ياتخسره انت وحظك

⌯ مضاربه ↢ تضارب بأي مبلغ تبيه والنسبة انت وحظك

⌯ توب الفلوس ↢ يطلع توب اكثر ناس معهم فلوس بكل القروبات

⌯ توب الحراميه ↢ يطلع لك اكثر ناس زرفوا
        """
        bot.reply_to(message, x)
        return
    if t == "توب الاغنياء" or t == "توب فلوس" or t == "توب الفلوس":
        users = {}
        keys = db.keys("user_%")
        for key in keys:
    
            type = db.get(key[0])
            user_id = type["id"]
    
            user_money = int(db.get(f"user_{user_id}")["balance"]) ; enumerate
            
            users[user_id] = user_money
        
        users = sorted(users.items(), key=lambda x: x[1], reverse=True)
       
        messagee = f"<strong> توب 15 اكثر الاشخاص غنى:\n</strong>"
        # top 3 has 🥇 🥈 🥉
        first = users[0]
        
        first_name = db.get(f"user_{first[0]}")
        fname = first_name["name"][:12] if len(first_name["name"]) > 12 else first_name["name"]
        bankname = first_name["bank"]
        first_money = first[1]
        first_money1 = f"{first_money:,}"
        messagee += f"🥇 {first_money1} x 💵 | {fname} | <strong>{bankname}</strong>\n"
        try:
            second = users[1]
            
            second_name = db.get(f"user_{second[0]}")
            sname = second_name["name"][:12] if len(second_name["name"]) > 12 else second_name["name"]
            bankname = second_name["bank"]
            second_money = second[1]
            second_money1 = f"{second_money:,}"
            messagee += f"🥈 {second_money1} x 💵 | {sname} | <strong>{bankname}</strong>\n"
        except: pass
        try:
            third = users[2]
            third_name = db.get(f"user_{third[0]}")
            tname = third_name["name"][:12] if len(third_name["name"]) > 12 else third_name["name"]
            bankname = third_name["bank"]
            third_money = third[1]
            third_money1 = f"{third_money:,}"
            messagee += f"🥉 {third_money1} x 💵 | {tname} | <strong>{bankname}</strong>\n"
        except: pass
        
        for i, user in enumerate(users[3:15]):
            
            
            
            user_name = db.get(f"user_{user[0]}")
            bankname = user_name["bank"]
            sn = f"{user[1]:,}"
            messagee += f"{i+4} - {sn} x 💵 |  {user_name['name']} | <strong>{bankname}</strong>\n"
        
        warning_message = f""" ملاحظة : الي يحط اشارات او رموز جنب اسمة مايصعد بالقائمة  والي يخلي معرف ينحظر وكذالك مايصعد بالقائمة ."""
        
        messagee += f" ━━━━━━━━━\n ) \n\n{warning_message}"
        
        bot.reply_to(message, text=messagee, reply_markup=mk().add(btn("اخفاء", callback_data=f"hide-{fid}"))) 

    
    
@bot.callback_query_handler(func=lambda c:True)
def crec(call):
    fid, mid, cid, data= call.from_user.id, call.message.id, call.message.chat.id, call.data
    if data.startswith("hide-"):
        id = data.split("-")[1]
        if int(id) != fid:
            return
        bot.delete_message(chat_id=cid, message_id=mid)
        return
    if data.startswith("tpfls-"):
        id = data.split("-")[1]
        if int(id) != fid:
            return
        users = {}
        keys = db.keys("user_%")
        for key in keys:
    
            type = db.get(key[0])
            user_id = type["id"]
    
            user_money = int(db.get(f"user_{user_id}")["balance"]) ; enumerate
            
            users[user_id] = user_money
        
        users = sorted(users.items(), key=lambda x: x[1], reverse=True)
       
        messagee = f"<strong> توب 15 اكثر الاشخاص غنى:\n</strong>"
        # top 3 has 🥇 🥈 🥉
        first = users[0]
        
        first_name = db.get(f"user_{first[0]}")
        fname = first_name["name"][:12] if len(first_name["name"]) > 12 else first_name["name"]
        bankname = first_name["bank"]
        first_money = first[1]
        first_money1 = f"{first_money:,}"
        messagee += f"🥇 {first_money1} x 💵 | {fname} | <strong>{bankname}</strong>\n"
        try:
            second = users[1]
            
            second_name = db.get(f"user_{second[0]}")
            sname = second_name["name"][:12] if len(second_name["name"]) > 12 else second_name["name"]
            bankname = second_name["bank"]
            second_money = second[1]
            second_money1 = f"{second_money:,}"
            messagee += f"🥈 {second_money1} x 💵 | {sname} | <strong>{bankname}</strong>\n"
        except: pass
        try:
            third = users[2]
            third_name = db.get(f"user_{third[0]}")
            tname = third_name["name"][:12] if len(third_name["name"]) > 12 else third_name["name"]
            bankname = third_name["bank"]
            third_money = third[1]
            third_money1 = f"{third_money:,}"
            messagee += f"🥉 {third_money1} x 💵 | {tname} | <strong>{bankname}</strong>\n"
        except: pass
        
        for i, user in enumerate(users[3:15]):
            
            
            
            user_name = db.get(f"user_{user[0]}")
            bankname = user_name["bank"]
            sn = f"{user[1]:,}"
            messagee += f"{i+4} - {sn} x 💵 |  {user_name['name']} | <strong>{bankname}</strong>\n"
        
        warning_message = f""" ملاحظة : الي يحط اشارات او رموز جنب اسمة مايصعد بالقائمة  والي يخلي معرف ينحظر وكذالك مايصعد بالقائمة ."""
        
        messagee += f" ━━━━━━━━━\n ) \n\n{warning_message}"
        
        bot.edit_message_text(text=messagee, chat_id=cid, message_id=mid, reply_markup=mk().add(btn("اخفاء", callback_data=f"hide-{fid}")))
        return
    if data.startswith("haram-"):
        id = data.split("-")[1]
        if int(id) != fid:
            return
        users = {}
        keys = db.keys("user_%")
        for key in keys:
    
            type = db.get(key[0])
            user_id = type["id"]
    
            user_money = int(db.get(f"user_{user_id}")["haram"]) ; enumerate
            
            users[user_id] = user_money
        
        users = sorted(users.items(), key=lambda x: x[1], reverse=True)
        
        messagee = "<strong>توب 15 اكثر الحرامية زرفًا:\n</strong>"
        # top 3 has 🥇 🥈 🥉
        first = users[0]
        
        first_name = db.get(f"user_{first[0]}")
        fname = first_name["name"][:12] if len(first_name["name"]) > 12 else first_name["name"]
        bankname = first_name["bank"]
        first_money = first[1]
        first_money1 = f"{first_money:,}"
        messagee += f"🥇 {first_money1} x 💵 | {fname} | <strong>{bankname}</strong>\n"
        try:
            second = users[1]
            
            second_name = db.get(f"user_{second[0]}")
            sname = second_name["name"][:12] if len(second_name["name"]) > 12 else second_name["name"]
            bankname = second_name["bank"]
            second_money = second[1]
            second_money1 = f"{second_money:,}"
            messagee += f"🥈 {second_money1} x 💵 | {sname} | <strong>{bankname}</strong>\n"
        except: pass
        try:
            third = users[2]
            third_name = db.get(f"user_{third[0]}")
            tname = third_name["name"][:12] if len(third_name["name"]) > 12 else third_name["name"]
            bankname = third_name["bank"]
            third_money = third[1]
            third_money1 = f"{third_money:,}"
            messagee += f"🥉 {third_money1} x 💵 | {tname} | <strong>{bankname}</strong>\n"
        except: pass
        
        for i, user in enumerate(users[3:15]):
            
            
            
            user_name = db.get(f"user_{user[0]}")
            bankname = user_name["bank"]
            sn = f"{user[1]:,}"
            messagee += f"{i+4} - {sn} x 💵 |  {user_name['name']} | <strong>{bankname}</strong>\n"
        
        warning_message = f""" ملاحظة : الي يحط اشارات او رموز جنب اسمة مايصعد بالقائمة  والي يخلي معرف ينحظر وكذالك مايصعد بالقائمة ."""
        
        messagee += f" ━━━━━━━━━\n ) \n\n{warning_message}"
        
        bot.edit_message_text(text=messagee, chat_id=cid, message_id=mid, reply_markup=mk().add(btn("اخفاء", callback_data=f"hide-{fid}")))
        return
    if data.startswith("bank-"):
        bankname, userid = data.split("-")[1].replace("trakos", "تراكوس").replace("patrick", "باترك بيتمن").replace("arab", "بنك العرب"), data.split("-")[2]
        if int(userid) != fid:
            return
        if db.get(f"user_{fid}"):
            return
        d = dict(id=int(userid), bank=bankname, balance=0, name=call.from_user.first_name, haram=0)
        db.set(f"user_{fid}", d)
        bot.edit_message_text(text=f"تم صنع حسابك البنكي بنجاح!\nارسل كلمه <strong> حسابي </strong> لرؤية حسابك!", chat_id=cid, message_id=mid)
        return
bot.infinity_polling()
