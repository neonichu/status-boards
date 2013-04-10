#!/usr/bin/env python

##
## Generate a table of your App.Net posts for Status Board by Panic.
##
## See http://panic.com/statusboard/
##

from BeautifulSoup import BeautifulSoup as soup
from datetime import datetime
from relativeDates import timesince
from time import mktime

import feedparser
import sys
import urllib2

TD_AVATAR = '<td class="avatar"><img src="%s" style="width:40px;"/></td>\n'
TD_POST   = '<td class="post">%s<br/><b style="margin-top: 5px;">%s</b> %s\n'


def get_avatar(username):
    html = soup(urllib2.urlopen('https://alpha.app.net/%s' % username))
    for a in html('a', {'class': 'avatar large'}):
        return a['style'].split('(')[1].split(')')[0]


def get_posts(username, avatar_url):
    posts_str = '<table id="posts">\n'

    feed_url = 'https://alpha-api.app.net/feed/rss/users/@%s/posts' % username
    feed = feedparser.parse(feed_url)

    for item in feed['items']:
      date = datetime.fromtimestamp(mktime(item['published_parsed']))
      date = '%s ago' % timesince(date)

      posts_str += '<tr>\n'
      posts_str += TD_AVATAR % avatar_url
      posts_str += TD_POST % (item['title'], username, date)
      posts_str += '</tr>\n'

    posts_str += '</table>\n'

    return posts_str


if __name__ == '__main__':
    username = sys.argv[1] if len(sys.argv) > 1 else 'neonacho'

    avatar_url = get_avatar(username)
    print get_posts(username, avatar_url).encode('utf8')
