import logging
import os
from Config import Messages as tr
from Config import Config as C
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
UPDATES_CHANNEL = C.UPDATES_CHANNEL
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.incoming & filters.command(['start']) & filters.private)
async def _start(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               await client.send_message(
                   chat_id=message.chat.id,
                   text="ببورە بەڕێزم, تۆ قەدەغە کراویت لە بەکار هێنانی من. پەیوەندی بکە بە [گرووپی پشتگیری](https://t.me/qawaxanaykltury).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text="**بەڕێزمم بۆ بەکار هێنانی من جۆینی  کەناڵەکەم بکە**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("کەناڵی نوێگەری", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(message.chat.id,
                text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
	        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                           InlineKeyboardButton("کەناڵی نوێگەری", url="https://t.me/kteb1"),
                           InlineKeyboardButton("گرووپی پشتگیری", url="https://t.me/qawaxanaykltury")
                      ],
                     [
                           InlineKeyboardButton("🧑‍💻داهێنەر🧑‍💻", url="https://t.me/MrMamo007")
                     ]
                 ]
             ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
            return
    await client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("کەناڵی نوێگەری", url="https://t.me/kteb1"),
                    InlineKeyboardButton("گرووپی پشتگیری", url="https://t.me/qawaxanaykltury")
                ],
                [
                    InlineKeyboardButton("🧑‍💻داهێنەر🧑‍💻", url="https://t.me/MrMamo007")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )


@Client.on_message(filters.incoming & filters.command(['source_code']) & filters.private)
async def _source_code(client, message):
    await client.send_message(message.chat.id,
        text=tr.SC_MSG.format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
                # [
                #     InlineKeyboardButton("Souce Code", url="https://github.com/sjmxaditi/ForceSub_Bot")
                # ],
                [
                    InlineKeyboardButton("کەناڵی نوێگەری", url="https://t.me/kteb1"),
                    InlineKeyboardButton("گرووپی پشتگیری", url="https://t.me/qawaxanaykltury")
                ],
                [
                    InlineKeyboardButton("🧑‍💻داهێنەر🧑‍💻", url="https://t.me/MrMamo007")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.incoming & filters.command(['help']) & filters.private)
async def _help(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               await client.send_message(
                   chat_id=message.chat.id,
                   text="ببورە گەورەم, تۆ قەدەغە کراویت لە بەکار هێنانی من. پەیوەندی بکە بە [گرووپی پشتگیری](https://t.me/qawaxanaykltury).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text="**بەڕێزمم بۆ بەکار هێنانی من جۆینی  کەناڵەکەم بکە**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("کەناڵی نوێگەری", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.chat.id,
                text="سڵاو، ئەم فرمانەم بە نامەی تایبەت پێبدە! \nبۆ وەرگرتنی زانیاری زیاتر پرسیار بکە لە [گرووپی پشتگیری](https://t.me/qawaxanaykltury).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
async def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    await client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '-->', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        button = [
            [InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '-->', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
