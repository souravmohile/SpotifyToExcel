import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]

SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-read-collaborative",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="BQDkAuSwzjCvLdtfBoqtBc6bAHtrXGj1Q9jymPypV9U6c7VL_13wcD5qIHHKM_X8xLz6z9skj5qALlRIIN6iUgJ-mQLe1yKJXieqccdZStsZ5bjqWHh-Y6rUHyuL7NHs98atIr0JRl8U5EFcSZSPcTllJOUCYqf8dhXVpnPMKeE"
    )
)

items = sp.playlist_tracks("5wkTHzQhzVPmS3z2NV38Tx")
# print(items)
length = len(items["items"])

songs_list = []
for num in range(0, length):
    songs_list.append(items["items"][num]["track"]["name"])

print(songs_list)

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for i in range(0, length):
    sheety_parameters = {
        "sheet1": {
            "name": songs_list[i]
        }
    }

    response = requests.post(url="https://api.sheety.co/20308d467201a276809c3b2f10ef2fc2/kpopPlaylistReview/sheet1",
                             json=sheety_parameters,
                             headers=sheety_header)




