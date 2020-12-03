
public class Hello {
		public static void main(String args[]){
			int sum=0,i=0;
			do{
			sum+=i;										//累加i的值
			i++;
			}while(i<=100);								//当i小于等于100
			System.out.println("从1到100的整数和为："+sum);
		}
	}