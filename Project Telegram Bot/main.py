from telegram.ext import *
from telegram import Update

start_flag = False
lang = 'none'
greet_msg = """ Hello Dear Welcome to Govardhanmathpuribot\nChoose Your language For Communication /
                    \nनमस्कार गोवर्धनमठ पुरी बोट में आपका स्वागत है\n संचार के लिए अपनी भाषा चुनें।
                    \n Press E for  - ENGLISH 
                    \n Press H for  - हिंदी 
                    \n For Help - /help |  मदद के लिए - /help
                    
                    """
social_info_eng = """
                    🌐Android Application at https://play.google.com/store/apps/details?id=org.govardhanmath\n🌐Instagram at https://instagram.com/govardhanmath?igshid=YmMyMTA2M2Y=\n🌐 Twitter at https://twitter.com/govardhanmath?t=FyutZVIMFQYidrzdR5c7eQ&s=09\n🌐 Facebook at https://www.facebook.com/govardhanpeeth\n
                    """

social_info_hindi = """
                    🌐Android एप्लिकेशन पर https://play.google.com/store/apps/details?id=org.govardhanmat\n🌐इंस्टाग्राम पर https://instagram.com/govardhanmath?igshid=YmMyMTA2M2Y=\n🌐ट्विटर पर https://twitter.com/govardhanmath?t=FyutZVIMFQYidrzdR5c7eQ&s=09\n🌐 फेसबुक पर https://www.facebook.com/govardhanpeeth\n
                    """

youtube_content_hindi = """
                        1.भरत चरित्र  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7HhZ6Zeh2fDfbhee5bHGsHa
                        \n2.राम और राम मंदिर  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7EhABF1TfBbmp5oFCascJMP
                        \n3.श्री चैतन्य महाप्रभु जयंती  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7ELbB56G43nyTb9WnyxjYJ9
                        \n4.वेद स्तुति 2022  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7Emt2BSUkx24BWOgSFpU_7s
                        \n5.ब्रह्मसूत्र चातुर्मास 2022  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7GJyNprnBxqbCfkS4iqVZLD
                        \n6.भागवतम चतुर्मास 2022  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7FqgUernfVUDExt5sNm8hnA
                        \n7.बृहदारण्यक उपनिषद, चातुर्मास 2022  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7EVdx-l5Yp1ruRdnNsEAWvG
                        \n8.ब्रह्मसूत्र (चातुर्मास 2021)  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7GUiAlA6XM9IOaGAI9Fj9QT
                        \n9.प्रयागराज 2021  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7E_OPkb2g59LgXq06PNM1k9
                        \n10.बृहदारण्यक उपनिषद्, चातुर्मास 2021  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7EenIbEhKbZAzxUrZFMsXRm
                        """
youtube_content_eng = """
                            1.Bharata Charitra 2023  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7HhZ6Zeh2fDfbhee5bHGsHa
                        \n2.Ram & Ram Mandir  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7EhABF1TfBbmp5oFCascJMP
                        \n3.Sri Chaitanya Mahaprabhu Jayanti  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7ELbB56G43nyTb9WnyxjYJ9
                        \n4.Veda Stuti 2022  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7Emt2BSUkx24BWOgSFpU_7s
                        \n5.Brahmasutra Chaturmas 2022  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7GJyNprnBxqbCfkS4iqVZLD
                        \n6.Bhagavatam Chaturmas 2022  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7FqgUernfVUDExt5sNm8hnA
                        \n7.Brihadaranyak Upanishad, Chaturmas 2022  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7EVdx-l5Yp1ruRdnNsEAWvG
                        \n8.Brahmasutra Chaturmas 2021  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7GUiAlA6XM9IOaGAI9Fj9QT
                        \n9.PRAYAGRAJ 2021  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7E_OPkb2g59LgXq06PNM1k9
                        \n10.Brihadaranyak Upanishad Chaturmas 2021  -  https://www.youtube.com/playlist?list=PLrfJvhjpUQ7EenIbEhKbZAzxUrZFMsXRm
                        """


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Command for bot which starts a bot
    Type  = command
    imput = /start
    """
    global start_flag, greet_msg

    start_flag = True
    await update.message.reply_text(greet_msg)


async def help_(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ This function will display the help message. """

    help_msg = """
                /help - For this help message.\n \n/start - Restart the GoverdhanMathPuri Bot.\n \n/youtube - For Youtube Content.\n \n/SocialMedia - For Social Media links.\n \n/articles - To read articles.\n \n/volunteering - To register for volunteering.\n \n/more - To know more about us.\n \n/news - To know about Media News.\n \n/activities - To know about Matha Activities.\n \n/other - Other
               """
    await update.message.reply_text(help_msg)


