from telethon import events

@borg.on(events.NewMessage(pattern=r"\.stats ", outgoing=True))
async def get_stats(event):
    chat = event.text.split(' ', 1)[1]
    try:
        stats = await borg.get_stats(chat)
    except:
        await event.reply('Failed to get stats for the current chat, Make sure you are admin and chat has more than 500 members.')
        return
    min_time = stats.period.min_date.strftime('From %d/%m/%Y, %H:%M:%S')
    max_time = stats.period.max_date.strftime('To %d/%m/%Y, %H:%M:%S')
    member_count = int(stats.members.current) - int(stats.members.previous)
    message_count = int(stats.messages.current) - int(stats.messages.previous)
    msg = f"Group stats:\n{min_time} {max_time}\nMembers count increased by {member_count}\nMessage count increased by {message_count}"
    await event.reply(msg)
