import java.util.ArrayList;
public class Rotor implements Passable{

	private static final String WHEEL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	private ArrayList<String> connection = new ArrayList<String>(26);
	private String notch;
	private String turnover;
	private String position;
	public Rotor(String connection,String notch, String turnover)
	{
		for(int i=0; i<=connection.length()-1; i++)
		{
			this.connection.add(connection.substring(i,i+1));
		}
		this.position = connection.substring(0, 1);
		this.notch=notch;
		this.turnover=turnover;
	}
	
	public Object[] pass(String input)
	{
		int pos=0;
		for(int i=0; i<=WHEEL.length()-1; i++)
		{
			if(input.equals(WHEEL.substring(i, i+1)))
				pos=i;
		}
		int step = step();
		return new Object[] {connection.get(pos),step};
	}
	
	private int step()
	{
				String temp = connection.get(0);
				connection.remove(0);
				connection.add(temp);
				position=this.connection.get(0);
				if(position.equals(turnover))
				{
					return 1;
				}
				else if(position.equals(notch))
				{
					return -1;
				}
				else
				{
					return 0;
				}
	}
	
	public String getPos()
	{
		return position;
	}
	
	public String getNotch()
	{
		return notch;
	}
}
