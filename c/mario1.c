


/*
1.显示背景
2.显示静止的马里奥
3.移动的马里奥
4.让背景随马里奥的移动而移动
5.显示障碍物
6.增加马里奥与障碍物的判断
7.增加野怪
8.增加背景音乐
9.完善代码*/
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
#include<graphics.h>
#include <math.h>
#pragma comment(lib,"Winmm.lib")



#define High 504  // 游戏画面尺寸
#define Width 1024
#define rwHigh 131
#define rwWidth 134  //人物图片的像素
#define gsHigh 128
#define gsWidth 128  //怪兽图片的像素

int i;
int ksjm;//定义开始界面
float bj_x;   //绘制图像在背景原图上的坐标

IMAGE img_zk; //定义砖块的图像
IMAGE img_ks;//定义开始的图像

IMAGE img_bk,img_human1,img_human2;     //定义背景，人物
float human_x,human_y;   //定义人物的坐标
float x,y;//定义人物的实际坐标
float jiao_y;//定义马里奥脚下的坐标
int left_i,right_i;    //定义左右移动动画序号
int picture_x,picture_y;  //绘制图像的位置
int sfkt;//中间变量，是否可跳;
int sfkz;//中间变量，判断是否可跳;
int ydfx; //定义移动方向,1表示向右，0表示向左;
int sfkcz;//定义是否可操作

IMAGE img_pd1,img_pd2;  //定义炮弹图像

struct ptzgt    //定义炮台结构体
{
	float pt_x,pt_y;
	float pd_x,pd_y;
};

ptzgt zpt[3];  //定义真炮台
float ptzjbl[3]; //定义中间变量，形成相对移动

float G;  //重力加速度
float tgz,pdtg,tgjl;  //定义最大跳高值，判断跳高，跳高纪录；

struct gs
{
	float gs_x,gs_y;    //定义怪兽的坐标
	float gssj_x,gssj_y; //定义怪兽实际坐标
	int gspicture_x,gspicture_y;  //绘制怪兽图像的位置
	
};
gs num[5];    //定义五个野怪
int gsleft_i,gsright_i;  //定义怪兽左右移动的序号 
int gsydfw;  //怪兽移动范围
int gsydfx;  //怪兽移动方向，1表示向右，0表示向左;
int gsydjl;  //怪兽移动记录;              
IMAGE img_gs1,img_gs2;  //定义怪兽
float t[5];   //怪兽坐标的中间变量，用于形成相对移动
int number[5];  //怪兽坐标的中间变量；


float time;//定义时间
float sjc;//定义时间差
float sjjg;//定义时间间隔
float score;//定义得分

struct kd  //定义空地
{
	float qs_x,zd_x;
};
kd n[9];


struct zc  //定义支撑体
{
	float qs_x,zd_x;
	float high;//定义支撑物体的高
};
zc pt[3];   //定义炮台支撑
zc zk[4];   //定义问号砖块的支撑
zc mk[3];   //定义木块的支撑
zc sk[9];   //定义石块的支撑
zc xsg[3];  //定义下水管的支撑
int zkc;//定义每个问号砖块的长度

struct zaw
{
	float z_x,y_x;  //定义障碍物左右坐标
	float high;//定义障碍物的高
};
zaw za[13];

struct ftqy  //定义反弹物的结构体
{
	float qs_x,zd_x;//定义反弹物的起始及终点坐标
	float high;//定义反弹临界高度
	float xlhigh;//定义反弹后所到的高度
	int zjcs;//定义撞击次数，每个问号砖块只能撞击一次
};
ftqy fmk[4];
ftqy fzk[4];

int gameStatus = 0; // 游戏状态，0为初始菜单界面，1为正常游戏，2为结束游戏状态，3为游戏介绍
void startMenu();
void show();
void startup();
void updateWithoutInput();
void updateWithInput();

void startMenu() // 初始菜单界面
{
	
	putimage(0,0,&img_ks);	// 显示背景
	setbkmode(TRANSPARENT);
	settextcolor(BLACK);
	settextstyle(50,0, _T("黑体"));
	outtextxy(Width*0.3, High*0.2, "1 新游戏");
	outtextxy(Width*0.3, High*0.3, "2 结束游戏");

	
	settextcolor(RED);
	settextstyle(30,0, _T("黑体"));
	outtextxy(Width*0.25, High*0.6, "A键向左移动");
	outtextxy(Width*0.25, High*0.65, "D键向右移动");
	outtextxy(Width*0.25, High*0.7, "空格跳跃");
	FlushBatchDraw();
	Sleep(2);
	
	
	char input;
	if(kbhit())  // 判断是否有输入
	{
		input = getch();  // 根据用户的不同输入来移动，不必输入回车
		if (input == '1') 
			gameStatus = 1;
		else if (input == '2')
		{
			//readRecordFile();
			gameStatus = 2;
			exit(0);
		}
		
	}
}


