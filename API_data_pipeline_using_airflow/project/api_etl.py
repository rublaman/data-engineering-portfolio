import pandas as pd
import json
import s3fs
import requests
import pandas as pd
from datetime import datetime


def main():
    
    API_KEY = "MY-API-KEY"
    
    channels_name = ["Codecademy", "GitHub", "Amazon Web Services", "Microsoft Azure"]
    channels_ids = ["UC5CMtpogD_P3mOoeiDHD5eQ", "UC7c3Kb6jYCRj4JOHHZTxKsQ", "UCd6MoB9NC6uYN2grvUNT-Zg", "UC0m-80FnNY2Qb7obvTL_2fA"]
    
    channels = {
        "Channel_name": channels_name,
        "Channel_id": channels_ids
    }

    df_channels = pd.DataFrame(channels)
    channels = channel_stats(df_channels, API_KEY)
    
    channels.to_csv("channels_to_analize.csv", encoding='utf-8', index=False)
    
    
def get_stats(api_key, channel_id):

    url_channel_stats = f'https://youtube.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}'
    response_channels = requests.get(url_channel_stats)
    channel_stats = json.loads(response_channels.content)
    
    channel_stats = channel_stats["items"][0]["statistics"]
    date = pd.to_datetime("today").strftime("%Y-%m-%d")

    data_channel = {
        "Created_at": date,
        "Total_Views": int(float(channel_stats["viewCount"])),
        "Subscribers": int(float(channel_stats["subscriberCount"])),
        "Video_count": int(float(channel_stats["videoCount"]))
    }

    return data_channel

def channel_stats(df_channels, API_KEY):
    
    date = []
    views = []
    suscriber = []
    video_count = []
    channel_name = []

    for index, row in df_channels.iterrows():
        stats_temp = get_stats(API_KEY, row["Channel_id"])

        date.append(stats_temp["Created_at"])
        views.append(stats_temp["Total_Views"])
        suscriber.append(stats_temp["Subscribers"])
        video_count.append(stats_temp["Video_count"])
        channel_name.append(row["Channel_name"])

    data = {
        "Channel_name": channel_name,
        "Subscribers": suscriber,
        "Video_Count": video_count,
        "Total_Views": views,
        "created_at": date
    }

    df_channels_final = pd.DataFrame(data)

    return df_channels_final
    
if __name__ == "__main__":
    main()