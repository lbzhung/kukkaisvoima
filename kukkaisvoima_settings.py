# -*- coding:UTF-8 -*-
"""

This file is part fo Kukkaisvoima. Kukkaisvoima a lightweight weblog
system.

Copyright (C) 2006-2008 Petteri Klemola

This is config file. Kukkaisvoima's license don't affect this file.

You should keep this file private and see that this in not readable
from public web. For example when using Apache webserver create
.htaccess file with the following entry:

<files kukkaisvoima_settings.py>
 order allow,deny
 deny from all
</files>

"""

# Config variables
# Url of the blog (without trailing /)
baseurl = 'http://yourdomain/blog/index.cgi'
# Use absolute url for this, like http://yourdomain/blog/kukka.css
stylesheet = 'http://www.yourhostname.info/kukka.css'
# Use absolute url for this, like http://yourdomain/blog/feed-icon-14x14.png
feedicon = 'http://www.yourhostname.info/feed.png'
blogname = 'blogname'
slogan = 'slogan'
description = "Jee"
encoding = 'UTF-8'
defaultauthor = 'You'
favicon = 'http://www.yourhostname.info/favicon.ico'
doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
# Email to send comments to
blogemail = 'you@yourdomain'
# Language for the feed
language = 'zh'
# time zone of GMT
timezone = '+0800'
# Number of entries per page
numberofentriesperpage = 4
# Directory which contains the blog entries
datadir = 'data'
# Directory which contains the index and comments. Must be script
# writable directory
indexdir = 'temp'
# Maximum comments per entry. Use -1 for no comments and 0 for no
# restriction
maxcomments = 30
# answer to spamquestion (question variable is l_nospam_question)
#nospamanswer = '5'
# This is admin password to manage comments. password should be
# something other than 'password'
passwd = 'password'
# Entry and comment Date format
dateformat = "%Y-%m-%d %H:%M:%S"
# Show only first paragraph when showing many entries
entrysummary = False

# Language variables
l_archives = '档案'
l_categories = '类别'
l_comments = '评论'
l_comments2 = '评论'
l_date = '日期'
l_nextpage = '下一页>>'
l_previouspage = '<<前一页'
l_leave_reply = '留个评论吧'
l_no_comments_allowed = '不允许评论'
l_no_comments = '没有评论'
l_name_needed = '名字 (必填)'
l_email_needed = '邮箱 (必填,不公开)'
l_webpage = '个人网站'
l_no_html = '回复不允许HTML标签'
#l_nospam_question = '2+3是多少?(必填)'
l_delete_comment = '删除评论'
l_passwd = '管理员密码'
l_admin = '管理'
l_admin_comments = '评论管理'
l_do_you_delete = '此处删除评论，你确定吗?'
# new in version 8
l_search = "搜索"
l_search2 = "找不到"
# new in version 10
l_recent_comments = "最近评论"
l_notify_comments= "如果有评论邮件通知我。"
# new in version 11
l_read_more = "...全文"
# new in version 12
l_toggle = "点击年份显示月份"
# footer
l_footer = '<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="知识共享许可协议" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />本博客采用<a rel="license" href="http://creativecommons.org/licenses/by/3.0/">知识共享署名 3.0 Unported许可协议</a>进行许可。'
