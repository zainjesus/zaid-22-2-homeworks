from aiogram import types, Dispatcher
import hashlib

from youtube_search import YoutubeSearch as YT


def finder(text):
    return YT(text, max_results=10).to_dict()


async def inline_wiki_handler(query: types.InlineQuery):
    text = query.query or "Python"
    link = f"https://ru.wikipedia.org/wiki/{text}"

    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        url=link,
        thumb_url="https://pbs.twimg.com/media/E-1gDMNWUAAXq8k.jpg",
        input_message_content=types.InputMessageContent(
            message_text=f"Лови ссылку сыночек\n{link}"
        )
    )]

    await query.answer(articles, cache_time=60)


def register_handler_inline(dp: Dispatcher):
    dp.register_inline_handler(inline_wiki_handler)
