import youtube_dl
from pydub import AudioSegment

def convert_to_mp3(file_path, mp3_path):
    sound = AudioSegment.from_file(file_path)
    sound.export(mp3_path, format="mp3")
    print("File converted to mp3 successfully")

def run():
    video_url = input("please enter youtube video url:")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp4"
    options={
        'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'keepvideo':True,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    mp3_path=video_info['title']+'.mp3'
    convert_to_mp3(filename, mp3_path)
    print("Download complete... {}".format(mp3_path))

if __name__=='__main__':
    run()