void startup() // 数据初始化
{
	
	
	sfkcz=1;
	sjjg=0.02;

	human_x=0;
	human_y=0;
	x=human_x;
	y=human_y;
	jiao_y=y+rwHigh/2;
	left_i=0;
	right_i=0;
	bj_x=0;
	picture_x=0;
	picture_y=0;
	
	//以下是对炮台坐标的初始化
	zpt[0].pt_x=815;
	zpt[0].pt_y=360;
	zpt[0].pd_x=zpt[0].pt_x;
	zpt[0].pd_y=zpt[0].pt_y;
	ptzjbl[0]=0;
	
	zpt[1].pt_x=1200;
	zpt[1].pt_y=255;
	zpt[1].pd_x=1024;
	zpt[1].pd_y=zpt[1].pt_y;
	ptzjbl[1]=zpt[1].pt_x-1024;
	
	zpt[2].pt_x=5905;
	zpt[2].pt_y=360;
	zpt[2].pd_x=1024;
	zpt[2].pd_y=zpt[2].pt_y;
	ptzjbl[2]=zpt[2].pt_x-1024;
	
	
	time = 300;
	score=0;
	
	G=7;
	tgz=200;
	pdtg=0;
	tgjl=0;
	sfkt=0;
	zkc=50;
	
	
	num[0].gs_y=319;  //以下是对怪兽坐标的初始化
	num[0].gs_x=444;
	num[0].gspicture_x=0;
	num[0].gspicture_y=128;
	num[0].gssj_x=num[0].gs_x;
	num[0].gssj_y=num[0].gs_y;
	
	num[1].gs_y=319;
	num[1].gs_x=1024;
	num[1].gspicture_x=0;
	num[1].gspicture_y=128;
	num[1].gssj_x=2000;
	num[1].gssj_y=num[0].gs_y;
	
	num[2].gs_y=319;
	num[2].gs_x=1024;
	num[2].gspicture_x=0;
	num[2].gspicture_y=128;
	num[2].gssj_x=3000;
	num[2].gssj_y=num[0].gs_y;
	
	num[3].gs_y=177;
	num[3].gs_x=1024;
	num[3].gspicture_x=0;
	num[3].gspicture_y=128;
	num[3].gssj_x=3200;
	num[3].gssj_y=162;
	
	num[4].gs_y=319;
	num[4].gs_x=1024;
	num[4].gspicture_x=0;
	num[4].gspicture_y=128;
	num[4].gssj_x=5200;
	num[4].gssj_y=num[0].gs_y;
	
	t[0]=0;
	t[1]=num[1].gssj_x-1024;;//怪兽坐标中间变量的初始化
	t[2]=num[2].gssj_x-1024-80;
	t[3]=num[3].gssj_x-1024+200;
	t[4]=num[4].gssj_x-1024;
	
	for(int i=1;i<=4;i++)
		number[i]=0;
	
	gsleft_i=0;  //怪兽动画移动序号的初始化
	gsright_i=0;
	
	gsydfw=200;  //怪兽移动范围
	gsydfx=0;
	gsydjl=0;
	
	//以下是对空地坐标的初始化
	n[0].qs_x=2158;
	n[0].zd_x=2257;
	
	n[1].qs_x=2630;
	n[1].zd_x=2689;
	
	n[2].qs_x=2775;
	n[2].zd_x=2784;
	
	n[3].qs_x=6220;
	n[3].zd_x=6240;
	
	n[4].qs_x=6845;
	n[4].zd_x=6865;
	
	n[5].qs_x=8238;
	n[5].zd_x=8258;
	
	n[6].qs_x=8476;
	n[6].zd_x=8553;
	
	n[7].qs_x=9053;
	n[7].zd_x=9215;
	
	n[8].qs_x=9484;
	n[8].zd_x=9852;
	
	//炮台支撑
	pt[0].qs_x=786;
	pt[0].zd_x=pt[0].qs_x+50;
	pt[0].high=289;
	
	pt[1].qs_x=1060;
	pt[1].zd_x=pt[1].qs_x+50;
	pt[1].high=329;
	
	pt[2].qs_x=1200;
	pt[2].zd_x=pt[2].qs_x+50;
	pt[2].high=252;
	
	//问号砖块支撑
	zk[0].qs_x=975;
	zk[0].zd_x=zk[0].qs_x+zkc;
	zk[0].high=330;
	
	zk[1].qs_x=1390;
	zk[1].zd_x=zk[1].qs_x+zkc*3;
	zk[1].high=330;
	
	zk[2].qs_x=5900;
	zk[2].zd_x=zk[2].qs_x+zkc*9;
	zk[2].high=290;
	
	zk[3].qs_x=8110;
	zk[3].zd_x=zk[3].qs_x+zkc*7;
	zk[3].high=290;
	
	//木块的支撑
	mk[0].qs_x=2880;
	mk[0].zd_x=mk[0].qs_x+zkc*10;
	mk[0].high=145;
	
	mk[1].qs_x=3260;
	mk[1].zd_x=mk[1].qs_x+zkc*8;
	mk[1].high=290;
	
	mk[2].qs_x=6815;
	mk[2].zd_x=mk[2].qs_x+zkc;
	mk[2].high=360;
	
	//石块的支撑
	sk[0].qs_x=3020;
	sk[0].zd_x=sk[0].qs_x+zkc;
	sk[0].high=325;	
	
	sk[1].qs_x=3645;
	sk[1].zd_x=sk[1].qs_x+zkc;
	sk[1].high=250;
	
	sk[2].qs_x=7485;
	sk[2].zd_x=sk[2].qs_x+zkc*13;
	sk[2].high=325;
	
	sk[3].qs_x=8975;
	sk[3].zd_x=sk[3].qs_x+zkc+10;
	sk[3].high=290;
	
	sk[4].qs_x=9120;
	sk[4].zd_x=sk[4].qs_x+zkc;
	sk[4].high=250;
	
	sk[5].qs_x=9310;
	sk[5].zd_x=sk[5].qs_x+zkc;
	sk[5].high=250;
	
	sk[6].qs_x=9410;
	sk[6].zd_x=sk[6].qs_x+zkc;
	sk[6].high=395;
	
	sk[7].qs_x=9455;
	sk[7].zd_x=sk[7].qs_x+zkc*2;
	sk[7].high=145;
	
	sk[8].qs_x=9885;
	sk[8].zd_x=sk[8].qs_x+zkc;
	sk[8].high=395;
	
	//下水管的支撑
	xsg[0].qs_x=5615;
	xsg[0].zd_x=5710;
	xsg[0].high=250;
	
	xsg[1].qs_x=8255;
	xsg[1].zd_x=8445;
	xsg[1].high=436;
	
	xsg[2].qs_x=8590;
	xsg[2].zd_x=8690;
	xsg[2].high=360;
	
	
	//障碍物坐标
	za[0].z_x=820;
	za[0].y_x=860;
	za[0].high=290;
	
	za[1].z_x=1060;
	za[1].y_x=1100;
	za[1].high=330;
	
	za[2].z_x=1200;
	za[2].y_x=1245;
	za[2].high=260;
	
	za[3].z_x=3020;
	za[3].y_x=3070;
	za[3].high=325;
	
	za[4].z_x=3645;
	za[4].y_x=3695;
	za[4].high=255;
	
	za[5].z_x=5620;
	za[5].y_x=5710;
	za[5].high=250;
	
	za[6].z_x=8110;
	za[6].y_x=8110;
	za[6].high=290;
	
	za[7].z_x=8635;
	za[7].y_x=8685;
	za[7].high=360;
	
	za[8].z_x=5900;
	za[8].y_x=6040;
	za[8].high=360;
	
	za[9].z_x=6285;
	za[9].y_x=6335;
	za[9].high=395;
	
	za[10].z_x=8975;
	za[10].y_x=9025;
	za[10].high=285;
	
	za[11].z_x=9405;
	za[11].y_x=9455;
	za[11].high=400;
	
	za[12].z_x=9895;
	za[12].y_x=9935;
	za[12].high=400;
	
	//反弹物中木块和石块的判断
	fmk[0].qs_x=mk[1].qs_x-zkc;
	fmk[0].zd_x=mk[1].zd_x;
	fmk[0].high=325;
	fmk[0].xlhigh=371;
	
	fmk[1].qs_x=mk[0].qs_x-zkc;
	fmk[1].zd_x=mk[0].zd_x-zkc;
	fmk[1].high=180;
	fmk[1].xlhigh=220;
	
	fmk[2].qs_x=sk[2].qs_x-zkc;
	fmk[2].zd_x=sk[2].zd_x-zkc;
	fmk[2].high=355;
	fmk[2].xlhigh=371;
	
	fmk[3].qs_x=sk[5].qs_x-zkc;
	fmk[3].zd_x=sk[5].zd_x-zkc;
	fmk[3].high=285;
	fmk[3].xlhigh=371;
	
	//以下是砖块反弹的数据
	fzk[0].qs_x=zk[0].qs_x-zkc;
	fzk[0].zd_x=zk[0].zd_x-zkc;
	fzk[0].high=360;
	fzk[0].xlhigh=371;
	
	fzk[1].qs_x=zk[1].qs_x-zkc;
	fzk[1].zd_x=zk[1].zd_x-zkc;
	fzk[1].high=360;
	fzk[1].xlhigh=371;
	
	fzk[2].qs_x=zk[2].qs_x-zkc;
	fzk[2].zd_x=zk[2].zd_x-zkc;
	fzk[2].high=320;
	fzk[2].xlhigh=371;
	
	fzk[3].qs_x=zk[3].qs_x-zkc;
	fzk[3].zd_x=zk[3].zd_x-zkc;
	fzk[3].high=320;
	fzk[3].xlhigh=371;
	for(i=0;i<4;i++)
		fzk[i].zjcs=0;
	
	
	mciSendString("open E:\\bj.mp3 alias bkmusic", NULL, 0, NULL);   //背景音乐
	mciSendString("play bkmusic repeat", NULL, 0, NULL);    //循环播放
	initgraph(Width, High);
	loadimage(&img_human2,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\马里奥.jpg");
	loadimage(&img_bk,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\背景.jpg");
	loadimage(&img_human1,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\马里奥掩码图.jpg");
	loadimage(&img_pd2,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\炮弹.jpg");
	loadimage(&img_pd1,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\炮弹掩码.jpg");
	loadimage(&img_gs1,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\野怪2 掩码图.jpg");
	loadimage(&img_gs2,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\野怪2.jpg");
	loadimage(&img_zk,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\砖块.jpg");
	loadimage(&img_ks,"E:\\Microsoft Visual Studio\\MyProjects\\超级玛丽\\ks.jpg");	
	BeginBatchDraw();
	while(gameStatus==0)
		startMenu();
	
}



void show()  // 显示画面
{

	
	

	
	putimage(0,0,Width,High,&img_bk,bj_x,0);
	putimage(human_x,human_y,rwWidth/2,rwHigh/2,&img_human1,picture_x,picture_y,NOTSRCERASE);
	putimage(human_x,human_y,rwWidth/2,rwHigh/2,&img_human2,picture_x,picture_y,SRCINVERT);//马里奥的图片
	
	
	putimage(num[0].gs_x,num[0].gs_y,gsWidth,gsHigh,&img_gs1,num[0].gspicture_x,num[0].gspicture_y,NOTSRCERASE);
	putimage(num[0].gs_x,num[0].gs_y,gsWidth,gsHigh,&img_gs2,num[0].gspicture_x,num[0].gspicture_y,SRCINVERT);//怪兽的图片
	
	if(num[1].gssj_x-x<512)
	{
		putimage(num[1].gs_x,num[1].gs_y,gsWidth,gsHigh,&img_gs1,num[1].gspicture_x,num[1].gspicture_y,NOTSRCERASE);
		putimage(num[1].gs_x,num[1].gs_y,gsWidth,gsHigh,&img_gs2,num[1].gspicture_x,num[1].gspicture_y,SRCINVERT);
	}
	if(num[2].gssj_x-x<512)
	{
		putimage(num[2].gs_x,num[2].gs_y,gsWidth,gsHigh,&img_gs1,num[2].gspicture_x,num[2].gspicture_y,NOTSRCERASE);
		putimage(num[2].gs_x,num[2].gs_y,gsWidth,gsHigh,&img_gs2,num[2].gspicture_x,num[2].gspicture_y,SRCINVERT);
	}
	if(num[3].gssj_x-x<512)
	{
		putimage(num[3].gs_x,num[3].gs_y,gsWidth,gsHigh,&img_gs1,num[3].gspicture_x,num[3].gspicture_y,NOTSRCERASE);
		putimage(num[3].gs_x,num[3].gs_y,gsWidth,gsHigh,&img_gs2,num[3].gspicture_x,num[3].gspicture_y,SRCINVERT);
	}
	if(num[4].gssj_x-x<512)
	{
		putimage(num[4].gs_x,num[4].gs_y,gsWidth,gsHigh,&img_gs1,num[4].gspicture_x,num[4].gspicture_y,NOTSRCERASE);
		putimage(num[4].gs_x,num[4].gs_y,gsWidth,gsHigh,&img_gs2,num[4].gspicture_x,num[4].gspicture_y,SRCINVERT);
	}
	
	
	putimage(zpt[0].pd_x,zpt[0].pd_y,94,81,&img_pd1,0,0,NOTSRCERASE);
	putimage(zpt[0].pd_x,zpt[0].pd_y,94,81,&img_pd2,0,0,SRCINVERT);
	
	if(zpt[1].pt_x-x<512)
	{
		putimage(zpt[1].pd_x,zpt[1].pd_y,94,81,&img_pd1,0,0,NOTSRCERASE);
		putimage(zpt[1].pd_x,zpt[1].pd_y,94,81,&img_pd2,0,0,SRCINVERT);
	}
	
	if(zpt[2].pt_x-x<512)
	{
		putimage(zpt[2].pd_x,zpt[2].pd_y,94,81,&img_pd1,0,0,NOTSRCERASE);
		putimage(zpt[2].pd_x,zpt[2].pd_y,94,81,&img_pd2,0,0,SRCINVERT);
	}
	
	/*settextcolor(YELLOW);
	settextstyle(16, 0, "宋体");
	char s[50];
	sprintf(s, "x=%f y=%f", x,y );
	outtextxy(10, 10, s);
	settextcolor(YELLOW);
	settextstyle(16, 0, "宋体");
	char s1[50];
	sprintf(s1, "jiao_y=%f", jiao_y);
	outtextxy(10, 30, s1);*/
	
	
	
	settextcolor(YELLOW);
	settextstyle(32, 0, "宋体");
	char s4[50];
	sprintf(s4, "time=%f", time);
	outtextxy(300, 10, s4);
	
	settextcolor(YELLOW);
	settextstyle(32, 0, "宋体");
	char s5[50];
	sprintf(s5, "score=%.8f", score);
	outtextxy(700, 10, s5);
	
	
	
	
	FlushBatchDraw();
	
}

void updateWithoutInput()  // 与用户输入无关的更新
{
	time-=sjjg;
	sfkt=0;
	sfkz=1;
	if(jiao_y>555)
	{
		mciSendString("close bkmusic", NULL, 0, NULL);
		mciSendString("close swmusic", NULL, 0, NULL);
		mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
		mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
		system("pause");
		exit(0);
	}
	
	
	//以下是对跳跃有关的说明
	if(pdtg==0&&jiao_y<436)  //没有跳高的情况下并且在地面以上
	{
		human_y+=G;
		y+=G;
		jiao_y+=G;
	}
	if(pdtg==1)
	{
		human_y-=G*2;
		y-=G*2;
		jiao_y-=G*2;
		tgjl+=G*2;
		if(tgjl>=tgz)
		{
			pdtg=0;
			tgjl=0;
		}
	}
	
	//以下是对空地的判断
	if(x+67>=n[0].qs_x+5&&x+67<=n[0].zd_x+20||human_y>391)  //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G;
			y+=G;
			jiao_y+=G;
		}
	}
	
	if(x+67>=n[1].qs_x&&x+67<=n[1].zd_x+20||human_y>391)  //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G;
			y+=G;
			jiao_y+=G;
		}
		
	}
	
	if(x+67>=n[2].qs_x&&x+67<=n[2].zd_x+20||human_y>391)  //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G;
			y+=G;
			jiao_y+=G;
		}
		
	}
	
	if(x+67>=n[3].qs_x&&x+67<=n[3].zd_x+20&&jiao_y>300||human_y>391)  //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G;
			y+=G;
			jiao_y+=G;
		}
		
	}
	
	if(x+67>=n[4].qs_x&&x+67<=n[4].zd_x+20&&jiao_y>375||human_y>391)  //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G;
			y+=G;
			jiao_y+=G;
		}
		
	}
	
	if(x+67>=n[5].qs_x&&x+67<=n[5].zd_x+20&&jiao_y>300||human_y>391)  //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G;
			y+=G;
			jiao_y+=G;
		}
		
	}
	
	if(x+67>=n[6].qs_x&&x+67<=n[6].zd_x+20)  //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G;
			y+=G;
			jiao_y+=G;
		}
		
	}
	
	if((x+67>=n[7].qs_x&&x+67<=n[7].qs_x+90)||(x+67>=n[7].qs_x+140&&x+67<=n[7].zd_x-10)||(x+67>=n[7].qs_x+90&&x+67<=n[7].qs_x+140&&jiao_y>=275))  //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G;
			y+=G;
			jiao_y+=G;
		}
		
	}
	
	if((x+67>=n[8].qs_x+100&&x+67<=n[8].zd_x-20)||(x+67>=n[8].qs_x&&x+67<=n[8].qs_x+100&&jiao_y>160) ) //人物处于空地中间并且人物已经下落了
	{
		
		if(pdtg==0)
		{
			human_y+=G/3;
			y+=G/3;
			jiao_y+=G/3;
		}
		
	}
	
	
	
	if (right_i == 1)
		right_i = -1;
	if (left_i == 1)
		left_i = -1;
	
	
	//炮弹的说明
	if(zpt[0].pd_x>-300)//保证炮弹完全的消失在画布的视野里面
	{
		zpt[0].pd_x-=6;
		zpt[0].pd_x-=bj_x-ptzjbl[0];
		ptzjbl[0]=bj_x;
	}
	
	if(zpt[1].pt_x-x<=512)
	{
		zpt[1].pd_x-=6;
		zpt[1].pd_x-=bj_x-ptzjbl[1];
		ptzjbl[1]=bj_x;
		if(zpt[1].pd_x<-300)
			zpt[1].pd_x=-300;
	}
	
	if(zpt[2].pt_x-x<=512)
	{
		zpt[2].pd_x-=6;
		zpt[2].pd_x-=bj_x-ptzjbl[2];
		ptzjbl[2]=bj_x;
		if(zpt[2].pd_x<-300)
			zpt[2].pd_x=-300;
	}
	for(i=0;i<3;i++)
	{
		if((abs(human_x+rwWidth/4-zpt[i].pd_x)<=5)&&(abs(human_y-zpt[i].pd_y)<=40))
		{
			mciSendString("close bkmusic", NULL, 0, NULL);
			mciSendString("close swmusic", NULL, 0, NULL);
			mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
			mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
			system("pause");
			exit(0);
		}
	}
	//怪兽的说明
	
	if(x>num[0].gssj_x)
	{
		
		num[0].gs_x=num[0].gs_x-(bj_x-t[0]);
		if(num[0].gs_x<-130)
		{
			num[0].gs_x=-300;
			num[0].gssj_x=-300;
		}
		t[0]=bj_x;
	}
	
	if(num[1].gssj_x-x<512)
	{
		num[1].gs_x=num[1].gs_x-(bj_x-t[1]);
		if(num[1].gs_x<-100)
		{
			num[1].gs_x=-300;
			num[1].gssj_x=-130;
		}
		t[1]=bj_x;
	}
	
	
	if(num[2].gssj_x-x<512)
	{
		num[2].gs_x=num[2].gs_x-(bj_x-t[2]);
		if(num[2].gs_x<-100)
		{
			num[2].gs_x=-300;
			num[2].gssj_x=-130;
		}
		t[2]=bj_x;
	}
	
	if(num[3].gssj_x-x<512)
	{
		num[3].gs_x=num[3].gs_x-(bj_x-t[3]);
		if(num[3].gs_x<-100)
		{
			num[3].gs_x=-300;
			num[3].gssj_x=-130;
		}
		t[3]=bj_x;
	}
	
	if(num[4].gssj_x-x<512)
	{
		num[4].gs_x=num[4].gs_x-(bj_x-t[4]);
		if(num[4].gs_x<-100)
		{
			num[4].gs_x=-300;
			num[4].gssj_x=-130;
		}
		t[4]=bj_x;
	}
	
	if(gsydfx==0)
	{
		gsleft_i++;
		num[0].gs_x-=2;
		num[0].gssj_x-=2;
		num[1].gs_x-=2;
		num[1].gssj_x-=2;
		num[2].gs_x-=2;
		num[2].gssj_x-=2;
		num[3].gs_x-=2;
		num[3].gssj_x-=2;
		num[4].gs_x-=2;
		num[4].gssj_x-=2;
		gsydjl+=2;
		if(gsydjl==gsydfw)
		{
			gsydfx=1;
			gsydjl=0;
			gsleft_i=-1;
		}
		num[0].gspicture_x=gsleft_i*gsWidth;
		num[0].gspicture_y=128;
		num[1].gspicture_x=gsleft_i*gsWidth;
		num[1].gspicture_y=128;
		num[2].gspicture_x=gsleft_i*gsWidth;
		num[2].gspicture_y=128;
		num[3].gspicture_x=gsleft_i*gsWidth;
		num[3].gspicture_y=128;
		num[4].gspicture_x=gsleft_i*gsWidth;
		num[4].gspicture_y=128;
		if(gsleft_i==3)
			gsleft_i=-1;
	}
	if(gsydfx==1)
	{
		gsright_i++;
		num[0].gs_x+=2;
		num[0].gssj_x+=2;
		num[1].gs_x+=2;
		num[1].gssj_x+=2;
		num[2].gs_x+=2;
		num[2].gssj_x+=2;
		num[3].gs_x+=2;
		num[3].gssj_x+=2;
		num[4].gs_x+=2;
		num[4].gssj_x+=2;
		gsydjl+=2;
		num[0].gspicture_x=gsright_i*gsWidth;
		num[0].gspicture_y=256;
		num[1].gspicture_x=gsright_i*gsWidth;
		num[1].gspicture_y=256;
		num[2].gspicture_x=gsright_i*gsWidth;
		num[2].gspicture_y=256;
		num[3].gspicture_x=gsright_i*gsWidth;
		num[3].gspicture_y=256;
		num[4].gspicture_x=gsright_i*gsWidth;
		num[4].gspicture_y=256;
		if(gsydjl==gsydfw)
		{
			gsydfx=0;
			gsydjl=0;
			gsright_i=-1;
		}
		if(gsright_i==3)
			gsright_i=-1;
		
	}
	
	
	
	
	
	
	
	
	
	//以下是对炮台支撑的说明
	if(x>=pt[0].qs_x&&x<pt[0].zd_x&&jiao_y<=296&&jiao_y>=289)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	if(x>=pt[1].qs_x-30&&x<pt[1].zd_x&&jiao_y<=334&&jiao_y>=329)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>=pt[2].qs_x-30&&x<pt[2].zd_x-30&&jiao_y<=275&&jiao_y>=255)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	//以下是对砖块支撑的说明
	if(x>zk[0].qs_x-rwWidth/4&&x<zk[0].zd_x-rwWidth/4&&jiao_y>=325+10&&jiao_y<=335+10)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>zk[1].qs_x-rwWidth/4&&x<zk[1].zd_x-rwWidth/4&&jiao_y>=325+10&&jiao_y<=335+10)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>zk[2].qs_x-rwWidth/4&&x<zk[2].zd_x-rwWidth/4&&jiao_y>=285+10&&jiao_y<=295+10)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>zk[3].qs_x-rwWidth/4&&x<zk[3].zd_x-rwWidth/4&&jiao_y>=285+10&&jiao_y<=295+10)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	//以下是对木块支撑的说明
	if(x>mk[0].qs_x-rwWidth/4&&x<mk[0].zd_x-rwWidth/4&&jiao_y>=150&&jiao_y<=160)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>mk[1].qs_x-rwWidth/4&&x<mk[1].zd_x-rwWidth/4&&jiao_y>=295&&jiao_y<=305)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>mk[2].qs_x-rwWidth/4&&x<mk[2].zd_x-rwWidth/4&&jiao_y>=365&&jiao_y<=375)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	//以下是对石块支撑的说明
	if(x>sk[0].qs_x-rwWidth/4&&x<sk[0].zd_x-rwWidth/4&&jiao_y>=sk[0].high+5&&jiao_y<=sk[0].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>sk[1].qs_x-rwWidth/4&&x<sk[1].zd_x-rwWidth/4&&jiao_y>=sk[1].high+5&&jiao_y<=sk[1].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>sk[2].qs_x-rwWidth/4&&x<sk[2].zd_x-rwWidth/4&&jiao_y>=sk[2].high+5&&jiao_y<=sk[2].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>sk[3].qs_x-rwWidth/4&&x<sk[3].zd_x-rwWidth/4&&jiao_y>=sk[3].high+5&&jiao_y<=sk[3].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>sk[4].qs_x-rwWidth/4&&x<sk[4].zd_x-rwWidth/4&&jiao_y>=sk[4].high+5&&jiao_y<=sk[4].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>sk[5].qs_x-rwWidth/4&&x<sk[5].zd_x-rwWidth/4&&jiao_y>=sk[5].high+5&&jiao_y<=sk[5].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>sk[6].qs_x-rwWidth/4&&x<sk[6].zd_x-rwWidth/4&&jiao_y>=sk[6].high+5&&jiao_y<=sk[6].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>sk[7].qs_x-rwWidth/4&&x<sk[7].zd_x-rwWidth/4&&jiao_y>=sk[7].high+5&&jiao_y<=sk[7].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>sk[8].qs_x-rwWidth/4&&x<sk[8].zd_x-rwWidth/4&&jiao_y>=sk[8].high+5&&jiao_y<=sk[8].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	//下水管的支撑
	if(x>xsg[0].qs_x-rwWidth/4&&x<xsg[0].zd_x-rwWidth/4&&jiao_y>=xsg[0].high+5&&jiao_y<=xsg[0].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	if(x>xsg[2].qs_x-rwWidth/4&&x<xsg[2].zd_x-rwWidth/4&&jiao_y>=xsg[2].high+5&&jiao_y<=xsg[2].high+15)
	{
		sfkt=1;
		pdtg=0;
		human_y-=G;
		y-=G;
		jiao_y-=G;
	}
	
	//以下是对行走的判断
	//向右的情况
	if(ydfx==1)
	{
		if(x>=za[0].z_x-rwWidth/2&&x<=za[0].z_x-rwWidth/2+5&&jiao_y>za[0].high+10)
			sfkz=0;
		if(x>=za[1].z_x-rwWidth/2&&x<=za[1].z_x-rwWidth/2+5&&jiao_y>za[1].high+10)
			sfkz=0;
		if(x>=za[2].z_x-rwWidth/2&&x<=za[2].z_x-rwWidth/2+5&&jiao_y>za[2].high+10)
			sfkz=0;
		if(x>=za[3].z_x-rwWidth/2&&x<=za[3].z_x-rwWidth/2+5&&jiao_y>za[3].high+10)
			sfkz=0;
		if(x>=za[4].z_x-rwWidth/2&&x<=za[4].z_x-rwWidth/2+5&&jiao_y>za[4].high+10&&jiao_y<za[4].high+70)
			sfkz=0;
		else if(x>=za[4].z_x-rwWidth/2&&x<=za[4].z_x-rwWidth/2+5&&jiao_y>400)                             //因为这个障碍位于空中，所以要对地面进行说明
			sfkz=1;
		if(x>=za[5].z_x-rwWidth/2&&x<=za[5].z_x-rwWidth/2+5&&jiao_y>za[5].high+10)
			sfkz=0;
		if(x>=za[6].z_x-rwWidth/2&&x<=za[6].z_x-rwWidth/2+5&&jiao_y>za[6].high+10&&jiao_y<za[4].high+70)
			sfkz=0;
		else if(x>=za[6].z_x-rwWidth/2&&x<=za[6].z_x-rwWidth/2+5&&jiao_y>400)                             //因为这个障碍位于空中，所以要对地面进行说明
			sfkz=1;
		if(x>=za[7].z_x-rwWidth/2&&x<=za[7].z_x-rwWidth/2+5&&jiao_y>za[7].high+10)
			sfkz=0;
		if(x>=za[8].z_x-rwWidth/2&&x<=za[8].z_x-rwWidth/2+5&&jiao_y>za[8].high+10)
			sfkz=0;
		if(x>=za[9].z_x-rwWidth/2&&x<=za[9].z_x-rwWidth/2+5&&jiao_y>za[9].high+10)
			sfkz=0;
		if(x>=za[10].z_x-rwWidth/2&&x<=za[10].z_x-rwWidth/2+5&&jiao_y>za[10].high+10)
			sfkz=0;
		if(x>=za[11].z_x-rwWidth/2+10&&x<=za[11].z_x-rwWidth/2+15&&jiao_y>za[11].high+10)
			sfkz=0;
		if(x>=za[12].z_x-rwWidth/2&&x<=za[12].z_x-rwWidth/2+5&&jiao_y>za[12].high+10)
			sfkz=0;
	}
	//向左的移动障碍判断
	if(ydfx==0)
	{
		if(x>=za[0].y_x-5&&x<za[0].y_x&&jiao_y>za[0].high+10)
			sfkz=0;
		if(x>=za[1].y_x-5&&x<za[1].y_x&&jiao_y>za[1].high+10)
			sfkz=0;
		if(x>=za[2].y_x-5&&x<za[2].y_x&&jiao_y>za[2].high+10)
			sfkz=0;
		if(x>=za[3].y_x-5&&x<za[3].y_x&&jiao_y>za[3].high+10)
			sfkz=0;
		if(x>=za[4].y_x-5&&x<za[4].y_x&&jiao_y>za[4].high+10&&jiao_y<za[4].high+70)
			sfkz=0;
		else if(x>=za[4].y_x&&x<=za[4].y_x+5&&jiao_y>400)                             //因为这个障碍位于空中，所以要对地面进行说明
			sfkz=1;
		if(x>=za[5].y_x-5&&x<za[5].y_x&&jiao_y>za[5].high+10)
			sfkz=0;
		if(x>=za[6].y_x-5&&x<za[6].y_x&&jiao_y>za[6].high+10&&jiao_y<za[4].high+70)
			sfkz=0;
		else if(x>=za[6].y_x&&x<=za[6].y_x+5&&jiao_y>400)                             //因为这个障碍位于空中，所以要对地面进行说明
			sfkz=1;
		if(x>=za[7].y_x-5&&x<za[7].y_x&&jiao_y>za[7].high+10)
			sfkz=0;
		if(x>=za[8].y_x-5&&x<za[8].y_x&&jiao_y>za[8].high+10)
			sfkz=0;
		if(x>=za[9].y_x-5&&x<za[9].y_x&&jiao_y>za[9].high+10)
			sfkz=0;
		if(x>=za[10].y_x-5&&x<za[10].y_x&&jiao_y>za[10].high+10)
			sfkz=0;
		if(x>=za[11].y_x-5&&x<za[11].y_x&&jiao_y>za[11].high+10)
			sfkz=0;
		if(x>=za[12].y_x-5&&x<za[12].y_x&&jiao_y>za[12].high+10)
			sfkz=0;
		
	}
	
	//以下是反弹部分的说明
	if(x>=fmk[0].qs_x&&x<=fmk[0].zd_x&&human_y>=fmk[0].high-30&&human_y<=fmk[0].high)
	{
		pdtg=0;
		human_y=fmk[0].xlhigh;
		y=fmk[0].xlhigh+65;
		jiao_y=y;
	}
	
	if(x>=fmk[1].qs_x&&x<=fmk[1].zd_x&&human_y>=fmk[1].high-30&&human_y<=fmk[1].high-10)
	{
		pdtg=0;
		human_y=fmk[1].xlhigh;
		y=fmk[1].xlhigh+65;
		jiao_y=y;
	}
	
	if(x>=fmk[2].qs_x&&x<=fmk[2].zd_x&&human_y>=fmk[2].high-30&&human_y<=fmk[2].high)
	{
		pdtg=0;
		human_y=fmk[2].xlhigh;
		y=fmk[2].xlhigh+65;
		jiao_y=y;
	}
	
	if(x>=fmk[3].qs_x&&x<=fmk[3].zd_x&&human_y>=fmk[3].high-30&&human_y<=fmk[3].high)
	{
		pdtg=0;
		human_y=fmk[3].xlhigh;
		y=fmk[3].xlhigh+65;
		jiao_y=y;
	}
	
	//以下是砖块的反弹
	if(x>=fzk[0].qs_x&&x<=fzk[0].zd_x&&human_y>=fzk[0].high-30&&human_y<=fzk[0].high)
	{
		pdtg=0;
		human_y=fzk[0].xlhigh;
		y=fzk[0].xlhigh+65;
		jiao_y=y;
		fzk[0].zjcs++;
		if(fzk[0].zjcs==1)
		{
			score+=100;
			mciSendString("close zkmusic", NULL, 0, NULL);
			mciSendString("open E:\\顶砖块.mp3 alias zkmusic", NULL, 0, NULL);
			mciSendString("play zkmusic", NULL, 0, NULL);   //仅播放一次音乐
		}
	}
	
	if(x>=fzk[1].qs_x&&x<=fzk[1].zd_x&&human_y>=fzk[1].high-30&&human_y<=fzk[1].high)
	{
		
		pdtg=0;
		human_y=fzk[1].xlhigh;
		y=fzk[1].xlhigh+65;
		jiao_y=y;
		fzk[1].zjcs++;
		if(fzk[1].zjcs==1)
		{
			score+=100;
			mciSendString("close zkmusic", NULL, 0, NULL);
			mciSendString("open E:\\顶砖块.mp3 alias zkmusic", NULL, 0, NULL);
			mciSendString("play zkmusic", NULL, 0, NULL);   //仅播放一次音乐
		}
	}
	
	if(x>=fzk[2].qs_x&&x<=fzk[2].zd_x&&human_y>=fzk[2].high-30&&human_y<=fzk[2].high)
	{
		pdtg=0;
		human_y=fzk[2].xlhigh;
		y=fzk[2].xlhigh+65;
		jiao_y=y;
		fzk[2].zjcs++;
		if(fzk[2].zjcs==1)
		{
			score+=100;
			mciSendString("close zkmusic", NULL, 0, NULL);
			mciSendString("open E:\\顶砖块.mp3 alias zkmusic", NULL, 0, NULL);
			mciSendString("play zkmusic", NULL, 0, NULL);   //仅播放一次音乐
		}
	}
	
	if(x>=fzk[3].qs_x&&x<=fzk[3].zd_x&&human_y>=fzk[3].high-30&&human_y<=fzk[3].high)
	{
		pdtg=0;
		human_y=fzk[3].xlhigh;
		y=fzk[3].xlhigh+65;
		jiao_y=y;
		fzk[3].zjcs++;
		if(fzk[3].zjcs==1)
		{
			score+=100;
			mciSendString("close zkmusic", NULL, 0, NULL);
			mciSendString("open E:\\顶砖块.mp3 alias zkmusic", NULL, 0, NULL);
			mciSendString("play zkmusic", NULL, 0, NULL);   //仅播放一次音乐
		}
	}
	
	
	//以下是对遇到怪兽的说明
	for(i=0;i<5;i++)
	{
		if(i==3)
		{
			if(ydfx==1&&gsydfx==1)
			{
				
				if(abs(human_x+rwWidth/2-num[i].gs_x-64)<=20&&human_y>300)
					sfkz=1;
				else if(abs(human_x+rwWidth/2-num[i].gs_x-64)<=20&&human_y>=num[i].gssj_y)
				{
					mciSendString("close bkmusic", NULL, 0, NULL);
					mciSendString("close swmusic", NULL, 0, NULL);
					mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
					mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
					human_y+=40;
					y+=40;
					jiao_y+=40;
				}
			}
			
			else if(ydfx==1&&gsydfx==0)
			{
				if(abs(human_x+rwWidth/2-num[i].gs_x-64)<=20&&human_y>300)
					sfkz=1;
				else if(abs(human_x+rwWidth/2-num[i].gs_x-64)<=20&&human_y>=num[i].gssj_y)
				{
					mciSendString("close bkmusic", NULL, 0, NULL);
					mciSendString("close swmusic", NULL, 0, NULL);
					mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
					mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
					human_y+=40;
					y+=40;
					jiao_y+=40;
				}
			}
			
			else if(ydfx==0&&gsydfx==1)
			{
				if(abs(human_x-num[i].gs_x-64)<=20&&human_y>300)
					sfkz=1;
				else if(abs(human_x-num[i].gs_x-64)<=20&&human_y>=num[i].gssj_y)
				{
					mciSendString("close bkmusic", NULL, 0, NULL);
					mciSendString("close swmusic", NULL, 0, NULL);
					mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
					mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
					human_y+=40;
					y+=40;
					jiao_y+=40;
				}
			}
			
			else if(ydfx==0&&gsydfx==0)
			{
				if(abs(human_x-num[i].gs_x-64)<=20&&human_y>300)
					sfkz=1;
				else if(abs(human_x-num[i].gs_x-64)<=20&&human_y>=num[i].gssj_y)
				{
					mciSendString("close bkmusic", NULL, 0, NULL);
					mciSendString("close swmusic", NULL, 0, NULL);
					mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
					mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
					human_y+=40;
					y+=40;
					jiao_y+=40;
				}
			}
			
		}
		else
		{
			if(ydfx==1&&gsydfx==1)
			{
				if(abs(human_x+rwWidth/2-num[i].gs_x-64)<=20&&human_y>=num[i].gssj_y)
				{
					mciSendString("close bkmusic", NULL, 0, NULL);
					mciSendString("close swmusic", NULL, 0, NULL);
					mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
					mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
					human_y+=40;
					y+=40;
					jiao_y+=40;
				}
			}
			
			else if(ydfx==1&&gsydfx==0)
			{
				if(abs(human_x+rwWidth/2-num[i].gs_x-64)<=20&&human_y>=num[i].gssj_y)
				{
					mciSendString("close bkmusic", NULL, 0, NULL);
					mciSendString("close swmusic", NULL, 0, NULL);
					mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
					mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
					human_y+=40;
					y+=40;
					jiao_y+=40;
				}
			}
			
			else if(ydfx==0&&gsydfx==1)
			{
				if(abs(human_x-num[i].gs_x-64)<=20&&human_y>=num[i].gssj_y)
				{
					mciSendString("close bkmusic", NULL, 0, NULL);
					mciSendString("close swmusic", NULL, 0, NULL);
					mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
					mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
					human_y+=40;
					y+=40;
					jiao_y+=40;
				}
			}
			
			else if(ydfx==0&&gsydfx==0)
			{
				if(abs(human_x-num[i].gs_x-64)<=20&&human_y>=num[i].gssj_y)
				{
					mciSendString("close bkmusic", NULL, 0, NULL);
					mciSendString("close swmusic", NULL, 0, NULL);
					mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
					mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
					human_y+=40;
					y+=40;
					jiao_y+=40;
					
				}
			}
		}
	}

	if(time<=0&&x<9910)
	{
		mciSendString("close bkmusic", NULL, 0, NULL);
		mciSendString("close swmusic", NULL, 0, NULL);
		mciSendString("open E:\\死亡.mp3 alias swmusic", NULL, 0, NULL);
		mciSendString("play swmusic", NULL, 0, NULL);   //仅播放一次音乐
		system("pause");
		exit(0);
	}
	if(x>=9910)
	{
		mciSendString("close bkmusic", NULL, 0, NULL);
		mciSendString("close lqmusic", NULL, 0, NULL);
		mciSendString("open E:\\lq.mp3 alias lqmusic", NULL, 0, NULL);
		mciSendString("play lqmusic", NULL, 0, NULL);   //仅播放一次音乐
		sjjg=0;
		sfkcz=0;
		while(x<10200)
		{
		human_x+=0.01;
		x+=0.01;
		right_i++;
		picture_x=right_i*rwWidth/2;
		picture_y=0;
		if(right_i==1)
				right_i=-1;
		}
		while(time>0)
		{
			
			sjc=time;
			time-=0.1;
			score+=(sjc-time)*10;
		}
		if(time<0)
				time=0;
		
	}
	}
	
	void updateWithInput()  // 与用户输入有关的更新
	{
		
		if ((GetAsyncKeyState(0x41)&0x8000)&&sfkcz==1) // 左移
		{
			ydfx=0;
			left_i++;
			if(human_x>0&&sfkz==1)
			{
				human_x-=5;
				x-=5;
			}
			picture_x=left_i*rwWidth/2;
			picture_y=rwHigh/2;
			if(left_i==1)
				left_i=-1;
			
		}
		if ((GetAsyncKeyState(0x44)&0x8000)&&sfkcz==1)  // 右移
		{
			ydfx=1;
			right_i++;
			
			
			if(human_x>Width/2&&bj_x<9296&&sfkz==1)
			{
				bj_x+=5;
				x+=5;
			}
			else if(human_x<959&&sfkz==1)
			{
				human_x+=5;
				x+=5;
			}
			picture_x=right_i*rwWidth/2;
			picture_y=0;
			if(right_i==1)
				right_i=-1;
			
		}
		if((GetAsyncKeyState(VK_SPACE)&0x8000)&&sfkcz==1) 
		{
			if(pdtg==0&&jiao_y>=436&&human_y<456||pdtg==0&&sfkt==1)
			{
				pdtg=1;
				mciSendString("close jpmusic", NULL, 0, NULL);
				mciSendString("open E:\\跳跃.mp3 alias jpmusic", NULL, 0, NULL);
				mciSendString("play jpmusic", NULL, 0, NULL);   //仅播放一次音乐
			}
		}
		
	}
	
	int main()
	{
		
		startup();  // 数据初始化
		
		while (1) //  游戏循环执行
		{
			show();  // 显示画面
			updateWithoutInput();  // 与用户输入无关的更新
			updateWithInput();  // 与用户输入有关的更新
			Sleep(10);
		}
		return 0;
	}