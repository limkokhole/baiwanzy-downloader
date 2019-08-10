# -*- coding: utf-8 -*-
from __future__ import unicode_literals #make python2 act as python3 unicode
# The MIT License (MIT)
# Copyright (c) 2019 limkokhole@gmail.com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
#from __future__ import absolute_import

__author__ = 'Lim Kok Hole'
__copyright__ = 'Copyright 2019'
__credits__ = []
__license__ = 'MIT'
__version__ = '1.0.1'
__maintainer__ = 'Lim Kok Hole'
__email__ = 'limkokhole@gmail.com'
__status__ = 'Production'

import sys, os, traceback
import youtube_dl
#import m3u8 #https://github.com/limkokhole/m3u8-Downloader

PY3 = sys.version_info[0] >= 3
if PY3:
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.parse import urlparse
    import urllib.request
    def unicode(mystr): #python3
        return mystr
    import html
else:
    from urllib2 import urlopen, HTTPError
    import urllib2
    from urlparse import urlparse
    input = raw_input
    from HTMLParser import HTMLParser
    html_parser = HTMLParser() #again, don't conflict name with other vars "parser"
try: from bs4 import BeautifulSoup, SoupStrainer #python3 #python2 also got, and python need use this or else error when `soup = BeautifulSoup(r, "lxml")` 
except ImportError: from BeautifulSoup import BeautifulSoup, SoupStrainer #python2


#https://github.com/limkokhole/random_user_agent
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
# Get Random User Agent String.
UA = user_agent_rotator.get_random_user_agent()
#UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

import argparse
arg_parser = argparse.ArgumentParser(description='Baiwanzy Downloader')
args = ""
def scrape_web(url):
    if args.d:
        print("Random UA: " + UA)
    try:
        
        if PY3:
            req = urllib.request.Request(url, data=None, headers={ 'User-Agent': UA })
            r = urllib.request.urlopen(req).read()
        else:
            req = urllib2.Request(url, headers={ 'User-Agent': UA })
            r = urllib2.urlopen(req).read()
    except Exception as e:
        print(e)
        print("Please check your network OR url.")
        os._exit(1)
    #print(r)
    soup = BeautifulSoup(r, "lxml")
    if args.d:
        print(soup)
    output_path_raw = None

    output_f = None
    for vnames in soup.find_all('div','vodh'):
        #https://stackoverflow.com/questions/22602279/beutifulsoup-parse-get-information-from-child-tag
        #print('Video name: ' + vnames.h2.text)
        output_f = os.path.basename(vnames.h2.text) #sanity ..

    if not output_f:
        print('No title found, Abort.')
        sys.exit()

    episode_m3u8 = {}
    add_gaoqing_once = False
    for divs in soup.find_all('div','vodplayinfo'):
        for div in divs.find_all('div'):
            if div.h3 and '来源' in div.h3.text:
                for li in div.find_all('li'):
                    source_url = li.input.get('value', '')
                    if source_url.endswith('.m3u8'):
                        #print(li.text) #第01集$https://videos8.jsyunbf.com/20190514/ywe2ene6/index.m3u8
                        episode_title = li.text.strip().split('$')[0]
                        if '集' not in episode_title and \
                             not (len(episode_title) >= 2 and episode_title[0].isdigit() and episode_title[1].isdigit()): #movie, not series

                            if add_gaoqing_once and ('超清' not in episode_title): #keep replace but don't replace by non-超清。
                                continue
                            if '超清' in episode_title:
                                add_gaoqing_once = True
                            episode_m3u8 = {} #replace by reset first

                        #test long filename error and ask for -s   
                        #episode_title = '大马老千诈骗套路 ] 切记小心 !😥  原来诈骗集团的套路是这样的！还出动到警长😱 真的是我人生中第一次遇到！我真的觉得自己太愚蠢😣了！ 因为正好讲中'*1000 + episode_title
                        #no nid + '.mp4', just let youtube-dl add by .%(ext)s
                        #if args.s > 0:
                        #    episode_title = episode_title[-args.s:]
                        final_path = os.path.basename( '_'.join([ output_f, os.path.basename(episode_title)]) )
                        if args.s > 0:
                            final_path = final_path[-args.s:]
                        episode_m3u8[ final_path] = source_url
    #downloader = m3u8.Downloader(50)
    #downloader.run('https://videos7.jsyunbf.com/20190709/BGS02mF6/index.m3u8', '.')

    d_name = None
    if len(episode_m3u8) > 1: #is series
        if args.s > 0:
            output_f = output_f[-args.s:]
        output_path_raw = os.path.join(os.getcwd(), output_f)
        d_name = output_path_raw
        if (not os.path.isdir(d_name)):
            os.makedirs(d_name)
        else:
            if PY3:
                answer = input('\n' + d_name + ' already exists.\n\
                    Are you sure you want to download inside ' + d_name + '  ? [y/n] : ')
            else:
                answer = input( ('\n' + d_name + ' already exists.\n\
                    Are you sure you want to download inside ' + d_name + '  ? [y/n] : ').encode('utf-8') )
            if not answer or answer[0].lower() != 'y': #yes is works bcoz get index [0]-only
                sys.exit()

    real_episode_m3u8 = {}
    
    if d_name:
        log_prefix = 'episode name'
        for episode, m3u8 in episode_m3u8.items():
            real_episode_m3u8[ os.path.join(d_name, episode) ] = m3u8
    else:
        log_prefix = 'movie name'
        real_episode_m3u8 = episode_m3u8

    total_episodes = len(real_episode_m3u8)
    download_index = 0
    #[todo:0] make dict in order 
    for episode_name, source_url in real_episode_m3u8.items():
        download_index+=1
        print( '[ ' + str(download_index) + '/' + str(total_episodes) + ' ]'
            + ' ' + log_prefix + ': ' + episode_name)
        print('source url: ' + source_url)
        #source_url = 'https://videos7.jsyunbf.com/20190709/BGS02mF6/index.m3u8'
        #https://stackoverflow.com/questions/52736897/custom-user-agent-in-youtube-dl-python-script
        youtube_dl.utils.std_headers['User-Agent'] = UA
        #youtube_dl.YoutubeDL( params={'-c': '', '--no-mtime': '', 'outtmpl': './%(uploader)s/%(title)s-%(upload_date)s-%(id)s.%(ext)s'} ).download([source_url])
        try:
            youtube_dl.YoutubeDL( params={'-c': '', '-g': '', '-q': '', '--no-mtime': '', 'outtmpl': episode_name + '.%(ext)s'} ).download([source_url])
        except youtube_dl.utils.DownloadError:
            print(traceback.format_exc())
            print('Possible reason is filename too long. Please retry with -s <maximum filename size>.')
            sys.exit()

if __name__ == "__main__":
    arg_parser.add_argument('-d', action='store_true', help='Debug by print the html.')
    arg_parser.add_argument('-s',  default=-1, type=int, help='Specify the maximum filename size.')
    arg_parser.add_argument('url', nargs='?', help='baiwanzy url') 
    args, remaining  = arg_parser.parse_known_args()
    if ( (args.s != -1) and (args.s < 1) ) or (args.s == 0): #no nid care if user insert -1, just ignore
        print('-s ' + str(args.s) + ', please specify a sensible -s maximum filename size. Abort.')
        sys.exit()
    if args.url:
        url = args.url
    else:
        if PY3:
            url = input('百万资源网 URL: ').strip()
        else: #https://bugs.python.org/issue7768
            url = input('百万资源网 URL: '.encode('utf-8')).strip()
    scrape_web(url)
