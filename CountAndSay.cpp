#include <bits/stdc++.h>
using namespace std;

void solve(int n)
{
	string p = "11"; int k; int j=2;
	if(n==1)
	    cout<<"1"<<endl;
	else if(n==2)
	    cout<<"11"<<endl;
	    
	else {
		while(true) {
		    k=1; j++; string r;
		
		for(int i=1; i <p.length(); ++i) {
			if(p[i]==p[i-1])
			    k++;
			else {
			    stringstream ss;
                ss << k;
                string str = ss.str();
				r+=str; r+=p[i-1]; k=1;
			//	cout<<str<<endl;
			}
		}
		if(k>0)
		{
			    stringstream ss;
                ss << k;
                string str = ss.str();
				r+=str; r+=p[p.length()-1]; k=1;			
		}
		if(j==n)
		{
			cout<<r<<endl; 
		    return;
		}
		p = r;
	    }
	}
}
int main()
 {
 	int t;  cin>>t;
 	while(t--)
 	{
 	   int n;   cin>>n;
	   solve(n);	
	}
 }
