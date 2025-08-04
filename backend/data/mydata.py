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
    "image": "/data/images/everest.jpg",
    "latitude": 27.9881,
    "longitude": 86.9250
  },
  {
    "id": 1,
    "name": "K2",
    "height": 8611,
    "location": "Pakistan/China",
    "continent": "Asia",
    "range": "Karakoram",
    "first_ascent": "1954",
    "image": "/data/images/k2.jpg",
    "latitude": 35.8808,
    "longitude": 76.5155
  },
  {
    "id": 2,
    "name": "Kangchenjunga",
    "height": 8586,
    "location": "Nepal/India",
    "continent": "Asia",
    "range": "Himalayas",
    "first_ascent": "1955",
    "image": "/data/images/kangchenjunga.jpg",
    "latitude": 27.7025,
    "longitude": 88.1475
  },
  {
    "id": 3,
    "name": "Denali",
    "height": 6190,
    "location": "Alaska, USA",
    "continent": "North America",
    "range": "Alaska Range",
    "first_ascent": "1913",
    "image": "/data/images/denali.jpg",
    "latitude": 63.0692,
    "longitude": -151.0070
  },
  {
    "id": 4,
    "name": "Mont Blanc",
    "height": 4807,
    "location": "France/Italy",
    "continent": "Europe",
    "range": "Alps",
    "first_ascent": "1786",
    "image": "/data/images/mont-blanc.jpg",
    "latitude": 45.8326,
    "longitude": 6.8652
  },
  {
    "id": 5,
    "name": "Aconcagua",
    "height": 6961,
    "location": "Argentina",
    "continent": "South America",
    "range": "Andes",
    "first_ascent": "1897",
    "image": "/data/images/aconcagua.jpg",
    "latitude": -32.6532,
    "longitude": -70.0109
  },
  {
    "id": 6,
    "name": "Mount Elbrus",
    "height": 5642,
    "location": "Russia",
    "continent": "Europe",
    "range": "Caucasus",
    "first_ascent": "1874",
    "image": "/data/images/mount-elbrus.jpg",
    "latitude": 43.3499,
    "longitude": 42.4453
  },
  {
    "id": 7,
    "name": "Vinson Massif",
    "height": 4892,
    "location": "Antarctica",
    "continent": "Antarctica",
    "range": "Sentinel Range",
    "first_ascent": "1966",
    "image": "/data/images/vinson-massif.jpg",
    "latitude": -78.5254,
    "longitude": -85.6171
  },
  {
    "id": 8,
    "name": "Mount Kosciuszko",
    "height": 2228,
    "location": "Australia",
    "continent": "Australia",
    "range": "Great Dividing Range",
    "first_ascent": "1840",
    "image": "/data/images/mount-kosciuszko.jpg",
    "latitude": -36.4560,
    "longitude": 148.2634
  },
  {
    "id": 9,
    "name": "Matterhorn",
    "height": 4478,
    "location": "Switzerland/Italy",
    "continent": "Europe",
    "range": "Alps",
    "first_ascent": "1865",
    "image": "/data/images/matterhorn.jpg",
    "latitude": 45.9763,
    "longitude": 7.6586
  },
  {
    "id": 10,
    "name": "Mount Kinabalu",
    "height": 4095,
    "location": "Sabah, Malaysia",
    "continent": "Asia",
    "range": "Crocker Range",
    "first_ascent": "1851",
    "image": "/data/images/mount-kinabalu.jpg",
    "latitude": 6.0753,
    "longitude": 116.5580
  },
  {
    "id": 11,
    "name": "Puncak Jaya",
    "height": 4884,
    "location": "Papua, Indonesia",
    "continent": "Australia",
    "range": "Sudirman Range",
    "first_ascent": "1962",
    "image": "/data/images/puncak-jaya.jpg",
    "latitude": -4.0783,
    "longitude": 137.1843
  }
]

# This part of your script writes the list to the mountains.json file
json_string = json.dumps(mountain_dict, indent=2)
with open("./backend/data/mountains.json", 'w') as f:
  f.write(json_string)