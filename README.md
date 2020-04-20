# Realtime gtfs project

## Table of Contents
- [API Guide](#api-guide)
    - [Real-time timetable relationship](#real-time-timetable-relationship)
    - [GTFS API](#gtfs-api)
- [Install](#install)
-[Contributing](#contributing)

## API Guide

[Google Transit APIs](https://developers.google.com/transit)   
[Google Realtime Transit](https://developers.google.com/transit/gtfs-realtime/reference#message_stoptimeupdate)     
[Troubleshooting](https://opendata.transport.nsw.gov.au/troubleshooting)    
[tfNSW_Realtime_Train_Technical_Doc](https://opendata.transport.nsw.gov.au/sites/default/files/TfNSW_Realtime_Train_Technical_Doc.pdf)   
[How to Use Open Data to Develop an Application](https://opendata.transport.nsw.gov.au/how-use-open-data-develop-application)      

### Real-time timetable relationship
The following picture shows the relationship between each file in real-time timetable model:
![image](data/dataProcess/timetable/gtfs_file_relationship.jpeg) 

### GTFS API     

[Public Transport - Timetables - For Realtime : ](https://opendata.transport.nsw.gov.au/node/332/exploreapi)  
Static timetables, stop locations, and route shape information in GTFS format for operators that support realtime.  
Public URI: https://api.transport.nsw.gov.au/v1/gtfs/schedule/   
Operations:  

    GET /sydneytrains     
    GET /buses and /buses/   
    GET /ferries    
    GET /lightrail/    
    GET /nswtrains    
    GET /regionbuses/    
    GET /metro     


[Public Transport - Realtime Trip Update : ](https://opendata.transport.nsw.gov.au/dataset/public-transport-realtime-trip-update)   
Stop time updates for active trips, replacement vehicles, and changed stopping patterns in GTFS-realtime format for Buses, Ferries, Light Rail, Trains and Metro.  
Public URI: https://api.transport.nsw.gov.au/v1/gtfs/realtime/   
Operations:  

    GET /sydneytrains  
    GET /buses  
    GET /ferries  
    GET /lightrail/  
    GET /nswtrains  
    GET /regionbuses/  
    GET /metro   


[Public Transport - Realtime Vehicle Positions : ](https://opendata.transport.nsw.gov.au/dataset/public-transport-realtime-vehicle-positions)     
Current vehicle positions in GTFS-realtime format for Buses, Ferries, Light Rail, Trains and Metro.  
Public URI: https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/   
Operations:  

    GET /sydneytrains  
    GET /buses  
    GET /ferries  
    GET /lightrail/  
    GET /nswtrains  
    GET /regionbuses/   
    GET /metro   


[Public Transport - Realtime Alerts : ](https://opendata.transport.nsw.gov.au/dataset/public-transport-realtime-alerts-0)  
Realtime alerts at either the stop, trip, or service line level in GTFS-realtime format for Buses, Ferries, Light Rail and Trains.    
Public URI: https://api.transport.nsw.gov.au/v1/gtfs/alerts  
Operations:  

    GET /sydneytrains  
    GET /buses  
    GET /ferries  
    GET /lightrail  
    GET /nswtrains   
    
## Install
Please refer to other document for the usage of [GTFS feed](https://github.com/FrankieWei727/Realtime/tree/master/data/README.md).  


## Contributing
This project exists thanks to all the people who contribute.   
<a href="github.com/FrankieWei727"><img src="https://avatars0.githubusercontent.com/u/31089132?s=400&u=52449db93dc4e8760f9f7c382a190df15c581c93&v=4" /></a>








