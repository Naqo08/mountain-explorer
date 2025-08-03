import json

mountain_dict = [
  {
    "id": 0,
    "name": "Mount Everest",
    "height": 8848,
    "location": "Nepal/China",
    "continent": "Asia",
    "range": "Himalayas",
    "first_ascent": "1953",
    "image": "/data/images/everest.jpg"
  },
  {
    "id": 1,
    "name": "K2",
    "height": 8611,
    "location": "Pakistan/China",
    "continent": "Asia",
    "range": "Karakoram",
    "first_ascent": "1954",
    "image": "/data/images/k2.jpg"
  },
  {
    "id": 2,
    "name": "Kangchenjunga",
    "height": 8586,
    "location": "Nepal/India",
    "continent": "Asia",
    "range": "Himalayas",
    "first_ascent": "1955",
    "image": "/data/images/kangchenjunga.jpg"
  },
  {
    "id": 3,
    "name": "Denali",
    "height": 6190,
    "location": "Alaska, USA",
    "continent": "North America",
    "range": "Alaska Range",
    "first_ascent": "1913",
    "image": "/data/images/denali.jpg"
  },
  {
    "id": 4,
    "name": "Mont Blanc",
    "height": 4807,
    "location": "France/Italy",
    "continent": "Europe",
    "range": "Alps",
    "first_ascent": "1786",
    "image": "/data/images/mont-blanc.jpg"
  },
  {
    "id": 5,
    "name": "Aconcagua",
    "height": 6961,
    "location": "Argentina",
    "continent": "South America",
    "range": "Andes",
    "first_ascent": "1897",
    "image": "/data/images/aconcagua.jpg"
  },
  {
    "id": 6,
    "name": "Mount Elbrus",
    "height": 5642,
    "location": "Russia",
    "continent": "Europe",
    "range": "Caucasus",
    "first_ascent": "1874",
    "image": "/data/images/mount-elbrus.jpg"
  },
  {
    "id": 7,
    "name": "Vinson Massif",
    "height": 4892,
    "location": "Antarctica",
    "continent": "Antarctica",
    "range": "Sentinel Range",
    "first_ascent": "1966",
    "image": "/data/images/vinson-massif.jpg"
  },
  {
    "id": 8,
    "name": "Mount Kosciuszko",
    "height": 2228,
    "location": "Australia",
    "continent": "Australia",
    "range": "Great Dividing Range",
    "first_ascent": "1840",
    "image": "/data/images/mount-kosciuszko.jpg"
  },
  {
    "id": 9,
    "name": "Matterhorn",
    "height": 4478,
    "location": "Switzerland/Italy",
    "continent": "Europe",
    "range": "Alps",
    "first_ascent": "1865",
    "image": "/data/images/matterhorn.jpg"
  }
]

json_string = json.dumps(mountain_dict, indent=2)
with open("./backend/data/mountains.json", 'w') as f:
  f.write(json_string)