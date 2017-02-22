# coding:utf8
# it is a program about download music from Wang Yi Yun

# get the music list page from http://music.163.com/playlist?id=477352112
# save the MusicTitle-Singer to music_list.txt

import urllib


# start with:
# <ul class="f-hide"><li>

# end with:  (from start to.)
# </ul>


def get_useful_music_list_piece(music_list_url):
    music_list_page_in = urllib.urlopen(music_list_url).read()
    start_with = '<ul class="f-hide"><li>'
    start_index = music_list_page_in.find(start_with)
    end_with = '</ul>'
    end_index = music_list_page_in.find(end_with, start_index)
    useful_piece_in = music_list_page_in[start_index:end_index]
    return useful_piece_in


# need:
# href="/song?id=441489836"
# key_word 'href=' end with '"'


def get_song_id(useful_piece_in):
    songs_num = useful_piece_in.count("href=")

    music_id_url_list_in = []
    start_num = 0
    for number in range(0, songs_num):
        href_loc = useful_piece_in.find("href=", start_num)
        end_loc = useful_piece_in.find(">", href_loc)
        start_num = end_loc
        useful_id_href_not_finish = useful_piece_in[href_loc+6:end_loc-1]
        music_id_finish = "http://music.163.com"+useful_id_href_not_finish
        music_id_url_list_in.append(music_id_finish)

    return music_id_url_list_in

# /song?id=29787426
# http://music.163.com/#/song?id=29787426



"""
music_list_page_download = open("Music_page.html", "w+")
music_list_page_download.write(music_list_page)
music_list_page_download.close()
print "finished"

"""


# get the inf from http://music.163.com/#/song?id=25975503

# start with:
# <em class="f-ff2">

# end with:
# <div class="m-info">

def get_music_useful_pieces(music_url):
    music_url_page = urllib.urlopen(music_url).read()
    start_with = '<em class="f-ff2">'
    end_with = '<div class="m-info">'
    start_num = music_url_page.find(start_with)
    end_num = music_url_page.find(end_with)
    useful_music_piece = music_url_page[start_num:end_num]
    return useful_music_piece


def get_music_inf(useful_piece):
    music_name_start_num = useful_piece.find('<em class="f-ff2">')
    music_name_end_num = useful_piece.find("</em>")
    music_name = useful_piece[music_name_start_num+18:music_name_end_num]

    music_singer_start_num = useful_piece.find("<span title=")
    music_singer_end_num = useful_piece.find('">', music_singer_start_num)
    music_singer = useful_piece[music_singer_start_num+13:music_singer_end_num]

    return_text = "%s - %s" % (music_name, music_singer)
    return return_text


def save_into_txt(music_inf, number):
    save_file = open("music_list.txt", "a")
    write_text = str(number) + ":" + music_inf + "\n"
    save_file.write(write_text)
    save_file.close()


# ------------------------Main------------------------
'''
music_list_url_out = "http://music.163.com/playlist?id=477352112"

music_page = get_music_list_page(music_list_url_out)
useful_piece = get_useful_piece(music_page)
music_id_url_list = get_song_id(useful_piece)

'''

user_url = "http://music.163.com/playlist?id=477352112"

useful_piece_music_list = get_useful_music_list_piece(user_url)
song_url_list = get_song_id(useful_piece_music_list)


music_amount = len(song_url_list)
music_number = 1
for each_music_url in song_url_list:
    print "No." + str(music_number)
    useful_piece_music = get_music_useful_pieces(each_music_url)
    song_inf = get_music_inf(useful_piece_music)
    save_into_txt(song_inf, music_number)
    music_number += 1


print "finished"
