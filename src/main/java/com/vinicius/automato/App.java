package com.vinicius.automato;

public class App 
{
    public static void main( String[] args )
    {
    	Automaton a = new Automaton();
    	a.loadAutomatonFromFile("AUTOMATO=({q0,q1,q2,q3},{a,b},q0,{q1,q3})");
    	System.out.println(a);
    }
}
