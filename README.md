# 百万资源网下载器 baiwanzy-downloader
Pick highest quality(movie), create directory(warning if directory exist) and save as relevant filenames automatically with just paste baiwanzy url

### Usage (Please ensure you copy-paste the correct format of url in video detail page):

    xb@dnxb:~/Downloads$ python baiwanzy.py http://baiwanzy.com/?m=vod-detail-id-25954.html
    Random UA: Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24
    [ 1/15 ] episode name: /home/xiaobai/Downloads/包青天再起风云粤语/包青天再起风云粤语_第01集
    source url: https://videos7.jsyunbf.com/20190722/9DbC2641/index.m3u8
    [generic] index: Requesting header
    [generic] index: Downloading m3u8 information
    [download] Destination: /home/xiaobai/Downloads/包青天再起风云粤语/包青天再起风云粤语_第01集.mp4
    ffmpeg version 3.4.6-0ubuntu0.18.04.1 Copyright (c) 2000-2019 the FFmpeg developers
    built with gcc 7 (Ubuntu 7.3.0-16ubuntu3)
    configuration: --prefix=/usr --extra-version=0ubuntu0.18.04.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared
    WARNING: library configuration mismatch
    avcodec     configuration: --prefix=/usr --extra-version=0ubuntu0.18.04.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared --enable-version3 --disable-doc --disable-programs --enable-libopencore_amrnb --enable-libopencore_amrwb --enable-libtesseract --enable-libvo_amrwbenc
    libavutil      55. 78.100 / 55. 78.100
    libavcodec     57.107.100 / 57.107.100
    libavformat    57. 83.100 / 57. 83.100
    libavdevice    57. 10.100 / 57. 10.100
    libavfilter     6.107.100 /  6.107.100
    libavresample   3.  7.  0 /  3.  7.  0
    libswscale      4.  8.100 /  4.  8.100
    libswresample   2.  9.100 /  2.  9.100
    libpostproc    54.  7.100 / 54.  7.100
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267000.ts' for reading
    Input #0, hls,applehttp, from 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/index.m3u8':
    Duration: 00:42:46.44, start: 1.497000, bitrate: 0 kb/s
    Program 0 
        Metadata:
        variant_bitrate : 0
        Stream #0:0: Video: h264 (High) ([27][0][0][0] / 0x001B), yuv420p, 1280x720, 25 tbr, 90k tbn, 50 tbc
        Metadata:
        variant_bitrate : 0
        Stream #0:1: Audio: aac (LC) ([15][0][0][0] / 0x000F), 44100 Hz, stereo, fltp
        Metadata:
        variant_bitrate : 0
    Output #0, mp4, to 'file:/home/xiaobai/Downloads/包青天再起风云粤语/包青天再起风云粤语_第01集.mp4.part':
    Metadata:
        encoder         : Lavf57.83.100
        Stream #0:0: Video: h264 (High) (avc1 / 0x31637661), yuv420p, 1280x720, q=2-31, 25 tbr, 90k tbn, 90k tbc
        Metadata:
        variant_bitrate : 0
        Stream #0:1: Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp
        Metadata:
        variant_bitrate : 0
    Stream mapping:
    Stream #0:0 -> #0:0 (copy)
    Stream #0:1 -> #0:1 (copy)
    Press [q] to stop, [?] for help
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267001.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267002.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267003.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267004.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267005.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267006.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267007.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267008.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267009.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267010.ts' for reading
    [hls,applehttp @ 0x5619491b6940] Opening 'https://videos7.jsyunbf.com/20190722/9DbC2641/900kb/hls/lYTUSWIJ5267011.ts' for reading
    ...

### Directory and filename created with relevant name automatically:

    xb@dnxb:~/Downloads$ l 包青天再起风云粤语/
    total 149M
    41804757 drwxrwxr-x   2 xiaobai xiaobai ? 4.0K Ogos 11 05:37 ./
    41680908 drwxr-xr-x 266 xiaobai xiaobai ? 204K Ogos 11 05:42 ../
    41687335 -rw-rw-r--   1 xiaobai xiaobai ? 149M Ogos 11 05:45 包青天再起风云粤语_第01集.mp4.part
    xb@dnxb:~/Downloads$ 

