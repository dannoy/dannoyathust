import java.sql.*;
import java.util.*;
public class Client {
	protected Connection  con;
	protected String url;
	protected String user;
	protected String password;
	protected String driverName = "dm.jdbc.driver.DmDriver";

	public Client(String user, String password, String url)
	{
		this.user = user;
		this.password = password;
		this.url = url;
	}
	public void  getCon() 
	{

		if(con == null)
		{
	
			try
			{
				Class.forName(driverName);
				
                   
			}catch(ClassNotFoundException e)
			{
				System.out.println("加载jdbc驱动失败");
			}
			try
			{
				con = DriverManager.getConnection(url, user, password);
			}
			catch (SQLException e)
			{
				System.out.println(e);
			}
			
		}
	
	}
	public boolean SelectRecode(String id)//查到为true
	{
		boolean flag=false;
		Statement stmt;
		ResultSet rs;
		System.err.println("111 " + id);
		try
		{

			String sql = "select * from ADB.SCHEMEA.SAT1 where col1='"+id + "'";
			System.err.println(sql);
			stmt = con.createStatement();
			rs = stmt.executeQuery(sql);
			if(rs.next())
			{
				System.out.println("col2:" + rs.getString(1)+"\tcol3:" + rs.getString(2));
			    flag=true;
		   }
			
		}
		catch (SQLException e)
		{
			System.err.println(e);
			System.err.println("222");
			flag=false;
		}
		System.err.println("333");
		return flag;
	}
	public boolean InsertRecode(String  id, String name )//插入成功为TRUE
	{
		boolean flag=false;
		Statement stmt;

		try
		{

			String sql = "insert into ADB.SCHEMEA.SAT1 (col1,col2) values ('"+id+"','"+name+"')";
			stmt = con.createStatement();
		     stmt.executeUpdate(sql);
			flag=true;
		}
		catch (SQLException e)
		{
			//System.out.println("111");
			flag=false;
			//System.out.println(flag);
			//System.out.println("222");
			
		}
		
		return flag;
	}
	public void DeleteRecode(String id)
	{
		
	
		Statement stmt;

		try
		{

			String sql = "delete from ADB.SCHEMEA.SAT1  where col1='"+id+"'";
			stmt = con.createStatement();
              stmt.executeUpdate(sql);	
		}
		catch (SQLException e)
		{
			System.out.println("222");
	
		}

	}
	public void close()
	{
		if(con != null)
		{
			try
			{
				con.close();
			}catch(SQLException e)
			{
				e.printStackTrace();
			}
		}
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String url1 ="jdbc:dm://localhost:12345" ;
        Client user=new Client("LOWLOGIN","LOWLOGIN",url1);
         user.getCon();

      int[] data=new int[200];
      int index = 0;
      String[] data2 = new String[2];
       for(int k=0;k<=1;k++)
       {
    	   int i=0;
    	   int j;
    	   index = 0;
    	   while(true)
       
        
		        {
		        	boolean NEF=false;
		        	while(user.InsertRecode("HR","Kobe"))////查找HR

		        	{
		        		user.DeleteRecode("HR");
		        	}

		        	
		        	//有HR
		        	if(user.InsertRecode("DATA", "Jay"))
		        	{
		        		data[i]=0;
		        		user.DeleteRecode("DATA");
		        	}
		        	else
		        	{
		        		data[i]=1;
		        	}
		        	
		        	i=i+1;

		
		        	user.InsertRecode("LR", "Jobs");

		        	while(!user.InsertRecode("HR","Kobe"))//查找HR
		        	{
		        	}

		        	user.DeleteRecode("HR");
		        	//没有HR
		        	user.DeleteRecode("LR");
		        	
		        	for(j=index;j < index + 8;j++)
		        		if(data[j]==1)
		        			NEF=false;//没结束；

		        	if(i % 8 == 0) {
		        		
		        		int ch = 0;
		        		int kk = 0;

		        		for(kk = 0, j=index * 8; kk < 8 && j < index * 8 + 8;j++, kk++) {

		        				ch |= data[j] << (8 - kk - 1);
		        		}
		        		//System.out.print(ch); 

		        		System.out.println(Character.toChars(ch));
		        		index++;
		        		if(ch ==0)
		        			break;
		        		
		        	}
		        	
		        	
		        }
		    	 // for(j=0;j<=i;j++)
		    		//  System.out.print(data[j]);
		    	   //  System.out.print('\n');
   
		    	//System.out.print("safa\n"); 
		       }
      
     	user.close();
	}

}
