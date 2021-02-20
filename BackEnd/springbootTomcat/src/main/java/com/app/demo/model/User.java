package com.app.demo.model;

import com.fasterxml.jackson.annotation.JsonProperty;

public class User {
    private String id;

    public User(@JsonProperty("id")String id){
        this.id = id;
    }

    public String getId(){
        return this.id;
    }
}
