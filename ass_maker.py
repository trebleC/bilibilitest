#coding:utf-8


def make_ass(filename, info, path):
    file_content = '''[Script Info]
Title: Default ASS file
ScriptType: v4.00+
WrapStyle: 2
Collisions: Normal
PlayResX: 960
PlayResY: 720
ScaledBorderAndShadow: yes
Video Zoom Percent: 1

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,微软雅黑,20,&H00FFFFFF,&H00FFFFFF,&H28533B3B,&H500E0A00,0,0,0,0,100.0,100.0,0.0,0.0,1,3.5546875,3.0,2,10,10,5,1
Style: left_down,微软雅黑,20,&H00FFFFFF,&H00FFFFFF,&H28533B3B,&H500E0A00,0,0,0,0,100.0,100.0,0.0,0.0,1,3.5546875,3.0,1,10,10,5,1
Style: right_down,微软雅黑,20,&H00FFFFFF,&H00FFFFFF,&H28533B3B,&H500E0A00,0,0,0,0,100.0,100.0,0.0,0.0,1,3.5546875,3.0,3,10,10,5,1
Style: left_up,微软雅黑,20,&H00FFFFFF,&H00FFFFFF,&H28533B3B,&H500E0A00,0,0,0,0,100.0,100.0,0.0,0.0,1,3.5546875,3.0,7,10,10,5,1
Style: right_up,微软雅黑,20,&H00FFFFFF,&H00FFFFFF,&H28533B3B,&H500E0A00,0,0,0,0,100.0,100.0,0.0,0.0,1,3.5546875,3.0,9,10,10,5,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 2,0:00:00.00,99:00:00.00,left_down,,0,0,0,,'''+info+'''
Dialogue: 2,0:00:00.00,99:00:00.00,right_down,,0,0,0,,基于树莓派3B，已开源\\N源码见https://github.com/chenxuuu/24h-raspberry-live-on-bilibili
Dialogue: 2,0:00:00.00,99:00:00.00,left_up,,0,0,0,,晨旭的树莓派点歌台~
Dialogue: 2,0:00:00.00,99:00:00.00,right_up,,0,0,0,,弹幕点歌方法：\\N发送song+音乐名，可搜索点歌\\N发送id+网易云歌曲id，可按id点歌\\N发送mv+MV名，可点播网易云MV\\N发送mvid+网易云MV id，可按id点MV\\N请点播十分钟内的歌曲\\N测试点歌台，功能不断完善中
'''
    file = open(path+'/downloads/'+str(filename)+'.ass','w')
    file.write(file_content)
    file.close()