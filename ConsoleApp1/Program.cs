using System.Collections.Generic;
using System.IO;
using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Automaton automaton = new Automaton();
            automaton.LoadAutomatonFromFile("AUTÔMATO=({q0,q1,q2,q3},{a,b},q0,{q1,q3})");
        }
    }
}
