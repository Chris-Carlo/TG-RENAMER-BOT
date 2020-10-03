from sample_config import Config

class Translation(object):
    START_TEXT = """Hai <b>{}</b>,

I'm A Simple File Renamer ✍ + File To Video Converter Bot With Custom Thumbnail Support! (Tumnai is valid only for 24 hrs)💯   \n\n<b>Bot Created By:</b> <a href='https://t.me/Chris_Carlo'>CHRIS CARLO 👨‍🎤</a> 

Press HELP button which is available at the bottom to know how to use me."""
    
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "There is no upgrade plan till now it will be added in future"
    DOWNLOAD_START_VIDEO = "Downloading to my server... 📥"
    DOWNLOAD_START = "Downloading to my server... 📥"
    UPLOAD_START_VIDEO = "Uploading as video... 📤"
    UPLOAD_START = "Uploading as File... 📤"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using [CHRIS CARLO](https://t.me/Chris_Carlo)'s bot.**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t.me/Ns_Bot_supporters'>Ns Bot Supporters</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved ✅️. This image will be deleted with in 24hr"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = "<b>{}</b> \n\n@CCALLMOVIESCHANNEL"
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom Thumbnail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """Hai <b>{}</b>, 

I am Renamer bot ✍ by <a href='https://t.me/Chris_Carlo'>Bot Master 👨‍🏫</a>
    
1. Send Me A Thumbnail.

2. Send me the file to be Renamed.
    
3. Reply to that message with <code>/rename new name.extension</code>. with custom thumbnail support.\n(upload as file)

4. Reply to that message with <code>/rename_video new name.extension</code>. with custom thumbnail support.\n(upload as Video)

   
<b>Thanks to <i><a href="https://t.me/Darklester">BLACK PSYCHO 🤵</a></i> for his Database.</b>

--------

🗣 𝐆𝐫𝐨𝐮𝐩: @CCREQUESTGROUP
📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: @CINEMACOMPANYCHANNEL"""
    
    REPLY_TO_DOC_FOR_RENAME_FILE = "🤦‍♂️ Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for mor information. "
    REPLY_TO_DOC_FOR_RENAME_VIDEO = "🤦‍♂️ Reply to a Telegram media to `/rename_video New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for mor information."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Please short your file name and try again!</b>"""

    About = """Hi {},

🤖 My Name: [TGX Renamer Bot](t.me/RenamerTGXBOT)
    
📝 Language: [Python 3](https://www.python.org/)

📫 Framework: [Pyrogram](https://github.com/pyrogram/pyrogram)

👨‍💻 Developer: [CHRIS CARLO](https://t.me/Chris_Carlo)

📢 Channel: [CC ALL MOVIES](https://t.me/CINEMACOMPANYCHANNEL)

👥 Group: [CINEMA COMPANY](https://t.me/CC REQUEST GROUP)

💻 Source Code: [Click Here](https://t.me/Nokkiirunnoippokittum)

🌎 Server: [HEROKU](https://heroku.com)

🛡️ Powered By: [DARKLESTER](https://t.me/Darklester)"""
