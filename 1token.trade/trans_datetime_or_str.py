import pandas as pd
import datetime

def main():
    df = pd.read_csv("f:/btcdata/merge3.csv")
    #df['date']= list(map(lambda x: print(type(x)), df['date']))
    df['date'] = list(map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'), df['date']))
    #df['date']= list(map(lambda x: print(type(x)), df['date']))
    df['date'] = list(map(lambda x: datetime.datetime.strftime(x, '%Y-%m-%d %H:%M'), df['date']))
    df.to_csv("f:/btcdata/merge4.csv",index=None)
if __name__ == "__main__":
  main()
