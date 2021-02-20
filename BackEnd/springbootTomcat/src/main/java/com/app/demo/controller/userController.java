package com.app.demo.controller;

import com.app.demo.model.User;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.bind.annotation.*;

import javax.annotation.PostConstruct;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;


@RestController
public class userController {
    private ArrayList<User> userArrayList;

    @PostConstruct
    public void initIT() throws IOException{
        ObjectMapper mapper = new ObjectMapper();
        userArrayList = new ArrayList<>(Arrays.asList(
                mapper.readValue(
                        Paths.get("src/main/resources/data/query.json").toFile(),
                        User[].class
                )
        ));
    }

    @GetMapping("/api/getUserList")
    public ArrayList<User> getUserArrayList(HttpServletResponse response) throws IOException{
        response.setStatus(200);
        return userArrayList;
    }

    @PostMapping("/api/addSuggestion/{id}")
    public void addSuggestion(@PathVariable String id, @RequestBody String query, HttpServletResponse response)  throws IOException{
        ObjectMapper mapper = new ObjectMapper();
        Boolean foundID = false;
        for (int i =0 ; i < userArrayList.size();i++){
            if (userArrayList.get(i).getId().equals(id)){
                foundID = true;
                userArrayList.get(i).addSuggest(query);
            }
        }
        if (!foundID){
            ArrayList<String> suggestArrList = new ArrayList<>();
            ArrayList<String> askArrList = new ArrayList<>();
            suggestArrList.add(query);
            User user = new User(id, askArrList, suggestArrList);
            userArrayList.add(user);
        }

        System.out.println(userArrayList.get(0).toString());
        mapper.writeValue(Paths.get("src/main/resources/data/query.json").toFile(), userArrayList);
        response.setStatus(201);
    }


}
