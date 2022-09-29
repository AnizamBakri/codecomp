#include <iostream>
#include <cstdlib>
#include<iomanip>
#include<string>
#include<fstream>

using namespace std;

const int SIZE=50;

int search(int [], int);
void addStudent(int[], string[], int[], char[]);
void changeMark(int []);

int matricNum[SIZE]={0};
string name[SIZE];
int mark[SIZE];
char grade[SIZE];

void readText(void)
{
	int nomatrix;
	string nama;
	int markah;
	char grad;
	ifstream inputFile1;
	int i=0;
	
	string	filename1 = "matricNo.txt";
	
	inputFile1.open(filename1.c_str());
		if  (inputFile1)
	{
		
		while (inputFile1 >> nomatrix >> nama>> markah>> grad)
		{	
			matricNum[i]=nomatrix;name[i]=nama;mark[i]=markah;grade[i]=grad;
			i++;
		}
		
	}
	inputFile1.close();
}

class Report
{
	private:
		int mark;
		string name;
		int matric;
		char grade;
		
	public:
		
		void setmatric(int);
		void setname(string);
		void setmark(int);
		
				
		int getmatric() const;
		string getname() const;
		int getmark() const;
		char getgrade() const;
	
};

void Report::setmatric(int matricC)
{
	matric=matricC;
}

void Report::setname(string nameC)
{
	name=nameC;
}

void Report::setmark(int markC)
{
	mark=markC;
}

int Report::getmatric() const
{
	return matric;
}

string Report::getname() const
{
	return name;
}

int Report::getmark() const
{
	return mark;
}

char Report::getgrade() const
{
	if(mark>=80)
	{
		return 'A';
	}

	else if(mark>=60&&mark<80)
	{
		return 'B';
	}

	else if(mark>=50&&mark<60)
	{
		return 'C';
	}

	else
	{
		return 'D';
	}
}

int showMenu()
{
	int i;

	cout << "Choose your menu"<<endl;
	cout << "	1. Add new student \n	2. Change marks \n	3. View student details \n	4. View all students details \n	5. Exit \n";
	
	cin>> i;
	while (i<1||i> 5)
	 {
	 	cout << "Please enter number between 1 until 5 : \n";
	 	cin >> i;
	 }
	 return i;
}

int main ()
{
	int nomatrix;
	int i,b;
	char N,n;
	int index=-1;
	ofstream inputFile1;
	string	filename1 = "matricNo.txt";
	cout <<"This is student report card system"<< endl<< endl;

	readText();
	
	i=showMenu();
	
	 switch (i)
	 {
	 	case 1:{system("cls");
				addStudent(matricNum,name,mark,grade);
				break;
	 	       }
	 	
	 	case 2:{system("cls");
	 		   changeMark(matricNum);
	 		   cout<<"Your mark have been changed succesfully!";
		       break;
	           }
	           
	 	case 3:
		 { system("cls");
	       cout<<"Enter the student's matric number : ";
		   cin>>nomatrix;
		
		 while(index<0)
		 {
		 index=search(matricNum,nomatrix);
			if(index<0)
				{
					cout<<"The Matric Number "<<nomatrix<<" is not available in our data. Please input stored Matric Number"<<endl<<endl;
					cout<<"Matric Number: ";
					cin>>nomatrix;	
				}
		 }
		 cout<<"Matric number:"<<matricNum[index]<<endl;cout<<"Name:"<<name[index]<<endl;cout<<"Mark:"<<mark[index]<<endl;cout<<"Grade:"<<grade[index];
		 break;
	     }
	     
	 	case 4:
		 {system("cls");
	     for(i=0;matricNum[i]!=0;i++)
		 {	
		 	cout<<matricNum[i]<<"	"<<name[i]<<"	"<<mark[i]<<"	"<<grade[i]<<endl;
		 }
		 break;
	     }
	 	default:  system("cls");cout<<"Thank you for using our program !!!"<<endl<<endl;break;
	 }

	inputFile1.open(filename1.c_str());
	for(i=0;matricNum[i]!=0;i++)
	{	
		inputFile1 << matricNum[i]<<"\t"<< name[i]<<"\t"<< mark[i]<<"\t"<<grade[i]<<endl;
	}
	inputFile1.close();
	return 0;
}

void addStudent(int matricNum[],string name[],int mark[],char grade[])
{
	cout<<"...........Add Student..........."<<endl<<endl;
	
	Report student[SIZE];
	int newIndex; 
	char save;
	
	newIndex=search(matricNum, 0);

	cout<<"Student's Matric Number: ";		
	cin>>matricNum[newIndex];
	student[newIndex].setmatric(matricNum[newIndex]);
	

	cout<<"Student's Name (First Name Only): ";
	cin>>name[newIndex];
	student[newIndex].setname(name[newIndex]);
	
	cout<<"Mark: ";
	cin>>mark[newIndex];
	student[newIndex].setmark(mark[newIndex]);
	
	grade[newIndex]=student[newIndex].getgrade();
	
	do
	{
		cout<<"Do you want to save the data?"<<endl;
		cout<<"[y] to save and [n] to cancel : ";
		cin>>save;
		
		if(save=='n')
		{
			matricNum[newIndex]=0;
			cout<<"Cancel data...";
			break;
		}	
		else if (save=='y')
			break;
		
		else 
			cout<<"Please press the [y] or [n] only"<<endl;
			
	}while(save!='n'||save!='y');
}

void changeMark(int matricNum[])
{
	Report student[SIZE];
	int nomatrix;
	int index=-1;
	cout<<"..........CHANGE MARK.........."<<endl<<endl;
	cout<<"Matric Number: ";
	cin>>nomatrix;
	
	while(index<0)
	{
		index = search(matricNum, nomatrix);
		
		if(index<0)
			{
				cout<<"The Matric Number "<<nomatrix<<" is not available in our data. Please input stored Matric Number"<<endl<<endl;
				cout<<"Matric Number: ";
				cin>>nomatrix;	
			}
	}
	
	
	cout<<"Name: "<<name[index]<<endl;
	cout<<"Previous Mark: "<<mark[index]<<endl;
	cout<<"New Mark: ";
	cin>>mark[index];
	student[index].setmark(mark[index]);
	grade[index]=student[index].getgrade();
		
	return;
}

int search(int matricNum[],int nomatrix)
{
	int index=0;
	int position=-1;
	bool found=false;
	
	while(index<SIZE&&!found)
	{	

		if(matricNum[index]==nomatrix)
		{
			found=true;
			position=index;
		
		}
		index++;
	}
	
	return position;
}







