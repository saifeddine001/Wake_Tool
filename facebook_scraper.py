!pip install facebook-scraper



from facebook_scraper import get_posts
import pandas as pd

for post in get_posts('Clients-Topnet-mécontents-565765370225548', pages=1):
  print(post['text'][:50])
  
  
!facebook-scraper --filename Topnet_posts.csv --pages 1 Clients-Topnet-mécontents-565765370225548


topnet=pd.read_csv('Topnet_posts.csv')
topnet
