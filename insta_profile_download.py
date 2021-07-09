# Download instagram profile picture
# pip install instaloader on terminal

import instaloader

insta=instaloader.Instaloader()

name=input("Enter the username : ")

insta.download_profile(name, profile_pic_only=True)
