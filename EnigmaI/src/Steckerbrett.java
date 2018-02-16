import java.util.ArrayList;

public class Steckerbrett implements Passable {
	private ArrayList<String> pair1 = new ArrayList<String>();
	private ArrayList<String> pair2 = new ArrayList<String>();
	
	public Steckerbrett(String pair1, String pair2)
	{
		for(int i=0; i<=pair1.length()-1; i++)
		{
			this.pair1.add(pair1.substring(i, i+1)):
			this.pair2.add(pair2.substring(i, i+1)):
		}
	}
	
	public Object[] pass(String input)
	{
		for (int i=0; i<=pair2.size()-1; i++)
		{
			if(input.equals(pair1.get(i)))
				return new Object[] {pair2.get(i),0};
			else if(input.equals(pair2.get(i)))
				return new Object[] {pair1.get(i),0};
		}
		return new Object[] {input,0};
	}
	
}
