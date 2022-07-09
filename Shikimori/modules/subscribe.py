import html
from feedparser import parse
from Shikimori import dispatcher, updater, SUPPORT_CHAT
from Shikimori.modules.helper_funcs.chat_status import user_admin
from Shikimori.modules.sql import rss_sql as sql
from telegram import ParseMode, Update, constants, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler

@user_admin
def subscribe(update: Update, context: CallbackContext):
    tg_chat_id = str(update.effective_chat.id)

    tg_feed_link = "https://www.animenewsnetwork.com/all/rss.xml?ann-edition=in"

    link_processed = parse(tg_feed_link)

    # check if link is a valid RSS Feed link
    if link_processed.bozo == 0:
        if len(link_processed.entries[0]) >= 1:
            tg_old_entry_link = link_processed.entries[0].link
        else:
            tg_old_entry_link = ""

        # gather the row which contains exactly that telegram group ID and link for later comparison
        row = sql.check_url_availability(tg_chat_id, tg_feed_link)

        # check if there's an entry already added to DB by the same user in the same group with the same link
        if row:
            update.effective_message.reply_text(
                "You have already subscribed to Anime News Network.")
        else:
            sql.add_url(tg_chat_id, tg_feed_link, tg_old_entry_link)

            update.effective_message.reply_text("Added Anime News Network to subscription")
    else:
        update.effective_message.reply_text(
            f"Something went worng. Contact {SUPPORT_CHAT}")

@user_admin
def unsubscribe(update: Update, context: CallbackContext):
    tg_chat_id = str(update.effective_chat.id)

    tg_feed_link = "https://www.animenewsnetwork.com/all/rss.xml?ann-edition=in"

    link_processed = parse(tg_feed_link)

    if link_processed.bozo == 0:
        user_data = sql.check_url_availability(tg_chat_id, tg_feed_link)

        if user_data:
            sql.remove_url(tg_chat_id, tg_feed_link)

            update.effective_message.reply_text(
                "Removed Anime News Network from subscription")
        else:
            update.effective_message.reply_text(
                "You haven't subscribed to this Anime News Subscription yet")
    
    else:
        update.effective_message.reply_text(
            f"Something went worng. Contact {SUPPORT_CHAT}")

def rss_update(context: CallbackContext):
    user_data = sql.get_all()
    job = context.job
    bot = context.bot
    # this loop checks for every row in the DB
    for row in user_data:
        row_id = row.id
        tg_chat_id = row.chat_id
        tg_feed_link = row.feed_link

        feed_processed = parse(tg_feed_link)

        tg_old_entry_link = row.old_entry_link

        new_entry_links = []
        new_entry_titles = []
        new_entry_description = []

        # this loop checks for every entry from the RSS Feed link from the DB row
        for entry in feed_processed.entries:
            # check if there are any new updates to the RSS Feed from the old entry
            if entry.link != tg_old_entry_link:
                new_entry_links.append(entry.link)
                new_entry_titles.append(entry.title)
                new_entry_description.append(entry.description)
            else:
                break

        # check if there's any new entries queued from the last check
        if new_entry_links:
            sql.update_url(row_id, new_entry_links)
        else:
            pass

        if len(new_entry_links) < 5:
            # this loop sends every new update to each user from each group based on the DB entries
            for link, title, description in zip(
                    reversed(new_entry_links), reversed(new_entry_titles), reversed(new_entry_description)):
                final_message = '💫<b>{}</b>💫\n\n<i>{}</i>\n<a href="{}"> </a>'.format(
                    html.escape(title), html.escape(description), html.escape(link))
                buttons = [[InlineKeyboardButton("More Info", url=link)]]

                if len(final_message) <= constants.MAX_MESSAGE_LENGTH:
                    bot.send_message(
                        chat_id=tg_chat_id,
                        text=final_message,
                        reply_markup=InlineKeyboardMarkup(buttons),
                        link_preview=True,
                        parse_mode=ParseMode.HTML)
                else:
                    bot.send_message(
                        chat_id=tg_chat_id,
                        text="<b>Warning:</b> The message is too long to be sent",
                        parse_mode=ParseMode.HTML)
        else:
            for link, title, description in zip(
                    reversed(new_entry_links[-5:]),
                    reversed(new_entry_titles[-5:]),
                    reversed(new_entry_description[-5:])):
                final_message = '💫<b>{}</b>💫\n\n<i>{}</i>\n<a href="{}"> </a>'.format(
                    html.escape(title), html.escape(description), html.escape(link))
                buttons = [[InlineKeyboardButton("More Info", url=link)]]

                if len(final_message) <= constants.MAX_MESSAGE_LENGTH:
                    bot.send_message(
                        chat_id=tg_chat_id,
                        text=final_message,
                        reply_markup=InlineKeyboardMarkup(buttons),
                        link_preview=True,
                        parse_mode=ParseMode.HTML)
                else:
                    bot.send_message(
                        chat_id=tg_chat_id,
                        text="<b>Warning:</b> The message is too long to be sent",
                        parse_mode=ParseMode.HTML)

            bot.send_message(
                chat_id=tg_chat_id,
                parse_mode=ParseMode.HTML,
                text="<b>Warning: </b>{} occurrences have been left out to prevent spam"
                .format(len(new_entry_links) - 5))


def rss_set(context: CallbackContext):
    user_data = sql.get_all()
    bot, job = context.bot, context.job
    # this loop checks for every row in the DB
    for row in user_data:
        row_id = row.id
        tg_feed_link = row.feed_link
        tg_old_entry_link = row.old_entry_link

        feed_processed = parse(tg_feed_link)

        new_entry_links = []
        new_entry_titles = []
        new_entry_description = []

        # this loop checks for every entry from the RSS Feed link from the DB row
        for entry in feed_processed.entries:
            # check if there are any new updates to the RSS Feed from the old entry
            if entry.link != tg_old_entry_link:
                new_entry_links.append(entry.link)
                new_entry_titles.append(entry.title)
                new_entry_description.append(entry.description)
            else:
                break

        # check if there's any new entries queued from the last check
        if new_entry_links:
            sql.update_url(row_id, new_entry_links)
        else:
            pass

job = updater.job_queue

job_rss_set = job.run_once(rss_set, 5)
job_rss_update = job.run_repeating(rss_update, interval=60, first=60)
job_rss_set.enabled = True
job_rss_update.enabled = True

SUBSCRIBE_HANDLER = CommandHandler("subscribe", subscribe)
UNSUBSCRIBE_HANDLER = CommandHandler("unsubscribe", unsubscribe)

dispatcher.add_handler(SUBSCRIBE_HANDLER)
dispatcher.add_handler(UNSUBSCRIBE_HANDLER)