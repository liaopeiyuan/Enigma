import java.util.LinkedList;

public class Enigma {
	private Reflector reflector;
	private LinkedList<Rotor> rotors;
	private Steckerbrett plugs;
	
	public Enigma(LinkedList<Rotor> rotors, Reflector reflector, Steckerbrett plugs)
	{
		this.rotors=rotors;
		this.reflector=reflector;
		this.plugs=plugs;
	}
	
	public String output(String input)
	{
		String forwardProp = (String)plugs.pass(input)[0];
	}
	
	public String forwardRotorProcess(String input)
	{
		int notch=0;
		int turn=0;
		String temp="";
		for(int i=0; i<=rotors.size()-1; i++)
		{
			
		}
	}
}
