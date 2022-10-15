from pytube import YouTube 


def download_Video(yt):  
  
  # Filter streams from object
  my_streams = yt.streams.filter(file_extension='mp4',only_video=True)

  # Columns 
  print("Video iTag\tResolution\t File Size")

  for streams in my_streams:
    # Print video itag, resolution, and file size of Mp4 streams
    print(f"{streams.itag} \t\t{streams.resolution}\t\t", end= " ")

    # Converts and prints filesize of stream from bytes into MBs
    size = yt.streams.get_by_itag(streams.itag).filesize
    print(str(round(size/ (1024 * 1024), 2)) + ' MBs')
    
    
  # Enter the video itag to download 
  input_itag = input("\nEnter Video itag: ")
  print()
  
  # Saves vidoe to stream based on itag value
  video = yt.streams.get_by_itag(input_itag)
  
  # File name notification
  print("Video is Downloading as VIDEO ONLY -",yt.title + ".mp4")
  print()

  # Downloads and adds prefix to file
  video.download(filename_prefix = "VIDEO ONLY - ")
  
  print("Video Download Complete.")
  print()



def download_Audio(yt):
  
  # Filter streams from object
  my_streams = yt.streams.filter(file_extension='mp4',only_audio=True)

  # Columns 
  print("Audio iTag\tFile Size")

  for streams in my_streams:
    # Print audio itag and file size of Mp4 streams
    print(f"{streams.itag} \t\t", end= " ")

    # Converts and prints filesize of stream from bytes into MBs
    size = yt.streams.get_by_itag(streams.itag).filesize
    print(str(round(size/ (1024 * 1024), 2)) + ' MBs')
    
    
  # Enter the audio itag to download  
  input_itag = input("\nEnter Video itag: ")
  print()
  
  # Saves vidoe to stream based on itag value
  video = yt.streams.get_by_itag(input_itag)
  
  # File name notification
  print("Audio is Downloading as AUDIO ONLY -",yt.title + ".mp4")
  print()

  # Downloads and adds prefix to file
  video.download(filename_prefix = "AUDIO ONLY - ")
  
  print("Audio Download Complete.")
  print()



try:  
  url = input("Enter YouTube URL: ")
  print()

  # Creates YouTube Object
  yt = YouTube(url)

  # Checks availability
  if(yt.check_availability):  

    print(yt.title)
    print(yt.description)
    print()

    # Calls the function to download audio
    download_Audio(yt)
    # Calls the function to download video
    download_Video(yt)

  else:
    print("Video is not available.")

except:
  print()
  print("The program encountered an error.")