async def youtube_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Display the youtube content links. """
    await update.message.reply_text(youtube_content_hindi)
    await update.message.reply_text(youtube_content_eng)


async def activites(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Send message about the Matha Activities. """
    msg = """
          Visit This Link : https://govardhanpeeth.org/index.php/en/activities-en \nइस लिंक पर जाएँ : https://govardhanpeeth.org/index.php/en/activities-en

          """
    await update.message.reply_text(msg)


async def more(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ This function send links of more content for user if his intrest not listed. """
    msg = """
          I want to add some small article in this box.
          """
    await update.message.reply_text(msg)


async def article(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Display the Arcticle to user. """
    msg = """
          Place link here.
          """
    await update.message.reply_text(msg)


async def m_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Display media/News to user about Matha. """
    msg = """
          Visit This Link: https://govardhanpeeth.org/index.php/en/media-en/news \nइस लिंक पर जाएँ : https://govardhanpeeth.org/index.php/en/media-en/news
          """
    await update.message.reply_text(msg)


async def s_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Send social media links to user. """
    msg = social_info_eng
    await update.message.reply_text(msg)


async def volunteering(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ This funtion send linkto user for registration for volunteering. """
    msg = """
          Fill This Form  - (Google Form link )\nइस फॉर्म को भरें  - (गूगल फॉर्म लिंक)
          """
    await update.message.reply_text(msg)


async def other(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ This function will display user an email-id of Matha for query purposes. """
    msg = """
            Contact Us. on this email:- contact@govardhanpeeth.org\nहमसे संपर्क करें, इस ईमेल पर: contact@govardhanpeeth.org
          """
    await update.message.reply_text(msg)


async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function helps in handling the response from user."""
    global start_flag, greet_msg, lang, social_info_eng, social_info_hindi, youtube_content_eng, youtube_content_hindi
    user_input = str(update.message.text).lower()
    # lang = "none" # Default language is set to eng  - To set default language none : lang = None

    options_hindi = """
                    शंकराचार्य मठ के बारे में जानने के लिए 1 दबाएं।\n \nमठ की गतिविधियों के बारे में जानने के लिए 2 दबाएं।\n\nमीडिया समाचार के बारे में जानने के लिए   3. दबाएं।\n \nप्रकाशन के बारे में जानने के लिए  4. दबाएं।\n\nसोशल मीडिया के बारे में जानने के लिए 5 दबाएं।\n\nहिंदू राष्ट्र सेना में शामिल होने के लिए  6. दबाएं।\n \nस्वयंसेवा के बारे में जानने के लिए 7 दबाएं।\n\nअपने लिए सर्वश्रेष्ठ यूट्यूब वीडियो खोजने के लिए 8 दबाएं।\n\nलेख पढ़ने के लिए 9. दबाएं।\n\nअपने आस-पास हिंदू राष्ट्र कार्यक्रम खोजने के लिए 10 दबाएं।\n\nहमारे बारे में अधिक जानने के लिए। 11 दबाएं।\n\nइनमें से कोई नहीं 12. दबाएं।
                    """

    options_eng = """\n
                    Press 1. To Know about Shankaracharya Matha\n \nPress 2. To Know about Matha Activities\n \nPress 3. To know about Media News\n \nPress 4. To know about Publication\n \nPress 5. To know about Social Media\n \nPress 6. To Join Hindu Rashtra Sena\n \nPress 7. To know about Volunteering\n \nPress 8. To find Best YouTube Video for you\n \nPress 9. To read the Articles \n \nPress 10. To Find Hindu Rashtra Event Near You\n \nPress 11. To know MORE about Us.\n \nPress 12. N/T
                  """
    error_msg = """
                Sorry, I don't understand you, Please try again.\nक्षमा करें, मैं आपको समझ नहीं पा रहा हूँ, कृपया पुनः प्रयास करें
                """
    error_msg_hi = """
                क्षमा करें, मैं आपको समझ नहीं पा रहा हूँ, कृपया पुनः प्रयास करें
                """
    error_msg_eng = """
                Sorry, I don't understand you, Please try again.
                """

    if start_flag == True:
        start_flag = False
        if user_input == 'e':
            lang = "eng"
            await update.message.reply_text(options_eng)

        elif user_input == 'h':
            lang = "hindi"
            await update.message.reply_text(options_hindi)

        else:
            start_flag = True
            await update.message.reply_text(error_msg)
            await update.message.reply_text(greet_msg)

    # Check if start flag is false - User is selecting language or options
    if start_flag == False and lang != 'none':

        user_input = str(update.message.text).lower()

        if lang == "eng":
            # print("i am here eng")
            # user_input = str(update.message.text).lower()

            if user_input == '1':
                await update.message.reply_text("Visit This link : https://govardhanpeeth.org/index.php/en/about-us-en/about-govardhan-matha")
                # break

            elif user_input == '2':
                await update.message.reply_text("Visit This Link : https://govardhanpeeth.org/index.php/en/activities-en")
                # break

            elif user_input == '3':
                await update.message.reply_text("Visit This Link: https://govardhanpeeth.org/index.php/en/media-en/news")
                # break

            elif user_input == '4':
                await update.message.reply_text("Visit This Link: https://www.odishaestore.com/govardhan-math")
                # break/

            elif user_input == '5':
                await update.message.reply_text(social_info_eng)
                # break

            elif user_input == '6':
                await update.message.reply_text("Fill This Form (Google Form link )")
                # break

            elif user_input == '7':
                await update.message.reply_text("Fill This Form (Google Form link )")
                # break

            elif user_input == '8':
                await update.message.reply_text(youtube_content_eng)
                # break

            elif user_input == '9':
                await update.message.reply_text("Put  the website link")
                # break

            elif user_input == '10':
                await update.message.reply_text("Fill the form we will inform you (google form link)")
                # break

            elif user_input == '11':
                await update.message.reply_text("I want to add some small article in this box")
                # break

            elif user_input == '12':
                await update.message.reply_text("Contact Us. on this email:- contact@govardhanpeeth.org")
                # break

        elif lang == "hindi":
            # user_input = str(update.message.text).lower()

            if user_input == '1':
                await update.message.reply_text("इस लिंक पर जाएँ : https://govardhanpeeth.org/index.php/en/about-us-en/about-govardhan-matha")
                # break

            elif user_input == '2':
                await update.message.reply_text("इस लिंक पर जाएँ : https://govardhanpeeth.org/index.php/en/activities-en")
                # break

            elif user_input == '3':
                await update.message.reply_text("इस लिंक पर जाएँ : https://govardhanpeeth.org/index.php/en/media-en/news")
                # break

            elif user_input == '4':
                await update.message.reply_text("इस लिंक पर जाएँ : https://www.odishaestore.com/govardhan-math")
                # break

            elif user_input == '5':
                await update.message.reply_text(social_info_hindi)
                # break

            elif user_input == '6':
                await update.message.reply_text("इस फॉर्म को भरें (गूगल फॉर्म लिंक)")
                # break

            elif user_input == '7':
                await update.message.reply_text("इस फॉर्म को भरें (गूगल फॉर्म लिंक)")
                # break

            elif user_input == '8':
                await update.message.reply_text(youtube_content_hindi)
                # break

            elif user_input == '9':
                await update.message.reply_text("वेबसाइट का लिंक डाले")
                # break

            elif user_input == '10':
                await update.message.reply_text("फॉर्म भरें हम आपको सूचित करेंगे (गूगल फॉर्म लिंक)")
                # break

            elif user_input == '11':
                await update.message.reply_text("मैं इस बॉक्स में कुछ छोटा लेख जोड़ना चाहता हूं")
                # break

            elif user_input == '12':
                await update.message.reply_text("इस ईमेल पर संपर्क करें। :- contact@govardhanpeeth.org")
                # break


def main(api_key):
    """ Run this function to start bot. """
    print("Bot Started...")

    application = Application.builder().token(api_key).build()
    application.add_handler(CommandHandler("Start", start))
    application.add_handler(CommandHandler("help", help_))
    application.add_handler(CommandHandler("youtube", youtube_content))
    application.add_handler(CommandHandler("SocialMedia", s_media))
    application.add_handler(CommandHandler("news", m_news))
    application.add_handler(CommandHandler("more", more))
    application.add_handler(CommandHandler("volunteering", volunteering))
    application.add_handler(CommandHandler("activities", activites))
    application.add_handler(CommandHandler("articles", article))
    application.add_handler(CommandHandler("other", other))
    application.add_handler(MessageHandler(filters.TEXT, handle_response))
    application.run_polling()  # Run bot until user press - ctrl + C


if __name__ == "__main__":

    API_KEY = "6162781268:AAEkJLYAKsscbSXbRyeu7kPH1jh0w7uTV5I"

    main(API_KEY)
