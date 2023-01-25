# creates string of page source
# with open("hepo_source.txt") as file:
#     data = file.read()

# how to search: data-text="
import requests


url = "https://hellopoetry.com/colmistoirm/poems/title/?page=3&rnd=0.649245656827161"  # rnd value may need to change?
headers = {
    ":authority": "hellopoetry.com",
    ":method": "GET",
    ":path": "/colmistoirm/poems/title/?page=2&rnd=0.3756923205373932",
    ":scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "_ga=GA1.2.2025214942.1673630189; __qca=P0-848995684-1674166169581; fs.session.id=68c03ffd-638f-4600-82bf-e32196a6dc18; _pbjs_userid_consent_data=3524755945110770; cookie=537f8adb-8691-44fc-a881-87c51e62790c; _lr_env_src_ats=false; __gads=ID=bc8c54f0299afead:T=1674166168:S=ALNI_Ma-smrsgvbWC04FxntWHyj-Q35yTw; _au_1d=AU1D-0100-001674166172-T2GNU6M3-QNRI; _au_last_seen_pixels=eyJhcG4iOjE2NzQxNjYxNzIsInR0ZCI6MTY3NDE2NjE3MiwicHViIjoxNjc0MTY2MTcyLCJ0YXBhZCI6MTY3NDE2NjE3MiwiYWR4IjoxNjc0MTY2MTcyLCJnb28iOjE2NzQxNjYxNzIsInRhYm9vbGEiOjE2NzQxNjYxNzIsInBwbnQiOjE2NzQxNjYxNzIsIm9wZW54IjoxNjc0MTY2MTcyLCJhZG8iOjE2NzQxNjYxNzJ9; _fbp=fb.1.1674166172775.1049204382; _gaid=jd586kd84fn3fkjw13x4qjy3m2nv2kdr8y2rw3qh; _gid=GA1.2.489499060.1674618682; fs.bot.check=true; _lr_retry_request=true; __gpi=UID=0000093dd241e786:T=1674166168:RT=1674618682:S=ALNI_MZBimR_iL4wFtt5Ay4Ipbz6OYwrpg; TAPAD=%7B%22id%22%3A%22efbc72c6-2acd-4d48-8820-c6659046dd64%22%7D; _awl=2.1674619132.5-8bf9c237a9a83cff1dd4e132721c9261-6763652d75732d6561737431-0; cto_bidid=VKTGoF9rTnY1SmglMkIlMkJWQTVkdE9yRTFZRHJiemVBMiUyQjYxQlBZTVhaSlpoJTJCZTBvbXVVempUVXFYSWxUV3glMkZ1RnpwN1dkQ1QzWkkwR1hlJTJCNGlEMnpOTklKN0N4Tk1DYXQ5QjBObXJBa2slMkZwOFlaT0FaZTQyeHpVTXk1MDMyTFZiSWFCSU9Q; cto_bundle=kzik7l9Va2VjVnUwdnB0QiUyRnZWUEVVcGpoZ0QyUyUyRmtVUURTbTF6cVkxVmVnaEdIcXNRajNZQjJIT1dKQ2l5SmVEVzl0eDBBbGhOJTJCNHhLbUFDbURCJTJGSkxGTDFTSlQ2NHolMkY1RXNwVGJoV2wlMkJ6UEZWcnd6QVdaTzg5U1VMVFAxS0N5RGoyRlZpd1dFcWV4RkNCVlgzUVZnRUNOaWclM0QlM0Q; _gat=1",
    "referer": "https://hellopoetry.com/colmistoirm/poems/title/",
    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}
