import requests

def get_progressive_url(soundcloud_url):
    client_id = "TỰ MÒ"
    api_url = f"https://api-v2.soundcloud.com/resolve?url={soundcloud_url}&client_id={client_id}"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        for transcoding in data['media']['transcodings']:
            if transcoding['format']['protocol'] == 'progressive':
                return transcoding['url']

    return None

def download_soundcloud_track(soundcloud_url):

    if not soundcloud_url:
        return {"error": "URL SoundCloud không được cung cấp."}

    progressive_url = get_progressive_url(soundcloud_url)

    if progressive_url:
        params = {
            "client_id": "TỰ MÒ"
        }
        headers = {
            "Accept": "*/*",
            "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
            "Connection": "keep-alive",
            "Dnt": "1",
            "Host": "api-v2.soundcloud.com",
            "Origin": "https://soundcloud.com",
            "Referer": "https://soundcloud.com/",
            "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "X-Datadome-Clientid": "TU_DI_MA_LAY"
        }

        response = requests.get(progressive_url, headers=headers, params=params)
        return {"data": response.json()}
    else:
        return {"error": "LỖI."}

if __name__ == '__main__':
    soundcloud_url = input("Nhập URL SoundCloud: ")
    result = download_soundcloud_track(soundcloud_url)
    print(result)
