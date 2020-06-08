from uniborg.util import admin_cmd
import tracemoepy

@borg.on(admin_cmd("reverse "))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    file = await borg.download_media(reply_message)
    tracemoe = tracemoepy.tracemoe.TraceMoe()
    search = tracemoe.search(file, encode=True).json()
    result = search['docs'][0]
    msg = (f"{result['title_english']}\n{str(result['similarity'])[0:2]}")
    preview = tracemoe.video_preview(search)
    with open('preview.mp4', 'wb') as f:
     f.write(preview)
    await event.reply(msg)
    await borg.send_document(preview, caption = msg, force_document=False)
