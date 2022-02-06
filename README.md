# OpenStreetMap-Django
The data of tourism place in kathmandu is fetched from overpass turbo.
The data are categorized accordingly.

For eg: 
'hotel','guest_house','museum','attraction','information','Outdoor_Activities','hostel','theme_park'

For each category the model is designed. And has respective endpoint.
The CRUD operation can be perform in all the endpoint.
To create an instance, endpoint is mention in the documentation.
For the documentation overview. Run the application and request in following endpoint:

 http://localhost:8000/swagger/
  
 http://localhost:8000/redocs/ 
 
 Some of the screenshot of output is listed below: 
 Hotel:
![hotel](https://user-images.githubusercontent.com/47235565/152684723-b80e5d11-4c9e-473a-9b1f-95a1e544968f.png)

Attraction:
![Screenshot from 2022-02-06 19-31-45](https://user-images.githubusercontent.com/47235565/152684743-eb2c99da-40ab-4253-ae10-e28527684378.png)
Information

![Screenshot from 2022-02-06 19-32-27](https://user-images.githubusercontent.com/47235565/152684765-bd0a497e-83d6-4647-89f9-f726fb44be26.png)

And so on of every category.

Addtionally, a draft model is also implemented for user rating and image upload.