### If already downloaded before, it will shows warning and skipped, e.g.:

    xb@dnxb:~/Downloads$ python baiwanzy.py http://baiwanzy.com/?m=vod-detail-id-21978.html
    Random UA: Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36

    /home/xiaobai/Downloads/降伏魔女的手段 already exists.
                        Are you sure you want to download inside /home/xiaobai/Downloads/降伏魔女的手段  ? [y/n] : y
    [ 1/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第01集
    source url: https://videos.bwzybf.com/2019/01/16/LbXIckKuEl1YqIy1/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第01集.mp4 has already been downloaded
    [download] 100% of 358.16MiB
    [ 2/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第12集
    source url: https://videos.bwzybf.com/2019/01/16/k9LVarcspvbxSCIX/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第12集.mp4 has already been downloaded
    [download] 100% of 400.20MiB
    [ 3/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第17集
    source url: https://videos.bwzybf.com/2019/01/16/ds11jqoRzoeu2UyG/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第17集.mp4 has already been downloaded
    [download] 100% of 419.87MiB
    [ 4/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第18集
    source url: https://videos.bwzybf.com/2019/01/16/oFHTvnN6dXHj32kW/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第18集.mp4 has already been downloaded
    [download] 100% of 444.18MiB
    [ 5/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第13集
    source url: https://videos.bwzybf.com/2019/01/16/PX7AY3x0UOrm2D5Q/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第13集.mp4 has already been downloaded
    [download] 100% of 399.73MiB
    [ 6/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第15集
    source url: https://videos.bwzybf.com/2019/01/16/UYwi573rnYDO5MRF/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第15集.mp4 has already been downloaded
    [download] 100% of 418.29MiB
    [ 7/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第04集
    source url: https://videos.bwzybf.com/2019/01/16/zanXVBovtKKb2gQk/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第04集.mp4 has already been downloaded
    [download] 100% of 368.60MiB
    [ 8/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第11集
    source url: https://videos.bwzybf.com/2019/01/16/J5wI6WkOU6quYNX0/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第11集.mp4 has already been downloaded
    [download] 100% of 389.73MiB
    [ 9/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第10集
    source url: https://videos.bwzybf.com/2019/01/16/Wv0VtQVuPuqs8OtN/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第10集.mp4 has already been downloaded
    [download] 100% of 422.57MiB
    [ 10/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第02集
    source url: https://videos.bwzybf.com/2019/01/16/Ictrmmar5Gbx6OXv/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第02集.mp4 has already been downloaded
    [download] 100% of 374.06MiB
    [ 11/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第06集
    source url: https://videos.bwzybf.com/2019/01/16/GokY8NxXOmJtR0Sl/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第06集.mp4 has already been downloaded
    [download] 100% of 399.14MiB
    [ 12/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第07集
    source url: https://videos.bwzybf.com/2019/01/16/aVHm9xe04bo1V2GM/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第07集.mp4 has already been downloaded
    [download] 100% of 445.05MiB
    [ 13/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第05集
    source url: https://videos.bwzybf.com/2019/01/16/1QIBJoQsBCK24Gd6/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第05集.mp4 has already been downloaded
    [download] 100% of 355.59MiB
    [ 14/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第03集
    source url: https://videos.bwzybf.com/2019/01/16/c74s6aW6Tve5OqwT/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第03集.mp4 has already been downloaded
    [download] 100% of 422.35MiB
    [ 15/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第09集
    source url: https://videos.bwzybf.com/2019/01/16/ZvDVVzQ9JxWiRy7S/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第09集.mp4 has already been downloaded
    [download] 100% of 399.38MiB
    [ 16/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第16集
    source url: https://videos.bwzybf.com/2019/01/16/l8slgenhBl4ICQ7p/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第16集.mp4 has already been downloaded
    [download] 100% of 400.17MiB
    [ 17/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第14集
    source url: https://videos.bwzybf.com/2019/01/16/KxRY3wuNkUzKO8KN/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第14集.mp4 has already been downloaded
    [download] 100% of 409.90MiB
    [ 18/18 ] episode name: /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第08集
    source url: https://videos.bwzybf.com/2019/01/16/EIZbtBSnzMCdvvQE/playlist.m3u8
    [generic] playlist: Requesting header
    [generic] playlist: Downloading m3u8 information
    [download] /home/xiaobai/Downloads/降伏魔女的手段/降伏魔女的手段_第08集.mp4 has already been downloaded
    [download] 100% of 395.64MiB
    xb@dnxb:~/Downloads$ l 降伏魔女的手段/
    total 7.1G
    42152369 -rw-rw-r--   1 xiaobai xiaobai ? 359M Jul  30 05:32 降伏魔女的手段_第01集.mp4
    42152373 -rw-rw-r--   1 xiaobai xiaobai ? 401M Jul  30 05:57 降伏魔女的手段_第12集.mp4
    42152375 -rw-rw-r--   1 xiaobai xiaobai ? 420M Jul  30 06:38 降伏魔女的手段_第17集.mp4
    42152376 -rw-rw-r--   1 xiaobai xiaobai ? 445M Jul  30 07:12 降伏魔女的手段_第18集.mp4
    42152377 -rw-rw-r--   1 xiaobai xiaobai ? 400M Jul  30 07:37 降伏魔女的手段_第13集.mp4
    42152378 -rw-rw-r--   1 xiaobai xiaobai ? 419M Jul  30 08:10 降伏魔女的手段_第15集.mp4
    42152379 -rw-rw-r--   1 xiaobai xiaobai ? 369M Jul  30 08:44 降伏魔女的手段_第04集.mp4
    42152380 -rw-rw-r--   1 xiaobai xiaobai ? 390M Jul  30 09:11 降伏魔女的手段_第11集.mp4
    42152381 -rw-rw-r--   1 xiaobai xiaobai ? 423M Jul  30 09:50 降伏魔女的手段_第10集.mp4
    42152382 -rw-rw-r--   1 xiaobai xiaobai ? 375M Ogos  4 05:08 降伏魔女的手段_第02集.mp4
    42151966 -rw-rw-r--   1 xiaobai xiaobai ? 400M Ogos  4 05:29 降伏魔女的手段_第06集.mp4
    42152248 -rw-rw-r--   1 xiaobai xiaobai ? 446M Ogos  4 05:54 降伏魔女的手段_第07集.mp4
    42152249 -rw-rw-r--   1 xiaobai xiaobai ? 356M Ogos  4 06:13 降伏魔女的手段_第05集.mp4
    42152250 -rw-rw-r--   1 xiaobai xiaobai ? 423M Ogos  4 06:36 降伏魔女的手段_第03集.mp4
    42152251 -rw-rw-r--   1 xiaobai xiaobai ? 400M Ogos  4 06:58 降伏魔女的手段_第09集.mp4
    42152252 -rw-rw-r--   1 xiaobai xiaobai ? 401M Ogos  4 07:20 降伏魔女的手段_第16集.mp4
    42152253 -rw-rw-r--   1 xiaobai xiaobai ? 410M Ogos  4 07:43 降伏魔女的手段_第14集.mp4
    42152254 -rw-rw-r--   1 xiaobai xiaobai ? 396M Ogos  4 08:05 降伏魔女的手段_第08集.mp4
    42165213 drwxrwxr-x   2 xiaobai xiaobai ? 4.0K Ogos  4 08:05 ./
    41680908 drwxr-xr-x 265 xiaobai xiaobai ? 204K Ogos 11 05:36 ../
    xb@dnxb:~/Downloads$ 

