# Instructions on how to download the .amz file for an Amazon mp3 purchase.

# Introduction #

The question is often asked "How do I get the .amz file from Amazon so I can
download my music?"

This page has been created to answer that question. Simply follow the pictorial
instructions below.


# Instructions #

The way the Amazon mp3 site works is that it looks for a cookie in your browser
that is set when you download the proprietary amazon mp3 downloader. If that
cookie exists, then the Amazon server will serve you the .amz file for your purchase.
Our task is to set this cookie without downloading and installing their proprietary
downloader.

First, you need to purchase an album from the Amazon mp3 via OneClick shopping:

![http://pymazon.googlecode.com/files/pymazon1.png](http://pymazon.googlecode.com/files/pymazon1.png)

Since you don't have the Amazon downloader installed (you _haven't_ installed it, right?),
you will be taken to the following screen which asks you download their software. On this screen, there is small text near the bottom that says "If you have already installed the Amazon MP3 downloader, click here to enable for use with this browser". Click that:

![http://pymazon.googlecode.com/files/pymazon2.png](http://pymazon.googlecode.com/files/pymazon2.png)

This will set the cookie in your browser. You will then be taken back to the order page where **you must again click on the one-click ordering button.**

After that, you will be take to a purchase overview screen. Click Continue:


![http://pymazon.googlecode.com/files/pymazon3.png](http://pymazon.googlecode.com/files/pymazon3.png)

The .amz file should now download to your machine. On my browser (Google Chrome) the download starts automatically. You may get a save dialog (or something similar) in Firefox or other browsers:

![http://pymazon.googlecode.com/files/pymazon4.png](http://pymazon.googlecode.com/files/pymazon4.png)


Now, open Pymazon and load this .amz file. Select your save dir and naming format and click download. It's that easy!


If you have any trouble, clear your browser cookies and try again!

If that still doesn't work, it may be Amazon getting crafty and/or your browser not taking the right cookie. You can manually set the cookie (I had to do this on Chrome and Firefox in order to download Albums with digital booklets and videos attached). The cookie you want to set is:

```
name: dmusic_download_manager_enabled
value: 1.0.10
domain: .amazon.com
path: /
expires: Wed 10 Jun 2010 12:21:08 AM EST
secure: No
```

There are Firefox and chrome extensions that let you manually set cookies. Google them.
