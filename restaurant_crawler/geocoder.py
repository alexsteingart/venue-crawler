import pymongo, urllib2, json, time

client = pymongo.MongoClient()
db = client['items']

venues = db.venues.find({ 'lat': {'$exists': False } })

for venue in venues:
    print venue['address']
    json_response = json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address=%s" % urllib2.quote(venue['address'])))
    db.venues.update_one({'_id': venue['_id']},
    {
        '$set': {
            'lat': json_response['results'][0]['geometry']['location']['lat'],
            'lng': json_response['results'][0]['geometry']['location']['lng']
        }
    })
    time.sleep(2)
