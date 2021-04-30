import re

import pandas as pd
import json
def scrape_wiki_table(url, table_index=0):
    df = pd.read_html(url, header=0)[table_index]
    return re.sub(r"\[?\s*(\d+)(?=(?:, \d+)|\])(?=[^\[]*\]).", "", df.to_csv(index=False))

if __name__ == '__main__':

      df = pd.read_html('http://musclememory.com/movies/byTitle.html')[0]
      df.to_json(r'data.json',orient='records')
    #   with open('data.json', 'w+') as f:

    #       f.write(json.dumps(df.to_json))
        # result = scrape_wiki_table('https://en.wikipedia.org/wiki/List_of_chief_executive_officers',1)
        # print(result)
