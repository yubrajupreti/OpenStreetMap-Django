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
![Alt text](file:///home/yubraj/Pictures/OSM/hotel.png)

Attraction:
![Alt text](file:///home/yubraj/Pictures/OSM/Screenshot%20from%202022-02-06%2019-31-45.png)

Information
![Alt text](file:///home/yubraj/Pictures/OSM/Screenshot%20from%202022-02-06%2019-32-27.png)

And so on of every category.

Addtionally, a draft model is also implemented for user rating and image upload.