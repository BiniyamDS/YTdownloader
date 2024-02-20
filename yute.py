#!/usr/bin/python3
import sys
import os
from pytube import YouTube
from pytube import Playlist


if (len(sys.argv) != 3):
   print('Please enter youtube link and tag')
   exit(1)

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    liveprogress = (bytes_downloaded / total_size) *  100
    print(f"Download progress: {liveprogress:.2f}% - {bytes_downloaded / (1024 *1024):.2f} out of {total_size / (1024 * 1204):.2f}", end='\r')

def downloadSingle(link, path=''):
    dPath = '/home/roha/Documents/Youtube/' + path
    try:
      youtubeObject = YouTube(link, on_progress_callback=progress_function)
      youtubeObject = youtubeObject.streams.get_highest_resolution()
      print(f"Downloading {youtubeObject.title}")
      youtubeObject.download(dPath)
      sys.stdout.write('\033[K')
      print("Download is completed successfully")
    except Exception as e:
      print(f"An error has occurred: {e}")


def donwloadPlaylist(link):
    playObj = Playlist(link)
    print(f'Downloading {playObj.title}')
    count = 1
    for url in playObj.video_urls:
       print(f"Dowloading {count}/ {len(playObj.video_urls)}")
       downloadSingle(url, playObj.title)
       count += 1
    print('Finshed downloading playlist')
    

link = sys.argv[2]
tag = sys.argv[1]
if tag == '-s':
  print('Starting download for a single video....')
  downloadSingle(link)
elif tag == '-p':
  print('Starting download for a playlist....')
  donwloadPlaylist(link)
else:
   print('unsupported tag')   

