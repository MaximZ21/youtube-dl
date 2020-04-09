# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import urljoin
import re


class ArchiverreeIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?yourextractor\.com/watch/(?P<id>[0-9]+)'
    _VALID_URL = r'http?:\/\/arhiiv\.err\.ee\/vaata\/(?P<id>[a-zA-Z-0-9]+)[\/[a-zA-Z0-9-]*]?'
    _TEST = {
        'url': 'http://arhiiv.err.ee/vaata/igihaljaid-hetki-etendusest-armastus-kolme-apelsini-vastu/popular-week',
        'info_dict': {
            'id': 'igihaljaid-hetki-etendusest-armastus-kolme-apelsini-vastu',
            'ext': 'mp4',
            'title': 'Igihaljaid hetki etendusest "Armastus kolme apelsini vastu"'
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        f = open("out","w+")
        f.write(f"Start\n")
        video_id = self._match_id(url)
        f.write(f"Video ID: {video_id}\n")
        webpage = self._download_webpage(url, video_id)
        var = urljoin('http:/', re.search(r'src: {\'hls\': \'(.+?\.m3u8)\'}', webpage).group(1))
        f.write(f"Re search: {var}")
        formats = self._extract_m3u8_formats(
            urljoin('http:', re.search(r'src: {\'hls\': \'(.+?\.m3u8)\'}', webpage).group(1)),
            video_id, 'mp4', entry_protocol='m3u8_native', m3u8_id='hls')

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')
        f.write(f"TITLE: {title}")

        return {
            'id': video_id,
            'title': title,
            'formats': formats
        }