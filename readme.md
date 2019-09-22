## Flight and location API
Root address for the API:

    https://traveldjangoapp.herokuapp.com/api/

  ### Get all Flights
    https://traveldjangoapp.herokuapp.com/api/flights/
  ### Get Flight by Departure and Arrival
  To get all flights by departure and arrival states, use
  `https://traveldjangoapp.herokuapp.com/api/flights/find/{ Departure state code }/{ Arrival state code }` . Replace { Departure state code } and { Arrival state code } with state codes (lowercase).
Example for Chandigarh (IXC) to Delhi (DEL) is:

    https://traveldjangoapp.herokuapp.com/api/flights/find/ixc/del/

### Get Flight by Departure and Arrival and Departure date
Add departure date at the end of above mentioned url in format of YYYY/MM/DD.
For example: Chandigarh to Delhi on 25/09/2019 will be:

    https://traveldjangoapp.herokuapp.com/api/flights/find/ixc/del/2019/09/25/
