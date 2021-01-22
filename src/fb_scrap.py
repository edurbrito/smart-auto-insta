#!./env/bin/python3

from facebook_scraper import get_posts
import requests
from emoji import UNICODE_EMOJI
import emoji

def extract_emojis(str):
  return [c for c in str if c in UNICODE_EMOJI]

print("######################")
print("#                    #")
print("#  FACEBOOK SCRAPER  #")
print("#                    #")
print("######################")
print()

ptext = ""
pimage = ""
for post in get_posts('babeth.braga', pages=1):
    ptext = post['text']
    pimage = post['image']
    if(emoji.emoji_count(ptext) > 0):
        for i in extract_emojis(ptext):
            ptext = ptext.replace(i, emoji.demojize(i, use_aliases=True))
            ptext = emoji.emojize(ptext,True)
    print("\'text\':", ptext)
    print()
    print("\'image\':", pimage)
    print()
    print("#####################################")
    print()
    break

file = open('../utils/post_info','r+')
old_ptext = file.read()
if(old_ptext[:30] != ptext[:30]):
    ptext = ptext.replace("<3",emoji.emojize(":red_heart:",True))
    file.seek(0)
    file.truncate()
    file.write(ptext)
    file.close()
    img_data = requests.get(pimage).content
    with open('../utils/post_image.jpg', 'wb') as handler:
        handler.write(img_data)
    # from insta_poster import insta_poster
    # insta_poster(True)
    # print("POST UPDATED")
