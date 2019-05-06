using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Automaton
    {
        private string id;
        private List<State> states;
        private List<char> symbols;
        private State initState;

        public Automaton()
        {
            id = "Defult";
            states = new List<State>();
            symbols = new List<char>();
            initState = null;
        }

        public void LoadAutomatonFromFile(string _fileName)
        {
            InitVariables(_fileName);
            Console.WriteLine(ToString());
            Console.ReadKey();
        }

        private void InitVariables(string _info)
        {
            string word = "";
            int count = 0;
            char letter = _info[count];

            //Gera o nome do Autômato
            while (letter != '=')
            {
                word += letter;
                letter = _info[++count];
            }
            id = word;

            count += 3;
            letter = _info[count];
            word = "";

            //Gera os estados do Autômato
            while (letter != '}')
            {
                if (letter == ',')
                {
                    states.Add(new State(word));
                    word = "";
                }
                else
                {
                    word += letter;
                }

                letter = _info[++count];
            }
            states.Add(new State(word));

            count += 3;
            letter = _info[count];

            //Lê Simbolos
            while (letter != '}')
            {
                if (letter != ',')
                {
                    symbols.Add(letter);
                }

                letter = _info[++count];
            }

            count += 2;
            letter = _info[count];
            word = "";

            //Lê estado inicial
            while (letter != ',')
            {
                word += letter;

                letter = _info[++count];
            }

            SetInitialState(word);

            count += 2;
            letter = _info[count];
            word = "";

            //Lê estados finais
            while (letter != '}')
            {
                if (letter == ',')
                {
                    SetFinalState(word);
                    word = "";
                }
                else
                {
                    word += letter;
                }

                letter = _info[++count];
            }
            SetFinalState(word);
        }

        public void SetInitialState(string _id)
        {
            foreach(State state in states)
            {
                if (state.id == _id)
                {
                    state.isInitial = true;
                    initState = state;
                }
            }
        }

        public void SetFinalState(string _id)
        {
            foreach (State state in states)
            {
                if (state.id == _id) state.isFinal = true;
            }
        }

        public override string ToString()
        {
            StringBuilder toString = new StringBuilder("Name: " + id);

            toString.Append("\nStates: [");
            foreach (State state in states)
            {
                toString.Append(state.id + ",");
            }
            toString[toString.Length - 1] = ']';

            toString.Append("\nSymbols: [");
            foreach (char symbol in symbols)
            {
                toString.Append(symbol + ",");
            }
            toString[toString.Length - 1] = ']';

            toString.Append("\nInitialState: " + initState.id);

            toString.Append("\nFinalStates: [");
            foreach (State state in states)
            {
                if(state.isFinal) toString.Append(state.id + ",");
            }
            toString[toString.Length - 1] = ']';

            return toString.ToString();
        }

        private class State
        {
            public string id;
            public bool isInitial;
            public bool isFinal;
            public List<State> nextState;

            public State(string _id)
            {
                id = _id;
                isInitial = false;
                isFinal = false;
                nextState = new List<State>();
            }
        }

    }
}
