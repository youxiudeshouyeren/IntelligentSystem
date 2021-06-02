int buttonpin = 13; //定义避障传感器接口

//定义各个灯的输出接口
int green1 =2;
int yellow1=1;
int red1   =3;

int green2 =4;
int yellow2=5;
int red2   =6;

int green3 =7;
int yellow3=8;
int red3   =9;

int green4 =10;
int yellow4=11;
int red4   =12;

int val;
int val2;
int count=1;
int accept_num;
void setup()
{
	pinMode(buttonpin, INPUT); //定义避障传感器为输入接口
	Serial.begin(9600);       //连接上位机，波特率为9600

	pinMode(green1,  OUTPUT);
	pinMode(yellow1, OUTPUT);
	pinMode(red1,    OUTPUT);

	pinMode(green2,  OUTPUT);
	pinMode(yellow2, OUTPUT);
	pinMode(red2,    OUTPUT);

	pinMode(green3,  OUTPUT);
	pinMode(yellow3, OUTPUT);
	pinMode(red3,    OUTPUT);

	pinMode(green4,  OUTPUT);
	pinMode(yellow4, OUTPUT);
	pinMode(red4,    OUTPUT);
}

void loop()
{
	val = digitalRead(buttonpin); //将数字接口3的值读取赋给val
    if (val == LOW) {              //当避障传感器检测低电平时，有障碍物
        Serial.print("YES\n");
    }
    else
    {          
        Serial.print("NO\n");
    }
	accept_num = Serial.read();
	if(accept_num==1)	
	{
		digitalWrite(green1,HIGH);
		digitalWrite(yellow1,LOW);
		digitalWrite(red1,LOW);

		digitalWrite(green2,LOW);
		digitalWrite(yellow2,LOW);
		digitalWrite(red2,HIGH);

		digitalWrite(green3,LOW);
		digitalWrite(yellow3,LOW);
		digitalWrite(red3,HIGH);

		digitalWrite(green4,LOW);
		digitalWrite(yellow4,LOW);
		digitalWrite(red4,HIGH);
	}
	else if(accept_num==2)
	{
		digitalWrite(green1,LOW);
		digitalWrite(yellow1,LOW);
		digitalWrite(red1,HIGH);

		digitalWrite(green2,HIGH);
		digitalWrite(yellow2,LOW);
		digitalWrite(red2,LOW);
		
		digitalWrite(green3,LOW);
		digitalWrite(yellow3,LOW);
		digitalWrite(red3,HIGH);

		digitalWrite(green4,LOW);
		digitalWrite(yellow4,LOW);
		digitalWrite(red4,HIGH);
	}
	else if(accept_num==3)
	{
		digitalWrite(green1,LOW);
		digitalWrite(yellow1,LOW);
		digitalWrite(red1,HIGH);

		digitalWrite(green2,LOW);
		digitalWrite(yellow2,LOW);
		digitalWrite(red2,HIGH);

		digitalWrite(green3,HIGH);
		digitalWrite(yellow3,LOW);
		digitalWrite(red3,LOW);

		digitalWrite(green4,LOW);
		digitalWrite(yellow4,LOW);
		digitalWrite(red4,HIGH);
	}
	else if(accept_num==4)
	{
		digitalWrite(green1,LOW);
		digitalWrite(yellow1,LOW);
		digitalWrite(red1,HIGH);

		digitalWrite(green2,LOW);
		digitalWrite(yellow2,LOW);
		digitalWrite(red2,HIGH);

		digitalWrite(green3,LOW);
		digitalWrite(yellow3,LOW);
		digitalWrite(red3,HIGH);

		digitalWrite(green4,HIGH);
		digitalWrite(yellow4,LOW);
		digitalWrite(red4,LOW);
	}
	else if(accept_num==5)
	{
		digitalWrite(green1,LOW);
		digitalWrite(yellow1,HIGH);
		digitalWrite(red1,LOW);

		digitalWrite(green2,LOW);
		digitalWrite(yellow2,LOW);
		digitalWrite(red2,HIGH);

		digitalWrite(green3,LOW);
		digitalWrite(yellow3,LOW);
		digitalWrite(red3,HIGH);

		digitalWrite(green4,LOW);
		digitalWrite(yellow4,LOW);
		digitalWrite(red4,HIGH);
	}
	else if(accept_num==6)
	{
		digitalWrite(green1,LOW);
		digitalWrite(yellow1,LOW);
		digitalWrite(red1,HIGH);

		digitalWrite(green2,LOW);
		digitalWrite(yellow2,HIGH);
		digitalWrite(red2,LOW);

		digitalWrite(green3,LOW);
		digitalWrite(yellow3,LOW);
		digitalWrite(red3,HIGH);

		digitalWrite(green4,LOW);
		digitalWrite(yellow4,LOW);
		digitalWrite(red4,HIGH);
	}
	else if(accept_num==7)
	{
		digitalWrite(green1,LOW);
		digitalWrite(yellow1,LOW);
		digitalWrite(red1,HIGH);

		digitalWrite(green2,LOW);
		digitalWrite(yellow2,LOW);
		digitalWrite(red2,HIGH);

		digitalWrite(green3,LOW);
		digitalWrite(yellow3,HIGH);
		digitalWrite(red3,LOW);

		digitalWrite(green4,LOW);
		digitalWrite(yellow4,LOW);
		digitalWrite(red4,HIGH);
	}
	else if(accept_num==8)
	{
		digitalWrite(green1,LOW);
		digitalWrite(yellow1,LOW);
		digitalWrite(red1,HIGH);

		digitalWrite(green2,LOW);
		digitalWrite(yellow2,LOW);
		digitalWrite(red2,HIGH);

		digitalWrite(green3,LOW);
		digitalWrite(yellow3,LOW);
		digitalWrite(red3,HIGH);

		digitalWrite(green4,LOW);
		digitalWrite(yellow4,HIGH);
		digitalWrite(red4,LOW);
	}
}