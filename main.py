import requests
import dotenv
import os

dotenv.load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")

URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(URL)
data = response.json()

title = data['title']
explanation = data['explanation']
img_url = data['hdurl']

# README.md 파일 생성
readme_content = f"""# {title}

![{title}]({img_url})

## Explanation
{explanation}
"""

with open("README.md", "w") as f:
    f.write(readme_content)

print("README.md 파일이 업데이트되었습니다!")
print(f"Image URL: {img_url}") 