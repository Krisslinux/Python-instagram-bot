from instabot import Bot
import instaloader
import os

# Function to download the latest Reel from a user
def download_latest_reel(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        if post.is_video:
            L.download_post(post, target=profile.username)
            return f"{profile.username}/{post.shortcode}.mp4"

bot = Bot()

# Log in to your account using environment variables
bot.login(username=os.getenv('INSTAGRAM_USERNAME'), password=os.getenv('INSTAGRAM_PASSWORD'))

# Define the username to fetch Reels from
source_username = "tyrone"

# Download the latest Reel
media_path = download_latest_reel(source_username)

# Post the media to your account
if media_path:
    bot.upload_video(media_path, caption="Reposting the latest reel! please like and follow")
