import twint

c = twint.Config()
c.Search = "rasis lu"
c.Lang = "id"
c.Near = "bandung"
c.Store_object = True
c.Limit = 20
twint.run.Search(c)
tlist = c.search_tweet_list

print(tlist[0])