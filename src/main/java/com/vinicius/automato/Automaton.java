package com.vinicius.automato;

import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Automaton {
	private String id;
    private Map<String, State> states;
    private List<String> symbols;
    private State initState;

    public Automaton()
    {
        id = "Defult";
        states = new HashMap<>();
        symbols = new LinkedList<>();
        initState = null;
    }

    public void loadAutomatonFromFile(String fileName)
    {
        initVariables(fileName);
        addTransitions(Arrays.asList("(q0,a)=q1", 
        							 "(q0,b)=q2",
        							 "(q1,b)=q2",
        							 "(q2,a)=q3",
        							 "(q2,a)=q2",
        							 "(q3,a)=q3",
        							 "(q3,b)=q2"));
     
    }
    
    private void addTransitions(List<String> transitions)
    {
    	for(String transition : transitions)
    	{
    		String temp = transition.substring(1);
    		temp = temp.replace(")=",",");
    		
    		String[] tokens = temp.split(",");
    		
    		addTransition(tokens[0], tokens[1], tokens[2]);
    	}
    }

    private void addTransition(String currentStateId, String symbol, String nextStateId)
    {
    	State currentState = states.get(currentStateId);
    	State nextState = states.get(nextStateId);

    	currentState.nextState.add(nextState);
    	
    	states.replace(currentStateId, currentState);
    }
    
    private void initVariables(String info)
    {
        String word = "";
        int count = 0;
        char letter = info.charAt(count);

        //Gera o nome do Autômato
        while (letter != '=')
        {
            word += letter;
            letter = info.charAt(++count);
        }
        id = word;

        count += 3;
        letter = info.charAt(count);
        word = "";

        //Gera os estados do Autômato
        while (letter != '}')
        {
            if (letter == ',')
            {
                states.put(word, new State(word));
                word = "";
            }
            else
            {
                word += letter;
            }

            letter = info.charAt(++count);
        }
        states.put(word, new State(word));

        count += 3;
        letter = info.charAt(count);

        //Lê Simbolos
        while (letter != '}')
        {
            if (letter != ',')
            {
                symbols.add(String.valueOf(letter));
            }

            letter = info.charAt(++count);
        }

        count += 2;
        letter = info.charAt(count);
        word = "";

        //Lê estado inicial
        while (letter != ',')
        {
            word += letter;

            letter = info.charAt(++count);
        }

        setInitialState(word);
 
        count += 2;
        letter = info.charAt(count);
        word = "";

        //Lê estados finais
        while (letter != '}')
        {
            if (letter == ',')
            {
                setFinalState(word);
                word = "";
            }
            else
            {
                word += letter;
            }

            letter = info.charAt(++count);
        }
        setFinalState(word);
    }

    public void setInitialState(String id)
    {
    	State state = states.get(id);
    	state.isInitial = true;
        initState = state;
        states.replace(id,  state);
    }

    public void setFinalState(String id)
    {
    	State state = states.get(id);
    	state.isFinal = true;
        states.replace(id,  state);
    }

    @Override
    public String toString()
    {
        StringBuilder toString = new StringBuilder("Name: " + id);

        Collection<State> statesList =  states.values();
        
        toString.append("\nStates: [");
        for(State state : statesList)
        {
            toString.append(state.id + ",");
        }
        
        toString.setCharAt(toString.length() - 1, ']');

        toString.append("\nSymbols: [");
        for (String symbol : symbols)
        {
            toString.append(symbol + ",");
        }
        toString.setCharAt(toString.length() - 1, ']');

        toString.append("\nInitialState: " + initState.id);

        toString.append("\nFinalStates: [");
        for(State state : statesList)
        {
            if(state.isFinal) toString.append(state.id + ",");
        }
        toString.setCharAt(toString.length() - 1, ']');

        toString.append("\nTransitions: \n   ").append(states.values());
        
        return toString.toString();
    }

    private class State
    {
        public String id;
        public boolean isInitial;
        public boolean isFinal;
        public List<State> nextState;

        public State(String id)
        {
            this.id = id;
            isInitial = false;
            isFinal = false;
            nextState = new LinkedList<>();
        }
        
        @Override
        public String toString()
        {
        	String ids = "";
        	for(State state : nextState)
        	{
        		ids += " " + state.id;
        	}
        	return id+" = [init="+isInitial+", final="+isFinal+", states="+ids+"]";
        }
    }
}
