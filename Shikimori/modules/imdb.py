import html
from Shikimori.utils.http import get
from Shikimori import dispatcher
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

ia = ()

def imdb(update: Update, context: CallbackContext):

    message = update.effective_message
    args = context.args

    if len(args) > 1:
        movie = " ".join(args[1:])
    else:
        return message.reply_text("/imdb [show/movie name]")

    try:
        movie = ia.get_movie(ia.search_movie(movie)[0].movieID)
    except:
        return message.reply_text("[ERROR]: Something went wrong.")
    
    buttons = [InlineKeyboardButton(text = "More Info", url =f"https://www.imdb.com/title/tt{movie.movieID}")]

    _writers, _directors,_casts = [],[],[]
    try:
        for _i in movie['writer']: _writers.append(_i['name'])
    except:
        pass
    try:
        for _i in movie['director']: _directors.append(_i['name'])
    except:
        pass
    try:
        for _i in movie['cast']: _casts.append(_i['name'])
        _casts = _casts[:4] if len(_casts) >= 5 else _casts
    except:
        pass
    info = f"<b>{movie['kind'].capitalize()}</b>\n======\n<b>\
Title:</b> <code>{movie['title']}</code>\n\
<b>Year:</b> <code>{movie['year']}</code>\n\
<b>Rating:</b> <code>{movie['rating'] if 'rating' in movie else 'Not Found'}</code>\n\
<b>Genre:</b> <code>{', '.join(movie['genres'])}</code>\n\
<b>Runtime:</b> <code>{movie['runtime'][0] if 'runtime' in movie else 'Not Found'}</code>\n\
<b>Writers:</b> <code>{', '.join(_writers)}</code>\n\
<b>Directors:</b> <code>{', '.join(_directors)}</code>\n\
<b>Actors:</b> <code>{', '.join(_casts)}</code>\n\
<b>Language:</b> <code>{movie['language'] if 'language' in movie else 'Not Found'}</code>\n\
<b>Country:</b> <code>{movie['country'] if 'country' in movie else 'Not Found'}</code>\n\
<b>Plot:</b> <code>{movie['plot outline'] if 'plot outline' in movie else 'Not available'}</code>\n\
    "
    try:
        update.effective_message.reply_photo(photo= movie['full-size cover url'], caption=info, reply_markup=InlineKeyboardMarkup(buttons), parse_mode=ParseMode.HTML)
    except KeyError:
        update.effective_message.reply_photo(photo= movie['cover url'], caption=info, reply_markup=InlineKeyboardMarkup(buttons), parse_mode=ParseMode.HTML)






IMDB_HANDLER = CommandHandler("imdb", imdb, run_async=True)

dispatcher.add_handler(IMDB_HANDLER)

__handlers__ = [
    IMDB_HANDLER
]

__mod_name__ = "IMDB"
__help__ = """
   ➢ `/imdb` <movie name> - To Get IMDB info about movie/show.

credits: rozari0   
"""