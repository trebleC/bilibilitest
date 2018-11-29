#coding:utf-8

#需要修改的值

deviceType = "vps"
#设备类型，可选类型为"pi"和"vps"，区分大小写

path = '/24h-raspberry-live-on-bilibili'
#本文件的路径，请修改

roomid = '3019948'
#房间id（真实id，不一定是网址里的那个数）

cookie = 'pgv_pvi=8627912704; fts=1506506250; rpdid=kwmwxsomlmdoswxswxoxw; LIVE_BUVID=6b0915603a3b82af6141060d94ed410f; LIVE_BUVID__ckMd5=7ab3ede41277e999; uTZ=-480; LIVE_PLAYER_TYPE=2; im_notify_type_33928665=0; __clickidc=152222226114295585; a=RPTwd0o90SP7; buvid3=1D16F0F2-C69B-4F29-AD26-5A8D7ACD233412256infoc; sid=i6u54xgk; stardustvideo=1; UM_distinctid=1664a5bd9d2147-07267c0ae7c26d-9393265-100200-1664a5bd9d333c; CURRENT_FNVAL=16; finger=edc6ecda; bp_t_offset_33928665=189563179089295955; DedeUserID=33928665; DedeUserID__ckMd5=5ab5bb8fc3e32362; SESSDATA=8868cb73%2C1545899036%2Cc56400b1; bili_jct=e0870124bf99983417e3a749eb95a9e4; CURRENT_QUALITY=32; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1543430457,1543434640,1543437644,1543439272; im_local_unread_33928665=0; im_seqno_33928665=19; _dfcaptcha=a4e92e6a54a5f4319ac3d7491a0a80a6; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1543480607'
#发送弹幕用的cookie
csrf_token = 'e0870124bf99983417e3a749eb95a9e4'
#发送弹幕用的csrf_token

download_api_url = 'https://qq.papapoi.com/163music/'
#获取音乐链接的api网址，服务器性能有限，尽量请换成自己的，php文件在php文件夹

rtmp = 'rtmp://js.live-send.acg.tv/live-js/'
#直播给的两个码，填在这里
live_code = '?streamname=live_33928665_3854859&key=e78d1b73427a9a62f30da06536ba476b'

free_space=15360
#允许download/default_mp3文件夹占用空间大小，超过时自动按时间顺序删除视频/音乐，单位：MiB

maxbitrate='3000'
#允许的最大码率，单位k，字符串类型，切勿改成数值型

dm_size=20
#每段弹幕的最大长度（20级以后可发30字）

use_gift_check = False
#是否使用投礼物才让点歌的设定

play_videos_when_night = False
#是否播放晚间专属视频？
