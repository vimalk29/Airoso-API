package com.aeroso.aerosoapi.payload.request;

import javax.validation.constraints.NotBlank;

public class AirosoIndex {
    //String timestamp
    @NotBlank
    String date;
    @NotBlank
    long latitude;
    @NotBlank
    long longitude;
    @NotBlank
    double uAindex;

//    {
//        "date": "2020-02-26T00:55:02+01:00",
//            "latitude": -73.40665435791016,
//            "longitude": 28.747451782226562,
//            "uAindex": -1.2676506002282294e+30
//    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public long getLatitude() {
        return latitude;
    }

    public void setLatitude(long latitude) {
        this.latitude = latitude;
    }

    public long getLongitude() {
        return longitude;
    }

    public void setLongitude(long longitude) {
        this.longitude = longitude;
    }

    public double getuAindex() {
        return uAindex;
    }

    public void setuAindex(double uAindex) {
        this.uAindex = uAindex;
    }
}
