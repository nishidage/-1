#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2021
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains an object that represents a Telegram Document."""

from typing import TYPE_CHECKING, Any

from telegram import PhotoSize
from telegram._files._basethumbedmedium import _BaseThumbedMedium

if TYPE_CHECKING:
    from telegram import Bot


class Document(_BaseThumbedMedium):
    """This object represents a general file
    (as opposed to photos, voice messages and audio files).

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`file_unique_id` is equal.

    Args:
        file_id (:obj:`str`): Identifier for this file, which can be used to download
            or reuse the file.
        file_unique_id (:obj:`str`): Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used to download or reuse the file.
        thumb (:class:`telegram.PhotoSize`, optional): Document thumbnail as defined by sender.
        file_name (:obj:`str`, optional): Original filename as defined by sender.
        mime_type (:obj:`str`, optional): MIME type of the file as defined by sender.
        file_size (:obj:`int`, optional): File size.
        bot (:class:`telegram.Bot`, optional): The Bot to use for instance methods.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        file_id (:obj:`str`): File identifier.
        file_unique_id (:obj:`str`): Unique identifier for this file, which
            is supposed to be the same over time and for different bots.
            Can't be used to download or reuse the file.
        thumb (:class:`telegram.PhotoSize`): Optional. Document thumbnail.
        file_name (:obj:`str`): Original filename.
        mime_type (:obj:`str`): Optional. MIME type of the file.
        file_size (:obj:`int`): Optional. File size.
        bot (:class:`telegram.Bot`): Optional. The Bot to use for instance methods.

    """

    __slots__ = ('file_name', 'mime_type')

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        thumb: PhotoSize = None,
        file_name: str = None,
        mime_type: str = None,
        file_size: int = None,
        bot: 'Bot' = None,
        **_kwargs: Any,
    ):
        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            file_size=file_size,
            thumb=thumb,
            bot=bot,
        )
        # Optional
        self.mime_type = mime_type
        self.file_name = file_name
