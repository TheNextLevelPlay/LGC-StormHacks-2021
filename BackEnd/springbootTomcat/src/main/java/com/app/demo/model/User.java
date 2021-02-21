package com.app.demo.model;

import com.fasterxml.jackson.annotation.JsonCreator;
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
    @JsonCreator
    public User(@JsonProperty("id")String id, @JsonProperty("ask")ArrayList<String>askArrList, @JsonProperty("suggest")ArrayList<String>suggestArrList, @JsonProperty("suggestSize") int suggestArrListSize, @JsonProperty("askSize") int askArrListSize){
        this.id = id;
        this.suggestArrList = suggestArrList;
        this.askArrList = askArrList;
        this.suggestArrListSize = suggestArrListSize;
        this.askArrListSize = askArrListSize;
    }

    public String getId(){
        return this.id;
    }

    public ArrayList<String> getSuggestArrList(){
        return this.suggestArrList;
    }

    public ArrayList<String> getAskArrList(){
        return this.askArrList;
    }

    public void addSuggest(String query){
        this.suggestArrList.add(query);
        this.suggestArrListSize = this.suggestArrList.size();
    }

    public void addAsk(String query){
        this.askArrList.add(query);
        this.askArrListSize = this.askArrList.size();
    }

    public void removeSuggest(int index){
        this.suggestArrList.remove(index);
        this.suggestArrListSize = this.suggestArrList.size();
    }

    public void removeAsk(int index){
        this.askArrList.remove(index);
        this.askArrListSize = this.askArrList.size();
    }

    public void clearSuggest(){
        this.suggestArrList.clear();
        this.suggestArrListSize = 0;
    }

    public void clearAsk(){
        this.askArrList.clear();
        this.askArrListSize = 0;
    }

    @Override
    public String toString() {
        return "User{" +
                "id='" + id + '\'' +
                ", suggestArrList=" + suggestArrList +
                ", askArrList=" + askArrList +
                ", suggestArrListSize=" + suggestArrListSize +
                ", askArrListSize=" + askArrListSize +
                '}';
    }
}
