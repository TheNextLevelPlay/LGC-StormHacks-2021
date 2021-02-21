package com.app.demo.controller;

import com.app.demo.model.User;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.bind.annotation.*;

import javax.annotation.PostConstruct;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.lang.reflect.Array;
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

        mapper.writeValue(Paths.get("src/main/resources/data/query.json").toFile(), userArrayList);
        response.setStatus(201);
    }

    @PostMapping("/api/addAsk/{id}")
    public void addAsk(@PathVariable String id, @RequestBody String query, HttpServletResponse response)  throws IOException{
        ObjectMapper mapper = new ObjectMapper();
        Boolean foundID = false;
        for (int i =0 ; i < userArrayList.size();i++){
            if (userArrayList.get(i).getId().equals(id)){
                foundID = true;
                userArrayList.get(i).addAsk(query);
            }
        }
        if (!foundID){
            ArrayList<String> suggestArrList = new ArrayList<>();
            ArrayList<String> askArrList = new ArrayList<>();
            askArrList.add(query);
            User user = new User(id, askArrList, suggestArrList);
            userArrayList.add(user);
        }

        mapper.writeValue(Paths.get("src/main/resources/data/query.json").toFile(), userArrayList);
        response.setStatus(201);
    }

    @GetMapping("/api/getSuggestion/{id}")
    public ArrayList<String> getSpecificSuggestionList(@PathVariable String id, HttpServletResponse response) throws IOException{
        for (int i = 0; i < userArrayList.size(); i++){
            if (userArrayList.get(i).getId().equals(id)){
                response.setStatus(200);
                return userArrayList.get(i).getSuggestArrList();
            }
        }

        ArrayList<String> suggestArrList = new ArrayList<>();
        ArrayList<String> askArrList = new ArrayList<>();
        User user = new User(id, askArrList, suggestArrList);
        userArrayList.add(user);


        response.resetBuffer();
        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        response.getOutputStream().print(response.getStatus());
        response.flushBuffer();
        return user.getSuggestArrList();
    }

    @GetMapping("/api/getAsk/{id}")
    public ArrayList<String> getSpecificAskList(@PathVariable String id, HttpServletResponse response) throws IOException{
        for (int i = 0; i < userArrayList.size(); i++){
            if (userArrayList.get(i).getId().equals(id)){
                response.setStatus(200);
                return userArrayList.get(i).getAskArrList();
            }
        }

        ArrayList<String> suggestArrList = new ArrayList<>();
        ArrayList<String> askArrList = new ArrayList<>();
        User user = new User(id, askArrList, suggestArrList);
        userArrayList.add(user);

        response.resetBuffer();
        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        response.getOutputStream().print(response.getStatus());
        response.flushBuffer();
        return user.getAskArrList();
    }

    @PostMapping("/api/rmSuggest/{id}")
    public void removeSuggestionFromList(@PathVariable String id, @RequestBody String index, HttpServletResponse response) throws IOException{
        ObjectMapper mapper = new ObjectMapper();
        for (int i = 0; i < userArrayList.size(); i++){
            if (userArrayList.get(i).getId().equals(id)){
                if (Integer.parseInt(index) < userArrayList.get(i).getSuggestArrList().size() && userArrayList.get(i).getAskArrList().size() > 0) {
                    response.setStatus(204);
                    System.out.println(index);
                    userArrayList.get(i).removeSuggest(Integer.parseInt(index));
                    mapper.writeValue(Paths.get("src/main/resources/data/query.json").toFile(), userArrayList);
                    return;
                }
            }
        }

        response.resetBuffer();
        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        response.getOutputStream().print(response.getStatus());
        response.flushBuffer();
    }

    @PostMapping("/api/rmAsk/{id}")
    public void removeAskFromList(@PathVariable String id, @RequestBody String index, HttpServletResponse response) throws IOException{
        ObjectMapper mapper = new ObjectMapper();
        for (int i = 0; i < userArrayList.size(); i++){
            if (userArrayList.get(i).getId().equals(id)){
                if (Integer.parseInt(index) < userArrayList.get(i).getAskArrList().size() && userArrayList.get(i).getAskArrList().size() > 0) {
                    response.setStatus(204);
                    userArrayList.get(i).removeAsk(Integer.parseInt(index));
                    mapper.writeValue(Paths.get("src/main/resources/data/query.json").toFile(), userArrayList);
                    return;
                }
            }
        }

        response.resetBuffer();
        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        response.getOutputStream().print(response.getStatus());
        response.flushBuffer();
    }

    @PostMapping("/api/resolveSuggest/{id}")
    public void resolveUserSuggest(@PathVariable String id, HttpServletResponse response) throws IOException{
        ObjectMapper mapper = new ObjectMapper();
        for (int i = 0; i < userArrayList.size(); i++){
            if (userArrayList.get(i).getId().equals(id)){
                response.setStatus(204);
                userArrayList.get(i).clearSuggest();
                mapper.writeValue(Paths.get("src/main/resources/data/query.json").toFile(), userArrayList);
                return;
            }
        }

        response.resetBuffer();
        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        response.getOutputStream().print(response.getStatus());
        response.flushBuffer();
    }

    @PostMapping("/api/resolveAsk/{id}")
    public void resolveUserAsk(@PathVariable String id, HttpServletResponse response) throws IOException{
        ObjectMapper mapper = new ObjectMapper();
        for (int i = 0; i < userArrayList.size(); i++){
            if (userArrayList.get(i).getId().equals(id)){
                response.setStatus(204);
                userArrayList.get(i).clearAsk();
                mapper.writeValue(Paths.get("src/main/resources/data/query.json").toFile(), userArrayList);
                return;
            }
        }

        response.resetBuffer();
        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        response.getOutputStream().print(response.getStatus());
        response.flushBuffer();
    }



}
