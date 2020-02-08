Simple tool pushing eventbrite events to your google spreadsheet. 

As they shamefully removed public API the way to have data is to: 

``````

go to Google chrome dev tools 
-> networking -> Do a search (city with all events on interesting data frame) 
-> Copy /search fetch 
-> Ctr V in console with pagination changed to 500 
-> get new /search in networking tab by "copy response" 
-> put response as "resp" file and run script


``````