package com.app.demo.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class User {
    private String id;
    private ArrayList<String> suggestArrList;
    private ArrayList<String> askArrList;
    @JsonProperty("suggestSize")
    private int suggestArrListSize;
    @JsonProperty("askSize")
    private int askArrListSize;

    public User(@JsonProperty("id")String id, @JsonProperty("ask")ArrayList<String>askArrList, @JsonProperty("suggest")ArrayList<String>suggestArrList){
        this.id = id;
        this.suggestArrList = suggestArrList;
        this.askArrList = askArrList;
        this.suggestArrListSize = suggestArrList.size();
        this.askArrListSize = askArrList.size();
    }

    public String getId(){
        return this.id;
    }

    public ArrayList<String> getSuggestArrList(){
        return this.suggestArrList;
    }

    public ArrayList<String> getAskArrList(){
        return this.getAskArrList();
    }

    public void addSuggest(String query){
        this.suggestArrList.add(query);
        this.suggestArrListSize++;
    }

    public void addAsk(String query){
        this.askArrList.add(query);
        this.askArrListSize++;
    }

    public void removeSuggest(){

    }

    public void removeAsk(){

    }


}
